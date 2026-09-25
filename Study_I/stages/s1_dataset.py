"""Stage 1: loads the evaluation sentences and profiles them."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from config import Config


def load_notes(cfg: Config) -> List[Dict[str, Any]]:
    if cfg.dataset == "fixture5":
        notes = _load_fixture(cfg.root / "fixtures" / "audit_5notes.json")
    elif cfg.dataset == "laymaker":
        notes = _load_laymaker(cfg.root / "data" / "laymaker_grade3_plain.json")
    else:
        raise SystemExit(f"[dataset] unknown dataset {cfg.dataset!r}")

    if cfg.num_notes and cfg.num_notes > 0:
        notes = notes[: cfg.num_notes]
    for i, n in enumerate(notes, start=1):
        n["note_idx"] = i
    return notes


def _load_fixture(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"[dataset] missing fixture {path}")
    raw = json.loads(path.read_text(encoding="utf-8-sig"))
    cases = raw["cases"] if isinstance(raw, dict) and "cases" in raw else raw
    out = []
    for c in cases:
        out.append({
            "id": c.get("case_id") or c.get("id"),
            "difficulty": c.get("difficulty"),
            "original": (c.get("original") or "").strip(),
            "reference": (c.get("reference") or "").strip(),
            "target_terms": c.get("target_terms") or [],
            "safety_facts": c.get("safety_facts") or [],
        })
    return [n for n in out if n["original"]]


def _ref_quality(ref: str) -> tuple:
    complete = bool(ref) and ref.rstrip()[-1:] in ".!?"
    try:
        import textstat
        grade = textstat.flesch_kincaid_grade(ref)
    except Exception:
        grade = 0.0
    return (0 if complete else 1, grade)


def _dedupe_by_input(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    best: Dict[str, Dict[str, Any]] = {}
    order: List[str] = []
    dropped: List[tuple] = []
    for r in rows:
        key = r["original"].strip().lower()
        if key not in best:
            best[key] = r
            order.append(key)
            continue
        cur = best[key]
        if (_ref_quality(r["reference"]), str(r["id"])) < \
           (_ref_quality(cur["reference"]), str(cur["id"])):
            best[key], loser = r, cur
        else:
            loser = r
        dropped.append((loser["id"], best[key]["id"]))
    if dropped:
        print(f"  [dedupe] {len(rows)} rows -> {len(best)} unique sentences; "
              f"kept the better reference of {len(dropped)} duplicate pair(s)")
        for lost, kept in dropped:
            print(f"           dropped id={lost} (kept id={kept})")
    return [best[k] for k in order]


def _load_laymaker(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"[dataset] missing {path}")
    rows = json.loads(path.read_text(encoding="utf-8-sig"))
    out = []
    for r in rows:
        orig = (r.get("ORIGINAL") or "").strip()
        ref = (r.get("REFERENCE") or "").strip()
        if not orig:
            continue
        out.append({
            "id": r.get("ID"),
            "difficulty": None,
            "original": orig,
            "reference": ref or orig,
            "grade": r.get("grade"),
        })
    return _dedupe_by_input(out)


def dataset_profile(notes: List[Dict[str, Any]]) -> Dict[str, Any]:
    import re
    import statistics

    try:
        import textstat
    except ImportError:
        textstat = None

    def toks(s: str) -> set:
        return set(re.findall(r"[a-z0-9]+", (s or "").lower()))

    n = len(notes)
    if not n:
        return {}
    jac, removed, added = [], [], []
    for r in notes:
        a, b = toks(r["original"]), toks(r["reference"])
        union = a | b
        jac.append(len(a & b) / len(union) if union else 0.0)
        removed.append(len(a - b))
        added.append(len(b - a))
    prof: Dict[str, Any] = {
        "n_notes": n,
        "mean_words_original": round(statistics.fmean(
            len(r["original"].split()) for r in notes), 2),
        "mean_words_reference": round(statistics.fmean(
            len(r["reference"].split()) for r in notes), 2),
        "mean_token_jaccard_orig_ref": round(statistics.fmean(jac), 3),
        "mean_tokens_removed_by_reference": round(statistics.fmean(removed), 2),
        "mean_tokens_added_by_reference": round(statistics.fmean(added), 2),
    }
    if textstat is not None:
        prof["mean_fkgl_original"] = round(statistics.fmean(
            textstat.flesch_kincaid_grade(r["original"]) for r in notes), 2)
        prof["mean_fkgl_reference"] = round(statistics.fmean(
            textstat.flesch_kincaid_grade(r["reference"]) for r in notes), 2)
    prof["note"] = (
        "References are minimal-edit lexical replacements. SARI and BERTScore "
        "against them under-credit any system that also restructures grammar; "
        "see metrics/sari.py for the worked counter-example."
    )
    return prof
