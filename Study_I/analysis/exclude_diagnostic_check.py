"""Recomputes the high-risk rate without the diagnostic-identity check (the rates reported
in the thesis) and repeats the focused statistics. Makes no API calls.

Usage:
    python analysis/exclude_diagnostic_check.py runs/run100_20260815_222318 --output-prefix runs/diagnostic_check_exclusion
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True

from analysis.focused_paper_statistics import CONTRASTS, FOCUSED_METRICS
from metrics.stats import benjamini_hochberg, compare_arms


def focused_statistics(model_rows: dict[str, list[dict[str, Any]]]) -> dict:
    contrasts = {}
    for arm_a, arm_b in CONTRASTS:
        records = []
        untested = []
        for model, rows in model_rows.items():
            comparison = compare_arms(
                rows, arm_a, arm_b, list(FOCUSED_METRICS),
                alpha=0.05, alternative="two-sided",
            )
            for metric_name in FOCUSED_METRICS:
                metric = comparison["metrics"][metric_name]
                bootstrap = metric.get("bootstrap") or {}
                test = metric.get("wilcoxon") or {}
                oriented = metric["diff"] * metric["direction"]
                record = {
                    "model": model,
                    "metric": metric_name,
                    "n_pairs": metric["n_pairs"],
                    "direction": metric["direction"],
                    "mean_a": metric["mean_a"],
                    "mean_b": metric["mean_b"],
                    "diff_a_minus_b": metric["diff"],
                    "ci_lo": bootstrap.get("ci_lo"),
                    "ci_hi": bootstrap.get("ci_hi"),
                    "raw_p_two_sided": test.get("p_value"),
                    "effect_direction": (
                        "improvement" if oriented > 0
                        else "deterioration" if oriented < 0 else "tie"
                    ),
                }
                if record["raw_p_two_sided"] is None:
                    untested.append(record)
                else:
                    records.append(record)

        adjusted, rejected = benjamini_hochberg(
            [record["raw_p_two_sided"] for record in records], alpha=0.05
        )
        for record, adjusted_p, significant in zip(records, adjusted, rejected):
            record["p_adjusted_bh"] = adjusted_p
            record["significant_after_fdr"] = bool(significant)
        contrasts[f"{arm_a}_vs_{arm_b}"] = {
            "arm_a": arm_a,
            "arm_b": arm_b,
            "n_tests": len(records),
            "n_significant": sum(rejected),
            "records": records,
            "untested": untested,
        }
    return contrasts


def verify_baseline(computed: dict, saved: dict) -> None:
    assert tuple(saved["metrics"]) == FOCUSED_METRICS
    for contrast_name, contrast in saved["contrasts"].items():
        actual = computed[contrast_name]
        assert actual["n_tests"] == contrast["n_tests"]
        assert actual["n_significant"] == contrast["n_significant"]
        actual_rows = {
            (record["model"], record["metric"]): record
            for record in actual["records"]
        }
        assert len(actual_rows) == len(contrast["records"])
        for expected in contrast["records"]:
            row = actual_rows[(expected["model"], expected["metric"])]
            for key, value in expected.items():
                if isinstance(value, float):
                    assert math.isclose(
                        value, row[key], rel_tol=1e-10, abs_tol=1e-12
                    ), (contrast_name, expected["model"], expected["metric"], key)
                else:
                    assert row[key] == value, (contrast_name, key)


def analyse(run_dir: Path) -> dict:
    run_dir = run_dir.resolve()
    saved_path = run_dir / "focused_paper_statistics.json"
    saved = json.loads(saved_path.read_text(encoding="utf-8"))
    models = sorted({
        record["model"]
        for contrast in saved["contrasts"].values()
        for record in contrast["records"]
    })
    inputs = [saved_path, run_dir / "manifest.json"]
    inputs += [
        run_dir / model / filename
        for model in models for filename in ("notes.json", "evaluation.json")
    ]
    hashes = {
        str(filename.relative_to(run_dir)):
        hashlib.sha256(filename.read_bytes()).hexdigest()
        for filename in inputs
    }
    original = {}
    revised = {}
    changed_outputs = []
    rates = []
    arms = ("naive", "termonly", "grounded")

    for model in models:
        notes = json.loads((run_dir / model / "notes.json").read_text(encoding="utf-8"))
        original[model] = [
            {"note_idx": note["note_idx"], "arms": {
                arm: {"metrics": copy.deepcopy(note["arms"][arm]["metrics"])}
                for arm in arms
            }}
            for note in notes
        ]
        revised[model] = copy.deepcopy(original[model])
        for note, updated in zip(notes, revised[model]):
            for arm in arms:
                record = note["arms"][arm]
                flags = [
                    flag for flag in record["detail"]["safety"]["safety_flags"]
                    if flag["severity"] == "critical"
                ]
                old_value = record["metrics"]["critical_error"]
                assert old_value == float(bool(flags)), (
                    model, arm, note["note_idx"], "Stored composite differs from flags"
                )
                new_value = float(any(
                    flag["slot"] != "diagnostic_identity" for flag in flags
                ))
                updated["arms"][arm]["metrics"]["critical_error"] = new_value
                if new_value != old_value:
                    changed_outputs.append({
                        "model": model, "arm": arm, "note_idx": note["note_idx"],
                        "original": note.get("original_clean") or note["original"],
                        "output": record["output"],
                        "before": old_value, "after": new_value,
                        "removed_flags": flags,
                    })
        for arm in arms:
            before = sum(row["arms"][arm]["metrics"]["critical_error"] for row in original[model])
            after = sum(row["arms"][arm]["metrics"]["critical_error"] for row in revised[model])
            rates.append({
                "model": model, "arm": arm, "n": len(notes),
                "original_count": int(before), "revised_count": int(after),
                "original_rate": before / len(notes),
                "revised_rate": after / len(notes),
            })

    baseline = focused_statistics(original)
    verify_baseline(baseline, saved)
    recomputed = focused_statistics(revised)
    changed_rows = []
    for name, old_contrast in baseline.items():
        new_contrast = recomputed[name]
        assert [(row["model"], row["metric"]) for row in old_contrast["records"]] == [
            (row["model"], row["metric"]) for row in new_contrast["records"]
        ]
        for before, after in zip(old_contrast["records"], new_contrast["records"]):
            if before != after:
                changed_rows.append({"contrast": name, "before": before, "after": after})

    for filename in inputs:
        assert hashlib.sha256(filename.read_bytes()).hexdigest() == hashes[str(filename.relative_to(run_dir))]
    return {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "run_dir": run_dir.name,
        "analysis": "post_hoc_exclusion_of_diagnostic_identity_from_high_risk_rate",
        "reason": "Fixed acceptance vocabulary lacked documented independent clinical validation and produced wording-dependent flags.",
        "scope": "Only the composite high-risk indicator is recomputed. No model outputs, human references, other metric values or original run files are changed.",
        "retained_critical_slots": ["negation", "uncertainty", "laterality", "number_unit", "severity_downgrade"],
        "drug_retention": "Already excluded from the composite under the executed replace policy.",
        "statistical_method": "Original six-outcome families, two-sided Wilcoxon with zsplit, 10000 paired bootstrap samples with seed 1234, and contrast-wide Benjamini-Hochberg at 0.05.",
        "baseline_statistics_reproduced": True,
        "input_sha256": hashes,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "rates": rates,
        "changed_outputs": changed_outputs,
        "changed_statistical_rows": changed_rows,
        "baseline_contrasts": baseline,
        "revised_contrasts": recomputed,
        "significance_decisions_changed": sum(
            row["before"]["significant_after_fdr"] != row["after"]["significant_after_fdr"]
            for row in changed_rows
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Diagnostic-Check Exclusion Reanalysis", "",
        "This is a disclosed post-hoc change to the reported high-risk rate, not a new experiment.",
        "No independent clinical validation of the fixed diagnostic acceptance list was documented. Removing its flags does not establish that the affected outputs are clinically correct, or validate the remaining checks.", "",
        "The original saved run is unchanged. All original focused estimates, bootstrap intervals and p-values were reproduced before the revised calculation.", "",
        "## Rates", "",
        "| Model | Arm | Sentences | Original flagged | Revised flagged | Original rate | Revised rate |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in report["rates"]:
        lines.append(f"| {row['model']} | {row['arm']} | {row['n']} | {row['original_count']} | {row['revised_count']} | {row['original_rate']:.3f} | {row['revised_rate']:.3f} |")
    lines += ["", "## Statistical Impact", ""]
    for name, contrast in report["revised_contrasts"].items():
        original = report["baseline_contrasts"][name]
        lines.append(f"- {name}: {original['n_significant']} of {original['n_tests']} significant before, {contrast['n_significant']} of {contrast['n_tests']} after.")
    lines += [
        f"- Significance decisions changed: {report['significance_decisions_changed']}.",
        "- Family-wide correction is recomputed, so adjusted p-values can change even for an unchanged metric.",
        "- The JSON report records every original and revised focused comparison, including untested all-tie pairs.",
        "", "## Changed Output Flags", "",
    ]
    for record in report["changed_outputs"]:
        lines += [
            f"### {record['model']}, {record['arm']}, Note {record['note_idx']}", "",
            f"Original: {record['original']}", "",
            f"Saved output: {record['output']}", "",
            f"Composite flag: {record['before']:.0f} to {record['after']:.0f}. No other active critical flag was present.", "",
        ]
    lines += [
        "## Reproduction", "",
        "Run the following from `Study_I`. The output prefix is outside the saved run.", "",
        "```bash",
        "python analysis/exclude_diagnostic_check.py runs/run100_20260815_222318 --output-prefix runs/diagnostic_check_exclusion",
        "```", "",
        "Without --output-prefix the script only prints this report. It makes no API calls.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--output-prefix", type=Path)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    if args.output_prefix:
        prefix = args.output_prefix.resolve()
        if prefix == run_dir or run_dir in prefix.parents:
            parser.error("Reports must be written outside the original run directory.")
    report = analyse(run_dir)
    markdown = render_markdown(report)
    if args.output_prefix:
        prefix.parent.mkdir(parents=True, exist_ok=True)
        prefix.with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        prefix.with_suffix(".md").write_text(markdown, encoding="utf-8")
    print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
