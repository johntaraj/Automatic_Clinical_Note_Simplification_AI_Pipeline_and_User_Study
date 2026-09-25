"""Descriptive statistics for each glossary: size, redundancy and readability."""

from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

DATA = ROOT / "data"
OUT = DATA / "glossary_stats.json"
WORD = re.compile(r"[A-Za-z][A-Za-z'\-]*")
MIN_WORDS_FOR_FKGL = 5


def _raise_csv_limit() -> None:
    limit = sys.maxsize
    while True:
        try:
            csv.field_size_limit(limit)
            return
        except OverflowError:
            limit //= 10


_raise_csv_limit()


def load_pairs(name: str) -> List[Tuple[str, str]]:
    path = DATA / name
    if name.endswith(".jsonl"):
        out = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    obj = json.loads(line)
                    out.append((obj.get("term") or "", obj.get("definition") or ""))
        return out
    if name == "nih.json":
        raw = json.loads(path.read_text(encoding="utf-8"))
        return [(k, v) for k, v in raw.items() if isinstance(v, str)]
    if name.endswith(".json"):
        raw = json.loads(path.read_text(encoding="utf-8-sig"))
        return [(o.get("term") or "", o.get("definition") or "")
                for o in raw if isinstance(o, dict)]
    with open(path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if name.startswith("dorland"):
        return [(r.get("term") or "", r.get("candidate") or "") for r in rows]
    return [(r.get("word") or "", r.get("definition") or "") for r in rows]


def describe(pairs: Iterable[Tuple[str, str]]) -> Dict[str, Any]:
    import textstat
    from wordfreq import zipf_frequency

    pairs = [(t.strip(), d.strip()) for t, d in pairs if t.strip() and d.strip()]
    lengths, fkgl, zipf_mean, zipf_min, term_zipf = [], [], [], [], []
    terms, definitions = set(), set()

    for term, definition in pairs:
        terms.add(term.casefold())
        definitions.add(definition.casefold())
        words = WORD.findall(definition)
        lengths.append(len(words))
        if len(words) >= MIN_WORDS_FOR_FKGL:
            try:
                fkgl.append(float(textstat.flesch_kincaid_grade(definition)))
            except Exception:
                pass
        content = [w.lower() for w in words if len(w) >= 3]
        if content:
            values = [zipf_frequency(w, "en") for w in content]
            values = [v for v in values if v > 0]
            if values:
                zipf_mean.append(statistics.fmean(values))
                zipf_min.append(min(values))
        tw = [w.lower() for w in WORD.findall(term)]
        if tw:
            tv = [zipf_frequency(w, "en") for w in tw]
            tv = [v for v in tv if v > 0]
            if tv:
                term_zipf.append(min(tv))

    def stat(values, digits=2):
        if not values:
            return None
        return {
            "mean": round(statistics.fmean(values), digits),
            "median": round(statistics.median(values), digits),
        }

    n = len(pairs)
    return {
        "entries": n,
        "unique_terms": len(terms),
        "unique_definitions": len(definitions),
        "definitions_per_term": round(n / len(terms), 2) if terms else None,
        "definition_words": stat(lengths, 1),
        "pct_scoreable_for_fkgl": round(100 * len(fkgl) / n, 1) if n else None,
        "fkgl": stat(fkgl),
        "zipf_mean": stat(zipf_mean),
        "zipf_min": stat(zipf_min),
        "term_zipf_min": stat(term_zipf),
    }


FILES = [
    ("readme_exp_good.jsonl", "readme", "Patient-education definitions, lay-written"),
    ("nih.json", "nih", "NCI Dictionary of Cancer Terms (patient audience)"),
    ("michigan_plmd.json", "michigan", "Michigan plain-language medical dictionary"),
    ("justplainclear_en_clean.json", "justplainclear", "JustPlainClear patient glossary"),
    ("Iowa.json", "iowa", "Iowa health-literacy glossary"),
    ("thesarus.json", "thesaurus", "Plain-language synonyms (comma-separated lists)"),
    ("wiktionary.json", "wiktionary", "Simple English Wiktionary, learner-written"),
    ("dorland_medical_abbreviations.csv", "dorland",
     "Abbreviation expansions (names, not sentences)"),
    ("dictonary.csv", "dictionary", "General English dictionary (Webster's 1913)"),
]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)

    report: Dict[str, Any] = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "tool": "tools/glossary_stats.py",
        "fkgl_note": (f"computed only over definitions of >= {MIN_WORDS_FOR_FKGL} "
                      "words; pct_scoreable_for_fkgl gives the share that qualified"),
        "zipf_note": ("zipf_mean = average commonness of a definition's content "
                      "words (higher = easier); zipf_min = its rarest content word"),
        "sources": {},
    }

    for name, label, what in FILES:
        if not (DATA / name).exists():
            print(f"[skip] {name}")
            continue
        stats = describe(load_pairs(name))
        stats["file"] = name
        stats["description"] = what
        report["sources"][label] = stats
        print(f"  {label:<16} {stats['entries']:>7} entries  "
              f"FKGL {stats['fkgl']['mean'] if stats['fkgl'] else 'n/a'}")

    rows = report["sources"]
    total_entries = sum(s["entries"] for s in rows.values())
    total_terms = sum(s["unique_terms"] for s in rows.values())

    print("\n\n### Knowledge base — size and redundancy\n")
    print("| source | entries | unique terms | defs/term | what it is |")
    print("|---|---:|---:|---:|---|")
    for label, s in rows.items():
        print(f"| `{s['file']}` | {s['entries']:,} | **{s['unique_terms']:,}** | "
              f"{s['definitions_per_term']} | {s['description']} |")
    print(f"| **total** | **{total_entries:,}** | **{total_terms:,}** | | |")

    print("\n\n### Knowledge base — how hard each source is to read\n")
    print("| source | def. length (words) | scoreable | mean FKGL | median FKGL "
          "| zipf mean | zipf min |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    for label, s in rows.items():
        fk = s["fkgl"] or {}
        print(f"| {label} | {s['definition_words']['mean']} | "
              f"{s['pct_scoreable_for_fkgl']}% | "
              f"{fk.get('mean', 'n/a')} | {fk.get('median', 'n/a')} | "
              f"{s['zipf_mean']['mean']} | {s['zipf_min']['mean']} |")

    if args.write:
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
        print(f"\nwrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
