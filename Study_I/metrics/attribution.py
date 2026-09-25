"""Aggregates per-edit ContextCite results into attribution metrics."""

from __future__ import annotations

import statistics
from typing import Any, Dict, Iterable, List, Optional

from .coverage import source_matches_term


def _cc_records(ops: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out = []
    for op in ops or []:
        cc = op.get("contextcite")
        if isinstance(cc, dict):
            out.append(cc)
    return out


def _cc_pairs(ops: Iterable[Dict[str, Any]]):
    return [(op, op["contextcite"]) for op in ops or []
            if isinstance(op.get("contextcite"), dict)]


def _pct(n: int, d: int) -> Optional[float]:
    return round(n / d, 4) if d else None


def attribution_summary(all_ops: List[Dict[str, Any]],
                        eps: float = 0.10,
                        lds_threshold: float = 0.40,
                        margin_threshold: float = 0.10) -> Dict[str, Any]:
    recs = _cc_records(all_ops)
    pairs = _cc_pairs(all_ops)
    n_total = len(recs)

    def _status(r: Dict[str, Any]) -> str:
        s = r.get("status")
        if s:
            return s
        return "attributed" if r.get("valid") else "failed"

    attributed = [r for r in recs if _status(r) == "attributed"]
    no_effect = [r for r in recs if _status(r) == "no_source_effect"]
    failed = [r for r in recs if _status(r) == "failed"]
    measurable = attributed + no_effect

    helped, hurt, neutral = [], [], []
    for r in measurable:
        eff = r.get("source_effect")
        if eff is None:
            continue
        if eff >= eps:
            helped.append(r)
        elif eff <= -eps:
            hurt.append(r)
        else:
            neutral.append(r)

    attributable = [
        r for r in helped
        if _status(r) == "attributed"
        and (r.get("lds") is not None and r["lds"] >= lds_threshold)
        and (r.get("winner_margin") is not None
             and r["winner_margin"] >= margin_threshold)
    ]

    lds_vals = [r["lds"] for r in attributed if r.get("lds") is not None]
    lds_in_vals = [r["lds_insample"] for r in attributed
                   if r.get("lds_insample") is not None]
    eff_vals = [r["source_effect"] for r in measurable
                if r.get("source_effect") is not None]

    def _drops(k: int, records: List[Dict[str, Any]]) -> List[float]:
        out = []
        for r in records:
            d = (r.get("top_k_drops") or {})
            v = d.get(str(k), d.get(k))
            if isinstance(v, (int, float)):
                out.append(float(v))
        return out

    scored = sum(r.get("num_valid_ablations", 0) for r in recs)
    failed_calls = sum(r.get("num_failed_ablations", 0) for r in recs)

    out: Dict[str, Any] = {
        "n_edits": n_total,
        "n_attributed": len(attributed),
        "n_no_source_effect": len(no_effect),
        "n_failed": len(failed),
        "n_measurable": len(measurable),
        "failure_reasons": _reason_counts(failed),
        "no_effect_reasons": _reason_counts(no_effect),
        "ablation_scores_ok": scored,
        "ablation_scores_failed": failed_calls,
        "ablation_success_rate": _pct(scored, scored + failed_calls),

        "n_helped": len(helped),
        "n_hurt": len(hurt),
        "n_neutral": len(neutral),
        "helped_rate": _pct(len(helped), len(measurable)),
        "hurt_rate": _pct(len(hurt), len(measurable)),
        "neutral_rate": _pct(len(neutral), len(measurable)),

        "n_attributable": len(attributable),
        "attributable_rate": _pct(len(attributable), len(helped)),

        "eps": eps,
        "lds_threshold": lds_threshold,
        "margin_threshold": margin_threshold,
    }

    helped_ids = {id(r) for r in helped}
    self_hits = considered = 0
    for op, cc in pairs:
        if id(cc) not in helped_ids or _status(cc) != "attributed":
            continue
        top = op.get("top_sources") or []
        if not top:
            continue
        considered += 1
        if source_matches_term(op.get("src_text") or "", top[0]):
            self_hits += 1
    out["n_self_term_considered"] = considered
    out["right_term_rate"] = _pct(self_hits, considered)

    out["n_lds_unavailable"] = sum(1 for r in attributed if r.get("lds") is None)

    rel = [r["n_relevant_sources"] for r in helped
           if isinstance(r.get("n_relevant_sources"), int)]
    if rel:
        out["n_relevant_sources_median"] = round(statistics.median(rel), 2)
        out["n_relevant_sources_p95"] = sorted(rel)[max(0, round(0.95 * len(rel)) - 1)]
        out["n_edits_with_a_relevant_source"] = sum(1 for v in rel if v > 0)
        out["relevant_source_rate"] = _pct(
            sum(1 for v in rel if v > 0), len(rel))
        agree = [(r.get("loo_top1"), r.get("lasso_top1")) for r in helped
                 if r.get("loo_top1") is not None
                 and r.get("lasso_top1") is not None]
        if agree:
            out["oracle_agreement"] = _pct(
                sum(1 for a, b in agree if a == b), len(agree))
            out["n_lasso_loo_compared"] = len(agree)

    if lds_vals:
        out["lds_median"] = round(statistics.median(lds_vals), 4)
        out["lds_mean"] = round(statistics.fmean(lds_vals), 4)
        out["lds_ge_0.4"] = _pct(sum(1 for v in lds_vals if v >= 0.4), len(lds_vals))
        out["n_lds"] = len(lds_vals)
    if lds_in_vals:
        out["lds_insample_median"] = round(statistics.median(lds_in_vals), 4)
        if lds_vals:
            out["lds_optimism_gap"] = round(
                statistics.median(lds_in_vals) - statistics.median(lds_vals), 4)
    if eff_vals:
        out["source_effect_median"] = round(statistics.median(eff_vals), 4)
        out["source_effect_mean"] = round(statistics.fmean(eff_vals), 4)
    for k in (1, 3):
        vals = _drops(k, attributed)
        if vals:
            out[f"top{k}_drop_median"] = round(statistics.median(vals), 4)
            out[f"top{k}_drop_mean"] = round(statistics.fmean(vals), 4)
            out[f"n_top{k}_drop"] = len(vals)
        helped_attr = [r for r in helped if _status(r) == "attributed"]
        hvals = _drops(k, helped_attr)
        if hvals:
            out[f"top{k}_drop_median_helped"] = round(statistics.median(hvals), 4)
            out[f"top{k}_drop_mean_helped"] = round(statistics.fmean(hvals), 4)
            out[f"n_top{k}_drop_helped"] = len(hvals)
    return out


def _reason_counts(records: List[Dict[str, Any]]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for r in records:
        reason = (r.get("invalid_reason") or "unspecified").split(";")[0].strip()
        counts[reason] = counts.get(reason, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: -kv[1]))


def threshold_sweep(all_ops: List[Dict[str, Any]],
                    epsilons: List[float] = (0.05, 0.10, 0.25, 0.693, 1.0)
                    ) -> List[Dict[str, Any]]:
    rows = []
    for eps in epsilons:
        s = attribution_summary(all_ops, eps=eps)
        rows.append({
            "eps": eps,
            "helped": s["n_helped"], "neutral": s["n_neutral"],
            "hurt": s["n_hurt"],
            "attributable_rate": s["attributable_rate"],
        })
    return rows


def per_edit_table(all_ops: List[Dict[str, Any]], eps: float = 0.10
                   ) -> List[Dict[str, Any]]:
    rows = []
    for op in all_ops or []:
        cc = op.get("contextcite") or {}
        status = cc.get("status") or ("attributed" if cc.get("valid") else "failed")
        eff = cc.get("source_effect")
        if status == "failed":
            verdict = "failed"
        elif eff is None:
            verdict = "unknown"
        elif eff >= eps:
            verdict = "helped"
        elif eff <= -eps:
            verdict = "hurt"
        else:
            verdict = "neutral"
        top = (op.get("top_sources") or [{}])[0]
        rows.append({
            "note_idx": op.get("note_idx"),
            "type": op.get("type"),
            "src": op.get("src_text"),
            "tgt": op.get("tgt_text"),
            "status": status,
            "verdict": verdict,
            "source_effect": round(eff, 3) if isinstance(eff, (int, float)) else None,
            "lds": cc.get("lds"),
            "lds_insample": cc.get("lds_insample"),
            "winner_margin": cc.get("winner_margin"),
            "top_source": top.get("source"),
            "top_source_text": top.get("text"),
            "top1_drop": (cc.get("top_k_drops") or {}).get("1"),
            "reason": cc.get("invalid_reason"),
        })
    return rows
