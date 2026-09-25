"""Focused paired statistics reported in the thesis: two-sided Wilcoxon tests, bootstrap
intervals and one Benjamini-Hochberg correction per contrast.

Usage:
    python analysis/focused_paper_statistics.py runs/run100_20260815_222318 [--write]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from metrics.stats import benjamini_hochberg, compare_arms

FOCUSED_METRICS: Tuple[str, ...] = (
    "human_edit_recall",
    "fkgl_drop",
    "coleman_liau_drop",
    "nli_faithfulness",
    "nli_completeness",
    "critical_error",
)

CONTRASTS: Tuple[Tuple[str, str], ...] = (
    ("termonly", "naive"),
    ("grounded", "termonly"),
)


def _rows(notes: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [
        {"note_idx": note["note_idx"], "arms": note.get("arms") or {}}
        for note in notes
    ]


def _model_dirs(run_dir: Path) -> List[Path]:
    return sorted(
        path for path in run_dir.iterdir()
        if path.is_dir() and (path / "notes.json").is_file()
    )


def analyse(run_dir: Path) -> Dict[str, Any]:
    model_rows: Dict[str, List[Dict[str, Any]]] = {}
    for model_dir in _model_dirs(run_dir):
        notes = json.loads((model_dir / "notes.json").read_text(encoding="utf-8"))
        model_rows[model_dir.name] = _rows(notes)

    contrasts: Dict[str, Any] = {}
    for arm_a, arm_b in CONTRASTS:
        records: List[Dict[str, Any]] = []
        for model, rows in model_rows.items():
            comparison = compare_arms(
                rows,
                arm_a,
                arm_b,
                list(FOCUSED_METRICS),
                alpha=0.05,
                alternative="two-sided",
            )
            for metric_name in FOCUSED_METRICS:
                metric = comparison["metrics"][metric_name]
                wilcoxon = metric.get("wilcoxon") or {}
                raw_p = wilcoxon.get("p_value")
                if not isinstance(raw_p, (int, float)):
                    continue
                bootstrap = metric.get("bootstrap") or {}
                oriented_difference = metric["diff"] * metric["direction"]
                records.append({
                    "model": model,
                    "metric": metric_name,
                    "n_pairs": metric["n_pairs"],
                    "direction": metric["direction"],
                    "mean_a": metric["mean_a"],
                    "mean_b": metric["mean_b"],
                    "diff_a_minus_b": metric["diff"],
                    "ci_lo": bootstrap.get("ci_lo"),
                    "ci_hi": bootstrap.get("ci_hi"),
                    "raw_p_two_sided": float(raw_p),
                    "effect_direction": (
                        "improvement" if oriented_difference > 0
                        else "deterioration" if oriented_difference < 0
                        else "tie"
                    ),
                })

        adjusted, rejected = benjamini_hochberg(
            [record["raw_p_two_sided"] for record in records], alpha=0.05
        )
        for record, adjusted_p, significant in zip(records, adjusted, rejected):
            record["p_adjusted_bh"] = adjusted_p
            record["significant_after_fdr"] = bool(significant)

        key = f"{arm_a}_vs_{arm_b}"
        contrasts[key] = {
            "arm_a": arm_a,
            "arm_b": arm_b,
            "n_tests": len(records),
            "n_significant": sum(
                record["significant_after_fdr"] for record in records
            ),
            "correction": (
                "benjamini-hochberg-fdr across all valid model-metric tests "
                "within this contrast"
            ),
            "records": records,
        }

    return {
        "run_dir": str(run_dir),
        "analysis": "post_hoc_focused_paper_tier_two_sided",
        "selection_rule": (
            "paper-tier, directional, sentence-level metrics available in both arms"
        ),
        "metrics": list(FOCUSED_METRICS),
        "contrasts": contrasts,
    }


def _format_p(value: float) -> str:
    return "<0.0001" if value < 0.0001 else f"{value:.4f}"


def render_markdown(result: Dict[str, Any]) -> str:
    lines = [
        "# Focused paper-tier statistical analysis",
        "",
        "This post hoc analysis includes only the six paper-tier metrics that",
        "are directional, measured per sentence, and available in both arms.",
        "It uses two-sided paired Wilcoxon tests and one Benjamini-Hochberg",
        "correction across all valid model-metric tests within each contrast.",
        "No generation or metric value was changed.",
        "",
        "Metrics: " + ", ".join(f"`{name}`" for name in result["metrics"]) + ".",
        "",
    ]

    for contrast in result["contrasts"].values():
        lines.extend([
            f"## {contrast['arm_a']} versus {contrast['arm_b']}",
            "",
            f"{contrast['n_significant']} of {contrast['n_tests']} valid tests "
            "survive contrast-wide FDR correction.",
            "",
            "| Model | Metric | n | Mean A | Mean B | A - B | 95% CI | Adjusted p | Result |",
            "|---|---|---:|---:|---:|---:|---|---:|---|",
        ])
        for record in contrast["records"]:
            adjusted = _format_p(record["p_adjusted_bh"])
            significant = record["significant_after_fdr"]
            result_label = record["effect_direction"] if significant else "not significant"
            lines.append(
                f"| `{record['model']}` | `{record['metric']}` | "
                f"{record['n_pairs']} | {record['mean_a']:.3f} | "
                f"{record['mean_b']:.3f} | {record['diff_a_minus_b']:+.3f} | "
                f"[{record['ci_lo']:+.3f}, {record['ci_hi']:+.3f}] | "
                f"{adjusted} | {result_label} |"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    if not args.run_dir.is_dir():
        parser.error(f"run directory does not exist: {args.run_dir}")

    result = analyse(args.run_dir)
    markdown = render_markdown(result)
    if args.write:
        json_path = args.run_dir / "focused_paper_statistics.json"
        markdown_path = args.run_dir / "FOCUSED_PAPER_STATISTICS.md"
        json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        markdown_path.write_text(markdown, encoding="utf-8")
        print(json_path)
        print(markdown_path)
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
