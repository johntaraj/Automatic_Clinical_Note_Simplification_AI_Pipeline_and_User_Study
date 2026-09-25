"""Regenerates Stages 6-7 for a finished run and re-scores it; generation and ContextCite
are left untouched.

Usage:
    python tools/redo_rationales.py runs/<run> [--models NAME ...]
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from config import preset_full100
from core.io import banner, load_json, save_json
from stages import s4_generate, s5_evaluate, s6_rationalize, s9_report


def _backup(path: Path) -> None:
    if path.exists():
        prev = path.with_suffix(path.suffix + ".prev")
        if not prev.exists():
            shutil.copy2(path, prev)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("run_dir")
    ap.add_argument("--models", nargs="+", default=None)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)

    run_dir = Path(a.run_dir).resolve()
    manifest = load_json(run_dir / "manifest.json", {}) or {}
    saved = manifest.get("config") or {}
    profile = manifest.get("dataset_profile") or {}

    cfg = preset_full100()
    cfg.use_cache = False
    for field in ("prompt_style", "tag_policy", "keep_gloss_scope",
                  "person_policy", "dataset", "num_notes", "arms"):
        if field in saved and hasattr(cfg, field):
            setattr(cfg, field, saved[field])

    targets = [d for d in sorted(run_dir.iterdir())
               if d.is_dir() and (d / "notes.json").exists()
               and (a.models is None or d.name in a.models)]
    if not targets:
        print(f"no completed models found under {run_dir}")
        return 1

    print(f"run              : {run_dir.name}")
    print(f"rationale budget : {cfg.rationale_max_tokens} tokens "
          f"(was 200 hardcoded)")
    print(f"models           : {', '.join(d.name for d in targets)}")
    if a.dry_run:
        return 0

    results = {}
    for d in targets:
        model_key = d.name
        banner(f"REDO rationales - {model_key}")
        notes = load_json(d / "notes.json", [])
        if not notes:
            print(f"  [skip] {model_key}: notes.json is empty")
            continue

        for name in ("evaluation.json", "notes.json", "report.md", "detail.md"):
            _backup(d / name)

        llm = s4_generate.make_llm(cfg, cfg.model_spec(model_key),
                                   require_echo=False)
        notes = s6_rationalize.run_rationales(cfg, llm, notes, "grounded")

        banner(f"audit - {model_key}")
        audit = s6_rationalize.run_audit(notes, "grounded")
        for k, v in audit.items():
            if isinstance(v, (int, float)):
                print(f"  {k:<34} {v}")

        evaluation = s5_evaluate.run(cfg, notes)
        evaluation["rationale_audit"] = audit

        save_json(d / "notes.json", notes)
        save_json(d / "evaluation.json", evaluation)
        s9_report.write(d / "report.md",
                        s9_report.build_report(cfg, model_key, notes,
                                               evaluation, profile))
        s9_report.write(d / "detail.md",
                        s9_report.build_detail(cfg, model_key, notes))
        results[model_key] = {"notes": notes, "evaluation": evaluation}
        print(f"  [saved] {d / 'evaluation.json'}  (.prev kept)")

    merged = dict(results)
    for d in sorted(run_dir.iterdir()):
        if not d.is_dir() or d.name in merged:
            continue
        ev = load_json(d / "evaluation.json", {})
        if ev and d.name in cfg.models:
            merged[d.name] = {"evaluation": ev}
    if merged:
        _backup(run_dir / "SUMMARY.md")
        s9_report.write(run_dir / "SUMMARY.md",
                        s9_report.cross_model_report(cfg, merged))
        print(f"\n  [saved] {run_dir / 'SUMMARY.md'}  ({len(merged)} models)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
