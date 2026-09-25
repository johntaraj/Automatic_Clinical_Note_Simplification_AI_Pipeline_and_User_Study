"""Runs the Study I pipeline: extraction, retrieval, three-arm generation, ContextCite
attribution, rationales, evaluation and reports.

Usage:
    python run.py --preset full100                            # reported setup, six models
    python run.py --preset full100 --models together-qwen3.5-9b
    python run.py --preset audit5                             # five-sentence smoke test
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import os
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, List

os.environ.setdefault("PYTHONUTF8", "1")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from config import MODEL_REGISTRY, Config, preset_audit5, preset_full100
from core import cache as cache_mod
from core.io import banner, load_json, save_json, tee_to
from core.llm import ProviderUnavailable
from stages import s1_dataset, s2_extract, s3_retrieve, s4_generate
from stages import s5_evaluate, s6_rationalize, s9_report


def parse_args(argv: List[str]) -> Config:
    ap = argparse.ArgumentParser(description="Study I clinical note simplification pipeline")
    ap.add_argument("--preset", choices=["audit5", "full100"], default="audit5")
    ap.add_argument("--models", nargs="+", default=None,
                    help=f"one or more of: {', '.join(sorted(MODEL_REGISTRY))}")
    ap.add_argument("--notes", type=int, default=None)
    ap.add_argument("--label", default=None)
    ap.add_argument("--stamp", action="store_true",
                    help="append a date-time to the run label so a new run "
                         "never overwrites an old one's results. ON by "
                         "default for --preset full100.")
    ap.add_argument("--no-stamp", action="store_true",
                    help="write to the bare label instead of a timestamped "
                         "folder. Only use this to RESUME an interrupted run, "
                         "and pass the stamped --label of the run you are "
                         "resuming.")
    ap.add_argument("--arms", nargs="+", default=None)
    ap.add_argument("--tag-policy", choices=["action", "replace"], default=None)
    ap.add_argument("--keep-gloss", choices=["names", "all_essential"],
                    default=None,
                    help="which terms get KEEP+GLOSS (default: names only)")
    ap.add_argument("--prompt-style", choices=["lean", "rich"], default=None,
                    help="lean (default) is ~4x cheaper under ContextCite")
    ap.add_argument("--cc-ablations", type=int, default=None,
                    help="fitting masks per NOTE (default 32)")
    ap.add_argument("--cc-heldout", type=int, default=None,
                    help="held-out masks per note for the held-out LDS (default 32)")
    ap.add_argument("--cc-sources", type=int, default=None,
                    help="max glossary entries shown per note (default 16)")
    ap.add_argument("--cc-notes", type=int, default=None,
                    help="run ContextCite on the first N notes only. Every note "
                         "still gets generation and all other metrics. Use this "
                         "to keep the 100-note run tractable (~2-4 min/edit).")
    ap.add_argument("--no-contextcite", action="store_true")
    ap.add_argument("--leave-one-out", action="store_true",
                    help="also ablate each glossary entry individually: adds "
                         "the paper's delta=2 relevant-source count (App. A.4) "
                         "and checks the LASSO winner against the oracle. "
                         "Costs ~+15%% of the scoring calls.")
    ap.add_argument("--no-torch", action="store_true")
    ap.add_argument("--no-rationales", action="store_true",
                    help="skip stages 6-7 (rationales + their audit)")
    ap.add_argument("--extract-stability", action="store_true",
                    help="extract every note twice and report the Jaccard "
                         "overlap of the two term sets (stage-2 reliability). "
                         "One extra Novita call per note, then cached.")
    ap.add_argument("--judge", action="store_true",
                    help="run the Novita LLM-judge panel (extra cost)")
    ap.add_argument("--no-cache", action="store_true",
                    help="bypass the on-disk LLM response cache")
    ap.add_argument("--force", action="store_true",
                    help="re-run models that already have results (default is "
                         "to resume and skip them)")
    ap.add_argument("--reuse-shared", action="store_true",
                    help="(deprecated, now the default) reuse cached "
                         "extraction/retrieval")
    ap.add_argument("--fresh-shared", action="store_true",
                    help="force re-extraction and re-retrieval")
    ap.add_argument("--keep-retrieval", action="store_true",
                    help="reuse the saved Stage 3 definitions instead of "
                         "looking them up again in data/")
    a = ap.parse_args(argv)

    cfg = preset_full100(a.models) if a.preset == "full100" else preset_audit5(a.models)
    if a.notes:
        cfg.num_notes = a.notes
        if a.notes > 5 and cfg.dataset == "fixture5":
            cfg.dataset = "laymaker"
    if a.label:
        cfg.run_label = a.label
    stamp = a.stamp or (a.preset == "full100" and not a.label)
    if a.no_stamp:
        stamp = False
    if stamp:
        cfg.run_label = (f"{cfg.run_label}_"
                         f"{datetime.datetime.now():%Y%m%d_%H%M%S}")
    if a.arms:
        cfg.arms = a.arms
    if a.tag_policy:
        cfg.tag_policy = a.tag_policy
    if a.keep_gloss:
        cfg.keep_gloss_scope = a.keep_gloss
    if a.prompt_style:
        cfg.prompt_style = a.prompt_style
    if a.cc_ablations:
        cfg.cc_num_ablations = a.cc_ablations
    if a.cc_heldout is not None:
        cfg.cc_heldout_ablations = a.cc_heldout
    if a.cc_sources:
        cfg.cc_max_sources = a.cc_sources
    if a.cc_notes:
        cfg.cc_max_notes = a.cc_notes
    if a.no_contextcite:
        cfg.cc_enabled = False
    if a.leave_one_out:
        cfg.cc_leave_one_out = True
    if a.no_torch:
        cfg.enable_torch_evals = False
    if a.no_rationales:
        cfg.run_rationales = False
        cfg.run_hallucination_audit = False
    if a.extract_stability:
        cfg.measure_extraction_stability = True
    if a.judge:
        cfg.run_judge = True
    if a.no_cache:
        cfg.use_cache = False
    cfg.force_rerun = a.force
    cfg.fresh_shared = a.fresh_shared
    cfg.keep_retrieval = a.keep_retrieval
    return cfg


def run_shared(cfg: Config) -> List[Dict[str, Any]]:
    shared = cfg.shared_dir()
    cache = shared / "notes.json"

    with tee_to(shared / "stage_log.txt"):
        banner("STAGE 1 — dataset")
        notes = s1_dataset.load_notes(cfg)
        profile = s1_dataset.dataset_profile(notes)
        print(f"  loaded {len(notes)} notes from {cfg.dataset!r}")
        for k, v in profile.items():
            print(f"    {k:<36} {v}")

    want_ids = [n.get("id") for n in notes]
    if not getattr(cfg, "fresh_shared", False) and cache.exists():
        cached = load_json(cache, []) or []
        if ([n.get("id") for n in cached] == want_ids
                and all(n.get("hard_items") is not None for n in cached)):
            # Returns the saved Stage 2-3 output unchanged, e.g. when some
            # knowledge-base files are not available locally.
            if (getattr(cfg, "keep_retrieval", False)
                    and all(n.get("retrieval") is not None for n in cached)):
                print(f"  [reuse] extraction and retrieval for {len(cached)} "
                      f"notes from {cache}")
                return cached
            print(f"  [reuse] extraction for {len(cached)} notes from {cache}")
            print(f"          (pass --fresh-shared to re-extract)")
            notes = _strip_retrieval(cached)
            with tee_to(shared / "stage_log.txt"):
                if getattr(cfg, "measure_extraction_stability", False):
                    banner("STAGE 2b - extraction stability replicate")
                    notes = s2_extract.add_stability(cfg, notes)
                banner("STAGE 3 - glossary retrieval + coverage")
                notes = s3_retrieve.run(cfg, notes)
            save_json(cache, notes)
            save_json(shared / "profile.json", profile)
            return notes
        print(f"  [shared] cache at {cache} does not match this dataset "
              f"({len(cached)} notes cached, {len(want_ids)} wanted) — re-extracting")

    with tee_to(shared / "stage_log.txt"):
        banner("STAGE 2 — hard-term extraction + classification (Novita)")
        notes = s2_extract.run(cfg, notes)

        banner("STAGE 3 — glossary retrieval + coverage")
        notes = s3_retrieve.run(cfg, notes)

    save_json(shared / "profile.json", profile)
    save_json(cache, notes)
    return notes


_SPLIT_ORIGINS = ("split_from_uncovered", "partial_split_from_uncovered")


def _strip_retrieval(notes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    import copy
    notes = copy.deepcopy(notes)
    for n in notes:
        for k in ("retrieval", "sources", "source_alignment"):
            n.pop(k, None)
        items = [h for h in n.get("hard_items", [])
                 if h.get("origin") not in _SPLIT_ORIGINS]
        for h in items:
            h.pop("attributions", None)
            h.pop("lookup_variant", None)
        n["hard_items"] = items
    return notes


def _fingerprint(cfg: Config, model_key: str) -> Dict[str, Any]:
    from stages import prompts as P
    sys_prompt = (P.naive_system(cfg.person_policy)
                  + P.simplifier_system(cfg.prompt_style, cfg.tag_policy,
                                        cfg.person_policy)
                  + P.TAG_WRAP_SYSTEM)
    return {
        "model": model_key,
        "dataset": cfg.dataset,
        "num_notes": cfg.num_notes,
        "arms": list(cfg.arms),
        "tag_policy": cfg.tag_policy,
        "keep_gloss_scope": cfg.keep_gloss_scope,
        "prompt_style": cfg.prompt_style,
        "prompt_sha": hashlib.sha256(sys_prompt.encode("utf-8")).hexdigest()[:16],
        "temperature": cfg.temperature,
        "max_new_tokens": cfg.max_new_tokens,
        "cc": [cfg.cc_enabled, cfg.cc_num_ablations, cfg.cc_heldout_ablations,
               cfg.cc_max_sources, cfg.cc_lambda, cfg.cc_seed,
               list(cfg.cc_topk), cfg.cc_max_notes],
        "extract_model": (cfg.extract_models or ["none"])[0],
    }


def _load_resumable(cfg: Config, model_key: str, out_dir: Path,
                    notes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    partial = out_dir / "notes_partial.json"
    if getattr(cfg, "force_rerun", False) or not partial.exists():
        return notes
    saved_fp = load_json(out_dir / "fingerprint.json", {}) or {}
    now_fp = _fingerprint(cfg, model_key)
    if saved_fp and saved_fp != now_fp:
        changed = [k for k in now_fp if saved_fp.get(k) != now_fp[k]]
        print(f"  [resume] IGNORING {partial.name}: the configuration changed "
              f"since it was written ({', '.join(changed)}).")
        print(f"           Regenerating from scratch so the run is internally "
              f"consistent.")
        return notes
    prev = load_json(partial, []) or []
    by_id = {n.get("id"): n for n in prev if n.get("arms")}
    if not by_id:
        return notes
    for n in notes:
        old = by_id.get(n.get("id"))
        if old and old.get("arms"):
            n["arms"] = old["arms"]
    return notes


def run_model(cfg: Config, model_key: str, notes: List[Dict[str, Any]],
              profile: Dict[str, Any]) -> Dict[str, Any]:
    import copy
    out_dir = cfg.out_dir(model_key)
    notes = copy.deepcopy(notes)
    cache = cache_mod.get_cache()
    cache.reset_stats()

    out_dir.mkdir(parents=True, exist_ok=True)
    notes = _load_resumable(cfg, model_key, out_dir, notes)
    save_json(out_dir / "fingerprint.json", _fingerprint(cfg, model_key))

    def checkpoint(current: List[Dict[str, Any]]) -> None:
        save_json(out_dir / "notes_partial.json", current)

    try:
        with tee_to(out_dir / "stage_log.txt"):
            banner(f"STAGE 4 - generation ({model_key})")
            notes = s4_generate.run(cfg, notes, model_key, checkpoint=checkpoint)

            from core.llm import scoring_failure_counts
            fails = scoring_failure_counts()
            if fails:
                print("\n  [warn] degraded ablations (scored as -1e4):")
                for kind, n in sorted(fails.items(), key=lambda kv: -kv[1]):
                    print(f"    {kind:<44} {n}")
                print("    A high count here means the attribution numbers "
                      "below are NOT trustworthy;")
                print("    lower num_workers in config.py and re-run "
                      "(cached calls make the retry cheap).")

            if cfg.run_rationales:
                banner(f"STAGE 6 - rationales ({model_key})")
                llm = s4_generate.make_llm(cfg, cfg.model_spec(model_key),
                                           require_echo=False)
                notes = s6_rationalize.run_rationales(cfg, llm, notes, "grounded")

            audit = {}
            if cfg.run_hallucination_audit:
                banner(f"STAGE 7 - rationale audit ({model_key})")
                audit = s6_rationalize.run_audit(notes, "grounded")
                for k, v in audit.items():
                    if isinstance(v, (int, float)):
                        print(f"  {k:<34} {v}")

            banner(f"STAGE 8 - evaluation ({model_key})")
            evaluation = s5_evaluate.run(cfg, notes)
            if audit:
                evaluation["rationale_audit"] = audit

            from metrics.stats import format_comparison
            for cmp in evaluation["comparisons"]:
                print(format_comparison(cmp))

            a = evaluation["attribution"]
            banner("ATTRIBUTION SUMMARY")
            for k in ("n_edits", "n_attributed", "n_no_source_effect", "n_failed",
                      "n_helped", "n_neutral", "n_hurt", "attributable_rate",
                      "lds_median", "lds_insample_median", "lds_optimism_gap",
                      "top1_drop_median", "ablation_success_rate"):
                if k in a:
                    print(f"  {k:<24} {a[k]}")

            cov = (evaluation.get("whole_term_coverage") or {}).get("overall", {})
            banner("RETRIEVAL COVERAGE")
            print(f"  overall {cov.get('coverage')} "
                  f"({cov.get('n_covered')}/{cov.get('n_terms')} terms)")
            for name, b in ((evaluation.get("whole_term_coverage") or {})
                            .get("by_zipf_stratum") or {}).items():
                print(f"    {name:<12} {b['coverage']}  ({b['n_covered']}/{b['n_terms']})")

            banner("LLM RESPONSE CACHE")
            for k, v in cache.stats().items():
                print(f"  {k:<12} {v}")
    except BaseException:
        save_json(out_dir / "notes_partial.json", notes)
        done = sum(1 for n in notes if n.get("arms"))
        print(f"\n  [partial] wrote {done}/{len(notes)} notes to "
              f"{out_dir / 'notes_partial.json'} before aborting.")
        raise

    evaluation["cache_stats"] = cache.stats()
    save_json(out_dir / "notes.json", notes)
    save_json(out_dir / "evaluation.json", evaluation)
    (out_dir / "notes_partial.json").unlink(missing_ok=True)
    s9_report.write(out_dir / "report.md",
                    s9_report.build_report(cfg, model_key, notes, evaluation, profile))
    s9_report.write(out_dir / "detail.md",
                    s9_report.build_detail(cfg, model_key, notes))
    s9_report.write(out_dir / "cost.txt", _cost_text(cfg, model_key, notes, evaluation))
    print(f"  [saved] {out_dir / 'report.md'}, detail.md, cost.txt")
    return {"notes": notes, "evaluation": evaluation}


_PRICE = {
    "accounts/fireworks/models/deepseek-v4-flash": (0.14, 0.028),
    "accounts/fireworks/models/deepseek-v4-pro": (1.74, 0.145),
    "accounts/fireworks/models/qwen3p7-plus": (0.40, 0.08),
    "accounts/fireworks/models/minimax-m3": (0.30, 0.059),
    "accounts/fireworks/models/gpt-oss-120b": (0.15, 0.014),
    "accounts/fireworks/models/gpt-oss-20b": (0.07, 0.035),
    "deepseek-ai/DeepSeek-V4-Pro": (1.74, 0.20),
    "zai-org/GLM-5.2": (1.40, 0.26),
    "MiniMaxAI/MiniMax-M3": (0.30, 0.06),
    "Qwen/Qwen3.5-9B": (0.17, None),
    "nvidia/nemotron-3-ultra-550b-a55b": (0.60, 0.20),
    "thinkingmachines/Inkling": (1.00, 0.17),
    "thinkingmachines/Inkling-Small": (0.50, 0.10),
    "meta-models/Muse-Glimmer-30B": (0.35, 0.04),
}


def _cost_text(cfg: Config, model_key: str, notes: List[Dict[str, Any]],
               evaluation: Dict[str, Any]) -> str:
    from stages import prompts as P

    spec = cfg.model_spec(model_key)
    sys_tok = len(P.simplifier_system(cfg.prompt_style, cfg.tag_policy)) // 4

    calls = 0
    prefix_tok = var_tok = 0
    n_edits = 0
    for n in notes:
        gr = (n.get("arms") or {}).get("grounded") or {}
        srcs = n.get("sources") or []
        gloss = len(P.format_glossary(srcs)) // 4
        pre = P.constant_prefix_tokens(
            n.get("original_clean") or n["original"], n.get("hard_items", []),
            cfg.tag_policy, cfg.keep_gloss_scope,
            P.simplifier_system(cfg.prompt_style, cfg.tag_policy))
        ops = gr.get("operations", [])
        n_edits += len(ops)
        first = next((op.get("contextcite") for op in ops
                      if op.get("contextcite")), None)
        if not first:
            continue
        c = len(first.get("log_probs") or []) + (first.get("extra_calls") or 0)
        calls += c
        prefix_tok += c * pre
        var_tok += c * (gloss // 2)

    total = prefix_tok + var_tok
    cs = evaluation.get("cache_stats") or {}
    price = _PRICE.get(spec.model_id)

    L = [
        "=" * 74,
        f"  COST REPORT - {spec.slug} ({spec.provider})  run `{cfg.run_label}`",
        "=" * 74,
        "",
        f"  notes                      {len(notes)}",
        f"  attributed edits           {n_edits}",
        f"  ContextCite scoring calls  {calls:,}"
        + (f"   ({calls / max(n_edits, 1):.1f} per edit)" if n_edits else ""),
        f"  system prompt              ~{sys_tok} tokens  (style: {cfg.prompt_style})",
        f"  masks per NOTE             {cfg.cc_num_ablations} fit + 2 boundary "
        f"+ {cfg.cc_heldout_ablations} held-out + top-k",
        f"  glossary cap               {cfg.cc_max_sources} entries",
        "",
        f"  input tokens (estimate)    {total:,}",
        f"    cacheable prefix         {prefix_tok:,}  ({prefix_tok / max(total, 1):.0%})",
        f"    varying glossary         {var_tok:,}",
        "",
        "  LLM response cache (across runs):",
        f"    hits {cs.get('hits', 0):,}   misses {cs.get('misses', 0):,}   "
        f"hit rate {cs.get('hit_rate')}",
        f"    dir  {cs.get('dir')}",
        "",
    ]
    if price:
        unc, cached = price
        no_cache = total / 1e6 * unc
        with_cache = (prefix_tok / 1e6 * cached + var_tok / 1e6 * unc) \
            if cached else no_cache
        L += [
            f"  list price                 ${unc:.3f}/M uncached"
            + (f", ${cached:.3f}/M cached" if cached else ", no cached tier"),
            f"  cost, no prompt caching    ${no_cache:.4f}",
            f"  cost, with prompt caching  ${with_cache:.4f}",
            "",
            f"  projection to 100 notes    ${no_cache * 100 / max(len(notes), 1):.2f} "
            f"/ ${with_cache * 100 / max(len(notes), 1):.2f} (cached)",
        ]
    else:
        L.append(f"  no published price recorded for {spec.model_id}")
    L += [
        "",
        "  NOTE: token counts are ~4 chars/token estimates over the prompts we",
        "  built; they exclude output tokens (small: <=512 per generation) and",
        "  the Novita extraction/annotation calls, which are cached across runs",
        "  and shared by every model.",
        "",
    ]
    return "\n".join(L)


def _data_provenance(cfg: Config) -> Dict[str, Any]:
    nih_manifest = load_json(cfg.root / "data" / "nih_manifest.json", {}) or {}
    return {
        "nih": {
            "source": nih_manifest.get("source"),
            "legacy_source": nih_manifest.get("legacy_source"),
            "legacy_sha256": nih_manifest.get("legacy_sha256"),
            "fetched_at_utc": nih_manifest.get("fetched_at_utc"),
            "output_sha256": nih_manifest.get("output_sha256"),
            "api": nih_manifest.get("api"),
            "repair": nih_manifest.get("repair"),
        }
    }


def _incomplete_arms(result: Dict[str, Any]) -> List[str]:
    agg = (result.get("evaluation") or {}).get("aggregate") or {}
    gaps = []
    for arm, stats in agg.items():
        rate = ((stats or {}).get("generation_success_rate") or {}).get("mean")
        if isinstance(rate, (int, float)) and rate < 1.0:
            gaps.append(f"{arm} generated {rate:.0%} of notes")
    return gaps


def main(argv: List[str]) -> int:
    cfg = parse_args(argv)
    started = datetime.datetime.now().isoformat(timespec="seconds")
    cache = cache_mod.configure(cfg.cache_dir, cfg.use_cache)

    banner(f"RUN  '{cfg.run_label}'")
    print(f"  dataset   : {cfg.dataset}  ({cfg.num_notes} notes)")
    print(f"  models    : {', '.join(cfg.models)}")
    print(f"  arms      : {', '.join(cfg.arms)}")
    print(f"  tag policy: {cfg.tag_policy}  keep-gloss: {cfg.keep_gloss_scope}"
          f"  prompt: {cfg.prompt_style}")
    print(f"  ContextCite: {cfg.cc_enabled}  "
          f"({cfg.cc_num_ablations}+{cfg.cc_heldout_ablations} masks, "
          f"<= {cfg.cc_max_sources} sources)")
    print(f"  rationales : {cfg.run_rationales}   audit: "
          f"{cfg.run_hallucination_audit}   judge: {cfg.run_judge}")
    print(f"  torch evals: {cfg.enable_torch_evals}")
    print(f"  LLM cache  : {'on -> ' + str(cfg.cache_dir) if cfg.use_cache else 'OFF'}")
    print(f"  output     : {cfg.out_root / cfg.run_label}")

    notes = run_shared(cfg)
    profile = load_json(cfg.shared_dir() / "profile.json", {}) or {}

    results: Dict[str, Dict[str, Any]] = {}
    failures: Dict[str, str] = {}
    degraded: Dict[str, List[str]] = {}
    for model_key in cfg.models:
        banner(f"MODEL  {model_key}")
        out_dir = cfg.out_dir(model_key)
        done = (out_dir / "notes.json").exists() and \
               (out_dir / "evaluation.json").exists()
        if done and not getattr(cfg, "force_rerun", False):
            saved_fp = load_json(out_dir / "fingerprint.json", {}) or {}
            now_fp = _fingerprint(cfg, model_key)
            if saved_fp == now_fp:
                print(f"  [resume] already complete, reusing "
                      f"{out_dir / 'evaluation.json'}")
                print(f"           (pass --force to redo it)")
                results[model_key] = {
                    "notes": load_json(out_dir / "notes.json"),
                    "evaluation": load_json(out_dir / "evaluation.json"),
                }
                continue
            changed = ([k for k in now_fp if saved_fp.get(k) != now_fp[k]]
                       if saved_fp else ["no fingerprint.json"])
            failures[model_key] = ("stale artefact: "
                                   + ", ".join(changed))
            print(f"  [STALE] {model_key} already has results in this folder, "
                  f"but they were produced by a DIFFERENT configuration")
            print(f"          ({', '.join(changed)}).")
            print(f"          Refusing to mix them into one result table. Use "
                  f"a fresh run folder, or --force to overwrite.")
            continue
        try:
            results[model_key] = run_model(cfg, model_key, notes, profile)
            gaps = _incomplete_arms(results[model_key])
            if gaps:
                degraded[model_key] = gaps
                print(f"  [INCOMPLETE] {model_key}: " + "; ".join(gaps))
        except ProviderUnavailable as e:
            failures[model_key] = f"ProviderUnavailable: {e}"
            print(f"  [SKIPPED] {model_key}: every API key for its provider "
                  f"was rejected.\n            Top up or add another key file "
                  f"in keys/, then re-run the SAME command -\n"
                  f"            finished models are skipped and cached calls "
                  f"are free.")
        except Exception as e:
            failures[model_key] = f"{type(e).__name__}: {e}"
            print(f"  [FAILED] {model_key}: {type(e).__name__}: {e}")
            traceback.print_exc()

    run_dir = cfg.out_root / cfg.run_label
    if results:
        merged: Dict[str, Dict[str, Any]] = {}
        for d in sorted(run_dir.glob("*/")):
            ev = d / "evaluation.json"
            if d.name in results or not ev.exists():
                continue
            if d.name not in cfg.models:
                print(f"  [summary] skipping {d.name}/: present in the folder "
                      f"but not in this run's model panel.")
                continue
            loaded = load_json(ev, {})
            if loaded:
                merged[d.name] = {"evaluation": loaded}
        merged.update(results)
        s9_report.write(run_dir / "SUMMARY.md",
                        s9_report.cross_model_report(cfg, merged))
        print(f"\n  [saved] {run_dir / 'SUMMARY.md'}  ({len(merged)} models)")

    save_json(run_dir / "manifest.json", {
        "started": started,
        "finished": datetime.datetime.now().isoformat(timespec="seconds"),
        "config": cfg.to_dict(),
        "models_ok": sorted(k for k in results if k not in degraded),
        "models_degraded": degraded,
        "models_failed": failures,
        "dataset_profile": profile,
        "data_provenance": _data_provenance(cfg),
        "cache_stats": cache.stats(),
    })

    banner("DONE")
    for m in cfg.models:
        if m in degraded:
            status = "INCOMPLETE - " + "; ".join(degraded[m])
        elif m in results:
            status = "ok"
        else:
            status = f"FAILED - {failures.get(m)}"
        print(f"  {m:<26} {status}")
    print(f"\n  cache: {cache.stats()}")
    print(f"  artefacts: {run_dir}")
    if degraded:
        print(f"\n  {len(degraded)} model(s) are missing generations. Their "
              f"means cover only the generated notes and are not comparable "
              f"with complete models.\n  Re-run those models before reporting.")
    if failures or degraded:
        print(f"\n  {len(failures)} of {len(cfg.models)} requested models "
              f"produced nothing, {len(degraded)} produced partial results. "
              f"Exit code 1.")
        return 1
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
