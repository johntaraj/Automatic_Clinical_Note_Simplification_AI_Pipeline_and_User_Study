"""Stage 9: report.md, detail.md, cost.txt and the cross-model SUMMARY.md."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from config import Config
from metrics import registry as R
from metrics.stats import format_comparison


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _agg(evaluation: Dict[str, Any], arm: str, key: str) -> Optional[float]:
    v = (evaluation.get("aggregate") or {}).get(arm, {}).get(key)
    return v.get("mean") if isinstance(v, dict) else None


def _n(evaluation: Dict[str, Any], arms: List[str], key: str) -> Optional[int]:
    for arm in arms:
        v = (evaluation.get("aggregate") or {}).get(arm, {}).get(key)
        if isinstance(v, dict) and v.get("n") is not None:
            return v["n"]
    return None


def _ref(evaluation: Dict[str, Any], which: str, key: str) -> Optional[float]:
    v = (evaluation.get("reference_rows") or {}).get(which, {}).get(key)
    return v.get("mean") if isinstance(v, dict) else None


def build_report(cfg: Config, model_key: str, notes: List[Dict[str, Any]],
                 evaluation: Dict[str, Any], profile: Dict[str, Any]) -> str:
    spec = cfg.model_spec(model_key)
    arms = [a for a in cfg.arms if (evaluation.get("aggregate") or {}).get(a)]
    L: List[str] = []

    L += [
        f"# {spec.slug} - run `{cfg.run_label}`",
        "",
        f"- model: `{spec.model_id}` ({spec.provider}, {spec.backend} backend)",
        f"- notes: {len(notes)} from `{cfg.dataset}`   arms: {', '.join(arms)}",
        f"- tag policy `{cfg.tag_policy}` / keep-gloss `{cfg.keep_gloss_scope}` "
        f"/ prompt `{cfg.prompt_style}`",
        f"- ContextCite: "
        + (f"{cfg.cc_num_ablations}+{cfg.cc_heldout_ablations} masks, "
           f"<= {cfg.cc_max_sources} sources"
           if (cfg.cc_enabled and spec.contextcite) else "OFF"),
        "",
        "## How to read this",
        "",
        "Every metric is annotated with **direction** (higher or lower is "
        "better) and a **target**. Metrics are split into two tiers:",
        "",
        "- **PAPER** - argued to be reliable for this task; these carry the claims.",
        "- **APPENDIX** - reported for comparability with the literature, but "
        "with a documented weakness on this dataset. Each row states it.",
        "",
        "`ORIGINAL` is the untouched clinical sentence and `REFERENCE` is the "
        "human simplification. They are shown wherever the metric is defined "
        "for plain text, so every system number can be read against *how hard "
        "the input was* and *what a human achieved*.",
        "",
    ]

    if profile:
        L += ["### Dataset", "", "| property | value |", "|---|---:|"]
        for k, v in profile.items():
            if k != "note":
                L.append(f"| {k} | {v} |")
        L += ["", f"> {profile.get('note', '')}", ""]

    stage_m = evaluation.get("stage_metrics") or {}
    for tier, title in (("paper", "PAPER metrics"),
                        ("appendix", "APPENDIX metrics")):
        L += [f"## {title}", ""]
        by_stage: Dict[str, List[R.MetricSpec]] = {}
        run_level: Dict[str, List[R.MetricSpec]] = {}
        for m in R.REGISTRY:
            if m.tier != tier:
                continue
            if any(_agg(evaluation, a, m.key) is not None for a in arms):
                by_stage.setdefault(m.stage, []).append(m)
            elif stage_m.get(m.key) is not None:
                run_level.setdefault(m.stage, []).append(m)

        for stage in sorted(set(by_stage) | set(run_level)):
            L += [f"### {stage}", ""]
            if stage in by_stage:
                L += ["| metric | n | ORIGINAL | REFERENCE | "
                      + " | ".join(arms) + " | direction | target | note |",
                      "|---|---:|---:|---:|" + "---:|" * len(arms) + "---|---|---|"]
                for m in by_stage[stage]:
                    orig = R.fmt(m.key, _ref(evaluation, "input", m.key)) \
                        if m.reference_row else ""
                    refv = R.fmt(m.key, _ref(evaluation, "reference", m.key)) \
                        if m.reference_row else ""
                    cells = [R.fmt(m.key, _agg(evaluation, a, m.key)) for a in arms]
                    n = _n(evaluation, arms, m.key)
                    note = m.caveat or m.what
                    L.append(f"| **{m.label}** | {n if n is not None else ''} "
                             f"| {orig} | {refv} | "
                             + " | ".join(cells) + f" | {R.arrow(m.key)} "
                             f"| {m.target} | {note} |")
                L.append("")
            if stage in run_level:
                L += ["| run-level metric | value | direction | target | note |",
                      "|---|---:|---|---|---|"]
                for m in run_level[stage]:
                    note = m.caveat or m.what
                    L.append(f"| **{m.label}** | {R.fmt(m.key, stage_m[m.key])} "
                             f"| {R.arrow(m.key)} | {m.target} | {note} |")
                L.append("")

    a = evaluation.get("attribution") or {}
    if a.get("n_edits"):
        L += [
            "## Attribution detail (stage 5)", "",
            "`source_effect = log p(edit | full glossary) - log p(edit | no "
            "glossary)`. This is the only measurement in the suite that says "
            "whether retrieval *caused* an edit.", "",
            "| quantity | value | meaning |", "|---|---:|---|",
            f"| edits attributed | {a.get('n_edits')} | |",
            f"| ranked fits | {a.get('n_attributed')} | a source could be ranked |",
            f"| flat fits | {a.get('n_no_source_effect')} | scoring worked, no "
            f"source mattered - a RESULT, not a failure |",
            f"| measurement failures | {a.get('n_failed')} | aim for 0 |",
            f"| **helped** | {a.get('n_helped')} | retrieval made the edit more likely |",
            f"| **neutral** | {a.get('n_neutral')} | the model knew it anyway |",
            f"| **hurt** | {a.get('n_hurt')} | retrieval made it LESS likely |",
            f"| attributable rate | {a.get('attributable_rate')} | of helped edits, "
            f"those with a trustworthy explanation |",
            f"| **winning source is the right term** | {a.get('right_term_rate')} | "
            f"of {a.get('n_self_term_considered')} caused edits; the rest are "
            f"cross-term contamination |",
            f"| held-out LDS (median) | {a.get('lds_median')} | aim > 0.60 |",
            f"| in-sample LDS (median) | {a.get('lds_insample_median')} | for contrast only |",
            f"| **LDS optimism gap** | {a.get('lds_optimism_gap')} | how much an "
            f"in-sample number would overstate faithfulness |",
            f"| edits with no LDS | {a.get('n_lds_unavailable')} | glossary too "
            f"small for a genuinely unseen held-out block |",
            f"| **top-1 drop, helped edits** | {a.get('top1_drop_median_helped')} | "
            f"paper Eq. 1 over the {a.get('n_top1_drop_helped')} edits where a "
            f"source mattered - the number comparable to the paper's Fig. 4a |",
            f"| **top-3 drop, helped edits** | {a.get('top3_drop_median_helped')} | "
            f"same, removing the top three |",
            f"| top-1 drop, ALL edits | {a.get('top1_drop_median')} | ~0 by "
            f"construction on the {a.get('n_neutral')} edits with no source "
            f"effect; do NOT quote this against the paper |",
            f"| ablation success | {a.get('ablation_success_rate')} | transport health |",
            "",
            "> Surrogate target: **logit-scaled probability**, per ContextCite "
            "Algorithm 1 line 4. Bucketing uses the log-probability difference, "
            "which answers \"would the model have produced this anyway?\". Both "
            "are stored per edit.",
            "",
        ]
        if a.get("relevant_source_rate") is not None:
            L += [
                "**Leave-one-out check** (`--leave-one-out`). Each entry ablated "
                "on its own, the rest of the glossary left in place. This is the "
                "baseline the paper *beats* (Sec. 4), not its method - it is "
                "here to validate the surrogate, not to replace it.", "",
                "| quantity | value | meaning |", "|---|---:|---|",
                f"| edits with >=1 individually relevant entry | "
                f"{a.get('relevant_source_rate')} | the paper's delta = 2 "
                f"criterion (App. A.4). Unlike `helped`, this removes ONE entry "
                f"and leaves the rest in place, so it cannot be dismissed as a "
                f"prompt-length effect |",
                f"| relevant entries per edit (median) | "
                f"{a.get('n_relevant_sources_median')} | analogue of the paper's "
                f"Figure 3a; staying small is the point |",
                f"| LASSO top-1 == oracle top-1 | "
                f"{a.get('oracle_agreement')} | over "
                f"{a.get('n_lasso_loo_compared')} edits - the cheap method "
                f"reaching the expensive method's answer |",
                "",
            ]
        sweep = evaluation.get("attribution_threshold_sweep") or []
        if sweep:
            L += ["**Threshold sensitivity** (the helped/hurt split depends on "
                  "an arbitrary cut-off, so it is swept):", "",
                  "| eps (nats) | helped | neutral | hurt | attributable |",
                  "|---:|---:|---:|---:|---:|"]
            for r in sweep:
                L.append(f"| {r['eps']} | {r['helped']} | {r['neutral']} | "
                         f"{r['hurt']} | {r['attributable_rate']} |")
            L.append("")

    strat = (evaluation.get("stratified") or {}).get("edits_by_zipf_stratum") or {}
    if strat:
        L += ["### Does grounding help more on rare terms?", "",
              "| Zipf stratum | edits | helped | neutral | hurt | helped rate | mean effect (nats) |",
              "|---|---:|---:|---:|---:|---:|---:|"]
        for name in ("very_rare", "rare", "uncommon", "common", "unknown"):
            b = strat.get(name)
            if b:
                L.append(f"| {name} | {b['n_edits']} | {b['n_helped']} | "
                         f"{b['n_neutral']} | {b['n_hurt']} | {b['helped_rate']} | "
                         f"{b['mean_source_effect']} |")
        L.append("")

    cov = evaluation.get("whole_term_coverage") or {}
    if cov:
        o = cov.get("overall", {})
        strict, addressed = o.get("coverage"), o.get("coverage_addressed")
        L += ["### Retrieval coverage (stage 3)", "",
              f"**{addressed}** of the extractor's terms had usable evidence in "
              f"the prompt by any route "
              f"({o.get('n_addressed')}/{o.get('n_terms')}).",
              "",
              f"Strict whole-term coverage is **{strict}** "
              f"({o.get('n_covered')}/{o.get('n_terms')}) - a lower bound, "
              f"because a compound with no whole-phrase entry is usually handled "
              f"by splitting it and every piece still reaches the prompt.",
              "",
              "| Zipf stratum | terms | covered | coverage | addressed |",
              "|---|---:|---:|---:|---:|"]
        for name, b in (cov.get("by_zipf_stratum") or {}).items():
            L.append(f"| {name} | {b['n_terms']} | {b['n_covered']} | "
                     f"{b['coverage']} | {b.get('coverage_addressed')} |")
        rare = (cov.get("by_zipf_stratum") or {}).get("very_rare") or {}
        common = (cov.get("by_zipf_stratum") or {}).get("common") or {}
        r_cov, c_cov = rare.get("coverage"), common.get("coverage")
        if r_cov is not None and c_cov is not None:
            verdict = ("Coverage is HIGHER on common terms than on rare ones, so "
                       "retrieval is firing where it cannot add value."
                       if c_cov > r_cov else
                       "Coverage is at least as good on rare terms as on common "
                       "ones, which is the direction retrieval needs.")
            L += ["", f"> {verdict} (very_rare {r_cov} vs common {c_cov})", ""]
        else:
            L.append("")

        align = (evaluation.get("source_alignment") or {}).get("overall") or {}
        if align:
            L += [f"Orphan-term rate **{align.get('orphan_term_rate')}** "
                  f"({align.get('n_orphan')}/{align.get('n_terms')} terms have NO "
                  f"entry about them in the prompt). ContextCite masks every "
                  f"shown entry for every edit, so an orphan term is attributed "
                  f"against pure noise - those are RETRIEVAL failures, not "
                  f"attribution failures.", ""]

        dr = evaluation.get("definition_readability") or {}
        if dr:
            L += [f"The {dr.get('n_definitions')} definitions actually shown read "
                  f"at **FKGL {dr.get('definition_fkgl')}** (median "
                  f"{dr.get('definition_fkgl_median')}). Grounded outputs borrow "
                  f"this vocabulary, so this is half of the lexical-borrowing "
                  f"story.", "",
                  "| glossary | mean FKGL of its entries |", "|---|---:|"]
            for src, val in (dr.get("by_source") or {}).items():
                L.append(f"| {src} | {val} |")
            L.append("")

        if cov.get("unaddressed_terms"):
            L += ["Nothing retrieved at all: "
                  + ", ".join(f"`{t}`" for t in cov["unaddressed_terms"]), ""]

    ra = evaluation.get("rationale_audit") or {}
    if ra.get("n_rationales"):
        L += ["### Rationale grounding (stages 6-7)", "",
              f"{ra['n_rationales']} rationales audited.", "",
              "| metric | value | direction | target |", "|---|---:|---|---|"]
        for k in ("rationale_fabrication_rate", "rationale_omission_rate",
                  "rationale_fact_recall", "rationale_source_correct",
                  "rationale_quote_verified", "rationale_template_rate"):
            m = R.spec(k)
            if m and ra.get(k) is not None:
                L.append(f"| {m.label} | {R.fmt(k, ra[k])} | {R.arrow(k)} | {m.target} |")
        L += ["", "> **grounding errors** (wrong source, invented quote, wrong "
              "number) and **omissions** (a statistic simply not mentioned) are "
              "reported separately. v7 merged them into one 42.3% "
              "'hallucination rate' that was almost entirely omissions.", ""]

    L += ["## Paired comparisons", ""]
    if len(notes) < 20:
        L += [f"> **Not reportable at n={len(notes)}.** The minimum achievable "
              "one-sided Wilcoxon p is 1/2^n and nothing can survive FDR "
              "correction. Shown only to verify the machinery.", ""]
    for cmp in evaluation.get("comparisons", []):
        L += ["```", format_comparison(cmp), "```", ""]

    L += ["## Clinical-safety flags", ""]
    any_flag = False
    for note in notes:
        for arm in arms:
            rec = (note.get("arms") or {}).get(arm) or {}
            for fl in (rec.get("detail", {}).get("safety") or {}).get("safety_flags") or []:
                any_flag = True
                L.append(f"- note {note['note_idx']} / `{arm}` / **{fl['slot']}** "
                         f"({fl['severity']}): lost {fl.get('lost') or fl.get('input_cues')}")
    if not any_flag:
        L.append("None raised.")
    L.append("")

    L += ["## Outputs", ""]
    for note in notes:
        L += [f"### Note {note['note_idx']} - `{note.get('id')}`"
              + (f" ({note['difficulty']})" if note.get("difficulty") else ""), ""]
        im = note.get("input_metrics") or {}
        rm = note.get("reference_metrics") or {}
        L += [f"- **ORIGINAL**  (FKGL {im.get('fkgl', '?'):.1f}, "
              f"{im.get('n_words', 0)} words): {note.get('original_clean') or note['original']}",
              f"- **REFERENCE** (FKGL {rm.get('fkgl', 0):.1f}, "
              f"{rm.get('n_words', 0)} words): {note.get('reference', '')}"]
        for arm in arms:
            rec = (note.get("arms") or {}).get(arm) or {}
            m = rec.get("metrics") or {}
            bits = [f"FKGL {m[k]:.1f}" if (k == "fkgl" and isinstance(m.get(k), float))
                    else "" for k in ("fkgl",)]
            extra = "  ".join(f"{lab}={m[k]:.2f}" for k, lab in
                              (("sari", "SARI"), ("critical_error", "crit"),
                               ("nli_faithfulness", "NLIf"), ("copy_jargon_rate", "copyjrg"))
                              if isinstance(m.get(k), float))
            L.append(f"- **{arm}** ({' '.join(b for b in bits if b)}, "
                     f"{m.get('n_words', 0)} words, "
                     f"{len(rec.get('operations') or [])} edits): {rec.get('output', '')}")
            if extra:
                L.append(f"    - {extra}")
        L.append("")

    return "\n".join(L)


def build_detail(cfg: Config, model_key: str, notes: List[Dict[str, Any]]) -> str:
    spec = cfg.model_spec(model_key)
    L = [f"# Step-by-step detail - {spec.slug} (`{cfg.run_label}`)", "",
         "Everything the pipeline did, per note and per stage. Not summarised.",
         ""]

    for note in notes:
        L += ["=" * 78, "",
              f"## Note {note['note_idx']} - `{note.get('id')}`"
              + (f"  ({note['difficulty']})" if note.get("difficulty") else ""),
              "",
              f"**ORIGINAL**  {note.get('original_clean') or note['original']}", "",
              f"**REFERENCE** {note.get('reference', '')}", ""]

        im, rm = note.get("input_metrics") or {}, note.get("reference_metrics") or {}
        if im:
            L += ["| | FKGL | FRE | SMOG | Coleman-Liau | words |",
                  "|---|---:|---:|---:|---:|---:|",
                  f"| ORIGINAL | {im.get('fkgl'):.2f} | {im.get('fre'):.2f} | "
                  f"{im.get('smog'):.2f} | {im.get('coleman_liau'):.2f} | {im.get('n_words')} |",
                  f"| REFERENCE | {rm.get('fkgl'):.2f} | {rm.get('fre'):.2f} | "
                  f"{rm.get('smog'):.2f} | {rm.get('coleman_liau'):.2f} | {rm.get('n_words')} |",
                  ""]

        L += ["### Stage 2 - extraction + classification", "",
              "| term | kind | category | action | Zipf | AoA | syll |",
              "|---|---|---|---|---:|---:|---:|"]
        for it in note.get("hard_items", []):
            f = it.get("features") or {}
            L.append(f"| `{it.get('text')}` | {it.get('kind')} | {it.get('category')} "
                     f"| {it.get('action')} | {f.get('zipf', '-')} | {f.get('aoa', '-')} "
                     f"| {f.get('syllables', '-')} |")
        L.append("")

        ret = note.get("retrieval") or {}
        L += ["### Stage 3 - retrieval", "",
              f"coverage **{ret.get('coverage')}** "
              f"({ret.get('n_covered')}/{ret.get('n_terms')}), "
              f"glossary budget {len(note.get('sources') or [])}/{cfg.cc_max_sources}", "",
              "| term | Zipf stratum | defs | sources | matched via | origin |",
              "|---|---|---:|---|---|---|"]
        for r in ret.get("per_term", []):
            L.append(f"| `{r['term']}` | {r['stratum']} | {r['n_defs']} | "
                     f"{', '.join(r['sources']) or '-'} | {r.get('lookup_variant') or '-'} "
                     f"| {r.get('origin')} |")
        L.append("")
        if note.get("sources"):
            L += ["Glossary shown to the model:", ""]
            for i, s in enumerate(note["sources"], 1):
                L.append(f"{i}. `[{s['source']}]` {s['text']}")
            L.append("")

        for arm, rec in (note.get("arms") or {}).items():
            L += [f"### Stage 4 - arm `{arm}`", "",
                  f"**output:** {rec.get('output', '')}", ""]
            m = rec.get("metrics") or {}
            if m:
                L += ["| metric | value |", "|---|---:|"]
                for k in sorted(m):
                    if isinstance(m[k], (int, float)):
                        L.append(f"| {k} | {R.fmt(k, m[k])} |")
                L.append("")
            ann = rec.get("annotation") or {}
            if ann:
                L += [f"annotation backend `{ann.get('backend')}`, "
                      f"{ann.get('n_ops')} edits kept", ""]
                for line in ann.get("dropped", []):
                    L.append(f"- rejected: {line}")
                L.append("")

            ops = rec.get("operations") or []
            if ops:
                L += ["| edit | type | status | effect (nats) | logit | "
                      "LDS held | LDS in | margin | top-1 drop |",
                      "|---|---|---|---:|---:|---:|---:|---:|---:|"]
                for op in ops:
                    cc = op.get("contextcite") or {}
                    def g(k, f="{:.3f}"):
                        v = cc.get(k)
                        return f.format(v) if isinstance(v, (int, float)) else "-"
                    L.append(f"| `{op.get('src_text')}` -> `{op.get('tgt_text')}` "
                             f"| {op.get('type')} | {cc.get('status', '-')} "
                             f"| {g('source_effect')} | {g('source_effect_logit')} "
                             f"| {g('lds')} | {g('lds_insample')} "
                             f"| {g('winner_margin')} "
                             f"| {(cc.get('top_k_drops') or {}).get('1', '-')} |")
                L.append("")

                for op in ops:
                    cc = op.get("contextcite") or {}
                    if not cc:
                        continue
                    L += [f"**edit `{op.get('src_text')}` -> `{op.get('tgt_text')}`**", "",
                          f"- status: `{cc.get('status')}`"
                          + (f" - {cc.get('invalid_reason')}" if cc.get("invalid_reason") else ""),
                          f"- log p full {cc.get('original_log_prob'):.4f}, "
                          f"empty {cc.get('empty_log_prob'):.4f}",
                          f"- masks scored: {cc.get('num_valid_ablations')}/"
                          f"{cc.get('num_valid_ablations', 0) + cc.get('num_failed_ablations', 0)}"
                          f" (+{cc.get('extra_calls', 0)} top-k)"]
                    tops = op.get("top_sources") or []
                    if tops:
                        L.append("- ranked sources:")
                        for s in tops:
                            if abs(s.get("weight", 0)) > 1e-9:
                                L.append(f"    - `{s['weight']:+.3f}` "
                                         f"[{s.get('source')}] {str(s.get('text'))[:110]}")
                    rat = op.get("rationale") or {}
                    if rat.get("text"):
                        L += ["", f"- rationale: {rat['text']}"]
                    aud = op.get("rationale_audit") or {}
                    if aud:
                        L.append(f"- audit: coverage {aud['slot_coverage']}, "
                                 f"grounding_error={aud['grounding_error']}, "
                                 f"omission={aud['omission']}, "
                                 f"source_ok={aud['source_ok']}, "
                                 f"passage_ok={aud['passage_ok']}")
                    L.append("")
    return "\n".join(L)


def cross_model_report(cfg: Config, results: Dict[str, Dict[str, Any]]) -> str:
    arms = list(cfg.arms)
    L = [f"# Cross-model summary - `{cfg.run_label}`", "",
         f"Models: {', '.join(results)}", "",
         "PAPER-tier metrics only. See each model's `report.md` for the "
         "appendix tier and the caveats.", ""]
    for m in R.REGISTRY:
        if m.tier != "paper":
            continue
        rows = []
        for model, res in results.items():
            cells = [R.fmt(m.key, _agg(res["evaluation"], a, m.key)) for a in arms]
            if any(c != "--" for c in cells):
                rows.append((model, cells))
        if not rows:
            continue
        L += [f"## {m.label}   ({R.arrow(m.key)}, target {m.target})", "",
              f"*{m.what}*", "",
              "| model | " + " | ".join(arms) + " |",
              "|---|" + "---:|" * len(arms)]
        for model, cells in rows:
            L.append(f"| {model} | " + " | ".join(cells) + " |")
        L.append("")

    L += ["## Attribution", "",
          "| model | edits | ranked | flat | failed | helped | neutral | hurt "
          "| attributable | LDS held | LDS in | gap |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for model, res in results.items():
        a = res["evaluation"].get("attribution") or {}
        L.append(f"| {model} | {a.get('n_edits', 0)} | {a.get('n_attributed', 0)} "
                 f"| {a.get('n_no_source_effect', 0)} | {a.get('n_failed', 0)} "
                 f"| {a.get('n_helped', 0)} | {a.get('n_neutral', 0)} "
                 f"| {a.get('n_hurt', 0)} | {a.get('attributable_rate')} "
                 f"| {a.get('lds_median')} | {a.get('lds_insample_median')} "
                 f"| {a.get('lds_optimism_gap')} |")
    L.append("")
    return "\n".join(L)
