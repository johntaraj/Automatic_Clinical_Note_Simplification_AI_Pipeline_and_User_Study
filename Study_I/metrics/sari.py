"""SARI (Xu et al., 2016)."""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from .text import ngrams, tokens


def sari_sentence(orig: str, sys_out: str, refs: List[str]) -> Optional[float]:
    if not (sys_out or "").strip():
        return None
    refs_t = [tokens(r) for r in refs if (r or "").strip()]
    if not refs_t:
        return None

    orig_t = tokens(orig)
    sys_t = tokens(sys_out)
    R = len(refs_t)

    def _score(n: int) -> Tuple[float, float, float]:
        og = ngrams(orig_t, n)
        sg = ngrams(sys_t, n)
        ref_gs = [ngrams(r, n) for r in refs_t]

        ref_w: Dict[Tuple[str, ...], float] = {}
        for rg in ref_gs:
            for g, c in rg.items():
                ref_w[g] = ref_w.get(g, 0.0) + min(c, 1)
        for g in ref_w:
            ref_w[g] /= R

        keep_keys = set(og) & set(sg)
        keep_tp = sum(min(og[g], sg[g]) * ref_w.get(g, 0.0) for g in keep_keys)
        keep_fp = sum(min(og[g], sg[g]) * (1 - ref_w.get(g, 0.0)) for g in keep_keys)
        keep_fn = sum(og.get(g, 0) * ref_w.get(g, 0.0) for g in set(og) - keep_keys)
        keep_p = keep_tp / (keep_tp + keep_fp) if keep_tp + keep_fp else 0.0
        keep_r = keep_tp / (keep_tp + keep_fn) if keep_tp + keep_fn else 0.0
        keep_f = 2 * keep_p * keep_r / (keep_p + keep_r) if keep_p + keep_r else 0.0

        del_keys = set(og) - set(sg)
        del_tp = sum(og[g] * (1 - ref_w.get(g, 0.0)) for g in del_keys)
        del_tot = sum(og[g] for g in del_keys)
        del_f = del_tp / del_tot if del_tot else 0.0

        add_keys = set(sg) - set(og)
        all_ref_keys: set = set()
        for rg in ref_gs:
            all_ref_keys |= set(rg)
        add_tp = sum(ref_w.get(g, 0.0) for g in add_keys)
        add_fp = sum(1 - ref_w.get(g, 0.0) for g in add_keys)
        add_fn = sum(ref_w.get(g, 0.0) for g in all_ref_keys - set(og) - set(sg))
        add_p = add_tp / (add_tp + add_fp) if add_tp + add_fp else 0.0
        add_r = add_tp / (add_tp + add_fn) if add_tp + add_fn else 0.0
        add_f = 2 * add_p * add_r / (add_p + add_r) if add_p + add_r else 0.0

        return keep_f, del_f, add_f

    k = d = a = 0.0
    for n in (1, 2, 3, 4):
        kf, df, af = _score(n)
        k += kf
        d += df
        a += af
    return 100.0 * ((k / 4) + (d / 4) + (a / 4)) / 3.0


def sari_components(orig: str, sys_out: str, refs: List[str]
                    ) -> Dict[str, float]:
    refs_t = [r for r in refs if (r or "").strip()]
    if not (sys_out or "").strip() or not refs_t:
        return {}
    orig_t, sys_t = tokens(orig), tokens(sys_out)
    ref_tok = [tokens(r) for r in refs_t]
    R = len(ref_tok)
    acc = {"keep": 0.0, "delete": 0.0, "add": 0.0}
    for n in (1, 2, 3, 4):
        og, sg = ngrams(orig_t, n), ngrams(sys_t, n)
        ref_gs = [ngrams(r, n) for r in ref_tok]
        ref_w: Dict[Tuple[str, ...], float] = {}
        for rg in ref_gs:
            for g, c in rg.items():
                ref_w[g] = ref_w.get(g, 0.0) + min(c, 1)
        for g in ref_w:
            ref_w[g] /= R
        keep_keys = set(og) & set(sg)
        keep_tp = sum(min(og[g], sg[g]) * ref_w.get(g, 0.0) for g in keep_keys)
        keep_fp = sum(min(og[g], sg[g]) * (1 - ref_w.get(g, 0.0)) for g in keep_keys)
        keep_fn = sum(og.get(g, 0) * ref_w.get(g, 0.0) for g in set(og) - keep_keys)
        kp = keep_tp / (keep_tp + keep_fp) if keep_tp + keep_fp else 0.0
        kr = keep_tp / (keep_tp + keep_fn) if keep_tp + keep_fn else 0.0
        acc["keep"] += 2 * kp * kr / (kp + kr) if kp + kr else 0.0
        del_keys = set(og) - set(sg)
        dt = sum(og[g] * (1 - ref_w.get(g, 0.0)) for g in del_keys)
        dtot = sum(og[g] for g in del_keys)
        acc["delete"] += dt / dtot if dtot else 0.0
        add_keys = set(sg) - set(og)
        allref: set = set()
        for rg in ref_gs:
            allref |= set(rg)
        at = sum(ref_w.get(g, 0.0) for g in add_keys)
        af_ = sum(1 - ref_w.get(g, 0.0) for g in add_keys)
        an = sum(ref_w.get(g, 0.0) for g in allref - set(og) - set(sg))
        ap = at / (at + af_) if at + af_ else 0.0
        ar = at / (at + an) if at + an else 0.0
        acc["add"] += 2 * ap * ar / (ap + ar) if ap + ar else 0.0
    return {k: round(100.0 * v / 4, 2) for k, v in acc.items()}


def corpus_sari(origs: List[str], sys_outs: List[str],
                refs: List[List[str]], prefer_easse: bool = True
                ) -> Tuple[Optional[float], str]:
    if prefer_easse:
        try:
            from easse.sari import corpus_sari as _easse
            n_ref = max((len(r) for r in refs), default=0)
            cols = [[(r[i] if i < len(r) else r[-1]) for r in refs]
                    for i in range(max(n_ref, 1))]
            return float(_easse(orig_sents=origs, sys_sents=sys_outs,
                                refs_sents=cols)), "easse"
        except Exception:
            pass
    vals = [s for s in (sari_sentence(o, y, r)
                        for o, y, r in zip(origs, sys_outs, refs))
            if s is not None]
    if not vals:
        return None, "internal-mean-of-sentence"
    return sum(vals) / len(vals), "internal-mean-of-sentence"
