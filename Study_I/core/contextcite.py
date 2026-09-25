"""ContextCite (Cohen-Wang et al., 2024): scores a fixed rewrite under masked glossary
contexts and fits a sparse linear surrogate to attribute each edit to its sources.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

import numpy as np


def _spearman(a: np.ndarray, b: np.ndarray) -> Optional[float]:
    if a.size < 3 or b.size < 3:
        return None
    try:
        import warnings
        from scipy.stats import spearmanr
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            rho, _ = spearmanr(a, b)
        if rho is None or (isinstance(rho, float) and math.isnan(rho)):
            return None
        return float(rho)
    except Exception:
        return None


def _finite(arr: np.ndarray) -> np.ndarray:
    return np.isfinite(arr) & (arr > -9999.0)


MIN_HELDOUT_FOR_LDS = 8

_DELTA2 = math.log(2.0)


def _sample_masks(rng, d: int, n_fit: int, n_held: int):
    n_held = max(0, n_held)
    want = n_fit + n_held
    space = (1 << d) if d < 62 else None

    if space is not None and space <= want:
        pool = np.array([[(i >> b) & 1 for b in range(d)] for i in range(space)],
                        dtype=np.int64)
        rng.shuffle(pool)
    else:
        seen: set = set()
        rows: List[np.ndarray] = []
        while len(rows) < want:
            m = rng.integers(0, 2, size=d, dtype=np.int64)
            key = m.tobytes()
            if key in seen:
                continue
            seen.add(key)
            rows.append(m)
        pool = np.vstack(rows)

    n_fit_eff = min(n_fit, len(pool))
    return pool[:n_fit_eff], pool[n_fit_eff:n_fit_eff + n_held]


def to_logit(logp: np.ndarray) -> np.ndarray:
    lp = np.minimum(np.asarray(logp, dtype=np.float64), -1e-12)
    return lp - np.log(-np.expm1(lp))


@dataclass
class ContextCiteResult:
    sources: List[Dict[str, Any]]
    attributions: List[float]
    intercept: float
    masks: List[List[int]]
    log_probs: List[float]
    original_log_prob: float
    empty_log_prob: float
    lds: Optional[float]
    lds_insample: Optional[float]
    n_heldout: int
    top_k_drops: Dict[int, Optional[float]]
    num_ablations: int
    lambd: float
    statement: str
    valid: bool
    status: str
    invalid_reason: Optional[str]
    num_valid_ablations: int
    num_failed_ablations: int
    extra_calls: int = 0
    loo_effects: Optional[List[float]] = None
    n_relevant_sources: Optional[int] = None
    loo_top1: Optional[int] = None

    @property
    def measurable(self) -> bool:
        return self.status in ("attributed", "no_source_effect")

    def as_dict(self) -> Dict[str, Any]:
        return {
            "sources": self.sources,
            "attributions": self.attributions,
            "intercept": self.intercept,
            "masks": self.masks,
            "log_probs": self.log_probs,
            "original_log_prob": self.original_log_prob,
            "empty_log_prob": self.empty_log_prob,
            "source_effect": self.source_effect if self.measurable else None,
            "source_effect_logit": (self.source_effect_logit
                                    if self.measurable else None),
            "surrogate_target": "logit",
            "winner_margin": self.winner_margin(),
            "lds": self.lds,
            "lds_insample": self.lds_insample,
            "n_heldout": self.n_heldout,
            "top_k_drops": self.top_k_drops,
            "num_ablations": self.num_ablations,
            "lambd": self.lambd,
            "statement": self.statement,
            "valid": self.valid,
            "status": self.status,
            "measurable": self.measurable,
            "invalid_reason": self.invalid_reason,
            "num_valid_ablations": self.num_valid_ablations,
            "num_failed_ablations": self.num_failed_ablations,
            "extra_calls": self.extra_calls,
            "loo_effects": self.loo_effects,
            "n_relevant_sources": self.n_relevant_sources,
            "loo_top1": self.loo_top1,
            "lasso_top1": self.lasso_top1,
        }

    @property
    def source_effect(self) -> float:
        return float(self.original_log_prob - self.empty_log_prob)

    @property
    def source_effect_logit(self) -> float:
        return float(to_logit(np.array([self.original_log_prob]))[0]
                     - to_logit(np.array([self.empty_log_prob]))[0])

    def winner_margin(self) -> Optional[float]:
        if not self.valid or len(self.attributions) < 2:
            return None
        w = np.sort(np.asarray(self.attributions))[::-1]
        return float(w[0] - w[1])

    @property
    def lasso_top1(self) -> Optional[int]:
        if not self.valid or not self.attributions:
            return None
        return int(np.argmax(self.attributions))

    def ranked_sources(self, k: int = 5) -> List[Dict[str, Any]]:
        if not self.valid:
            return []
        idx = np.argsort(self.attributions)[::-1][:k]
        return [{**self.sources[i], "weight": float(self.attributions[i])}
                for i in idx]


def _score_masks_spans(llm, sources, build_prompt, response,
                       spans: List[tuple], masks: np.ndarray,
                       batch_size: int) -> np.ndarray:
    prompts = [build_prompt([s for s, keep in zip(sources, m) if keep == 1])
               for m in masks]
    fn = getattr(llm, "log_prob_spans_batch", None)
    if fn is not None:
        return np.asarray(fn(prompts, response, spans, batch_size=batch_size),
                          dtype=np.float64)
    out = np.zeros((len(prompts), len(spans)), dtype=np.float64)
    for j, (start, end) in enumerate(spans):
        col = llm.log_prob_batch([p + response[:start] for p in prompts],
                                 response[start:end], batch_size=batch_size)
        out[:, j] = np.asarray(col, dtype=np.float64)
    return out


def _span_token_counts(llm, sources, build_prompt, response,
                       spans: List[tuple]) -> List[int]:
    fn = getattr(llm, "span_token_counts", None)
    if fn is not None:
        try:
            counts = fn(build_prompt(list(sources)), response, spans)
            if counts and all(c > 0 for c in counts):
                return list(counts)
        except Exception:
            pass
    return [max(1, round(len(response[s:e]) / 4)) for s, e in spans]


def _fit_surrogate(X: np.ndarray, y: np.ndarray, num_output_tokens: int,
                   alpha: float, seed: int):
    from sklearn.linear_model import Lasso
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    n_tok = max(1, int(num_output_tokens))
    scaler = StandardScaler()
    lasso = Lasso(alpha=alpha, random_state=seed, fit_intercept=True,
                  max_iter=20000)
    make_pipeline(scaler, lasso).fit(X.astype(np.float64), y / n_tok)
    scale = np.where(scaler.scale_ == 0, 1.0, scaler.scale_)
    weight = lasso.coef_ / scale
    bias = float(lasso.intercept_ - (scaler.mean_ / scale) @ lasso.coef_.T)
    return weight * n_tok, bias * n_tok


def _failed_result(sources, statement, reason, d) -> ContextCiteResult:
    return ContextCiteResult(
        sources=sources, attributions=[0.0] * d, intercept=0.0, masks=[],
        log_probs=[], original_log_prob=float("nan"),
        empty_log_prob=float("nan"), lds=None, lds_insample=None, n_heldout=0,
        top_k_drops={}, num_ablations=0, lambd=0.0, statement=statement,
        valid=False, status="failed", invalid_reason=reason,
        num_valid_ablations=0, num_failed_ablations=0,
    )


def contextcite_note(
    llm,
    sources: List[Dict[str, Any]],
    build_prompt: Callable[[List[Dict[str, Any]]], str],
    response: str,
    spans: List[tuple],
    num_ablations: int = 32,
    heldout_ablations: int = 32,
    lambd: float = 0.01,
    seed: int = 1234,
    score_batch_size: int = 8,
    top_k: List[int] = (1, 3),
    score_topk_masks: bool = True,
    leave_one_out: bool = False,
) -> List[ContextCiteResult]:
    d = len(sources)
    if not spans:
        return []
    if d == 0:
        return [_failed_result(sources, response[s:e],
                               "no sources retrieved for this edit", d)
                for s, e in spans]

    rng = np.random.default_rng(seed)
    fit_masks, held_masks = _sample_masks(rng, d, num_ablations,
                                          heldout_ablations)
    ones = np.ones((1, d), dtype=np.int64)
    zeros = np.zeros((1, d), dtype=np.int64)
    loo_masks = (np.ones((d, d), dtype=np.int64) - np.eye(d, dtype=np.int64)
                 if leave_one_out else np.zeros((0, d), dtype=np.int64))
    all_masks = np.vstack([fit_masks, held_masks, ones, zeros, loo_masks])
    n_fit, n_held = fit_masks.shape[0], held_masks.shape[0]
    i_ones, i_zeros = n_fit + n_held, n_fit + n_held + 1
    i_loo = n_fit + n_held + 2

    scores = _score_masks_spans(llm, sources, build_prompt, response, spans,
                                all_masks, score_batch_size)
    tok_counts = _span_token_counts(llm, sources, build_prompt, response, spans)

    results: List[ContextCiteResult] = []
    pending: Dict[bytes, np.ndarray] = {}
    plans: List[Dict[int, Optional[bytes]]] = []

    fitted: List[Dict[str, Any]] = []
    for j, (start, end) in enumerate(spans):
        col = scores[:, j]
        ok = _finite(col)
        statement = response[start:end]
        invalid: List[str] = []
        min_valid = max(2, min(8, n_fit), math.ceil(n_fit / 2))
        boundary_ok = bool(ok[i_ones] and ok[i_zeros])
        n_fit_ok = int(ok[:n_fit].sum())
        if not boundary_ok:
            invalid.append("full or empty boundary score failed")
        if n_fit_ok < min_valid:
            invalid.append(f"only {n_fit_ok}/{n_fit} fitting scores usable; "
                           f"need {min_valid}")
        status = "failed" if invalid else "attributed"
        valid = status == "attributed"

        X = fit_masks[ok[:n_fit]].astype(np.float64)
        y = to_logit(col[:n_fit][ok[:n_fit]])
        attribs = np.zeros(d, dtype=np.float64)
        intercept = float(y.mean()) if y.size else 0.0
        lds_held = lds_in = None

        if valid and float(y.std()) < 1e-9:
            status, valid = "no_source_effect", False
            invalid.append("log-prob is identical under every ablation; "
                           "the edit does not depend on any source")
        elif valid:
            try:
                attribs, intercept = _fit_surrogate(X, y, tok_counts[j],
                                                    lambd, seed)
                pred_fit = X @ attribs + intercept
                lds_in = _spearman(y, pred_fit)
                if n_held >= MIN_HELDOUT_FOR_LDS:
                    hok = ok[n_fit:n_fit + n_held]
                    Xh = held_masks[hok].astype(np.float64)
                    yh = to_logit(col[n_fit:n_fit + n_held][hok])
                    if yh.size >= 5 and float(np.std(yh)) > 1e-9:
                        lds_held = _spearman(yh, Xh @ attribs + intercept)
                if not np.any(np.abs(attribs) > 1e-9):
                    status, valid = "no_source_effect", False
                    attribs = np.zeros(d, dtype=np.float64)
                    invalid.append("LASSO shrank every source weight to zero; "
                                   "no individual source is load-bearing")
                elif lds_in is None and float(np.std(pred_fit)) < 1e-9:
                    status, valid = "no_source_effect", False
                    invalid.append("surrogate predictions are constant; "
                                   "LDS is undefined")
            except Exception as e:
                status, valid = "failed", False
                invalid.append(f"surrogate fitting failed: {type(e).__name__}")

        plan: Dict[int, Optional[bytes]] = {}
        if valid and score_topk_masks:
            order = np.argsort(attribs)[::-1]
            for k in top_k:
                k = int(k)
                if k <= 0 or k > d:
                    continue
                m = np.ones(d, dtype=np.int64)
                m[order[:k]] = 0
                key = m.tobytes()
                pending.setdefault(key, m)
                plan[k] = key
        plans.append(plan)

        fitted.append({
            "col": col, "ok": ok, "statement": statement, "invalid": invalid,
            "status": status, "valid": valid, "attribs": attribs,
            "intercept": intercept, "lds_held": lds_held, "lds_in": lds_in,
        })

    topk_scores: Dict[bytes, np.ndarray] = {}
    if pending:
        keys = list(pending)
        extra = _score_masks_spans(llm, sources, build_prompt, response, spans,
                                   np.vstack([pending[k] for k in keys]),
                                   score_batch_size)
        topk_scores = {k: extra[i] for i, k in enumerate(keys)}
    extra_per_span = len(pending)

    for j, f in enumerate(fitted):
        col, ok = f["col"], f["ok"]
        original_lp = float(col[i_ones])
        empty_lp = float(col[i_zeros])
        drops: Dict[int, Optional[float]] = {int(k): None for k in top_k}
        for k, key in plans[j].items():
            lp = float(topk_scores[key][j]) if key in topk_scores else float("nan")
            if np.isfinite(lp) and lp > -9999:
                drops[k] = float(original_lp - lp)

        loo_effects: Optional[List[Optional[float]]] = None
        n_relevant = loo_top1 = None
        if leave_one_out and np.isfinite(original_lp) and original_lp > -9999:
            effs: List[Optional[float]] = [
                (float(original_lp - col[i_loo + i]) if ok[i_loo + i] else None)
                for i in range(d)
            ]
            measured = [(i, e) for i, e in enumerate(effs) if e is not None]
            if measured:
                loo_effects = effs
                n_relevant = sum(1 for _, e in measured if abs(e) >= _DELTA2)
                loo_top1 = max(measured, key=lambda ie: ie[1])[0]

        results.append(ContextCiteResult(
            sources=sources,
            attributions=np.asarray(f["attribs"]).tolist(),
            intercept=float(f["intercept"]),
            masks=all_masks.tolist(),
            log_probs=col.tolist(),
            original_log_prob=original_lp,
            empty_log_prob=empty_lp,
            lds=f["lds_held"],
            lds_insample=f["lds_in"],
            n_heldout=int(n_held),
            top_k_drops=drops,
            num_ablations=n_fit,
            lambd=lambd,
            statement=f["statement"],
            valid=f["valid"],
            status=f["status"],
            invalid_reason="; ".join(f["invalid"]) or None,
            num_valid_ablations=int(ok.sum()),
            num_failed_ablations=int(len(ok) - ok.sum()),
            extra_calls=extra_per_span,
            loo_effects=loo_effects,
            n_relevant_sources=n_relevant,
            loo_top1=loo_top1,
        ))
    return results


def contextcite(
    llm,
    sources: List[Dict[str, Any]],
    build_prompt: Callable[[List[Dict[str, Any]]], str],
    response: str,
    statement_start: int = 0,
    statement_end: Optional[int] = None,
    num_ablations: int = 32,
    heldout_ablations: int = 32,
    lambd: float = 0.01,
    seed: int = 1234,
    score_batch_size: int = 8,
    top_k: List[int] = (1, 3),
    score_topk_masks: bool = True,
    leave_one_out: bool = False,
) -> ContextCiteResult:
    end = len(response) if statement_end is None else statement_end
    return contextcite_note(
        llm, sources, build_prompt, response, [(statement_start, end)],
        num_ablations=num_ablations, heldout_ablations=heldout_ablations,
        lambd=lambd, seed=seed, score_batch_size=score_batch_size,
        top_k=top_k, score_topk_masks=score_topk_masks,
        leave_one_out=leave_one_out,
    )[0]

def format_result(result: ContextCiteResult, show_sources: int = 4) -> str:
    lines = [
        f"      statement : {result.statement.strip()[:110]!r}",
        f"      scored    : {result.num_valid_ablations}/"
        f"{result.num_valid_ablations + result.num_failed_ablations} masks"
        f"  (+{result.extra_calls} top-k)   sources: {len(result.sources)}",
        f"      status    : {result.status}"
        + (f"  - {result.invalid_reason}" if result.invalid_reason else ""),
    ]
    if result.measurable:
        lines.append(
            f"      log p     : full {result.original_log_prob:+.2f}   "
            f"empty {result.empty_log_prob:+.2f}   "
            f"effect {result.source_effect:+.2f} nats "
            f"(logit {result.source_effect_logit:+.2f})"
        )
    if result.valid:
        lds_s = f"{result.lds:+.3f}" if result.lds is not None else "n/a"
        lds_i = f"{result.lds_insample:+.3f}" if result.lds_insample is not None else "n/a"
        drops = "  ".join(
            f"top{k}={v:+.2f}" if v is not None else f"top{k}=n/a"
            for k, v in sorted(result.top_k_drops.items())
        )
        lines.append(f"      LDS       : held-out {lds_s}  (in-sample {lds_i})   {drops}")
        if result.n_relevant_sources is not None:
            agree = ("same" if result.loo_top1 == result.lasso_top1 else "DIFFERS")
            lines.append(
                f"      leave-1-out: {result.n_relevant_sources}/"
                f"{len(result.sources)} sources relevant at delta=2   "
                f"top-1 vs LASSO: {agree}")
        for s in result.ranked_sources(show_sources):
            if abs(s.get("weight", 0.0)) < 1e-9:
                continue
            lines.append(f"        {s['weight']:+7.3f}  [{s.get('source','?')}] "
                         f"{str(s.get('text', ''))[:80]}")
    return "\n".join(lines)
