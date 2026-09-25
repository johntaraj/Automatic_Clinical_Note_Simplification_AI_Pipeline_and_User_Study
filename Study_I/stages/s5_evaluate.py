"""Evaluation (Stage 8 in the thesis): per-note metrics for every arm and paired arm comparisons."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from config import Config
from core.io import rule
from metrics import attribution as attr_metrics
from metrics import coverage as cov_metrics
from metrics import neural
from metrics.edits import edit_replacement
from metrics.readability import length_ratio, readability, readability_deltas
from metrics.safety import clinical_safety
from metrics.sari import sari_components, sari_sentence
from metrics.stats import compare_arms

COMPARISON_METRICS = [
    "sari", "bertscore_f1",
    "fkgl_drop", "smog_drop", "coleman_liau_drop",
    "nli_faithfulness", "nli_completeness",
    "human_edit_recall",
    "critical_error", "drug_preservation", "number_unit_preservation",
    "diagnostic_identity_preservation", "severity_downgrade",
]


def _flatten(m: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in m.items()
            if isinstance(v, (int, float)) or v is None}


def run(cfg: Config, notes: List[Dict[str, Any]]) -> Dict[str, Any]:
    torch_on = cfg.enable_torch_evals

    for note in notes:
        orig = note.get("original_clean") or note["original"]
        ref = note.get("reference", "")
        input_m = readability(orig)
        note["input_metrics"] = input_m
        note["reference_metrics"] = readability(ref)
        hard_items = note.get("hard_items", [])

        for arm, rec in (note.get("arms") or {}).items():
            out = (rec or {}).get("output", "") or ""
            m: Dict[str, Any] = {}
            if not out.strip():
                rec["metrics"] = {}
                rec["detail"] = {}
                continue

            m.update(readability(out))
            m.update(readability_deltas(m, input_m))
            m["length_ratio"] = length_ratio(out, ref)
            m["sari"] = sari_sentence(orig, out, [ref])

            detail: Dict[str, Any] = {
                "sari_components": sari_components(orig, out, [ref]),
            }

            ed = edit_replacement(orig, ref, out, hard_items)
            if ed:
                for k in ("human_edit_recall", "replacement_precision",
                          "replacement_f1", "copy_jargon_rate",
                          "definition_borrow_rate", "rewrite_aggressiveness",
                          "replacement_quality", "replacement_hit_rate",
                          "replacement_quality_edited",
                          "n_replacement_aligned", "n_replacement_edited",
                          "n_replacement_ambiguous"):
                    m[k] = ed[k]
                detail["edits"] = ed

            safe = clinical_safety(
                orig, out, drug_is_critical=(cfg.tag_policy != "replace"))
            if safe:
                for k, v in safe.items():
                    if isinstance(v, (int, float)) or v is None:
                        m[k] = v
                detail["safety"] = safe

            rec["metrics"] = m
            rec["detail"] = detail

    if torch_on:
        _attach_bertscore(cfg, notes)
        _attach_nli(cfg, notes)
        _attach_citations(cfg, notes)

    arms = list(cfg.arms)
    aggregate = {arm: _aggregate(notes, arm, arms) for arm in arms}

    reference_rows = {
        "input": _aggregate_rows([n.get("input_metrics") or {} for n in notes]),
        "reference": _aggregate_rows(
            [n.get("reference_metrics") or {} for n in notes]),
    }

    comparisons = []
    ladder = [(arms[i], arms[i - 1]) for i in range(1, len(arms))]
    if "grounded" in arms and "naive" in arms and ("grounded", "naive") not in ladder:
        ladder.append(("grounded", "naive"))
    for a, b in ladder:
        comparisons.append(compare_arms(_rows(notes), a, b,
                                        COMPARISON_METRICS, cfg.fdr_alpha))

    grounded_ops = []
    for note in notes:
        rec = (note.get("arms") or {}).get("grounded") or {}
        for op in rec.get("operations", []):
            op = dict(op)
            op["note_idx"] = note["note_idx"]
            grounded_ops.append(op)

    out = {
        "aggregate": aggregate,
        "reference_rows": reference_rows,
        "comparisons": comparisons,
        "attribution": attr_metrics.attribution_summary(
            grounded_ops, eps=cfg.cc_effect_threshold,
            lds_threshold=cfg.cc_attributable_lds,
            margin_threshold=cfg.cc_attributable_margin),
        "attribution_threshold_sweep": attr_metrics.threshold_sweep(
            grounded_ops, epsilons=cfg.cc_effect_threshold_sweep),
        "attribution_per_edit": attr_metrics.per_edit_table(
            grounded_ops, eps=cfg.cc_effect_threshold),
        "whole_term_coverage": cov_metrics.coverage_summary(notes, cfg.zipf_strata),
        "definition_readability": cov_metrics.definition_readability(notes),
        "source_alignment": cov_metrics.source_alignment_summary(notes),
        "stratified": _stratify(cfg, notes),
    }
    out["stage_metrics"] = _stage_metrics(notes, out)
    return out


def _stage_metrics(notes: List[Dict[str, Any]],
                   ev: Dict[str, Any]) -> Dict[str, Any]:
    cov = (ev.get("whole_term_coverage") or {}).get("overall") or {}
    align = (ev.get("source_alignment") or {}).get("overall") or {}
    split_align = (ev.get("source_alignment") or {}).get("split_adjusted") or {}
    attr = ev.get("attribution") or {}
    defs = ev.get("definition_readability") or {}
    stab = [n["extraction_stability"] for n in notes
            if isinstance(n.get("extraction_stability"), (int, float))]
    stability = round(sum(stab) / len(stab), 4) if stab else None

    out: Dict[str, Any] = {
        "whole_term_coverage": cov.get("coverage"),
        "evidence_coverage": cov.get("coverage_addressed"),
        "mean_defs_per_term": cov.get("mean_defs"),
        "n_expansion_definitions": (ev.get("whole_term_coverage") or {})
        .get("n_expansion_definitions"),
        "orphan_term_rate": align.get("orphan_term_rate"),
        "split_adjusted_orphan_rate": split_align.get(
            "split_adjusted_orphan_rate"),
        "on_term_sources": align.get("on_term_sources"),
        "definition_fkgl": defs.get("definition_fkgl"),
        "extraction_stability": stability,
        "attributable_rate": attr.get("attributable_rate"),
        "lds_median": attr.get("lds_median"),
        "lds_optimism_gap": attr.get("lds_optimism_gap"),
        "helped_rate": attr.get("helped_rate"),
        "hurt_rate": attr.get("hurt_rate"),
        "right_term_rate": attr.get("right_term_rate"),
        "oracle_agreement": attr.get("oracle_agreement"),
        "relevant_source_rate": attr.get("relevant_source_rate"),
        "n_relevant_sources_median": attr.get("n_relevant_sources_median"),
        "top1_drop_median": attr.get("top1_drop_median"),
        "top1_drop_median_helped": attr.get("top1_drop_median_helped"),
        "ablation_success_rate": attr.get("ablation_success_rate"),
    }
    return {k: v for k, v in out.items() if v is not None}


def _rows(notes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [{"note_idx": n["note_idx"], "arms": n.get("arms") or {}}
            for n in notes]


def _attach_bertscore(cfg: Config, notes: List[Dict[str, Any]]) -> None:
    targets = []
    for note in notes:
        for arm, rec in (note.get("arms") or {}).items():
            out = (rec or {}).get("output", "")
            if out and note.get("reference"):
                targets.append((rec, out, note["reference"]))
    if not targets:
        return
    scores = neural.bertscore_batch(
        [t[1] for t in targets], [t[2] for t in targets],
        cfg.bertscore_model, cfg.bertscore_layers, cfg.bertscore_rescale)
    if not scores:
        return
    for (rec, _, _), s in zip(targets, scores):
        if s is not None:
            rec.setdefault("metrics", {})["bertscore_f1"] = s


def _attach_nli(cfg: Config, notes: List[Dict[str, Any]]) -> None:
    for note in notes:
        orig = note.get("original_clean") or note["original"]
        for arm, rec in (note.get("arms") or {}).items():
            out = (rec or {}).get("output", "")
            if not out:
                continue
            f = neural.nli_faithfulness(orig, out, cfg.nli_model)
            c = neural.nli_completeness(orig, out, cfg.nli_model)
            if f is not None:
                rec.setdefault("metrics", {})["nli_faithfulness"] = f
            if c is not None:
                rec.setdefault("metrics", {})["nli_completeness"] = c


def _attach_citations(cfg: Config, notes: List[Dict[str, Any]]) -> None:
    for note in notes:
        rec = (note.get("arms") or {}).get("grounded")
        if not rec:
            continue
        cit = neural.citation_support(rec.get("operations", []), cfg.nli_model)
        if cit:
            rec.setdefault("detail", {})["citation"] = cit


def _aggregate(notes: List[Dict[str, Any]], arm: str,
               all_arms: List[str]) -> Dict[str, Any]:
    per_arm = [{a: (((n.get("arms") or {}).get(a) or {}).get("metrics") or {})
                for a in all_arms} for n in notes]

    keys: set = set()
    for row in per_arm:
        for a in all_arms:
            keys |= {k for k, v in row[a].items() if isinstance(v, (int, float))}

    agg: Dict[str, Any] = {
        "n_notes": sum(1 for row in per_arm if row.get(arm)),
    }
    for k in sorted(keys):
        paired = [row for row in per_arm
                  if all(isinstance(row[a].get(k), (int, float)) for a in all_arms)]
        vals = [row[arm][k] for row in paired]
        if vals:
            agg[k] = {
                "mean": round(sum(vals) / len(vals), 4),
                "n": len(vals),
                "min": round(min(vals), 4),
                "max": round(max(vals), 4),
            }
    n_total = len(notes)
    n_ok = sum(1 for n in notes
               if (((n.get("arms") or {}).get(arm) or {}).get("output") or "").strip())
    agg["n_notes_total"] = n_total
    agg["generation_success_rate"] = {
        "mean": round(n_ok / n_total, 4) if n_total else None,
        "n": n_total, "min": None, "max": None,
    }
    recs = [((n.get("arms") or {}).get(arm) or {}) for n in notes]
    attempts = [r.get("generation_attempts") for r in recs
                if isinstance(r.get("generation_attempts"), int)]
    if attempts:
        agg["generation_first_attempt_rate"] = {
            "mean": round(sum(1 for a in attempts if a == 1) / len(attempts), 4),
            "n": len(attempts), "min": min(attempts), "max": max(attempts),
        }
        agg["generation_attempts_mean"] = {
            "mean": round(sum(attempts) / len(attempts), 4),
            "n": len(attempts), "min": min(attempts), "max": max(attempts),
        }
    scored = [r for r in recs if (r.get("output") or "").strip()]
    if scored:
        n_clean = sum(1 for r in scored if not (r.get("output_problems") or []))
        agg["output_valid_rate"] = {
            "mean": round(n_clean / len(scored), 4),
            "n": len(scored), "min": None, "max": None,
        }
    return agg


def _aggregate_rows(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    rows = [r for r in rows if r]
    keys: set = set()
    for r in rows:
        keys |= {k for k, v in r.items() if isinstance(v, (int, float))}
    out: Dict[str, Any] = {"n_notes": len(rows)}
    for k in sorted(keys):
        vals = [r[k] for r in rows if isinstance(r.get(k), (int, float))]
        if vals:
            out[k] = {
                "mean": round(sum(vals) / len(vals), 4),
                "n": len(vals),
                "min": round(min(vals), 4),
                "max": round(max(vals), 4),
            }
    return out


def _stratify(cfg: Config, notes: List[Dict[str, Any]]) -> Dict[str, Any]:
    buckets: Dict[str, Dict[str, Any]] = {}
    for note in notes:
        gr = (note.get("arms") or {}).get("grounded") or {}
        for op in gr.get("operations", []):
            term = op.get("src_text") or ""
            z = cov_metrics.term_zipf(term)
            name = cov_metrics.zipf_stratum(z, cfg.zipf_strata)
            b = buckets.setdefault(name, {
                "n_edits": 0, "n_helped": 0, "n_neutral": 0, "n_hurt": 0,
                "n_failed": 0, "effects": [], "terms": [],
            })
            b["n_edits"] += 1
            if len(b["terms"]) < 25:
                b["terms"].append(term)
            cc = op.get("contextcite") or {}
            if not cc:
                continue
            status = cc.get("status") or ("attributed" if cc.get("valid") else "failed")
            if status == "failed":
                b["n_failed"] += 1
                continue
            eff = cc.get("source_effect")
            if eff is None:
                continue
            b["effects"].append(eff)
            if eff >= cfg.cc_effect_threshold:
                b["n_helped"] += 1
            elif eff <= -cfg.cc_effect_threshold:
                b["n_hurt"] += 1
            else:
                b["n_neutral"] += 1

    for b in buckets.values():
        eff = b.pop("effects")
        b["mean_source_effect"] = round(sum(eff) / len(eff), 4) if eff else None
        scored = b["n_helped"] + b["n_neutral"] + b["n_hurt"]
        b["helped_rate"] = round(b["n_helped"] / scored, 4) if scored else None

    cov = cov_metrics.coverage_summary(notes, cfg.zipf_strata)
    return {
        "edits_by_zipf_stratum": buckets,
        "coverage_by_zipf_stratum": cov.get("by_zipf_stratum", {}),
    }
