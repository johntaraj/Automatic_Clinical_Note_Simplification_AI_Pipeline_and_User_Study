"""Builds data/wiktionary.json from a Simple English Wiktionary (wiktextract) dump."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DEFAULT_SOURCE = DATA / "archive" / "wikitionary.jsonl"
OUTPUT = DATA / "wiktionary.json"
MANIFEST = DATA / "wiktionary_manifest.json"

_WORD = re.compile(r"[A-Za-z][A-Za-z'\-]*")
_MIN_GLOSS_WORDS = 3
_MAX_SENSES_PER_WORD = 3

_POINTERS = (
    re.compile(r"^(?:the )?plural form of ([\w'\-]+)", re.I),
    re.compile(r"^plural of ([\w'\-]+)", re.I),
    re.compile(
        r"^the (?:past tense and past participle|past participle|past tense|"
        r"present participle|third[- ]person singular|simple past|"
        r"comparative form|superlative form)[\w\s]*? of ([\w'\-]+)", re.I),
    re.compile(r"^(?:past tense|past participle|present participle|"
               r"comparative|superlative) of ([\w'\-]+)", re.I),
    re.compile(r"^(?:an? )?(?:alternative|another) (?:spelling|form) of ([\w'\-]+)",
               re.I),
)


def _pointer_target(gloss: str) -> Optional[str]:
    for pattern in _POINTERS:
        m = pattern.match(gloss)
        if m:
            return m.group(1).strip().strip(".,;:")
    return None


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").replace("\u00a0", " ")).strip()


def read_dump(path: Path) -> Tuple[Dict[str, List[str]], Dict[str, int]]:
    words: Dict[str, List[str]] = {}
    counts = {"records": 0, "skipped_proper_noun": 0, "skipped_redirect": 0,
              "skipped_non_english": 0, "raw_glosses": 0}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            counts["records"] += 1
            pos = (obj.get("pos") or "").strip()
            if pos == "hard-redirect":
                counts["skipped_redirect"] += 1
                continue
            if (obj.get("lang_code") or "") != "en":
                counts["skipped_non_english"] += 1
                continue
            if pos == "name":
                counts["skipped_proper_noun"] += 1
                continue
            word = _clean(obj.get("word", ""))
            if not word:
                continue
            bucket = words.setdefault(word, [])
            for sense in obj.get("senses") or []:
                for gloss in sense.get("glosses") or []:
                    g = _clean(gloss)
                    if not g:
                        continue
                    counts["raw_glosses"] += 1
                    if g not in bucket:
                        bucket.append(g)
    return {w: g for w, g in words.items() if g}, counts


def build(words: Dict[str, List[str]]
          ) -> Tuple[List[Dict[str, str]], Dict[str, Any]]:
    def usable(gloss: str) -> bool:
        return (not gloss.endswith(":")
                and len(_WORD.findall(gloss)) >= _MIN_GLOSS_WORDS)

    real: Dict[str, str] = {}
    for word, glosses in words.items():
        for gloss in glosses:
            if _pointer_target(gloss) is None and usable(gloss):
                real[word.casefold()] = gloss
                break

    out: List[Dict[str, str]] = []
    seen: set = set()
    resolved = kept = dropped_pointer = dropped_thin = 0
    for word, glosses in words.items():
        emitted = 0
        for gloss in glosses:
            if emitted >= _MAX_SENSES_PER_WORD:
                break
            target = _pointer_target(gloss)
            if target is not None:
                lemma = real.get(target.casefold())
                if not lemma:
                    dropped_pointer += 1
                    continue
                gloss, was_pointer = lemma, True
            else:
                was_pointer = False
                if not usable(gloss):
                    dropped_thin += 1
                    continue
            key = (word.casefold(), gloss.casefold())
            if key in seen:
                continue
            seen.add(key)
            out.append({"term": word, "definition": gloss})
            emitted += 1
            resolved += was_pointer
            kept += not was_pointer

    stats = {
        "headwords_after_filters": len(words),
        "entries_written": len(out),
        "unique_terms": len({e["term"].casefold() for e in out}),
        "resolved_inflection_pointers": resolved,
        "kept_real_glosses": kept,
        "dropped_unresolvable_pointer": dropped_pointer,
        "dropped_truncated_or_too_short": dropped_thin,
        "max_senses_per_word": _MAX_SENSES_PER_WORD,
        "min_gloss_words": _MIN_GLOSS_WORDS,
    }
    return out, stats


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


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)

    if not args.source.exists():
        raise SystemExit(f"[err] missing source dump: {args.source}")

    words, counts = read_dump(args.source)
    entries, stats = build(words)
    stats.update(counts)
    content = (json.dumps(entries, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    stats["output_sha256"] = hashlib.sha256(content).hexdigest()

    print(json.dumps(stats, indent=2))
    if not args.write:
        print("\naudit only; pass --write to create data/wiktionary.json")
        return 0

    manifest = {
        "source": "Simple English Wiktionary via wiktextract",
        "source_file": str(args.source.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "tool": "tools/build_wiktionary.py",
        "strategy": (
            "keep headword + glosses only; skip proper-noun (pos=name) and "
            "redirect records; resolve inflection glosses to the lemma's first "
            "real gloss; drop unresolvable pointers, truncated glosses ending "
            f"in ':' and glosses under {_MIN_GLOSS_WORDS} words; at most "
            f"{_MAX_SENSES_PER_WORD} senses per headword"),
        "stats": stats,
    }
    _atomic_write(OUTPUT, content)
    _atomic_write(MANIFEST,
                  (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"wrote {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
