"""LLM judge for replacement correctness and equivalence; writes replacement_judge.json
into each model folder.

Usage:
    python tools/judge_replacements.py runs/run100_20260815_222318 [--models NAME ...] [--arms ARM ...] [--limit N]
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

BATCH = 20
JUDGE_MAX_TOKENS = 8192
SCORE = {"yes": 1.0, "partly": 0.5, "no": 0.0}

SYSTEM = """You grade plain-language rewrites of clinical terms for a patient.

For each item you get:
  term   - the original clinical term
  human  - what a human editor replaced it with
  ours   - what an automatic system replaced it with

Answer TWO questions per item.

1. "equivalent": does `ours` convey the SAME meaning as `human`?
   yes    - same meaning, even if the words are completely different
            ("got better" vs "went away" = yes)
   partly - overlapping but loses or adds something important
   no     - different meaning, or nonsense

2. "correct": is `ours` a correct, plain-English rendering of `term` itself?
   Judge this against `term`, NOT against `human`. `ours` may be better than
   `human`.
   yes    - a patient would correctly understand `term` from it
   partly - roughly right but vague, incomplete, or slightly off
   no     - wrong, misleading, or unrelated

If `ours` is empty or is just the original term unchanged, both are "no".

Return ONLY a JSON array, one object per item, in the SAME ORDER, no prose:
[{"id": 0, "equivalent": "yes", "correct": "yes"}, ...]"""


def _items(run: Path, models: List[str], arms: List[str], limit: int
           ) -> List[Dict[str, Any]]:
    from metrics.edits import replacement_quality

    out: List[Dict[str, Any]] = []
    for d in sorted(p for p in run.iterdir() if p.is_dir()):
        if models and d.name not in models:
            continue
        f = d / "notes.json"
        if not f.exists():
            continue
        notes = json.loads(f.read_text(encoding="utf-8"))
        for n in notes:
            orig = n.get("original_clean") or n.get("original") or ""
            ref = n.get("reference") or ""
            terms = [(i.get("text") or "") for i in n.get("hard_items") or []]
            for arm in arms:
                rec = (n.get("arms") or {}).get(arm) or {}
                sys_out = rec.get("output") or ""
                if not (sys_out and ref and terms):
                    continue
                q = replacement_quality(orig, ref, sys_out, terms)
                for r in q["per_replacement"]:
                    if r.get("ambiguous") or r.get("f1") is None:
                        continue
                    if not r.get("human_edited"):
                        continue
                    out.append({
                        "model": d.name, "arm": arm,
                        "note_idx": n.get("note_idx"),
                        "term": r["term"],
                        "human": r["gold_replacement"],
                        "ours": r["sys_replacement"],
                        "f1_lexical": r["f1"],
                    })
    return out[:limit] if limit else out


def _judge(client, model: str, batch: List[Dict[str, Any]]
           ) -> List[Dict[str, str]]:
    from core import cache as cache_mod

    cache = cache_mod.get_cache()
    payload = json.dumps([{"id": i, "term": b["term"], "human": b["human"],
                           "ours": b["ours"]}
                          for i, b in enumerate(batch)], ensure_ascii=False)
    key = cache.make_key("replacement-judge", f"{model}@0.0", SYSTEM + payload)
    hit = cache.get(key)
    raw = hit.get("raw") if hit else None
    if raw is None:
        raw = ""
        for attempt in range(3):
            try:
                resp = client.chat.completions.create(
                    model=model, temperature=0.0, max_tokens=JUDGE_MAX_TOKENS,
                    timeout=90,
                    messages=[{"role": "system", "content": SYSTEM},
                              {"role": "user", "content": payload}])
                raw = resp.choices[0].message.content or ""
                if resp.choices[0].finish_reason == "length" and not raw:
                    print("      [warn] judge hit max_tokens with EMPTY "
                          "content - reasoning ate the budget", flush=True)
                break
            except Exception as e:
                print(f"      [warn] judge call failed "
                      f"({type(e).__name__}), attempt {attempt + 1}/3",
                      flush=True)
                time.sleep(2 * (attempt + 1))
    parsed = _parse(raw)
    if parsed is None or len(parsed) != len(batch):
        return []
    cache.put(key, {"raw": raw})
    return parsed


def _parse(raw: str):
    s = (raw or "").strip()
    if s.startswith("```"):
        s = s.split("```")[1]
        s = s.split("\n", 1)[1] if "\n" in s else s
    i, j = s.find("["), s.rfind("]")
    if i < 0 or j < 0:
        return None
    try:
        data = json.loads(s[i:j + 1])
    except Exception:
        return None
    if not isinstance(data, list):
        return None
    for d in data:
        if not isinstance(d, dict):
            return None
        for k in ("equivalent", "correct"):
            if str(d.get(k, "")).lower() not in SCORE:
                return None
    return data


def main(argv: List[str]) -> int:
    import config
    from openai import OpenAI

    if not argv:
        print(__doc__)
        return 1
    run = Path(argv[0])
    if not run.is_dir():
        print(f"[err] not a run directory: {run}")
        return 1
    models = _flag(argv, "--models")
    arms = _flag(argv, "--arms") or ["naive", "termonly", "grounded"]
    lim = _flag(argv, "--limit")
    limit = int(lim[0]) if lim else 0

    cfg = config.Config()
    client = OpenAI(api_key=cfg.api_key("novita"),
                    base_url=cfg.novita_base_url, timeout=60, max_retries=1)
    judge_model = cfg.extract_models[0]

    items = _items(run, models, arms, limit)
    print(f"  run          : {run.name}", flush=True)
    print(f"  judge model  : {judge_model}", flush=True)
    print(f"  items to grade: {len(items)}", flush=True)
    if not items:
        return 1

    t0 = time.time()
    graded = 0
    for start in range(0, len(items), BATCH):
        batch = items[start:start + BATCH]
        verdicts = _judge(client, judge_model, batch)
        if not verdicts:
            verdicts = []
            for b in batch:
                v = _judge(client, judge_model, [b])
                verdicts.append(v[0] if v else
                                {"equivalent": "no", "correct": "no",
                                 "unparsed": True})
        for b, v in zip(batch, verdicts):
            b["equivalent"] = str(v.get("equivalent", "no")).lower()
            b["correct"] = str(v.get("correct", "no")).lower()
            b["unparsed"] = bool(v.get("unparsed"))
        graded += len(batch)
        rate = graded / max(time.time() - t0, 1e-6)
        eta = (len(items) - graded) / rate if rate else 0
        print(f"    graded {graded}/{len(items)}  "
              f"({rate:.1f}/s, eta {eta / 60:.1f} min)", flush=True)
        _save(run, items)

    by: Dict[tuple, List[Dict[str, Any]]] = {}
    for b in items:
        by.setdefault((b["model"], b["arm"]), []).append(b)

    print()
    print(f"{'model':<24}{'arm':<10}{'lexical':>9}{'equivalent':>12}"
          f"{'correct':>9}{'n':>6}{'unparsed':>10}")
    print("-" * 80)
    for (m, arm), rows in sorted(by.items()):
        n = len(rows)
        lex = sum(r["f1_lexical"] for r in rows) / n
        eqv = sum(SCORE[r["equivalent"]] for r in rows) / n
        cor = sum(SCORE[r["correct"]] for r in rows) / n
        bad = sum(1 for r in rows if r.get("unparsed"))
        print(f"{m.replace('together-', ''):<24}{arm:<10}"
              f"{lex:>9.3f}{eqv:>12.3f}{cor:>9.3f}{n:>6}{bad:>10}")

    _save(run, items)
    return 0


def _save(run: Path, items: List[Dict[str, Any]]) -> None:
    for d in sorted({b["model"] for b in items}):
        rows = [b for b in items if b["model"] == d and "correct" in b]
        if not rows:
            continue
        (run / d / "replacement_judge.json").write_text(
            json.dumps({"items": rows}, indent=2, ensure_ascii=False),
            encoding="utf-8")


def _flag(argv: List[str], name: str):
    if name not in argv:
        return []
    i = argv.index(name) + 1
    out = []
    while i < len(argv) and not argv[i].startswith("--"):
        out.append(argv[i])
        i += 1
    return out


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
