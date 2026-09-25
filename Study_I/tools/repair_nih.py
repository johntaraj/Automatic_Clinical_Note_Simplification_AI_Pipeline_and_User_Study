"""Rebuilds data/nih.json from the official NCI Dictionary of Cancer Terms API."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Tuple

import requests


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "archive" / "nih_legacy_corrupt.json"
DEFAULT_OUTPUT = ROOT / "data" / "nih.json"
DEFAULT_MANIFEST = ROOT / "data" / "nih_manifest.json"
API_BASE = "https://webapis.cancer.gov/glossary/v1"
DICTIONARY = "Cancer.gov"
AUDIENCE = "Patient"
LANGUAGE = "en"
LETTERS = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + ("%23",)

CORRUPT_RANGES = (
    ("PDX", "pyroxamide"),
    ("National Center for Complementary and Integrative Health", "cytotoxin"),
)

SENTINELS = {
    "PDX": "tumor tissue that has been taken from a patient",
    "psychological": "how the mind works",
    "physician assistant": "licensed to do certain medical procedures",
    "National Center for Complementary and Integrative Health": "a federal agency",
    "pyroxamide": "histone deacetylase inhibitors",
    "cytotoxin": "can kill cells",
}


def _normalize_term(text: str) -> str:
    text = text.casefold().replace("’", "'").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", text).strip()


def _corrupt_keys(data: Dict[str, str]) -> set[str]:
    starts = {start: end for start, end in CORRUPT_RANGES}
    active_end = None
    out: set[str] = set()
    for key in data:
        if key in starts:
            if active_end is not None:
                raise ValueError(f"overlapping corrupt ranges before {key!r}")
            active_end = starts[key]
        if active_end is not None:
            out.add(key)
            if key == active_end:
                active_end = None
    if active_end is not None:
        raise ValueError(f"corrupt range end {active_end!r} not found")
    expected = 1692
    if len(out) != expected:
        raise ValueError(f"expected {expected} quarantined keys, found {len(out)}")
    return out


def _get_json(session: requests.Session, url: str) -> Any:
    response = session.get(url, timeout=90)
    response.raise_for_status()
    return response.json()


def fetch_official() -> Tuple[Dict[str, Dict[str, str]], Dict[str, Any]]:
    session = requests.Session()
    session.headers["User-Agent"] = "clinical-simplification-thesis/1.0"
    expected = int(_get_json(
        session,
        f"{API_BASE}/Terms/count/{DICTIONARY}/{AUDIENCE}/{LANGUAGE}",
    ))

    by_key: Dict[str, Dict[str, str]] = {}
    duplicate_keys: list[str] = []
    per_letter: Dict[str, int] = {}
    for letter in LETTERS:
        url = (
            f"{API_BASE}/Terms/expand/{DICTIONARY}/{AUDIENCE}/{LANGUAGE}/"
            f"{letter}?size=10000"
        )
        payload = _get_json(session, url)
        results = payload.get("results") or []
        total = int((payload.get("meta") or {}).get("totalResults", -1))
        if total != len(results):
            raise RuntimeError(
                f"API pagination incomplete for {letter}: meta={total}, rows={len(results)}"
            )
        per_letter[letter] = len(results)
        for row in results:
            term = str(row.get("termName") or "").strip()
            definition = str((row.get("definition") or {}).get("text") or "").strip()
            if not term or not definition:
                raise RuntimeError(f"empty official term or definition: {row!r}")
            key = _normalize_term(term)
            if key in by_key and by_key[key]["term"] != term:
                duplicate_keys.append(key)
                continue
            by_key[key] = {
                "term": term,
                "definition": definition,
                "term_id": str(row.get("termId") or ""),
                "pretty_url": str(row.get("prettyUrlName") or ""),
            }

    fetched = sum(per_letter.values())
    if fetched != expected:
        raise RuntimeError(f"official count is {expected}, but fetched {fetched}")
    if duplicate_keys:
        raise RuntimeError(f"case-normalized duplicate terms: {duplicate_keys[:10]}")

    meta = {
        "api_base": API_BASE,
        "dictionary": DICTIONARY,
        "audience": AUDIENCE,
        "language": LANGUAGE,
        "official_count": expected,
        "fetched_count": fetched,
        "unique_normalized_terms": len(by_key),
        "per_letter": per_letter,
    }
    return by_key, meta


def repair(
    legacy: Dict[str, str], official: Dict[str, Dict[str, str]]
) -> Tuple[Dict[str, str], Dict[str, Any]]:
    corrupt = _corrupt_keys(legacy)
    repaired = dict(legacy)
    matched: list[str] = []
    missing: list[str] = []
    for term in corrupt:
        official_row = official.get(_normalize_term(term))
        if official_row is None:
            missing.append(term)
            del repaired[term]
            continue
        repaired[term] = official_row["definition"]
        matched.append(term)

    changed_outside = [
        key for key, value in legacy.items()
        if key not in corrupt and repaired.get(key) != value
    ]
    if changed_outside:
        raise RuntimeError(f"non-quarantined mappings changed: {changed_outside[:10]}")

    for term, phrase in SENTINELS.items():
        definition = repaired.get(term, "")
        if phrase.casefold() not in definition.casefold():
            raise RuntimeError(
                f"sentinel failed for {term!r}: expected phrase {phrase!r}; "
                f"got {definition[:160]!r}"
            )

    stats = {
        "legacy_count": len(legacy),
        "quarantined_count": len(corrupt),
        "repaired_count": len(matched),
        "removed_missing_from_current_nci": len(missing),
        "removed_terms": sorted(missing, key=str.casefold),
        "final_count": len(repaired),
        "final_unique_normalized_terms": len({_normalize_term(key) for key in repaired}),
        "unchanged_count": len(legacy) - len(corrupt),
    }
    return repaired, stats


def _json_bytes(data: Any) -> bytes:
    return (json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False) + "\n").encode(
        "utf-8"
    )


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)

    legacy = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(legacy, dict):
        raise SystemExit("[err] legacy NIH file is not a JSON object")

    official, api_meta = fetch_official()
    repaired, repair_stats = repair(legacy, official)
    content = _json_bytes(repaired)
    digest = hashlib.sha256(content).hexdigest()

    manifest = {
        "source": "NCI Dictionary of Cancer Terms",
        "source_url": "https://www.cancer.gov/publications/dictionaries/cancer-terms",
        "legacy_source": str(args.input.relative_to(ROOT)),
        "legacy_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "strategy": (
            "Preserve every non-quarantined legacy mapping; replace quarantined "
            "headwords by normalized exact-name match against the official NCI API; "
            "remove quarantined legacy terms absent from the current API."
        ),
        "api": api_meta,
        "repair": repair_stats,
        "output_sha256": digest,
        "sentinels": SENTINELS,
    }

    print(json.dumps({"api": api_meta, "repair": repair_stats}, indent=2))
    print(f"output sha256: {digest}")
    if not args.write:
        print("audit complete; no files written (pass --write to apply)")
        return 0

    _atomic_write(args.output, content)
    _atomic_write(args.manifest, _json_bytes(manifest))
    print(f"legacy source: {args.input}")
    print(f"repaired dictionary: {args.output}")
    print(f"manifest: {args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
