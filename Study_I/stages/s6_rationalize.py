"""Stage 6: per-edit explanations; Stage 7: deterministic audit of their claims."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

from config import Config
from core.io import rule

RATIONALE_SYSTEM = """You explain, to a patient, why one phrase in a medical \
sentence was replaced with another.

Write ONE short paragraph of 3 sentences, in this order:

1. MEANING. Say what the glossary source tells us about the original term, and
   how the replacement carries that meaning in plain words. Lead with this.
2. NUMBERS. Give the measured difficulty change, using the exact values you
   were given. Say "word frequency" or "phrase frequency" for Zipf (HIGHER =
   more common = easier) and "age of acquisition" for AoA (LOWER = learned
   younger = easier). Only mention a statistic if you were given BOTH its
   before and after value.
3. BENEFIT. One sentence on what the reader can now understand.

STYLE
- Vary your wording between rationales. Do not reuse the same sentence frames.
- Never invent a statistic, a source name, or a quotation.
- If you are told there is NO glossary source, do not refer to a source at all
  — not by name, and not as "the source" or "the glossary". Explain the term
  in your own words instead.
- Output only the paragraph. No headings, no bullets, no word counts.

EXAMPLE OF THE SHAPE (do not copy the wording)
The source describes atrial fibrillation as an irregular, often fast
heartbeat, so "irregular heartbeat" keeps its central feature in plain
language. Phrase frequency increases from Zipf 2.6 to 3.4, while age of
acquisition falls from 14.6 to 9.2. Patients can understand the basic
heart-rhythm problem without first knowing the diagnostic name."""


def _fmt(v: Optional[float]) -> Optional[str]:
    return None if v is None else f"{float(v):.2f}"


def _user(term: str, replacement: str, feats: Dict[str, Any],
          tgt_feats: Dict[str, Any], source: str, passage: str,
          source_is_influential: bool) -> str:
    lines = [f'Original term: "{term}"', f'Replacement: "{replacement}"', ""]

    z0, z1 = _fmt(feats.get("zipf")), _fmt(tgt_feats.get("zipf"))
    a0, a1 = _fmt(feats.get("aoa")), _fmt(tgt_feats.get("aoa"))
    stats = []
    if z0 and z1:
        stats.append(f"Frequency (Zipf): {z0} -> {z1}   (higher = more common)")
    if a0 and a1:
        stats.append(f"Age of acquisition: {a0} -> {a1}   (lower = learned younger)")
    if feats.get("syllables") and tgt_feats.get("syllables"):
        stats.append(f"Syllables: {feats['syllables']} -> {tgt_feats['syllables']}")
    lines.append("Measured difficulty change:")
    lines.extend(f"  {s}" for s in stats or
                 ["  (no paired measurement available - do not cite numbers)"])
    lines.append("")

    if source_is_influential and passage:
        lines.append(f"Glossary source that measurably caused this edit: {source}")
        lines.append(f'Its text: "{passage}"')
    else:
        lines.append(
            "NO glossary entry influenced this edit. You have NO source, NO "
            "definition and NO quotation. Do NOT write \"the source says\", "
            "\"the glossary defines\" or anything similar, and do not "
            "describe what any source contains. Open instead by stating in "
            "your own words what the original term means and how the "
            "replacement carries that meaning, then give the numbers.")
    lines.append("")
    lines.append("Write the paragraph now.")
    return "\n".join(lines)


_STOP = ["\n\n", "response_", "\nresponse", "Original term:"]
_RESPONSE_MARKER = re.compile(r"\bresponse[_ ]?\d+\s*:", re.I)
_LEADING_ARTEFACT = re.compile(r"^[_\s]*\d*\s*:\s*")


def _clean_rationale(text: str) -> str:
    text = _RESPONSE_MARKER.split(text)[0]
    text = _LEADING_ARTEFACT.sub("", text.strip())
    para = text.split("\n\n")[0].strip()
    seen, kept = set(), []
    for sent in re.split(r"(?<=[.!?])\s+", para):
        s = sent.strip()
        if not s:
            continue
        norm = s.lower()
        if norm in seen:
            break
        seen.add(norm)
        kept.append(s)
    return " ".join(kept).strip()


def phrase_features(text: str, aoa: Dict[str, Any]) -> Dict[str, Any]:
    from stages.s2_extract import lex_features
    f = lex_features(text or "", aoa)
    return {"zipf": f.get("zipf"), "aoa": f.get("aoa"),
            "syllables": f.get("syllables")}


def source_matches_edit(src_text: str, top: Dict[str, Any]) -> bool:
    from metrics.coverage import source_matches_term
    return source_matches_term(src_text, top)


def run_rationales(cfg: Config, llm, notes: List[Dict[str, Any]],
                   arm: str = "grounded") -> List[Dict[str, Any]]:
    from stages.s2_extract import load_aoa
    aoa = load_aoa(cfg.root / "data" / "en.aoa.csv")

    feats_by_term: Dict[str, Dict[str, Any]] = {}
    for note in notes:
        for it in note.get("hard_items", []):
            t = (it.get("text") or "").strip().lower()
            if t:
                feats_by_term[t] = it.get("features") or {}

    n_gated = 0
    for note in notes:
        rec = (note.get("arms") or {}).get(arm) or {}
        ops = rec.get("operations") or []
        if not ops:
            continue
        rule(f"note {note['note_idx']} - rationales ({len(ops)} edits)")
        for op in ops:
            cc = op.get("contextcite") or {}
            top = (op.get("top_sources") or [{}])[0]
            src = (op.get("src_text") or "").strip()
            tgt = (op.get("tgt_text") or "").strip()

            feats = dict(feats_by_term.get(src.lower(), {}))
            if feats.get("zipf") is None or feats.get("aoa") is None:
                auto = phrase_features(src, aoa)
                for k in ("zipf", "aoa", "syllables"):
                    if feats.get(k) is None:
                        feats[k] = auto[k]
            tgt_feats = phrase_features(tgt, aoa)

            effect = cc.get("source_effect")
            lds = cc.get("lds")
            margin = cc.get("winner_margin")
            influential = (isinstance(effect, (int, float))
                           and effect >= cfg.cc_effect_threshold
                           and bool(top.get("passage"))
                           and source_matches_edit(src, top)
                           and isinstance(lds, (int, float))
                           and lds >= cfg.cc_attributable_lds
                           and isinstance(margin, (int, float))
                           and margin >= cfg.cc_attributable_margin)
            if not influential:
                n_gated += 1

            source_short = top.get("source") or ""
            passage = top.get("passage") or ""

            prompt = llm.apply_chat_template([
                {"role": "system", "content": RATIONALE_SYSTEM},
                {"role": "user", "content": _user(src, tgt, feats, tgt_feats,
                                                  source_short, passage,
                                                  influential)},
            ])
            try:
                text = llm.complete(prompt,
                                    max_new_tokens=getattr(
                                        cfg, "rationale_max_tokens", 3072),
                                    temperature=0.0, stop_strings=_STOP)
            except Exception as e:
                text = ""
                print(f"    [warn] rationale failed for {src!r}: "
                      f"{type(e).__name__}")
            text = _clean_rationale(text)
            op["rationale"] = {
                "text": text.strip(),
                "source_claimed": influential,
                "ground_truth": {
                    "src_features": feats,
                    "tgt_features": tgt_feats,
                    "source_short": source_short if influential else "",
                    "source_passage": passage if influential else "",
                    "source_effect": effect,
                    "cc_status": cc.get("status"),
                },
            }
            flag = "" if influential else "  [no source claimed]"
            print(f"    {src!r} -> {tgt!r}: {len(text.split())} words{flag}")
    if n_gated:
        print(f"\n  {n_gated} edit(s) had no measurably influential source "
              f"(effect < {cfg.cc_effect_threshold} nats); their rationales "
              f"cite no glossary entry.")
    return notes


_NUM_RE = re.compile(r"-?\d+(?:\.\d+)?")
_SOURCE_VOCAB = ("readme", "nih", "dorland", "dictionary", "iowa", "michigan",
                 "justplainclear", "thesaurus", "umls", "no-source")
_MIN_QUOTE_WORDS = 4


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", (s or "").lower()).strip()


def _quotes(text: str) -> List[str]:
    if not text:
        return []
    t = (text.replace("\u201c", '"').replace("\u201d", '"')
             .replace("\u2018", "'").replace("\u2019", "'"))
    parts = t.split('"')
    if len(parts) % 2 == 0:
        parts = parts[:-1]
    return [p for i, p in enumerate(parts) if i % 2 == 1]


_RISE_WORDS = ("increase", "increases", "increased", "increasing", "rise",
               "rises", "rose", "rising", "higher", "grows", "grew", "up from",
               "improves to", "goes up", "went up", "more common")
_FALL_WORDS = ("decrease", "decreases", "decreased", "decreasing", "fall",
               "falls", "fell", "falling", "lower", "drops", "dropped",
               "declines", "declined", "down from", "goes down", "went down",
               "reduces", "reduced", "less common")


def _direction_errors(text: str, feats: Dict[str, Any],
                      tgt_feats: Dict[str, Any]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    clauses = re.split(r"(?<!\d)[.,;]|[.,;](?!\d)| while | and | but ",
                       text.lower())
    for key, label in (("zipf", "frequency"), ("aoa", "age of acquisition")):
        before, after = feats.get(key), tgt_feats.get(key)
        if before is None or after is None or abs(after - before) < 1e-9:
            continue
        went_up = after > before
        for c in clauses:
            if not any(str(round(float(v), 2)) in c or str(v) in c
                       for v in (before, after)):
                continue
            said_up = any(w in c for w in _RISE_WORDS)
            said_down = any(w in c for w in _FALL_WORDS)
            if said_up == said_down:
                continue
            if said_up != went_up:
                out.append({"slot": key, "label": label,
                            "before": before, "after": after,
                            "said": "increase" if said_up else "decrease",
                            "clause": c.strip()[:80]})
            break
    return out


def audit_one(op: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    r = op.get("rationale") or {}
    text = (r.get("text") or "").strip()
    if not text:
        return None
    gt = r.get("ground_truth") or {}
    feats = gt.get("src_features") or {}
    tgt_feats = gt.get("tgt_features") or {}
    nums = [float(m.group(0)) for m in _NUM_RE.finditer(text)]

    expected = {}
    for k in ("zipf", "aoa"):
        if feats.get(k) is not None and tgt_feats.get(k) is not None:
            expected[f"{k}_before"] = feats[k]
            expected[f"{k}_after"] = tgt_feats[k]
    omitted, wrong, correct = [], [], []
    for name, exp in expected.items():
        if exp is None:
            continue
        if any(abs(n - float(exp)) <= 0.1 for n in nums):
            correct.append(name)
        elif nums:
            near = [n for n in nums if abs(n - float(exp)) <= 3.0]
            (wrong if near else omitted).append(
                {"slot": name, "expected": exp, "saw": near or None})
        else:
            omitted.append({"slot": name, "expected": exp})

    direction_wrong = _direction_errors(text, feats, tgt_feats)

    src_short = (gt.get("source_short") or "").lower()
    named = [s for s in _SOURCE_VOCAB if s != "no-source" and s in text.lower()]
    if not src_short:
        source_ok = not named
        source_wrong = bool(named)
    else:
        generic = any(w in text.lower()
                      for w in ("the glossary", "the source", "glossary entry",
                                "glossary defines", "source describes"))
        wrong_named = [s for s in named if s != src_short]
        source_ok = (src_short in text.lower() or generic) and not wrong_named
        source_wrong = bool(wrong_named)

    expected_passage = _norm(gt.get("source_passage") or "")
    edit_quotes = {_norm(op.get("src_text") or ""), _norm(op.get("tgt_text") or "")}
    candidates = [q for q in _quotes(text)
                  if len(q.strip().split()) >= _MIN_QUOTE_WORDS
                  and _norm(q) not in edit_quotes]
    unsupported: List[str] = []
    passage_ok = True
    if candidates:
        passage_ok = False
        for q in candidates:
            qn = _norm(q)
            if qn and expected_passage and (
                    qn in expected_passage or expected_passage.startswith(qn)):
                passage_ok = True
            else:
                unsupported.append(q)
        passage_ok = passage_ok and not unsupported

    checkable = len(correct) + len(wrong) + len(omitted) \
        + (1 if expected_passage else 0) + (1 if src_short else 0)
    landed = (len(correct)
              + (1 if passage_ok and expected_passage else 0)
              + (1 if source_ok and src_short else 0))

    grounding_error = bool(wrong or source_wrong or unsupported or direction_wrong)
    omission = bool(omitted)

    return {
        "src_text": op.get("src_text"),
        "tgt_text": op.get("tgt_text"),
        "slot_coverage": round(landed / checkable, 3) if checkable else 1.0,
        "numeric_correct": correct,
        "numeric_wrong": wrong,
        "numeric_omitted": omitted,
        "direction_wrong": direction_wrong,
        "source_ok": source_ok,
        "source_wrong": source_wrong,
        "passage_ok": passage_ok,
        "unsupported_quotes": unsupported,
        "grounding_error": grounding_error,
        "omission": omission,
        "text": (r.get("text") or "")[:400],
    }


def _overlap(a: str, b: str) -> float:
    A = {w for w in _norm(a).split() if len(w) >= 4}
    B = {w for w in _norm(b).split() if len(w) >= 4}
    if not A or not B:
        return 0.0
    return len(A & B) / min(len(A), len(B))


def run_audit(notes: List[Dict[str, Any]], arm: str = "grounded"
              ) -> Dict[str, Any]:
    rows: List[Dict[str, Any]] = []
    for note in notes:
        rec = (note.get("arms") or {}).get(arm) or {}
        for op in rec.get("operations") or []:
            a = audit_one(op)
            if a:
                a["note_idx"] = note["note_idx"]
                op["rationale_audit"] = a
                rows.append(a)

    if not rows:
        return {"n_rationales": 0}

    texts = [r["text"] for r in rows]
    templated = sum(1 for i in range(len(texts)) for j in range(i + 1, len(texts))
                    if _overlap(texts[i], texts[j]) >= 0.85)
    n_pairs = max(1, len(texts) * (len(texts) - 1) // 2)
    n = len(rows)
    return {
        "n_rationales": n,
        "rationale_fact_recall": round(
            sum(r["slot_coverage"] for r in rows) / n, 4),
        "rationale_fabrication_rate": round(
            sum(1 for r in rows if r["grounding_error"]) / n, 4),
        "rationale_omission_rate": round(
            sum(1 for r in rows if r["omission"]) / n, 4),
        "rationale_source_correct": round(
            sum(1 for r in rows if r["source_ok"]) / n, 4),
        "rationale_quote_verified": round(
            sum(1 for r in rows if r["passage_ok"]) / n, 4),
        "rationale_template_rate": round(templated / n_pairs, 4),
        "n_templated_pairs": templated,
        "per_edit": rows,
    }
