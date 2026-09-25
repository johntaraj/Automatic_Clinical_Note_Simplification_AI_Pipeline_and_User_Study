"""BERTScore, NLI faithfulness and completeness, and citation support.
Uses local copies of roberta-large and roberta-large-mnli.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from .text import split_sentences

_BS_FN = None
_BS_READY = None


def _load_bertscore(model_path: str):
    global _BS_FN, _BS_READY
    if _BS_READY is not None:
        return _BS_READY
    try:
        from bert_score import score as _score
        _BS_FN = _score
    except ImportError:
        print("  [info] bert-score not installed — BERTScore disabled.")
        _BS_READY = False
        return False
    p = Path(model_path)
    if not (p.exists() and (p / "config.json").exists()):
        print(f"  [info] BERTScore model dir not found at {model_path} — disabled.")
        _BS_READY = False
        return False
    _BS_READY = True
    print(f"  [info] BERTScore model: {model_path}")
    return True


def _baseline_path(model_path: str, lang: str = "en") -> Optional[str]:
    try:
        import bert_score
        name = Path(model_path).name
        p = (Path(bert_score.__file__).parent / "rescale_baseline" / lang
             / f"{name}.tsv")
        return str(p) if p.is_file() else None
    except Exception:
        return None


def bertscore_batch(cands: List[str], refs: List[str], model_path: str,
                    num_layers: int = 17, rescale: bool = True
                    ) -> Optional[List[Optional[float]]]:
    if not cands or not _load_bertscore(model_path):
        return None
    idx = [i for i, (c, r) in enumerate(zip(cands, refs))
           if (c or "").strip() and (r or "").strip()]
    if not idx:
        return [None] * len(cands)
    baseline = _baseline_path(model_path) if rescale else None
    if rescale and baseline is None:
        print("  [warn] no BERTScore rescaling baseline for "
              f"{Path(model_path).name} - reporting RAW scores, which sit in "
              "0.90-0.96 for any same-topic pair.")
        rescale = False
    try:
        P, R, F1 = _BS_FN([cands[i] for i in idx], [refs[i] for i in idx],
                          model_type=model_path, num_layers=num_layers,
                          lang="en", verbose=False,
                          rescale_with_baseline=rescale,
                          baseline_path=baseline)
    except Exception as e:
        if rescale:
            print(f"  [warn] BERTScore rescaling failed ({type(e).__name__}); "
                  f"retrying without baseline rescaling.")
            return bertscore_batch(cands, refs, model_path, num_layers, False)
        print(f"  [warn] BERTScore failed: {type(e).__name__}: {e}")
        return None
    out: List[Optional[float]] = [None] * len(cands)
    for slot, i in enumerate(idx):
        out[i] = round(float(F1[slot]), 4)
    return out


_NLI = None
_NLI_READY = None
_NLI_ENTAIL_IDX: Optional[int] = None


def _load_nli(model_path: str):
    global _NLI, _NLI_READY, _NLI_ENTAIL_IDX
    if _NLI_READY is not None:
        return _NLI_READY
    p = Path(model_path)
    if not (p.exists() and (p / "config.json").exists()):
        print(f"  [info] NLI model dir not found at {model_path} — disabled.")
        _NLI_READY = False
        return False
    try:
        import torch
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
        tok = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSequenceClassification.from_pretrained(model_path)
        model.eval()
        if torch.cuda.is_available():
            model = model.cuda()
        id2label = getattr(model.config, "id2label", {}) or {}
        mapping = {str(v).lower(): int(k) for k, v in id2label.items()}
        _NLI_ENTAIL_IDX = mapping.get("entailment", 2)
        _NLI = (model, tok, torch)
        _NLI_READY = True
        print(f"  [info] NLI model: {model_path} (entailment index "
              f"{_NLI_ENTAIL_IDX})")
        return True
    except Exception as e:
        print(f"  [warn] NLI load failed: {type(e).__name__}: {e}")
        _NLI_READY = False
        return False


def entailment(premise: str, hypothesis: str, model_path: str) -> Optional[float]:
    if not _load_nli(model_path):
        return None
    if not (premise or "").strip() or not (hypothesis or "").strip():
        return None
    model, tok, torch = _NLI
    try:
        inputs = tok(premise, hypothesis, return_tensors="pt",
                     truncation=True, max_length=512, padding=True)
        if torch.cuda.is_available():
            inputs = {k: v.cuda() for k, v in inputs.items()}
        with torch.no_grad():
            probs = torch.softmax(model(**inputs).logits[0], dim=-1)
        return float(probs[_NLI_ENTAIL_IDX].item())
    except Exception:
        return None


def _directional(premise_text: str, hypothesis_text: str, model_path: str
                 ) -> Optional[float]:
    hyps = split_sentences(hypothesis_text)
    prems = split_sentences(premise_text)
    if not hyps or not prems:
        return None
    per: List[float] = []
    for h in hyps:
        best = 0.0
        for p in prems:
            v = entailment(p, h, model_path)
            if v is None:
                return None
            best = max(best, v)
        per.append(best)
    return round(sum(per) / len(per), 4)


def nli_faithfulness(orig: str, sys_out: str, model_path: str) -> Optional[float]:
    return _directional(orig, sys_out, model_path)


def nli_completeness(orig: str, sys_out: str, model_path: str) -> Optional[float]:
    return _directional(sys_out, orig, model_path)


def citation_support(ops: List[Dict[str, Any]], model_path: str
                     ) -> Optional[Dict[str, Any]]:
    if not ops:
        return None
    precs: List[float] = []
    recs: List[float] = []
    skipped_invalid = 0
    skipped_uncited = 0

    for op in ops:
        tgt = (op.get("tgt_text") or "").strip()
        if not tgt:
            continue
        cc = op.get("contextcite") or {}
        status = cc.get("status") or ("attributed" if cc.get("valid", True) else "failed")
        if cc and status != "attributed":
            skipped_invalid += 1
            continue
        top = op.get("top_sources") or []
        if not top:
            skipped_uncited += 1
            continue
        passages = [(s.get("passage") or s.get("text") or "").strip()
                    for s in top[:3]]
        passages = [p for p in passages if p]
        if not passages:
            skipped_uncited += 1
            continue
        p1 = entailment(passages[0], tgt, model_path)
        if p1 is None:
            return None
        precs.append(p1)
        best = p1
        for p in passages[1:]:
            v = entailment(p, tgt, model_path)
            if v is None:
                return None
            best = max(best, v)
        recs.append(best)

    if not precs:
        return None
    mp = sum(precs) / len(precs)
    mr = sum(recs) / len(recs)
    return {
        "citation_precision": round(mp, 4),
        "citation_recall": round(mr, 4),
        "citation_f1": round(2 * mp * mr / (mp + mr), 4) if (mp + mr) else 0.0,
        "n_cited_ops": len(precs),
        "n_skipped_invalid_fit": skipped_invalid,
        "n_skipped_uncited": skipped_uncited,
    }
