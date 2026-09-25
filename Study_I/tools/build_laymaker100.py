"""Builds data/laymaker_grade3_plain.json, the 100 evaluation sentences, from the Laymaker pool."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TARGET = DATA / "laymaker_grade3_plain.json"
POOL = DATA / "laymaker.json"
ARCHIVE = DATA / "archive" / "laymaker_grade3_plain_93unique.json"
MANIFEST = DATA / "laymaker_manifest.json"

ADDITIONS = [116, 592, 249, 701, 826, 751, 496]

WORD = re.compile(r"[A-Za-z][A-Za-z\-']+")


def norm(s: str) -> str:
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = re.sub(r"\s+([,.;:!?%)])", r"\1", s)
    s = re.sub(r"([(])\s+", r"\1", s)
    return s


def ref_quality(ref: str) -> tuple:
    complete = bool(ref) and ref.rstrip()[-1:] in ".!?"
    try:
        import textstat
        grade = textstat.flesch_kincaid_grade(ref)
    except Exception:
        grade = 0.0
    return (0 if complete else 1, grade)


def main(write: bool) -> int:
    cur = json.loads(TARGET.read_text(encoding="utf-8"))
    pool = json.loads(POOL.read_text(encoding="utf-8"))
    print(f"current file : {len(cur)} rows, "
          f"{len({norm(r['ORIGINAL']).lower() for r in cur})} unique inputs")

    best: dict = {}
    order: list = []
    dropped: list = []
    for r in cur:
        key = norm(r["ORIGINAL"]).lower()
        if key not in best:
            best[key] = r
            order.append(key)
            continue
        cur_r = best[key]
        if (ref_quality(r["REFERENCE"]), str(r["ID"])) < \
           (ref_quality(cur_r["REFERENCE"]), str(cur_r["ID"])):
            best[key], loser = r, cur_r
        else:
            loser = r
        dropped.append((loser["ID"], best[key]["ID"]))
    kept = [best[k] for k in order]
    print(f"deduped      : {len(kept)} unique; dropped "
          f"{[d[0] for d in dropped]} in favour of {[d[1] for d in dropped]}")

    by_id = {r["ID"]: r for r in pool}
    have_ids = {r["ID"] for r in kept}
    have_txt = {norm(r["ORIGINAL"]).lower() for r in kept}
    added = []
    for nid in ADDITIONS:
        r = by_id.get(nid)
        if r is None:
            raise SystemExit(f"[build] id {nid} is not in {POOL.name}")
        o, ref = norm(r["ORIGINAL"]), norm(r["REFERENCE"])
        problems = []
        if nid in have_ids:
            problems.append("id already present")
        if o.lower() in have_txt:
            problems.append("input already present")
        if r.get("grade") != 3:
            problems.append(f"grade {r.get('grade')}")
        if not r.get("fully_plain"):
            problems.append("not fully_plain")
        if ref.rstrip()[-1:] not in ".!?":
            problems.append("reference truncated")
        if o.lower() == ref.lower():
            problems.append("reference identical to input")
        if problems:
            raise SystemExit(f"[build] id {nid} rejected: {'; '.join(problems)}")
        row = {"ID": nid, "ORIGINAL": o, "REFERENCE": ref,
               "grade": r["grade"], "fully_plain": r["fully_plain"]}
        added.append(row)
        have_ids.add(nid)
        have_txt.add(o.lower())

    out = kept + added
    print(f"added        : {[r['ID'] for r in added]}")
    for r in added:
        new_words = sorted({w.lower() for w in WORD.findall(r["ORIGINAL"])}
                           - {w.lower() for k in kept
                              for w in WORD.findall(k["ORIGINAL"])})
        print(f"  {r['ID']:>4}  {r['ORIGINAL'][:66]}")
        print(f"        -> {r['REFERENCE'][:66]}")
        print(f"        new vocabulary: {new_words[:8]}")

    ids = [r["ID"] for r in out]
    txt = [norm(r["ORIGINAL"]).lower() for r in out]
    assert len(out) == 100, f"expected 100 rows, got {len(out)}"
    assert len(set(ids)) == 100, "duplicate IDs"
    assert len(set(txt)) == 100, "duplicate inputs"
    assert all(r.get("grade") == 3 for r in out), "non grade-3 row"
    assert all(r.get("fully_plain") for r in out), "non fully_plain row"
    assert all((r.get("REFERENCE") or "").strip() for r in out), "empty reference"
    print(f"\nOK: {len(out)} rows, {len(set(ids))} unique IDs, "
          f"{len(set(txt))} unique inputs, all grade 3 / fully_plain")

    if not write:
        print("\n(audit only - pass --write to archive and rewrite)")
        return 0

    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    if not ARCHIVE.exists():
        shutil.copy2(TARGET, ARCHIVE)
    body = json.dumps(out, indent=2, ensure_ascii=False) + "\n"
    TARGET.write_text(body, encoding="utf-8")
    MANIFEST.write_text(json.dumps({
        "built": date.today().isoformat(),
        "output": TARGET.name,
        "output_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "n_rows": len(out),
        "n_unique_inputs": len(set(txt)),
        "archived_input": str(ARCHIVE.relative_to(ROOT)),
        "deduplicated_pairs": [{"dropped": d, "kept": k} for d, k in dropped],
        "added_from_pool": [r["ID"] for r in added],
        "pool": POOL.name,
        "constraints": "grade == 3, fully_plain, complete reference, "
                       "unique ID and unique input text",
    }, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {TARGET.name} and {MANIFEST.name}; archived to "
          f"{ARCHIVE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--write" in sys.argv))
