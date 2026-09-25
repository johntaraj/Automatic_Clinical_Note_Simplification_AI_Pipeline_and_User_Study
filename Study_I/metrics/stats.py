"""Paired arm comparisons: bootstrap intervals, Wilcoxon signed-rank tests and
Benjamini-Hochberg correction.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Sequence, Tuple

METRIC_DIRECTION: Dict[str, int] = {
    "sari": +1,
    "fkgl_drop": +1, "fre_gain": +1, "smog_drop": +1, "coleman_liau_drop": +1,
    "bertscore_f1": +1,
    "nli_faithfulness": +1, "nli_completeness": +1,
    "human_edit_recall": +1, "replacement_precision": +1, "replacement_f1": +1,
    "copy_jargon_rate": -1,
    "definition_borrow_rate": 0,
    "rewrite_aggressiveness": 0,
    "critical_error": -1,
    "drug_preservation": +1,
    "diagnostic_identity_preservation": +1,
    "severity_downgrade": -1,
    "number_unit_preservation": +1,
    "laterality_preservation": +1,
    "negation_preservation": +1,
    "length_ratio": 0,
}

DESCRIPTIVE_ONLY = {
    "citation_precision", "citation_recall", "citation_f1",
    "lds", "source_effect", "attributable_rate",
}


def paired_bootstrap(a: Sequence[float], b: Sequence[float],
                     n_iter: int = 10000, alpha: float = 0.05,
                     seed: int = 1234) -> Optional[Dict[str, float]]:
    pairs = [(x, y) for x, y in zip(a, b)
             if isinstance(x, (int, float)) and isinstance(y, (int, float))]
    n = len(pairs)
    if n < 3:
        return None
    rnd = random.Random(seed)
    diffs: List[float] = []
    wins = 0
    for _ in range(n_iter):
        sample = [pairs[rnd.randrange(n)] for _ in range(n)]
        d = (sum(s[0] for s in sample) - sum(s[1] for s in sample)) / n
        diffs.append(d)
        if d > 0:
            wins += 1
    diffs.sort()
    return {
        "n_pairs": n,
        "mean_diff": (sum(x for x, _ in pairs) - sum(y for _, y in pairs)) / n,
        "ci_lo": diffs[int(n_iter * (alpha / 2))],
        "ci_hi": diffs[int(n_iter * (1 - alpha / 2))],
        "bootstrap_win_rate": wins / n_iter,
    }


def wilcoxon(a: Sequence[float], b: Sequence[float], direction: int = 1,
             alternative: str = "better"
             ) -> Optional[Dict[str, Any]]:
    pairs = [(x, y) for x, y in zip(a, b)
             if isinstance(x, (int, float)) and isinstance(y, (int, float))]
    if len(pairs) < 5 or direction == 0:
        return None
    try:
        from scipy.stats import wilcoxon as _w
    except ImportError:
        return None
    xs = [p for p, _ in pairs]
    ys = [q for _, q in pairs]
    diffs = [(p - q) * direction for p, q in pairs]
    if all(d == 0 for d in diffs):
        return None
    if alternative not in {"better", "two-sided"}:
        raise ValueError("alternative must be 'better' or 'two-sided'")
    alt = ("two-sided" if alternative == "two-sided"
           else ("greater" if direction > 0 else "less"))
    try:
        stat, p = _w(xs, ys, zero_method="zsplit", alternative=alt)
    except Exception:
        return None
    nz = [d for d in diffs if d != 0]
    return {
        "n_pairs": len(pairs),
        "statistic": float(stat),
        "p_value": float(p),
        "effect_size_rbc": rank_biserial(nz),
        "alternative": (
            "arms differ (two-sided; effect direction oriented so positive "
            f"favours arm_a, direction={direction:+d})"
            if alternative == "two-sided"
            else f"arm_a better than arm_b (one-sided, direction={direction:+d})"
        ),
    }


def rank_biserial(diffs: Sequence[float]) -> Optional[float]:
    nz = [float(d) for d in diffs if d != 0]
    if not nz:
        return None
    try:
        from scipy.stats import rankdata
        ranks = rankdata([abs(d) for d in nz])
    except ImportError:
        order = sorted(range(len(nz)), key=lambda i: abs(nz[i]))
        ranks = [0.0] * len(nz)
        for r, i in enumerate(order, start=1):
            ranks[i] = float(r)
    w_pos = sum(r for r, d in zip(ranks, nz) if d > 0)
    w_neg = sum(r for r, d in zip(ranks, nz) if d < 0)
    total = w_pos + w_neg
    return round((w_pos - w_neg) / total, 3) if total else None


def benjamini_hochberg(pvals: List[float], alpha: float = 0.05
                       ) -> Tuple[List[float], List[bool]]:
    m = len(pvals)
    if m == 0:
        return [], []
    order = sorted(range(m), key=lambda i: pvals[i])
    adj = [0.0] * m
    running = 1.0
    for rank, idx in enumerate(reversed(order), start=1):
        i = m - rank + 1
        running = min(running, pvals[idx] * m / i)
        adj[idx] = min(1.0, running)
    reject = [adj[i] <= alpha for i in range(m)]
    return adj, reject


def compare_arms(per_note: List[Dict[str, Any]], arm_a: str, arm_b: str,
                 metrics: List[str], alpha: float = 0.05,
                 alternative: str = "better"
                 ) -> Dict[str, Any]:
    results: Dict[str, Any] = {}
    testable: List[str] = []

    for m in metrics:
        if m in DESCRIPTIVE_ONLY:
            results[m] = {"skipped": "descriptive_only — one arm cannot score "
                                     "above zero by construction"}
            continue
        direction = METRIC_DIRECTION.get(m, +1)
        xs: List[float] = []
        ys: List[float] = []
        for row in per_note:
            arms = row.get("arms") or {}
            pa = ((arms.get(arm_a) or {}).get("metrics") or {}).get(m)
            pb = ((arms.get(arm_b) or {}).get("metrics") or {}).get(m)
            if isinstance(pa, (int, float)) and isinstance(pb, (int, float)):
                xs.append(float(pa))
                ys.append(float(pb))
        if len(xs) < 3:
            results[m] = {"skipped": f"only {len(xs)} paired notes"}
            continue
        boot = paired_bootstrap(xs, ys, alpha=alpha)
        wil = (wilcoxon(xs, ys, direction=direction, alternative=alternative)
               if direction else None)
        results[m] = {
            "n_pairs": len(xs),
            "direction": direction,
            "mean_a": sum(xs) / len(xs),
            "mean_b": sum(ys) / len(ys),
            "diff": sum(xs) / len(xs) - sum(ys) / len(ys),
            "bootstrap": boot,
            "wilcoxon": wil,
        }
        if wil:
            testable.append(m)

    if testable:
        raw = [results[m]["wilcoxon"]["p_value"] for m in testable]
        adj, rej = benjamini_hochberg(raw, alpha=alpha)
        for m, a_, r_ in zip(testable, adj, rej):
            results[m]["p_adjusted_bh"] = round(a_, 5)
            results[m]["significant_after_fdr"] = bool(r_)

    return {
        "arm_a": arm_a,
        "arm_b": arm_b,
        "alpha": alpha,
        "n_tests_in_family": len(testable),
        "correction": "benjamini-hochberg-fdr",
        "alternative": alternative,
        "metrics": results,
    }


def format_comparison(cmp: Dict[str, Any]) -> str:
    a, b = cmp["arm_a"], cmp["arm_b"]
    alternative = cmp.get("alternative", "better")
    test_label = (
        "Wilcoxon two-sided"
        if alternative == "two-sided"
        else f"Wilcoxon one-sided ('{a}' better)"
    )
    lines = [
        "",
        "=" * 100,
        f"  PAIRED COMPARISON   {a}  vs  {b}",
        "=" * 100,
        f"  {test_label}, paired bootstrap 95% CI, "
        f"rank-biserial effect size.",
        f"  {cmp['n_tests_in_family']} tests -> Benjamini-Hochberg FDR at "
        f"alpha={cmp['alpha']}. Report p_adj, not p.",
        "",
        f"  {'metric':<26}{'n':>4}{'dir':>5}{a[:8]:>10}{b[:8]:>10}"
        f"{'diff':>9}{'95% CI':>20}{'p':>9}{'p_adj':>9}{'rbc':>7}",
        "  " + "-" * 96,
    ]
    for m, r in cmp["metrics"].items():
        if "skipped" in r:
            lines.append(f"  {m:<26}  -- skipped: {r['skipped']}")
            continue
        boot = r.get("bootstrap") or {}
        wil = r.get("wilcoxon") or {}
        ci = ("[%+.2f, %+.2f]" % (boot["ci_lo"], boot["ci_hi"])
              if boot.get("ci_lo") is not None else "n/a")
        p = wil.get("p_value")
        padj = r.get("p_adjusted_bh")
        star = "*" if r.get("significant_after_fdr") else ""
        p_s = f"{p:.4f}" if p is not None else "n/a"
        padj_s = f"{padj:.4f}{star}" if padj is not None else "n/a"
        rbc_s = f"{wil['effect_size_rbc']:+.2f}" if wil else "n/a"
        lines.append(
            f"  {m:<26}{r['n_pairs']:>4}{r['direction']:>+5}"
            f"{r['mean_a']:>10.3f}{r['mean_b']:>10.3f}{r['diff']:>+9.3f}"
            f"{ci:>20}{p_s:>9}{padj_s:>9}{rbc_s:>7}"
        )
    lines.append("")
    lines.append("  * = survives FDR correction. Anything without a star is "
                 "NOT a significant result, whatever the raw p says.")
    return "\n".join(lines)
