"""Removes duplicate, empty and self-referential glossary entries and writes
data/glossary_manifest.json. Audit only unless --write is given.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

DATA = ROOT / "data"
ARCHIVE = DATA / "archive"
MANIFEST = DATA / "glossary_manifest.json"

_STUB = re.compile(r"^(?:alt\.\s+of|of)\s+([A-Za-z][A-Za-z'\-]*)\.?$", re.I)
_LEADING_PUNCT = re.compile(r"^[,.;:\-\s]")
_REPLACEMENT_CHAR = "\ufffd"


def _raise_csv_limit() -> None:
    limit = sys.maxsize
    while True:
        try:
            csv.field_size_limit(limit)
            return
        except OverflowError:
            limit //= 10


_raise_csv_limit()


def _norm(text: str) -> str:
    t = unicodedata.normalize("NFKC", text or "").casefold()
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _clean_text(text: str) -> str:
    t = unicodedata.normalize("NFKC", text or "").replace(_REPLACEMENT_CHAR, "")
    return re.sub(r"\s+", " ", t).strip()


def clean_readme(path: Path) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))

    kept: List[Dict[str, Any]] = []
    seen: set = set()
    dropped_dup = dropped_empty = 0
    for row in rows:
        term = _clean_text(row.get("term", ""))
        definition = _clean_text(row.get("definition", ""))
        if not term or not definition:
            dropped_empty += 1
            continue
        key = (term.casefold(), _norm(definition))
        if key in seen:
            dropped_dup += 1
            continue
        seen.add(key)
        out = dict(row)
        out["term"] = term
        out["definition"] = definition
        kept.append(out)

    stats = {
        "rows_before": len(rows),
        "rows_after": len(kept),
        "dropped_exact_duplicate": dropped_dup,
        "dropped_empty": dropped_empty,
        "unique_terms_after": len({r["term"].casefold() for r in kept}),
    }
    return kept, stats


def clean_dictionary(path: Path) -> Tuple[List[Dict[str, str]], Dict[str, Any]]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    real: Dict[str, str] = {}
    for row in rows:
        word = _clean_text(row.get("word", ""))
        definition = _clean_text(row.get("definition", ""))
        if not word or not definition or _STUB.fullmatch(definition):
            continue
        real.setdefault(word.casefold(), definition)

    kept: List[Dict[str, str]] = []
    seen: set = set()
    resolved = dropped_stub = dropped_dup = dropped_empty = dropped_self = 0
    repaired_chars = 0
    for row in rows:
        word = _clean_text(row.get("word", ""))
        definition_raw = row.get("definition", "") or ""
        definition = _clean_text(definition_raw)
        if _REPLACEMENT_CHAR in definition_raw or _REPLACEMENT_CHAR in (row.get("word") or ""):
            repaired_chars += 1
        if not word or not definition:
            dropped_empty += 1
            continue

        stub = _STUB.fullmatch(definition)
        if stub:
            target = real.get(stub.group(1).strip().casefold())
            if target:
                definition = target
                resolved += 1
            else:
                dropped_stub += 1
                continue

        if _norm(definition) == _norm(word):
            dropped_self += 1
            continue

        key = (word.casefold(), _norm(definition))
        if key in seen:
            dropped_dup += 1
            continue
        seen.add(key)
        kept.append({"word": word, "pos": (row.get("pos") or "").strip(),
                     "definition": definition})

    stats = {
        "rows_before": len(rows),
        "rows_after": len(kept),
        "resolved_inflection_pointers": resolved,
        "dropped_unresolvable_pointer": dropped_stub,
        "dropped_duplicate": dropped_dup,
        "dropped_empty": dropped_empty,
        "dropped_self_definition": dropped_self,
        "rows_with_repaired_encoding": repaired_chars,
        "unique_words_after": len({r["word"].casefold() for r in kept}),
    }
    return kept, stats


def clean_dorland(path: Path) -> Tuple[List[Dict[str, str]], Dict[str, Any]]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    by_term: Dict[str, List[str]] = defaultdict(list)
    order: List[str] = []
    dropped_empty = dropped_junk = dropped_self = dropped_dup = 0
    for row in rows:
        term = _clean_text(row.get("term", ""))
        candidate = _clean_text(row.get("candidate", ""))
        if not term or not candidate:
            dropped_empty += 1
            continue
        if _LEADING_PUNCT.match(row.get("candidate", "")):
            dropped_junk += 1
            continue
        if _norm(candidate) == _norm(term):
            dropped_self += 1
            continue
        if term not in by_term:
            order.append(term)
        if any(_norm(c) == _norm(candidate) for c in by_term[term]):
            dropped_dup += 1
            continue
        by_term[term].append(candidate)

    kept: List[Dict[str, str]] = []
    for term in order:
        candidates = by_term.get(term) or []
        for i, candidate in enumerate(candidates):
            kept.append({
                "term": term,
                "candidate_id": str(i),
                "candidate": candidate,
                "num_candidates_for_term": str(len(candidates)),
            })

    stats = {
        "rows_before": len(rows),
        "rows_after": len(kept),
        "dropped_empty": dropped_empty,
        "dropped_sentence_fragment": dropped_junk,
        "dropped_self_definition": dropped_self,
        "dropped_duplicate": dropped_dup,
        "unique_terms_after": len(by_term),
        "note": "candidate_id and num_candidates_for_term are recomputed",
    }
    return kept, stats


def clean_simple_json(path: Path) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    raw = json.loads(path.read_text(encoding="utf-8-sig"))
    kept: List[Dict[str, Any]] = []
    seen: set = set()
    dropped_dup = dropped_empty = dropped_self = 0
    for obj in raw:
        if not isinstance(obj, dict):
            continue
        term = _clean_text(obj.get("term", ""))
        definition = _clean_text(obj.get("definition", ""))
        if not term or not definition:
            dropped_empty += 1
            continue
        if _norm(definition) == _norm(term):
            dropped_self += 1
            continue
        key = (term.casefold(), _norm(definition))
        if key in seen:
            dropped_dup += 1
            continue
        seen.add(key)
        out = dict(obj)
        out["term"] = term
        out["definition"] = definition
        kept.append(out)

    stats = {
        "rows_before": len(raw),
        "rows_after": len(kept),
        "dropped_duplicate": dropped_dup,
        "dropped_empty": dropped_empty,
        "dropped_self_definition": dropped_self,
        "unique_terms_after": len({r["term"].casefold() for r in kept}),
    }
    return kept, stats


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
    except Exception:
        try:
            os.unlink(temp)
        except OSError:
            pass
        raise


def _jsonl_bytes(rows: List[Dict[str, Any]]) -> bytes:
    body = "\n".join(json.dumps(r, ensure_ascii=False) for r in rows)
    return (body + "\n").encode("utf-8")


def _json_bytes(data: Any) -> bytes:
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def _csv_bytes(rows: List[Dict[str, str]], columns: List[str]) -> bytes:
    from io import StringIO
    buf = StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue().encode("utf-8")


JOBS = (
    ("readme_exp_good.jsonl", clean_readme, "jsonl", None),
    ("dictonary.csv", clean_dictionary, "csv", ["word", "pos", "definition"]),
    ("dorland_medical_abbreviations.csv", clean_dorland, "csv",
     ["term", "candidate_id", "candidate", "num_candidates_for_term"]),
    ("thesarus.json", clean_simple_json, "json", None),
    ("Iowa.json", clean_simple_json, "json", None),
    ("michigan_plmd.json", clean_simple_json, "json", None),
    ("justplainclear_en_clean.json", clean_simple_json, "json", None),
)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)

    manifest: Dict[str, Any] = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "tool": "tools/clean_glossaries.py",
        "note": ("nih.json is cleaned separately by tools/repair_nih.py and is "
                 "tracked in data/nih_manifest.json"),
        "files": {},
    }

    for name, cleaner, kind, columns in JOBS:
        path = DATA / name
        if not path.exists():
            print(f"[skip] {name} not found")
            continue
        rows, stats = cleaner(path)
        removed = stats["rows_before"] - stats["rows_after"]
        pct = 100 * removed / stats["rows_before"] if stats["rows_before"] else 0.0
        print(f"\n{name}")
        for key, value in stats.items():
            print(f"    {key:<34} {value}")
        print(f"    {'removed_total':<34} {removed}  ({pct:.1f}%)")

        content = (_jsonl_bytes(rows) if kind == "jsonl"
                   else _json_bytes(rows) if kind == "json"
                   else _csv_bytes(rows, columns or []))
        stats["output_sha256"] = hashlib.sha256(content).hexdigest()
        stats["archived_original"] = f"archive/{name}"
        manifest["files"][name] = stats

        if not args.write:
            continue
        archived = ARCHIVE / name
        if not archived.exists():
            _atomic_write(archived, path.read_bytes())
        _atomic_write(path, content)
        print(f"    archived -> {archived.relative_to(ROOT)}")
        print(f"    rewrote  -> {path.relative_to(ROOT)}")

    if args.write:
        _atomic_write(MANIFEST, _json_bytes(manifest))
        print(f"\nmanifest -> {MANIFEST.relative_to(ROOT)}")
    else:
        print("\naudit only; pass --write to archive originals and rewrite")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
