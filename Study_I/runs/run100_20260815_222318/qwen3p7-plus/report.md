# qwen3p7-plus - run `run100_20260815_222318`

- model: `accounts/fireworks/models/qwen3p7-plus` (fireworks, fireworks backend)
- notes: 100 from `laymaker`   arms: naive, termonly, grounded
- tag policy `replace` / keep-gloss `names` / prompt `lean`
- ContextCite: 32+32 masks, <= 16 sources

## How to read this

Every metric is annotated with **direction** (higher or lower is better) and a **target**. Metrics are split into two tiers:

- **PAPER** - argued to be reliable for this task; these carry the claims.
- **APPENDIX** - reported for comparability with the literature, but with a documented weakness on this dataset. Each row states it.

`ORIGINAL` is the untouched clinical sentence and `REFERENCE` is the human simplification. They are shown wherever the metric is defined for plain text, so every system number can be read against *how hard the input was* and *what a human achieved*.

### Dataset

| property | value |
|---|---:|
| n_notes | 100 |
| mean_words_original | 12.25 |
| mean_words_reference | 14.74 |
| mean_token_jaccard_orig_ref | 0.584 |
| mean_tokens_removed_by_reference | 2.32 |
| mean_tokens_added_by_reference | 4.32 |
| mean_fkgl_original | 10.51 |
| mean_fkgl_reference | 8.54 |

> References are minimal-edit lexical replacements. SARI and BERTScore against them under-credit any system that also restructures grammar; see metrics/sari.py for the worked counter-example.

## PAPER metrics

### 2 extraction

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **extraction stability** | 0.800 | higher is better | > 0.90 | the only stage-2 number that does not require hand annotation. It matters because everything downstream is conditioned on the term list: if this is below ~0.9, two runs of the identical config are not comparable and an A/B measures extraction noise rather than the change under test |

### 3 retrieval

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **terms with evidence shown** | 0.965 | higher is better | > 0.90 overall; the very_rare stratum is the binding one | answers the question retrieval actually exists to answer: did the generator have evidence for this term. Still says nothing about whether the evidence was USED (that is attribution's job) or whether it was any good - `C-diff: Clostridioides difficile` counted as covered and caused the run's worst hallucination |
| **orphan-term rate** | 0.021 | LOWER is better | < 0.10 | different from whole_term_coverage: a term can be 'covered' by the retriever yet lose its entry to the 16-slot budget, or be covered only by an entry about a different term. ContextCite masks every shown entry for every edit, so an orphan term is attributed against pure noise - those edits are RETRIEVAL failures and should be excluded from attribution statistics |

### 4 edits

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **generation success rate** | 100 |  |  | 1.000 | 1.000 | 1.000 | higher is better | 1.00 | a blank output contributes NO metrics, so it silently leaves the averages rather than scoring zero - a model that fails on hard notes would otherwise look better than one that tries. Read every other mean against this number |
| **usable-output rate** | 100 |  |  | 1.000 | 1.000 | 1.000 | higher is better | 1.00 | the companion to generation_success_rate, which only checks that an output is NON-EMPTY. An echo of the system prompt or a bare '### Response:' is non-empty, scores 1.000 there, and then poisons every readability, NLI and length number computed from it. Measured after up to max_generation_attempts tries, so a value below 1.00 means the model could not be coaxed into a rewrite even on retry. Detection is a fixed marker list (core/validity.py), so it is a LOWER bound on the true rate |
| **human edit recall** | 99 |  |  | 0.718 | 0.976 | 0.981 | higher is better | > 0.85 | of the jargon the human replaced, how much did we replace |

### 4 faithfulness

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **NLI faithfulness** | 100 |  |  | 0.833 | 0.826 | 0.839 | higher is better | > 0.70 | general-domain MNLI head; absolute values are compressed |
| **NLI completeness** | 100 |  |  | 0.820 | 0.790 | 0.807 | higher is better | > 0.60 | omission is the dominant clinical failure mode, which is why this direction is reported separately |

### 4 readability

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **FKGL drop vs input** | 100 |  |  | 3.77 | 4.03 | 3.73 | higher is better | > +4 grades | gameable by chopping sentences - read with length ratio |
| **Coleman-Liau drop** | 100 |  |  | 4.56 | 4.56 | 4.41 | higher is better | > +4 | none - this is the robustness check on FKGL |
| **length ratio vs reference** | 100 |  |  | 1.06 | 0.95 | 0.96 | descriptive | 0.9-1.3 | descriptive, not a quality score; >1.4 means the model is glossing everything |

### 4 safety

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **critical-error rate** | 100 |  |  | 0.130 | 0.100 | 0.100 | LOWER is better | 0.00 - any value > 0 needs review | fraction of outputs that lost a high-risk slot: negation, uncertainty, laterality, a number/unit, or a drug name |

### 5 attribution

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **attributable rate** | 0.607 | higher is better | > 0.50 | of the edits retrieval demonstrably caused, the fraction with a trustworthy explanation (held-out LDS >= 0.4, clear winner) |
| **held-out LDS (median)** | 0.693 | higher is better | > 0.60 (paper reports 0.6-0.85) | Spearman between the surrogate's predictions and the true log-probs on masks it never saw - how trustworthy the attributions are |
| **helped rate** | 0.316 | descriptive | descriptive - the split is the finding | fraction of edits retrieval made more likely (effect >= 0.10 nats) |
| **hurt rate** | 0.000 | LOWER is better | < 0.10 | fraction of edits retrieval made LESS likely - glossary actively harming the rewrite |
| **top-1 log-prob drop (helped edits)** | 0.96 | higher is better | > 0.5 nats | the paper reports roughly 0.43-0.75 for top-1 across three benchmarks, so this is the number to compare against |
| **winning source is the right term** | 0.929 | higher is better | > 0.80 | the complement is cross-term contamination - the definition of a DIFFERENT word in the same sentence winning the attribution and changing the meaning. Needs no gold labels, which is what makes it the closest thing this family has to a precision score |

## APPENDIX metrics

### 3 retrieval

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **whole-term coverage** | 0.648 | higher is better | > 0.80 overall; the RARE strata matter | a strict lower bound, and demoted to the appendix because of it. A compound with no whole-phrase entry may still be handled by splitting, and those pieces DO reach the prompt: on the 93-note run 71 of 86 apparent misses were phrases like `chronic UTIs`, whose parts were both defined and both shown. Quote `evidence_coverage` as the headline. Counts extracted terms only; salvaged fragments are definable by construction and are reported separately as `coverage_incl_salvage` |
| **expansion definitions** | 4 | descriptive |  | fires rarely by design (3 terms / 93 notes) - it triggers only when a definition NAMES the term instead of explaining it and the expansion contains a rare token to query with. Append-only, so it can add evidence but never removes the expansion itself |
| **definitions per term** | 1.68 | descriptive | 2-3 | average glossary entries retrieved per covered term |
| **definition reading grade** | 8.65 | LOWER is better | 6-8 (US grade) | the missing half of the lexical-borrowing finding. Grounded outputs demonstrably reuse the definition's vocabulary, so how the definitions are WRITTEN decides whether that helps. A high grade here predicts that borrowing hurts, and it is what separates 'making more pee' from 'Clostridioides difficile' |
| **entries about the edited term** | 3.17 | higher is better | >= 1.0 | how many of the shown entries are about the term being edited |

### 4 edits

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **first-attempt success rate** | 100 |  |  | 1.000 | 1.000 | 1.000 | higher is better | > 0.95 | the honest measure of how stable a model is on this task. Reported separately from output_valid_rate because retrying HIDES instability: a model that needs three attempts on a third of the corpus can still finish at output_valid_rate 1.000. Quote both, and remember the retries cost real money |
| **mean generation attempts** | 100 |  |  | 1.000 | 1.000 | 1.000 | LOWER is better | 1.00 | descriptive. Reads as a cost multiplier for the arm: 1.30 means 30% more generation calls than the ideal |
| **copy-jargon rate** | 99 |  |  | 0.282 | 0.024 | 0.019 | LOWER is better | < 0.10 | exactly 1 - human_edit_recall, by construction: every gold term is either recalled or copied. Report it as a restatement, not as separate evidence, and keep it out of the significance family or one result consumes two FDR slots |
| **reference-vocabulary hit (NOT a precision)** | 85 |  |  | 0.624 | 0.741 | 0.753 | higher is better | descriptive only - see caveat | BROKEN AS NAMED, measured 2026-08-15. The support test is `ref_added & sys_content_words`, and `ref_added` is derived from (reference, original) only - it does not depend on the term being scored. So the same verdict is applied to every changed term in a note and the per-note value can only be 0 or 1. Verified on CLEAN93/qwen3p7-plus: 265 of 265 note-arm values are exactly 0.0 or 1.0, and no note has two terms that disagree. One incidental shared word credits every replacement in the sentence. Making this a real precision needs term-to-replacement span alignment, which does not exist yet. Do not quote it as evidence that replacements were correct |
| **definition borrowing** | 85 |  |  | 0.424 | 0.479 | 0.512 | descriptive | descriptive - the arm gap IS the finding | the mechanism behind the grounded-vs-termonly result, measured per note instead of only in analysis/conditional_grounding.py. Deliberately DESCRIPTIVE: grounded is shown the definitions and the other arms are not, so a difference here is expected by construction and testing it would burn an FDR slot to confirm something guaranteed. Read it as 'how much of the glossary's wording ended up in the output', then read what that cost in human_edit_recall and NLI |
| **replacement F1 (inherits a broken precision)** | 99 |  |  | 0.490 | 0.751 | 0.764 | higher is better | descriptive only - see caveat | DEMOTED from paper tier 2026-08-15. Half of it is replacement_precision, which is not per-term (see its caveat), so this cannot support a claim that the system replaced jargon CORRECTLY. Quote human_edit_recall instead - that half is genuinely per-term and is unaffected |
| **rewrite aggressiveness** | 100 |  |  | 0.378 | 0.142 | 0.141 | descriptive | descriptive | NOT an error rate - legitimate restructuring scores here |

### 4 quality

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **SARI** | 100 |  |  | 32.21 | 46.20 | 46.55 | higher is better | 40-60 typical | the references are MINIMAL-EDIT, so SARI rewards not editing. Measured: a perfect rewrite scored 25.97 vs 22.64 for doing nothing. Report, do not lead with it |
| **BERTScore F1** | 100 |  |  | 0.594 | 0.689 | 0.693 | higher is better | 0.4-0.7 rescaled | read the RESCALED value. Until bug 42 the baseline lookup was silently failing for a local model directory, so raw scores were reported and everything landed in 0.90-0.96 - which is why this metric was demoted for having no dynamic range. Rescaled, the same 5 notes span 0.556-0.620, a gap six times wider. The demotion should be re-examined on the full run |

### 4 readability

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **FKGL (absolute)** | 100 | 10.51 | 8.54 | 6.75 | 6.49 | 6.78 | LOWER is better | 6-8 (US grade) | absolute grade is dominated by sentence length; the DROP is the honest number |
| **Coleman-Liau (absolute)** | 100 | 12.78 | 9.80 | 8.23 | 8.22 | 8.38 | LOWER is better | 6-8 | character-based grade level |
| **Flesch Reading Ease** | 100 | 41.1 | 60.0 | 70.6 | 72.5 | 70.7 | higher is better | 60-80 (plain English) | uses the SAME two inputs as FKGL; not independent evidence |
| **FRE gain** | 100 |  |  | 29.6 | 31.4 | 29.6 | higher is better | > +20 | redundant with fkgl_drop |
| **SMOG** | 100 | 11.49 | 9.83 | 8.05 | 7.73 | 8.07 | LOWER is better | 6-8 | calibrated for 30+ sentence passages; very jumpy on one sentence |
| **SMOG drop** | 100 |  |  | 3.44 | 3.76 | 3.42 | higher is better | > +3 | same single-sentence calibration problem |
| **words out** | 100 | 12.2 | 14.8 | 14.9 | 13.6 | 13.8 | descriptive | close to the reference | output length |

### 4 safety

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **drug-name preservation** | 2 |  |  | 1.000 | 0.000 | 0.000 | higher is better | 1.00 - nothing less is acceptable | APPENDIX because of the DENOMINATOR, not the metric: only 2 of the 93 laymaker notes contain a detected drug name, so the mean is two observations wearing a percentage. Report the cases, not the rate. Also read it against tag_policy - under `replace` the pipeline is INSTRUCTED to drop drug names |
| **diagnostic-identity preservation** | 5 |  |  | 1.000 | 1.000 | 1.000 | higher is better | 1.00 - nothing less is acceptable | scored only over a closed curated table of conditions, and only 4 of 93 notes contain one, so the mean is four observations. An unlisted diagnosis is not scored rather than guessed at, so this under-reports rather than over-reports. Report the cases |
| **severity downgrade rate** | 10 |  |  | 0.200 | 0.300 | 0.200 | LOWER is better | 0.00 | 3-tier ordinal lexicon; lay renderings ('very bad') sit at the same tier as their clinical equivalent so correct paraphrase is not penalised. Appendix on denominator: 10 of 93 notes state a severity at all |
| **number/unit preservation** | 14 |  |  | 0.714 | 0.893 | 0.893 | higher is better | 1.00 | all doses and units survive (spelled-out numbers and expanded unit abbreviations count) |
| **negation preservation** | 24 |  |  | 0.875 | 0.875 | 0.875 | higher is better | 1.00 | type-level, so it cannot see WHICH negation was lost |
| **laterality preservation** | 8 |  |  | 0.812 | 0.812 | 0.812 | higher is better | 1.00 | left/right/bilateral/basal survive (instance-level) |
| **uncertainty preservation** | 9 |  |  | 0.778 | 0.778 | 0.778 | higher is better | 1.00 | hedging survives - 'cannot be excluded' must not become 'is present' |

### 5 attribution

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **LDS optimism gap** | 0.149 | LOWER is better | < 0.15 | a methodological result in its own right, not a quality score |
| **top-1 log-prob drop (all edits)** | 0.09 | higher is better | descriptive | NOT comparable to the paper's Figure 4a. Most edits have no source effect at all, so there is nothing to remove and the drop is ~0 by construction; the median over all edits therefore reads as a failure when the method is working. Quote `top1_drop_median_helped` instead |
| **ablation success rate** | 1.000 | higher is better | 1.00 | scoring calls that returned usable log-probs - a transport health check, not a quality metric |

## Attribution detail (stage 5)

`source_effect = log p(edit | full glossary) - log p(edit | no glossary)`. This is the only measurement in the suite that says whether retrieval *caused* an edit.

| quantity | value | meaning |
|---|---:|---|
| edits attributed | 177 | |
| ranked fits | 177 | a source could be ranked |
| flat fits | 0 | scoring worked, no source mattered - a RESULT, not a failure |
| measurement failures | 0 | aim for 0 |
| **helped** | 56 | retrieval made the edit more likely |
| **neutral** | 121 | the model knew it anyway |
| **hurt** | 0 | retrieval made it LESS likely |
| attributable rate | 0.6071 | of helped edits, those with a trustworthy explanation |
| **winning source is the right term** | 0.9286 | of 56 caused edits; the rest are cross-term contamination |
| held-out LDS (median) | 0.6926 | aim > 0.60 |
| in-sample LDS (median) | 0.8415 | for contrast only |
| **LDS optimism gap** | 0.1489 | how much an in-sample number would overstate faithfulness |
| edits with no LDS | 59 | glossary too small for a genuinely unseen held-out block |
| **top-1 drop, helped edits** | 0.9593 | paper Eq. 1 over the 56 edits where a source mattered - the number comparable to the paper's Fig. 4a |
| **top-3 drop, helped edits** | 1.9319 | same, removing the top three |
| top-1 drop, ALL edits | 0.0938 | ~0 by construction on the 121 edits with no source effect; do NOT quote this against the paper |
| ablation success | 1.0 | transport health |

> Surrogate target: **logit-scaled probability**, per ContextCite Algorithm 1 line 4. Bucketing uses the log-probability difference, which answers "would the model have produced this anyway?". Both are stored per edit.

**Threshold sensitivity** (the helped/hurt split depends on an arbitrary cut-off, so it is swept):

| eps (nats) | helped | neutral | hurt | attributable |
|---:|---:|---:|---:|---:|
| 0.05 | 109 | 39 | 29 | 0.4771 |
| 0.1 | 96 | 56 | 25 | 0.4792 |
| 0.25 | 82 | 79 | 16 | 0.5366 |
| 0.693 | 56 | 121 | 0 | 0.6071 |
| 1.0 | 45 | 132 | 0 | 0.6222 |

### Does grounding help more on rare terms?

| Zipf stratum | edits | helped | neutral | hurt | helped rate | mean effect (nats) |
|---|---:|---:|---:|---:|---:|---:|
| very_rare | 49 | 17 | 31 | 0 | 0.3542 | 0.7649 |
| rare | 67 | 25 | 42 | 0 | 0.3731 | 1.228 |
| uncommon | 49 | 12 | 37 | 0 | 0.2449 | 0.7432 |
| common | 11 | 1 | 10 | 0 | 0.0909 | 1.3485 |
| unknown | 2 | 1 | 1 | 0 | 0.5 | 0.4411 |

### Retrieval coverage (stage 3)

**0.9648** of the extractor's terms had usable evidence in the prompt by any route (219/227).

Strict whole-term coverage is **0.6476** (147/227) - a lower bound, because a compound with no whole-phrase entry is usually handled by splitting it and every piece still reaches the prompt.

| Zipf stratum | terms | covered | coverage | addressed |
|---|---:|---:|---:|---:|
| very_rare | 61 | 33 | 0.541 | 0.8852 |
| rare | 77 | 53 | 0.6883 | 0.987 |
| uncommon | 68 | 47 | 0.6912 | 1.0 |
| common | 18 | 12 | 0.6667 | 1.0 |
| unknown | 3 | 2 | 0.6667 | 1.0 |

> Coverage is HIGHER on common terms than on rare ones, so retrieval is firing where it cannot add value. (very_rare 0.541 vs common 0.6667)

Orphan-term rate **0.0211** (8/380 terms have NO entry about them in the prompt). ContextCite masks every shown entry for every edit, so an orphan term is attributed against pure noise - those are RETRIEVAL failures, not attribution failures.

The 770 definitions actually shown read at **FKGL 8.65** (median 8.41). Grounded outputs borrow this vocabulary, so this is half of the lexical-borrowing story.

| glossary | mean FKGL of its entries |
|---|---:|
| dorland | 13.93 |
| iowa | 10.13 |
| justplainclear | 10.0 |
| dictionary | 9.9 |
| thesaurus | 9.39 |
| nih | 9.17 |
| readme | 9.16 |
| wiktionary | 7.83 |
| michigan | 6.69 |

Nothing retrieved at all: `Ativan`, `Lasix`, `anhedonic`, `cardio`, `hepatosplenomegaly`, `nonmobile`, `paresthesias`, `retrosternal area`

### Rationale grounding (stages 6-7)

178 rationales audited.

| metric | value | direction | target |
|---|---:|---|---|
| rationale fabrications | 0.000 | LOWER is better | < 0.05 |
| rationale slot omissions | 0.006 | LOWER is better | < 0.40 |
| rationale fact recall | 0.997 | higher is better | > 0.85 |
| rationale source correct | 1.000 | higher is better | > 0.95 |
| rationale quote verified | 1.000 | higher is better | 1.00 |
| templated rationales | 0.000 | LOWER is better | < 0.30 |

> **grounding errors** (wrong source, invented quote, wrong number) and **omissions** (a statistic simply not mentioned) are reported separately. v7 merged them into one 42.3% 'hallucination rate' that was almost entirely omissions.

## Paired comparisons

```

====================================================================================================
  PAIRED COMPARISON   termonly  vs  naive
====================================================================================================
  Wilcoxon one-sided ('termonly' better), paired bootstrap 95% CI, rank-biserial effect size.
  13 tests -> Benjamini-Hochberg FDR at alpha=0.05. Report p_adj, not p.

  metric                       n  dir  termonly     naive     diff              95% CI        p    p_adj    rbc
  ------------------------------------------------------------------------------------------------
  sari                       100   +1    46.201    32.206  +13.995     [+9.65, +18.48]   0.0000  0.0000*  +0.67
  bertscore_f1               100   +1     0.689     0.594   +0.095      [+0.07, +0.12]   0.0000  0.0000*  +0.69
  fkgl_drop                  100   +1     4.026     3.769   +0.258      [-0.38, +0.89]   0.0916   0.1808  +0.15
  smog_drop                  100   +1     3.758     3.443   +0.315      [-0.45, +1.09]   0.1335   0.2169  +0.15
  coleman_liau_drop          100   +1     4.563     4.556   +0.008      [-0.63, +0.62]   0.5130   0.6669  -0.01
  nli_faithfulness           100   +1     0.826     0.833   -0.007      [-0.06, +0.05]   0.9808   1.0000  -0.24
  nli_completeness           100   +1     0.790     0.820   -0.030      [-0.10, +0.04]   0.9668   1.0000  -0.21
  human_edit_recall           99   +1     0.976     0.718   +0.259      [+0.18, +0.34]   0.0000  0.0000*  +0.92
  replacement_precision       85   +1     0.741     0.624   +0.118      [+0.02, +0.21]   0.0341   0.0887  +0.62
  replacement_f1              99   +1     0.751     0.490   +0.261      [+0.17, +0.36]   0.0000  0.0000*  +0.79
  critical_error             100   -1     0.100     0.130   -0.030      [-0.07, +0.00]   0.2810   0.4059  +1.00
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.714   +0.179      [+0.00, +0.39]   0.0974   0.1808  +1.00
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.300     0.200   +0.100      [+0.00, +0.30]   1.0000   1.0000  -1.00

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

```

====================================================================================================
  PAIRED COMPARISON   grounded  vs  termonly
====================================================================================================
  Wilcoxon one-sided ('grounded' better), paired bootstrap 95% CI, rank-biserial effect size.
  11 tests -> Benjamini-Hochberg FDR at alpha=0.05. Report p_adj, not p.

  metric                       n  dir  grounded  termonly     diff              95% CI        p    p_adj    rbc
  ------------------------------------------------------------------------------------------------
  sari                       100   +1    46.553    46.201   +0.352      [-0.71, +1.50]   0.2453   0.6875  +0.07
  bertscore_f1               100   +1     0.693     0.689   +0.004      [-0.01, +0.02]   0.4848   0.6875  +0.06
  fkgl_drop                  100   +1     3.730     4.026   -0.296      [-0.58, -0.05]   0.9627   0.9627  -0.29
  smog_drop                  100   +1     3.421     3.758   -0.337      [-0.65, -0.04]   0.9379   0.9627  -0.55
  coleman_liau_drop          100   +1     4.407     4.563   -0.156      [-0.47, +0.12]   0.6585   0.8049  -0.08
  nli_faithfulness           100   +1     0.839     0.826   +0.013      [-0.01, +0.04]   0.2349   0.6875  +0.13
  nli_completeness           100   +1     0.807     0.790   +0.017      [-0.00, +0.04]   0.2172   0.6875  +0.11
  human_edit_recall           99   +1     0.981     0.976   +0.005      [+0.00, +0.01]   0.3475   0.6875  +1.00
  replacement_precision       99   +1     0.768     0.758   +0.010      [-0.05, +0.07]   0.4271   0.6875  +0.11
  replacement_f1              99   +1     0.764     0.751   +0.013      [-0.05, +0.07]   0.2995   0.6875  +0.15
  critical_error             100   -1     0.100     0.100   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.893   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.200     0.300   -0.100      [-0.30, +0.00]   0.5000   0.6875  +1.00

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

```

====================================================================================================
  PAIRED COMPARISON   grounded  vs  naive
====================================================================================================
  Wilcoxon one-sided ('grounded' better), paired bootstrap 95% CI, rank-biserial effect size.
  12 tests -> Benjamini-Hochberg FDR at alpha=0.05. Report p_adj, not p.

  metric                       n  dir  grounded     naive     diff              95% CI        p    p_adj    rbc
  ------------------------------------------------------------------------------------------------
  sari                       100   +1    46.553    32.206  +14.347    [+10.00, +18.89]   0.0000  0.0000*  +0.67
  bertscore_f1               100   +1     0.693     0.594   +0.098      [+0.07, +0.13]   0.0000  0.0000*  +0.67
  fkgl_drop                  100   +1     3.730     3.769   -0.038      [-0.73, +0.63]   0.2507   0.4215  +0.07
  smog_drop                  100   +1     3.421     3.443   -0.022      [-0.78, +0.74]   0.3617   0.4822  +0.01
  coleman_liau_drop          100   +1     4.407     4.556   -0.149      [-0.79, +0.50]   0.5486   0.6583  -0.01
  nli_faithfulness           100   +1     0.839     0.833   +0.006      [-0.05, +0.07]   0.9133   0.9133  -0.15
  nli_completeness           100   +1     0.807     0.820   -0.013      [-0.09, +0.06]   0.8406   0.9133  -0.11
  human_edit_recall           99   +1     0.981     0.718   +0.263      [+0.18, +0.35]   0.0000  0.0000*  +0.92
  replacement_precision       85   +1     0.753     0.624   +0.129      [+0.04, +0.22]   0.0256   0.0614  +0.58
  replacement_f1              99   +1     0.764     0.490   +0.274      [+0.17, +0.38]   0.0000  0.0000*  +0.72
  critical_error             100   -1     0.100     0.130   -0.030      [-0.07, +0.00]   0.2810   0.4215  +1.00
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.714   +0.179      [+0.00, +0.39]   0.0974   0.1947  +1.00
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.200     0.200   +0.000      [+0.00, +0.00]      n/a      n/a    n/a

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

## Clinical-safety flags

- note 2 / `naive` / **negation** (critical): lost ['can not be excluded', 'excluded', 'not']
- note 2 / `termonly` / **negation** (critical): lost ['can not be excluded', 'excluded', 'not']
- note 2 / `grounded` / **negation** (critical): lost ['can not be excluded', 'excluded', 'not']
- note 9 / `naive` / **number_unit** (critical): lost ['1']
- note 9 / `termonly` / **number_unit** (critical): lost ['1']
- note 9 / `grounded` / **temporality** (warning): lost ['currently']
- note 9 / `grounded` / **number_unit** (critical): lost ['1']
- note 10 / `naive` / **temporality** (warning): lost ['new onset']
- note 10 / `termonly` / **temporality** (warning): lost ['new onset']
- note 10 / `grounded` / **temporality** (warning): lost ['new onset']
- note 26 / `naive` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `termonly` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `termonly` / **temporality** (warning): lost ['acute']
- note 26 / `grounded` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `grounded` / **temporality** (warning): lost ['acute']
- note 28 / `naive` / **uncertainty** (critical): lost ['consideration']
- note 28 / `termonly` / **uncertainty** (critical): lost ['consideration']
- note 28 / `grounded` / **uncertainty** (critical): lost ['consideration']
- note 36 / `naive` / **temporality** (warning): lost ['status post']
- note 36 / `termonly` / **temporality** (warning): lost ['status post']
- note 36 / `grounded` / **temporality** (warning): lost ['status post']
- note 38 / `naive` / **severity** (warning): lost ['severe']
- note 38 / `naive` / **severity_downgrade** (critical): lost ['grave severity stated as mild or absent']
- note 38 / `termonly` / **severity** (warning): lost ['severe']
- note 38 / `termonly` / **severity_downgrade** (critical): lost ['grave severity stated as mild or absent']
- note 38 / `grounded` / **severity** (warning): lost ['severe']
- note 38 / `grounded` / **severity_downgrade** (critical): lost ['grave severity stated as mild or absent']
- note 39 / `termonly` / **severity** (warning): lost ['significant']
- note 39 / `termonly` / **severity_downgrade** (warning): lost ['tier 2']
- note 39 / `grounded` / **severity** (warning): lost ['significant']
- note 42 / `naive` / **temporality** (warning): lost ['now']
- note 42 / `termonly` / **temporality** (warning): lost ['now']
- note 42 / `grounded` / **temporality** (warning): lost ['now']
- note 44 / `naive` / **negation** (critical): lost ['not']
- note 44 / `naive` / **severity** (warning): lost ['significant']
- note 44 / `naive` / **severity_downgrade** (warning): lost ['tier 2']
- note 44 / `termonly` / **negation** (critical): lost ['not']
- note 44 / `termonly` / **severity** (warning): lost ['significant']
- note 44 / `termonly` / **severity_downgrade** (warning): lost ['tier 2']
- note 44 / `grounded` / **negation** (critical): lost ['not']
- note 44 / `grounded` / **severity** (warning): lost ['significant']
- note 44 / `grounded` / **severity_downgrade** (warning): lost ['tier 2']
- note 51 / `naive` / **laterality** (critical): lost ['lateral']
- note 51 / `termonly` / **laterality** (critical): lost ['lateral']
- note 51 / `grounded` / **laterality** (critical): lost ['lateral']
- note 53 / `naive` / **number_unit** (critical): lost ['1']
- note 54 / `naive` / **number_unit** (critical): lost ['1']
- note 60 / `naive` / **temporality** (warning): lost ['now']
- note 60 / `termonly` / **temporality** (warning): lost ['now']
- note 60 / `grounded` / **temporality** (warning): lost ['now']
- note 67 / `termonly` / **drug** (policy): lost ['prednisone']
- note 67 / `grounded` / **drug** (policy): lost ['prednisone']
- note 70 / `naive` / **number_unit** (critical): lost ['2']
- note 78 / `naive` / **number_unit** (critical): lost ['1']
- note 78 / `termonly` / **number_unit** (critical): lost ['1']
- note 78 / `grounded` / **number_unit** (critical): lost ['1']
- note 83 / `termonly` / **drug** (policy): lost ['prednisone']
- note 83 / `grounded` / **drug** (policy): lost ['prednisone']
- note 86 / `naive` / **temporality** (warning): lost ['chronic']
- note 86 / `termonly` / **temporality** (warning): lost ['chronic']
- note 86 / `grounded` / **temporality** (warning): lost ['chronic']
- note 88 / `naive` / **laterality** (critical): lost ['anterior']
- note 88 / `termonly` / **laterality** (critical): lost ['anterior']
- note 88 / `grounded` / **laterality** (critical): lost ['anterior']
- note 100 / `naive` / **negation** (critical): lost ['unremarkable']
- note 100 / `termonly` / **negation** (critical): lost ['unremarkable']
- note 100 / `grounded` / **negation** (critical): lost ['unremarkable']

## Outputs

### Note 1 - `8`

- **ORIGINAL**  (FKGL 16.0, 17 words): He became anhedonic and disinterested in social activities, and had difficulty sleeping for frequent waking and restlessness.
- **REFERENCE** (FKGL 15.2, 20 words): He became unable to feel pleasure and disinterested in social activities, and had difficulty sleeping for frequent waking and restlessness.
- **naive** (FKGL 6.0, 30 words, 0 edits): He lost interest in things he used to enjoy and stopped wanting to spend time with others. He also had trouble sleeping because he kept waking up and felt restless.
    - SARI=11.45  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 11.0, 24 words, 2 edits): He lost interest in things and did not care about social activities, and had trouble sleeping because he woke up often and felt restless.
    - SARI=18.88  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 11.0, 24 words, 2 edits): He lost interest in things and did not care about social activities, and had trouble sleeping because he woke up often and felt restless.
    - SARI=18.88  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 2 - `18`

- **ORIGINAL**  (FKGL 14.3, 6 words): Myocardial infarction can not be excluded.
- **REFERENCE** (FKGL 4.5, 6 words): Heart attack can not be excluded.
- **naive** (FKGL 4.8, 10 words, 0 edits): It is possible that the patient had a heart attack.
    - SARI=20.13  crit=1.00  NLIf=0.86  copyjrg=0.00
- **termonly** (FKGL 4.5, 6 words, 1 edits): A heart attack is still possible.
    - SARI=22.38  crit=1.00  NLIf=0.81  copyjrg=0.00
- **grounded** (FKGL 4.5, 6 words, 1 edits): A heart attack is still possible.
    - SARI=22.38  crit=1.00  NLIf=0.81  copyjrg=0.00

### Note 3 - `21`

- **ORIGINAL**  (FKGL 6.0, 10 words): There was marked hematoma and swelling within the subdeltoid bursa.
- **REFERENCE** (FKGL 7.6, 14 words): There was obvious collection of blood and swelling within the side of the shoulder.
- **naive** (FKGL 5.9, 11 words, 0 edits): There was a large bruise and swelling inside the subdeltoid bursa.
    - SARI=34.23  crit=0.00  NLIf=0.98  copyjrg=0.50
- **termonly** (FKGL 3.7, 11 words, 3 edits): There was a large bruise and swelling under the shoulder pad.
    - SARI=41.51  crit=0.00  NLIf=0.46  copyjrg=0.00
- **grounded** (FKGL 6.0, 15 words, 3 edits): There was a large bruise and swelling in the fluid sac under the shoulder muscle.
    - SARI=41.05  crit=0.00  NLIf=0.78  copyjrg=0.00

### Note 4 - `26`

- **ORIGINAL**  (FKGL 19.4, 5 words): Smoking history, hypertension, and hyperlipidemia.
- **REFERENCE** (FKGL 4.8, 11 words): Smoking history, high blood pressure, and high fat in the blood.
- **naive** (FKGL 8.5, 13 words, 0 edits): The patient has a history of smoking, high blood pressure, and high cholesterol.
    - SARI=51.55  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 9.7, 8 words, 2 edits): Smoking history, high blood pressure, and high cholesterol.
    - SARI=71.24  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 9.7, 8 words, 2 edits): Smoking history, high blood pressure, and high cholesterol.
    - SARI=71.24  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 5 - `31`

- **ORIGINAL**  (FKGL 8.9, 21 words): She did complain of bladder spasms when she urinated and she did say that she has a history of chronic UTIs.
- **REFERENCE** (FKGL 11.8, 23 words): She did complain of bladder spasms when she urinated and she did say that she has a history of chronic urinary tract infections
- **naive** (FKGL 8.6, 19 words, 0 edits): She said she had bladder spasms when she urinated and mentioned that she has a history of chronic UTIs.
    - SARI=23.08  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 9.1, 19 words, 3 edits): She complained of bladder cramps when she peed and said she has a history of long-lasting urine infections.
    - SARI=18.32  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 11.1, 21 words, 3 edits): She said her bladder muscles tightened and hurt when she peed, and she has a history of long-lasting urinary infections.
    - SARI=19.21  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 6 - `32`

- **ORIGINAL**  (FKGL 7.2, 10 words): There was no instability of the knee and no effusion.
- **REFERENCE** (FKGL 8.0, 11 words): There was no instability of the knee and no fluid collection.
- **naive** (FKGL 2.3, 8 words, 0 edits): The knee was stable and had no swelling.
    - SARI=13.62  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 2.3, 8 words, 2 edits): The knee was steady and had no swelling.
    - SARI=13.62  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.7, 9 words, 2 edits): The knee was steady and had no fluid buildup.
    - SARI=18.25  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 7 - `64`

- **ORIGINAL**  (FKGL 4.9, 13 words): Two days later, the pain resolved and she has not had a recurrence.
- **REFERENCE** (FKGL 5.0, 14 words): Two days later, the pain got better and she has not had a recurrence.
- **naive** (FKGL 3.6, 15 words, 0 edits): Two days later, the pain went away and she has not had it come back.
    - SARI=46.29  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.6, 15 words, 2 edits): Two days later, the pain went away and she has not had it come back.
    - SARI=46.29  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.6, 15 words, 2 edits): Two days later, the pain went away and she has not had it come back.
    - SARI=46.29  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 8 - `81`

- **ORIGINAL**  (FKGL 14.1, 7 words): Description : Fever, otitis media, and possible sepsis.
- **REFERENCE** (FKGL 15.6, 8 words): Description : Fever, ear infection, and possible general infection.
- **naive** (FKGL 5.8, 12 words, 0 edits): The patient has a fever, an ear infection, and might have sepsis.
    - SARI=37.05  crit=0.00  NLIf=0.82  copyjrg=0.50
- **termonly** (FKGL 14.1, 9 words, 2 edits): Description: Fever, middle ear infection, and possible severe infection.
    - SARI=61.87  crit=0.00  NLIf=0.67  copyjrg=0.00
- **grounded** (FKGL 12.8, 9 words, 2 edits): Description: Fever, ear infection, and possible severe blood infection.
    - SARI=68.98  crit=0.00  NLIf=0.67  copyjrg=0.00

### Note 9 - `101`

- **ORIGINAL**  (FKGL 7.6, 13 words): Currently, primary complaint is one of fatigue that she feels throughout the day.
- **REFERENCE** (FKGL 8.4, 14 words): Currently, primary complaint is one of feeling tired that she feels throughout the day.
- **naive** (FKGL 3.7, 10 words, 0 edits): Her main problem right now is feeling tired all day.
    - SARI=14.86  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.7, 10 words, 2 edits): Right now, her main problem is feeling tired all day.
    - SARI=14.86  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.8, 8 words, 2 edits): Her main problem is feeling tired all day.
    - SARI=15.97  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 10 - `108`

- **ORIGINAL**  (FKGL 12.3, 19 words): He has noted some stool irregularity with occasional loose stools and new onset of pain predominantly in left neck.
- **REFERENCE** (FKGL 12.3, 19 words): He has noted some poop irregularity with occasional loose poop and new onset of pain predominantly in left neck.
- **naive** (FKGL 12.9, 27 words, 0 edits): He has noticed some changes in his bowel movements, including occasional loose stools, and has recently started having pain mostly in the left side of his neck.
    - SARI=16.67  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 10.6, 21 words, 4 edits): He has noted some changes in bowel movements with occasional watery stools and recent start of pain mostly in left neck.
    - SARI=29.30  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 11.1, 19 words, 4 edits): He has noted some bowel changes with occasional watery poop and recently started pain mostly in the left neck.
    - SARI=30.61  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 11 - `143`

- **ORIGINAL**  (FKGL 11.7, 12 words): Description : The patient presents for a followup for history of erythema nodosum.
- **REFERENCE** (FKGL 12.6, 17 words): Description : The patient presents for a followup for history of red, painful tender lumps around fatty areas.
- **naive** (FKGL 9.1, 17 words, 0 edits): The patient is coming for a follow-up visit because of a past case of erythema nodosum.
    - SARI=10.55  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 7.6, 16 words, 1 edits): The patient comes for a follow-up visit for a history of painful red skin lumps.
    - SARI=23.30  crit=0.00  NLIf=0.38  copyjrg=0.00
- **grounded** (FKGL 5.8, 14 words, 1 edits): The patient comes for a follow-up for a history of red skin bumps.
    - SARI=23.17  crit=0.00  NLIf=0.60  copyjrg=0.00

### Note 12 - `144`

- **ORIGINAL**  (FKGL 7.5, 22 words): She was iron deficient last year, and with her multiple surgeries and poor p. o. intake, may have become iron deficient again.
- **REFERENCE** (FKGL 12.4, 23 words): She was iron deficient last year, and with her multiple surgeries and poor food and fluid intake, may have become iron deficient again.
- **naive** (FKGL 5.0, 28 words, 0 edits): She was low on iron last year. Because she had several surgeries and did not eat or drink enough by mouth, she may be low on iron again.
    - SARI=14.89  crit=0.00  NLIf=0.50  copyjrg=0.00
- **termonly** (FKGL 8.9, 21 words, 3 edits): She had low iron last year, and with her multiple surgeries and poor intake by mouth, may have low iron again.
    - SARI=33.67  crit=0.00  NLIf=0.10  copyjrg=0.00
- **grounded** (FKGL 10.7, 25 words, 2 edits): She did not have enough iron last year, and with her multiple surgeries and poor intake by mouth, may have become low in iron again.
    - SARI=35.75  crit=0.00  NLIf=0.10  copyjrg=0.00

### Note 13 - `150`

- **ORIGINAL**  (FKGL 9.1, 15 words): We will schedule him for the Holter monitor and refer him back to his cardiologist.
- **REFERENCE** (FKGL 10.6, 16 words): We will schedule him for the continuous heart monitor and refer him back to his cardiologist.
- **naive** (FKGL 6.6, 21 words, 0 edits): We will set up a time for him to wear a Holter monitor and send him back to his heart doctor.
    - SARI=23.12  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 6.1, 16 words, 2 edits): We will schedule him for the heart monitor and refer him back to his heart doctor.
    - SARI=64.22  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 7.7, 17 words, 2 edits): We will schedule him for a portable heart monitor and refer him back to his heart doctor.
    - SARI=54.75  crit=0.00  NLIf=0.70  copyjrg=0.00

### Note 14 - `161`

- **ORIGINAL**  (FKGL 11.1, 8 words): The patient wished to proceed with operative intervention.
- **REFERENCE** (FKGL 6.7, 8 words): The patient wished to proceed with an operation
- **naive** (FKGL 6.7, 8 words, 0 edits): The patient wanted to go ahead with surgery.
    - SARI=22.50  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.4, 6 words, 1 edits): The patient wanted to have surgery.
    - SARI=20.56  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.4, 6 words, 1 edits): The patient wanted to have surgery.
    - SARI=20.56  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 15 - `178`

- **ORIGINAL**  (FKGL 7.2, 10 words): A KUB was obtained showing an abnormal bowel gas pattern.
- **REFERENCE** (FKGL 8.4, 17 words): An x-ray of the kidney, ureter and bladder was obtained showing an abnormal bowel gas pattern.
- **naive** (FKGL 9.1, 19 words, 0 edits): An X-ray of the abdomen was taken, and it showed an unusual pattern of gas in the intestines.
    - SARI=24.54  crit=0.00  NLIf=0.88  copyjrg=0.00
- **termonly** (FKGL 9.1, 16 words, 2 edits): An X-ray of the belly was taken showing an unusual gas pattern in the intestines.
    - SARI=30.93  crit=0.00  NLIf=0.77  copyjrg=0.00
- **grounded** (FKGL 6.9, 12 words, 1 edits): An x-ray of the belly showed unusual gas in the intestines.
    - SARI=23.47  crit=0.00  NLIf=0.90  copyjrg=0.00

### Note 16 - `185`

- **ORIGINAL**  (FKGL 12.3, 19 words): She has been sedated with Ativan and came into the emergency room obtunded and unable to give any history.
- **REFERENCE** (FKGL 12.3, 20 words): She has been sedated with Ativan and came into the emergency room very drowsy and unable to give any history.
- **naive** (FKGL 7.1, 28 words, 0 edits): She was given Ativan to make her sleepy. When she arrived at the emergency room, she was very drowsy and could not answer any questions about her health.
    - SARI=17.48  crit=0.00  NLIf=0.80  copyjrg=0.00
- **termonly** (FKGL 12.9, 23 words, 2 edits): She was given a medicine to make her sleepy and came into the emergency room very drowsy and unable to give any history.
    - SARI=49.27  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 12.3, 22 words, 3 edits): She was made sleepy with a medicine and came into the emergency room not fully alert and unable to give any history.
    - SARI=35.18  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 17 - `202`

- **ORIGINAL**  (FKGL 4.4, 15 words): He has no edema now, but has had some mild leg swelling in the past.
- **REFERENCE** (FKGL 3.6, 15 words): He has no swelling now, but has had some mild leg swelling in the past.
- **naive** (FKGL 4.5, 18 words, 0 edits): He does not have swelling now, but he had some mild swelling in his legs in the past.
    - SARI=26.34  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.6, 15 words, 1 edits): He has no swelling now, but has had some mild leg swelling in the past.
    - SARI=91.67  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.6, 15 words, 1 edits): He has no swelling now, but has had some mild leg swelling in the past.
    - SARI=91.67  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 18 - `231`

- **ORIGINAL**  (FKGL 21.0, 3 words): Mild secondary hyperparathyroidism.
- **REFERENCE** (FKGL 14.7, 5 words): Mild secondary hyperactive parathyroid gland
- **naive** (FKGL 8.9, 9 words, 0 edits): The patient has a mild case of secondary hyperparathyroidism.
    - SARI=15.00  crit=0.00  NLIf=0.96  copyjrg=1.00
- **termonly** (FKGL 11.1, 8 words, 1 edits): Mild overactive parathyroid glands caused by another condition.
    - SARI=23.89  crit=0.00  NLIf=0.91  copyjrg=0.00
- **grounded** (FKGL 9.1, 7 words, 1 edits): Mild overactive parathyroid glands from another cause.
    - SARI=24.07  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 19 - `248`

- **ORIGINAL**  (FKGL 10.6, 16 words): Otherwise, a complete review of systems was obtained and was negative except for as mentioned above.
- **REFERENCE** (FKGL 9.8, 16 words): Otherwise, a complete review of systems was obtained and was normal except for as mentioned above.
- **naive** (FKGL 9.8, 19 words, 0 edits): The doctor checked the patient’s overall health and found no other problems, except for the ones already mentioned.
    - SARI=10.93  crit=0.00  NLIf=0.10  copyjrg=0.00
- **termonly** (FKGL 8.5, 18 words, 3 edits): Otherwise, a check of all body systems was done and showed no problems except for those mentioned above.
    - SARI=18.40  crit=0.00  NLIf=0.23  copyjrg=0.00
- **grounded** (FKGL 11.1, 18 words, 3 edits): Otherwise, questions about symptoms in different body parts were asked and showed no issues except as mentioned above.
    - SARI=14.98  crit=0.00  NLIf=0.23  copyjrg=0.00

### Note 20 - `277`

- **ORIGINAL**  (FKGL 7.6, 16 words): Symptoms are worse when sitting for any length of time, such as driving a motor vehicle.
- **REFERENCE** (FKGL 5.2, 15 words): Symptoms are worse when sitting for any length of time, such as driving a car.
- **naive** (FKGL 6.1, 16 words, 0 edits): The symptoms get worse when sitting for any amount of time, like when driving a car.
    - SARI=31.60  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.2, 15 words, 1 edits): Symptoms are worse when sitting for any length of time, such as driving a car.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.2, 15 words, 1 edits): Symptoms are worse when sitting for any length of time, such as driving a car.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 21 - `290`

- **ORIGINAL**  (FKGL 12.8, 9 words): Forearm, elbow and shoulder exams reveal no neurologic compromise.
- **REFERENCE** (FKGL 7.6, 9 words): Forearm, elbow and shoulder exams reveal no nerve problems
- **naive** (FKGL 5.9, 11 words, 0 edits): Exams of the forearm, elbow, and shoulder show no nerve problems.
    - SARI=47.22  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.9, 11 words, 1 edits): Exams of the forearm, elbow, and shoulder show no nerve damage.
    - SARI=41.13  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 5.9, 11 words, 1 edits): Exams of the forearm, elbow, and shoulder show no nerve damage.
    - SARI=41.13  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 22 - `296`

- **ORIGINAL**  (FKGL 13.7, 12 words): Thereafter, the local anesthesia was injected into the area around the tumor.
- **REFERENCE** (FKGL 11.7, 12 words): Thereafter, the numbing agent was injected into the area around the tumor.
- **naive** (FKGL 12.2, 13 words, 0 edits): After that, the local anesthesia was injected into the area around the tumor.
    - SARI=43.37  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 10.4, 13 words, 2 edits): After that, the numbing medicine was injected into the area around the growth.
    - SARI=56.27  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 8.5, 13 words, 2 edits): After that, the numbing drug was injected into the area around the growth.
    - SARI=56.27  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 23 - `307`

- **ORIGINAL**  (FKGL 3.7, 11 words): There is no numbness or paresthesias in the hand or arm.
- **REFERENCE** (FKGL 5.8, 12 words): There is no numbness or abnormal sensation in the hand or arm.
- **naive** (FKGL 4.9, 13 words, 0 edits): The patient does not have numbness or tingling in the hand or arm.
    - SARI=39.52  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 3.7, 11 words, 1 edits): There is no numbness or tingling in the hand or arm.
    - SARI=66.67  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 3.7, 11 words, 1 edits): There is no numbness or tingling in the hand or arm.
    - SARI=66.67  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 24 - `357`

- **ORIGINAL**  (FKGL 7.6, 16 words): I do not think she has an obvious current abscessed lesion, although there is some drainage.
- **REFERENCE** (FKGL 7.7, 17 words): I do not think she has an obvious current collection of pus, although there is some drainage.
- **naive** (FKGL 8.6, 19 words, 0 edits): The patient does not appear to have an obvious infected sore right now, even though there is some drainage.
    - SARI=24.73  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 7.8, 19 words, 2 edits): I do not think she has an obvious current pus-filled sore, although there is some fluid leaking out.
    - SARI=58.94  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 8.5, 18 words, 2 edits): I do not think she has an obvious current infected sore, although there is some fluid leaking out.
    - SARI=57.08  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 25 - `358`

- **ORIGINAL**  (FKGL 9.1, 11 words): At this time, we would rehydrate with intravenous fluids and reassess.
- **REFERENCE** (FKGL 5.8, 13 words): At this time, we would rehydrate with fluids through the vein and reassess.
- **naive** (FKGL 5.2, 15 words, 0 edits): At this time, the patient would receive fluids through a vein and be checked again.
    - SARI=31.98  crit=0.00  NLIf=0.89  copyjrg=0.00
- **termonly** (FKGL 2.9, 12 words, 2 edits): At this time, we would give fluids by vein and check again.
    - SARI=45.56  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 2.9, 12 words, 2 edits): At this time, we would give fluids by vein and check again.
    - SARI=45.56  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 26 - `380`

- **ORIGINAL**  (FKGL 14.3, 6 words): Findings are compatible with acute appendicitis.
- **REFERENCE** (FKGL 12.8, 9 words): Findings are compatible with acute inflammation of the appendix
- **naive** (FKGL 12.3, 5 words, 0 edits): The findings suggest acute appendicitis.
    - SARI=11.81  crit=1.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 9.1, 7 words, 1 edits): The results suggest a sudden inflamed appendix.
    - SARI=10.95  crit=1.00  NLIf=0.85  copyjrg=0.00
- **grounded** (FKGL 10.4, 6 words, 2 edits): The results suggest sudden appendix swelling.
    - SARI=11.25  crit=1.00  NLIf=0.90  copyjrg=0.00

### Note 27 - `391`

- **ORIGINAL**  (FKGL 10.5, 18 words): She denies weight loss, but acknowledged decreased appetite and increased generalized fatigue for the past 3-4 months.
- **REFERENCE** (FKGL 10.5, 18 words): She denies weight loss, but acknowledged reduced appetite and more generalized tiredness for the past 3-4 months.
- **naive** (FKGL 8.8, 26 words, 0 edits): She says she has not lost weight, but she has had less appetite and more tiredness all over her body for the past 3-4 months.
    - SARI=47.48  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 7.8, 26 words, 2 edits): She says she has not lost weight, but she said she has had less hunger and more tiredness all over for the past 3-4 months.
    - SARI=44.97  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 8.0, 25 words, 1 edits): She says she did not lose weight, but admitted she wanted to eat less and felt tired all over for the past 3-4 months.
    - SARI=42.08  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 28 - `392`

- **ORIGINAL**  (FKGL 21.8, 5 words): Consideration given to completion thyroidectomy.
- **REFERENCE** (FKGL 11.5, 9 words): Consideration given to remove remaining parts of the thyroid
- **naive** (FKGL 8.4, 15 words, 0 edits): The doctors are thinking about doing surgery to remove the rest of the thyroid gland.
    - SARI=33.47  crit=1.00  NLIf=0.11  copyjrg=0.00
- **termonly** (FKGL 9.1, 11 words, 0 edits): The doctors thought about finishing the surgery to remove the thyroid.
    - SARI=32.04  crit=1.00  NLIf=0.41  copyjrg=0.00
- **grounded** (FKGL 8.4, 10 words, 0 edits): They thought about finishing the surgery to remove the thyroid.
    - SARI=32.18  crit=1.00  NLIf=0.94  copyjrg=0.00

### Note 29 - `394`

- **ORIGINAL**  (FKGL 10.5, 19 words): She notes that she had epistaxis a few days ago, requiring nasal packing and fortunately that had resolved now.
- **REFERENCE** (FKGL 9.5, 21 words): She notes that she had a nose bleed a few days ago, requiring nose packing and fortunately that had resolved now.
- **naive** (FKGL 3.4, 25 words, 0 edits): She says she had a nosebleed a few days ago. It needed packing in her nose to stop the bleeding, but it has now healed.
    - SARI=28.39  crit=0.00  NLIf=0.76  copyjrg=0.00
- **termonly** (FKGL 8.5, 22 words, 4 edits): She notes that she had a nosebleed a few days ago, needing cotton in her nose, and fortunately that had stopped now.
    - SARI=48.86  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 10.7, 27 words, 4 edits): She notes that she had a nosebleed a few days ago, needing material put in her nose to help it heal, and fortunately that has stopped now.
    - SARI=44.12  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 30 - `396`

- **ORIGINAL**  (FKGL 8.9, 9 words): I also explained to the patient about conscious sedation.
- **REFERENCE** (FKGL 8.9, 9 words): I also explained to the patient about awake sedation.
- **naive** (FKGL 8.2, 8 words, 0 edits): I also explained conscious sedation to the patient.
    - SARI=27.00  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 10.1, 14 words, 1 edits): I also explained to the patient about being awake but relaxed during the procedure.
    - SARI=64.33  crit=0.00  NLIf=0.04  copyjrg=0.00
- **grounded** (FKGL 7.6, 9 words, 1 edits): I also explained to the patient about light sedation.
    - SARI=66.67  crit=0.00  NLIf=0.02  copyjrg=0.00

### Note 31 - `762`

- **ORIGINAL**  (FKGL 5.2, 8 words): Palpation of her right knee reveals no crepitus.
- **REFERENCE** (FKGL 5.0, 9 words): Feeling of her right knee reveals no crunchy feeling.
- **naive** (FKGL 4.2, 14 words, 0 edits): When the doctor felt her right knee, there was no grinding or crackling sound.
    - SARI=28.93  crit=0.00  NLIf=0.47  copyjrg=0.00
- **termonly** (FKGL 2.3, 7 words, 1 edits): Feeling her right knee shows no grinding.
    - SARI=32.26  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 2.3, 7 words, 1 edits): Feeling her right knee shows no grinding.
    - SARI=32.26  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 32 - `427`

- **ORIGINAL**  (FKGL 10.1, 14 words): She stepped on ideas, concerns and expectations the evening prior and twisted her ankle.
- **REFERENCE** (FKGL 4.8, 11 words): She stepped on ice the evening prior and twisted her ankle.
- **naive** (FKGL 5.7, 7 words, 0 edits): She twisted her ankle the evening before.
    - SARI=29.95  crit=0.00  NLIf=0.99
- **termonly** (FKGL 9.3, 14 words, 1 edits): She stepped on ideas, concerns and expectations the night before and twisted her ankle.
    - SARI=21.81  crit=0.00  NLIf=0.99
- **grounded** (FKGL 9.3, 14 words, 1 edits): She stepped on ideas, concerns and expectations the night before and twisted her ankle.
    - SARI=21.81  crit=0.00  NLIf=0.99

### Note 33 - `439`

- **ORIGINAL**  (FKGL 14.1, 9 words): Modifying Factors : Patient 's condition is aggravated by throwing.
- **REFERENCE** (FKGL 9.6, 10 words): Modifying Factors : Patient 's condition is made worse by throwing.
- **naive** (FKGL 3.8, 9 words, 0 edits): The patient's condition gets worse when they throw.
    - SARI=26.63  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.7, 14 words, 1 edits): Things that change the condition: The patient's condition is made worse by throwing.
    - SARI=58.33  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.7, 14 words, 1 edits): Things that change the condition: The patient's condition is made worse by throwing.
    - SARI=58.33  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 34 - `451`

- **ORIGINAL**  (FKGL 21.3, 10 words): History of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis and kidney stones.
- **REFERENCE** (FKGL 14.9, 13 words): History of joint inflammation, bone degeneration, underactive thyroid, hay fever and kidney stones.
- **naive** (FKGL 17.7, 14 words, 0 edits): The patient has a history of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis, and kidney stones.
    - SARI=11.57  crit=0.00  NLIf=0.96  copyjrg=1.00
- **termonly** (FKGL 6.7, 13 words, 4 edits): History of joint wear, weak bones, low thyroid, nose allergies and kidney stones.
    - SARI=62.18  crit=0.00  NLIf=0.88  copyjrg=0.00
- **grounded** (FKGL 5.8, 13 words, 4 edits): History of joint wear, weak bones, low thyroid, hay fever, and kidney stones.
    - SARI=72.04  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 35 - `465`

- **ORIGINAL**  (FKGL 15.8, 7 words): The ultrasound was negative for intracranial hemorrhage.
- **REFERENCE** (FKGL 6.3, 9 words): The ultrasound was negative for bleeding in the brain.
- **naive** (FKGL 6.0, 10 words, 0 edits): The ultrasound did not show any bleeding inside the skull.
    - SARI=23.93  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 5.2, 8 words, 1 edits): The ultrasound showed no bleeding inside the skull.
    - SARI=24.35  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 5.2, 8 words, 1 edits): The ultrasound showed no bleeding inside the brain.
    - SARI=28.10  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 36 - `466`

- **ORIGINAL**  (FKGL 14.7, 12 words): He is status post laparoscopic appendicectomy, and he is tolerating oral diet.
- **REFERENCE** (FKGL 12.3, 15 words): He is status after keyhole surgery to remove appendix, and he is tolerating oral diet.
- **naive** (FKGL 10.0, 21 words, 0 edits): He had his appendix removed using small cuts and a camera, and he is able to eat food without any problems.
    - SARI=31.94  crit=0.00  NLIf=0.40  copyjrg=0.00
- **termonly** (FKGL 4.4, 15 words, 0 edits): He had his appendix removed through small cuts, and he can eat food by mouth.
    - SARI=23.01  crit=0.00  NLIf=0.62  copyjrg=0.00
- **grounded** (FKGL 6.3, 17 words, 2 edits): He had surgery to remove his appendix through small cuts, and he can eat food by mouth.
    - SARI=27.66  crit=0.00  NLIf=0.72  copyjrg=0.00

### Note 37 - `478`

- **ORIGINAL**  (FKGL 8.4, 14 words): We believe that her walking is most likely not being affected by the hydrocephalus.
- **REFERENCE** (FKGL 8.5, 18 words): We believe that her walking is most likely not being affected by the excess fluid in the brain.
- **naive** (FKGL 6.7, 13 words, 0 edits): We think that her walking is most likely not affected by the hydrocephalus.
    - SARI=23.68  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 8.6, 19 words, 1 edits): We believe that her walking is most likely not being affected by the buildup of fluid in the brain.
    - SARI=81.31  crit=0.00  NLIf=0.70  copyjrg=0.00
- **grounded** (FKGL 8.5, 18 words, 1 edits): We believe that her walking is most likely not being affected by the fluid buildup in her brain.
    - SARI=72.92  crit=0.00  NLIf=0.43  copyjrg=0.00

### Note 38 - `505`

- **ORIGINAL**  (FKGL 12.3, 11 words): She noted complaints of fatigue, lightheadedness, and severe dyspnea on exertion.
- **REFERENCE** (FKGL 13.1, 15 words): She noted complaints of tiredness, lightheadedness, and severe shortness of breath on doing anything physical.
- **naive** (FKGL 8.4, 14 words, 0 edits): She reported feeling tired, lightheaded, and very short of breath when she was active.
    - SARI=26.48  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 7.8, 12 words, 4 edits): She reported feeling tired, dizzy, and very short of breath when active.
    - SARI=26.63  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 7.8, 12 words, 4 edits): She reported feeling tired, dizzy, and very short of breath when active.
    - SARI=26.63  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 39 - `516`

- **ORIGINAL**  (FKGL 10.9, 14 words): No significant amount of edema associated with these in the dorsum of the hand.
- **REFERENCE** (FKGL 9.3, 14 words): No significant amount of swelling associated with these in the back of the hand.
- **naive** (FKGL 6.7, 14 words, 0 edits): There is no significant swelling on the back of the hand related to these.
    - SARI=39.55  crit=0.00  NLIf=0.90  copyjrg=0.00
- **termonly** (FKGL 2.9, 12 words, 3 edits): No major swelling linked to these on the back of the hand.
    - SARI=38.22  crit=0.00  NLIf=0.60  copyjrg=0.00
- **grounded** (FKGL 1.9, 12 words, 3 edits): No big swelling linked to these on the back of the hand.
    - SARI=38.22  crit=0.00  NLIf=0.57  copyjrg=0.00

### Note 40 - `523`

- **ORIGINAL**  (FKGL 12.3, 5 words): No cardio or pulmonary complaints.
- **REFERENCE** (FKGL 0.5, 5 words): No heart or lung complaints.
- **naive** (FKGL 2.3, 8 words, 0 edits): The patient has no heart or lung problems.
    - SARI=52.02  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 0.5, 5 words, 2 edits): No heart or lung complaints.
    - SARI=75.00  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 0.5, 5 words, 2 edits): No heart or lung complaints.
    - SARI=75.00  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 41 - `553`

- **ORIGINAL**  (FKGL 6.9, 11 words): At that time, the Coreg had been held secondary to hypotension.
- **REFERENCE** (FKGL 3.1, 13 words): At that time, the Coreg had been held because of low blood pressure
- **naive** (FKGL 3.1, 13 words, 0 edits): At that time, the Coreg had been stopped because of low blood pressure.
    - SARI=76.67  crit=0.00  NLIf=0.86  copyjrg=0.00
- **termonly** (FKGL 6.0, 15 words, 3 edits): At that time, the blood pressure medicine had been held because of low blood pressure.
    - SARI=66.79  crit=0.00  NLIf=0.77  copyjrg=0.00
- **grounded** (FKGL 6.0, 15 words, 3 edits): At that time, the blood pressure medicine had been held because of low blood pressure.
    - SARI=66.79  crit=0.00  NLIf=0.77  copyjrg=0.00

### Note 42 - `554`

- **ORIGINAL**  (FKGL 12.8, 16 words): Her diarrhea now has settled down and she is having less urinary incontinence, less pedal edema.
- **REFERENCE** (FKGL 8.4, 17 words): Her watery poop now has settled down and she is having less uncontrolled peeing, less foot swelling.
- **naive** (FKGL 9.2, 19 words, 0 edits): Her diarrhea has improved, and she is having less trouble with bladder control and less swelling in her feet.
    - SARI=42.52  crit=0.00  NLIf=0.82  copyjrg=0.33
- **termonly** (FKGL 6.5, 18 words, 3 edits): Her loose stools have settled down and she is having less urine leakage, less swelling in her feet.
    - SARI=54.84  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 8.0, 19 words, 3 edits): Her loose, watery poop has settled down and she is having less loss of bladder control, less swollen feet.
    - SARI=62.90  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 43 - `556`

- **ORIGINAL**  (FKGL 19.4, 13 words): Description : Nausea and abdominal pain after eating - Gall bladder disease - Laparoscopic cholecystectomy scheduled.
- **REFERENCE** (FKGL 14.4, 18 words): Description : Nausea and abdominal pain after eating - Gall bladder disease - keyhole surgery to remove the gall bladder scheduled.
- **naive** (FKGL 12.2, 18 words, 0 edits): The patient has nausea and belly pain after eating because of gallbladder disease. A laparoscopic cholecystectomy is scheduled.
    - SARI=19.81  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 12.3, 15 words, 0 edits): Feeling sick and belly pain after eating - gallbladder problem - surgery to remove the gallbladder scheduled.
    - SARI=29.57  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 11.3, 16 words, 3 edits): Feeling sick and belly pain after eating - gallbladder problem - surgery to remove the gallbladder is planned.
    - SARI=27.73  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 44 - `618`

- **ORIGINAL**  (FKGL 12.3, 20 words): She states that she has underlying history of heart disease but is not able to elaborate to any significant extent.
- **REFERENCE** (FKGL 12.3, 22 words): She states that she has underlying history of heart disease but is not able to go into detail to any significant extent.
- **naive** (FKGL 6.8, 15 words, 0 edits): She says she has a history of heart disease, but she cannot give many details.
    - SARI=19.50  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.7, 14 words, 0 edits): She says she has a history of heart disease but cannot give many details.
    - SARI=19.50  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.7, 14 words, 0 edits): She says she has a history of heart disease but cannot give many details.
    - SARI=19.50  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 45 - `661`

- **ORIGINAL**  (FKGL 6.5, 18 words): There was some slight edema of the fourth digit, on which he still is wearing his wedding band.
- **REFERENCE** (FKGL 5.9, 18 words): There was some slight swelling of the fourth finger, on which he still is wearing his wedding band.
- **naive** (FKGL 5.4, 16 words, 0 edits): The fourth toe was slightly swollen, and he was still wearing his wedding band on it.
    - SARI=28.17  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 5.2, 18 words, 2 edits): There was some slight swelling of the fourth toe, on which he still is wearing his wedding band.
    - SARI=83.33  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 5.6, 17 words, 2 edits): There was slight swelling of the fourth finger, on which he still is wearing his wedding band.
    - SARI=83.97  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 46 - `669`

- **ORIGINAL**  (FKGL 12.8, 21 words): Parents do state that she does appear to breathe rapidly, tires somewhat with the feeding with increased respiratory effort and diaphoresis.
- **REFERENCE** (FKGL 10.0, 21 words): Parents do state that she does appear to breathe quickly, tires somewhat with the feeding with increased breathing effort and sweating.
- **naive** (FKGL 5.4, 16 words, 0 edits): Her parents say she breathes fast, gets tired while feeding, works harder to breathe, and sweats.
    - SARI=15.84  crit=0.00  NLIf=0.13  copyjrg=0.00
- **termonly** (FKGL 6.3, 17 words, 3 edits): Parents say she seems to breathe fast, gets tired during feeding, works harder to breathe, and sweats.
    - SARI=15.84  crit=0.00  NLIf=0.20  copyjrg=0.00
- **grounded** (FKGL 6.3, 17 words, 3 edits): Parents say she seems to breathe fast, gets tired during feeding, works harder to breathe, and sweats.
    - SARI=15.84  crit=0.00  NLIf=0.20  copyjrg=0.00

### Note 47 - `673`

- **ORIGINAL**  (FKGL 11.3, 26 words): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had onset of chest pain this evening.
- **REFERENCE** (FKGL 10.5, 24 words): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had chest pain this evening.
- **naive** (FKGL 8.8, 23 words, 0 edits): The patient said he has not used amphetamines for at least four to five months, but he started having chest pain this evening.
    - SARI=37.20  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 11.3, 26 words, 2 edits): The patient has not used stimulant drugs for at least four to five months, according to the patient; however, he started having chest pain this evening.
    - SARI=46.76  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 10.7, 27 words, 2 edits): The patient has not used stimulants for at least four to five months, according to the patient; however, he had the start of chest pain this evening.
    - SARI=46.93  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 48 - `675`

- **ORIGINAL**  (FKGL 8.4, 10 words): Orogastric suction carried out with only scant clear stomach contents.
- **REFERENCE** (FKGL 7.6, 16 words): Suction of stomach through the mouth carried out with only a small amount clear stomach contents
- **naive** (FKGL 8.0, 22 words, 0 edits): The doctor used a tube through the mouth to suction the stomach, but only a small amount of clear fluid came out.
    - SARI=36.19  crit=0.00  NLIf=0.16  copyjrg=0.00
- **termonly** (FKGL 6.3, 17 words, 0 edits): Suction through the mouth was done with only a small amount of clear fluid from the stomach.
    - SARI=42.70  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 5.9, 14 words, 1 edits): Suction through the mouth was done with very little clear fluid from the stomach.
    - SARI=29.69  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 49 - `680`

- **ORIGINAL**  (FKGL 11.5, 9 words): Probably there is some restrictive element because of fibrosis.
- **REFERENCE** (FKGL 10.2, 11 words): Probably there is some restrictive element because of scarring of tissues.
- **naive** (FKGL 8.9, 9 words, 0 edits): There is likely a restrictive element due to fibrosis.
    - SARI=12.80  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 5.2, 8 words, 2 edits): There is likely some tightness because of scarring.
    - SARI=23.43  crit=0.00  NLIf=0.91  copyjrg=0.00
- **grounded** (FKGL 6.3, 9 words, 2 edits): There is likely a limiting part because of scarring.
    - SARI=20.79  crit=0.00  NLIf=0.89  copyjrg=0.00

### Note 50 - `681`

- **ORIGINAL**  (FKGL 10.2, 9 words): The uterus was placed back into the abdominal cavity.
- **REFERENCE** (FKGL 3.8, 8 words): The womb was placed back into the abdomen
- **naive** (FKGL 5.2, 8 words, 0 edits): The uterus was put back into the belly.
    - SARI=34.72  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL 2.3, 8 words, 2 edits): The womb was placed back into the belly.
    - SARI=87.50  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 2.3, 8 words, 2 edits): The womb was placed back into the belly.
    - SARI=87.50  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 51 - `682`

- **ORIGINAL**  (FKGL 5.0, 9 words): This was viewed on the AP and lateral projections.
- **REFERENCE** (FKGL -0.7, 8 words): This was viewed from the front and sides.
- **naive** (FKGL -0.3, 9 words, 0 edits): This was seen on the front and side views.
    - SARI=46.30  crit=1.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL -0.3, 9 words, 2 edits): This was viewed on the front and side views.
    - SARI=58.96  crit=1.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 2.3, 11 words, 2 edits): This was viewed on the front-to-back and side views.
    - SARI=54.23  crit=1.00  NLIf=0.91  copyjrg=0.00

### Note 52 - `686`

- **ORIGINAL**  (FKGL 8.2, 8 words): The cords move normally with phonation and ventilation.
- **REFERENCE** (FKGL 5.2, 8 words): The cords move normally when speaking and breathing
- **naive** (FKGL 4.8, 11 words, 0 edits): The vocal cords move normally when the patient speaks and breathes.
    - SARI=55.14  crit=0.00  NLIf=0.90  copyjrg=0.00
- **termonly** (FKGL 6.3, 9 words, 2 edits): The vocal folds move normally when speaking and breathing.
    - SARI=58.97  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 6.3, 9 words, 2 edits): The vocal cords move normally when speaking and breathing.
    - SARI=76.03  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 53 - `688`

- **ORIGINAL**  (FKGL 7.6, 13 words): Once the abdomen was opened, there was noted to be gross purulent drainage.
- **REFERENCE** (FKGL 6.0, 15 words): Once the abdomen was opened, there was noted to be a lot of pus draining.
- **naive** (FKGL 5.8, 12 words, 0 edits): After the abdomen was opened, there was a large amount of pus.
    - SARI=43.10  crit=1.00  NLIf=0.84  copyjrg=0.00
- **termonly** (FKGL 2.3, 9 words, 2 edits): Once the belly was opened, there was thick pus.
    - SARI=31.13  crit=0.00  NLIf=0.67  copyjrg=0.00
- **grounded** (FKGL 3.7, 10 words, 2 edits): Once the belly was opened, thick pus was leaking out.
    - SARI=20.65  crit=0.00  NLIf=0.79  copyjrg=0.00

### Note 54 - `692`

- **ORIGINAL**  (FKGL 4.0, 13 words): Once all four ports were placed, the right upper quadrant was then explored.
- **REFERENCE** (FKGL 5.4, 16 words): Once all four tubes were placed, the top right corner of her abdomen was then explored.
- **naive** (FKGL 7.6, 16 words, 0 edits): After all four ports were placed, the doctor examined the upper right part of the abdomen.
    - SARI=35.97  crit=1.00  NLIf=0.48  copyjrg=0.25
- **termonly** (FKGL 8.4, 16 words, 2 edits): Once all four small openings were made, the doctor looked inside the upper right belly area.
    - SARI=36.99  crit=0.00  NLIf=0.38  copyjrg=0.00
- **grounded** (FKGL 6.1, 16 words, 2 edits): Once all four small tubes were placed, the doctor looked at the upper right belly area.
    - SARI=48.62  crit=0.00  NLIf=0.35  copyjrg=0.00

### Note 55 - `693`

- **ORIGINAL**  (FKGL 15.4, 15 words): Options such as watchful waiting, robotic prostatectomy, seed implantation with and without radiation were discussed.
- **REFERENCE** (FKGL 11.8, 23 words): Options such as watch and wait, removing the prostate with the help of a robot, seed implantation with and without radiation were discussed.
- **naive** (FKGL 15.3, 17 words, 0 edits): The doctor discussed options such as watchful waiting, robotic prostatectomy, and seed implantation with or without radiation.
    - SARI=22.42  crit=0.00  NLIf=0.15  copyjrg=1.00
- **termonly** (FKGL 13.3, 18 words, 4 edits): Options such as close monitoring, robot-assisted surgery, and placing seeds with or without energy beams were discussed.
    - SARI=31.72  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 13.1, 20 words, 4 edits): Options such as close watching, robot-assisted prostate removal, and placing seeds with or without high-energy rays were discussed.
    - SARI=32.43  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 56 - `695`

- **ORIGINAL**  (FKGL 14.3, 10 words): He also reportedly was on Lasix prior to hospitalization, possible
- **REFERENCE** (FKGL 11.5, 15 words): He also was reportedly on water pills (lasix) before his admission to the hospital, possible
- **naive** (FKGL 10.7, 12 words, 0 edits): He also reportedly was on Lasix before going to the hospital, possibly.
    - SARI=48.79  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 14.3, 10 words, 0 edits): He also reportedly was on Lasix prior to hospitalization, possible
    - SARI=9.07  crit=0.00  NLIf=0.99  copyjrg=1.00
- **grounded** (FKGL 14.3, 10 words, 0 edits): He also reportedly was on Lasix prior to hospitalization, possible
    - SARI=9.07  crit=0.00  NLIf=0.99  copyjrg=1.00

### Note 57 - `697`

- **ORIGINAL**  (FKGL 10.2, 9 words): The four cardiac chambers dimensions are within normal limits.
- **REFERENCE** (FKGL 4.9, 13 words): The sizes of the four parts of the heart are within normal limits.
- **naive** (FKGL 3.7, 9 words, 0 edits): The sizes of the four heart chambers are normal.
    - SARI=47.28  crit=0.00  NLIf=0.97  copyjrg=0.25
- **termonly** (FKGL 2.3, 8 words, 2 edits): The four heart chambers are normal in size.
    - SARI=33.60  crit=0.00  NLIf=0.97  copyjrg=0.25
- **grounded** (FKGL 2.3, 7 words, 3 edits): The four heart room sizes are normal.
    - SARI=37.42  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 58 - `698`

- **ORIGINAL**  (FKGL 11.5, 9 words): Digital rectal examination was performed, which showed no masses.
- **REFERENCE** (FKGL 6.9, 11 words): Examination of the back passage was performed, which showed no lumps.
- **naive** (FKGL 6.0, 16 words, 0 edits): The doctor checked the patient's rectum with a finger and did not find any lumps.
    - SARI=18.93  crit=0.00  NLIf=0.18  copyjrg=0.00
- **termonly** (FKGL 3.8, 12 words, 2 edits): The doctor checked the rectum with a finger and found no lumps.
    - SARI=23.19  crit=0.00  NLIf=0.07  copyjrg=0.00
- **grounded** (FKGL 3.8, 12 words, 3 edits): The doctor checked the rectum with a finger and found no lumps.
    - SARI=23.19  crit=0.00  NLIf=0.07  copyjrg=0.00

### Note 59 - `699`

- **ORIGINAL**  (FKGL 11.2, 23 words): He then had a problem with seizures, hemiparesis, has been to the hospital, developed C-diff, and is in the nursing home currently.
- **REFERENCE** (FKGL 12.0, 29 words): He then had a problem with fits, weakness on one side, has been to the hospital, developed an infection in the gut, and is in the nursing home currently.
- **naive** (FKGL 5.5, 30 words, 0 edits): He then had seizures and weakness on one side of his body. He went to the hospital, got an infection called C-diff, and is now in a nursing home.
    - SARI=30.77  crit=0.00  NLIf=0.94  copyjrg=0.67
- **termonly** (FKGL 12.0, 27 words, 2 edits): He then had a problem with seizures, weakness on one side, has been to the hospital, developed a gut infection, and is in the nursing home currently.
    - SARI=80.94  crit=0.00  NLIf=0.91  copyjrg=0.33
- **grounded** (FKGL 13.0, 30 words, 2 edits): He then had a problem with seizures, weakness on one side of the body, has been to the hospital, developed a gut infection, and is in the nursing home currently.
    - SARI=75.63  crit=0.00  NLIf=0.92  copyjrg=0.33

### Note 60 - `700`

- **ORIGINAL**  (FKGL 12.3, 22 words): He has been on continuous positive airway pressure now for several months, and returns for followup to review his response to treatment.
- **REFERENCE** (FKGL 9.7, 25 words): He has been using a breathing mask now for several months, and returns for follow up to review how he is doing with the treatment.
- **naive** (FKGL 11.6, 25 words, 0 edits): He has used continuous positive airway pressure for several months and is coming back for a checkup to see how well the treatment is working.
    - SARI=42.23  crit=0.00  NLIf=0.99  copyjrg=0.83
- **termonly** (FKGL 7.0, 20 words, 2 edits): He has used a breathing machine for several months and comes back to check how well the treatment is working.
    - SARI=48.89  crit=0.00  NLIf=0.83  copyjrg=0.00
- **grounded** (FKGL 8.7, 20 words, 2 edits): He has used a breathing machine for several months and returns for a checkup to review his response to treatment.
    - SARI=53.10  crit=0.00  NLIf=0.86  copyjrg=0.00

### Note 61 - `709`

- **ORIGINAL**  (FKGL 8.5, 18 words): The patient to take small bite and small sips to help decrease the risk of aspiration and penetration.
- **REFERENCE** (FKGL 9.9, 30 words): The patient is to take small bite and small sips to help decrease the risk of having the food or drink going down the wrong pipe and piercing the pipe.
- **naive** (FKGL 8.0, 22 words, 0 edits): The patient should take small bites and small sips to help lower the risk of food or liquid going into the airway.
    - SARI=39.02  crit=0.00  NLIf=0.66  copyjrg=0.00
- **termonly** (FKGL 7.5, 22 words, 1 edits): The patient should take small bites and small sips to help lower the risk of food going into the airway or lungs.
    - SARI=38.44  crit=0.00  NLIf=0.55  copyjrg=0.00
- **grounded** (FKGL 6.4, 20 words, 2 edits): The patient should take small bites and sips to lower the risk of breathing food into the lungs or throat.
    - SARI=26.69  crit=0.00  NLIf=0.73  copyjrg=0.00

### Note 62 - `714`

- **ORIGINAL**  (FKGL 12.3, 15 words): The patient was awakened and extubated and moved to the recovery room in satisfactory condition.
- **REFERENCE** (FKGL 11.1, 20 words): The patient was awakened and tube was removed from the airway and moved to the recovery room in satisfactory condition.
- **naive** (FKGL 8.0, 19 words, 0 edits): The patient woke up, had the breathing tube removed, and was moved to the recovery room in good condition.
    - SARI=36.87  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 7.8, 18 words, 3 edits): The patient woke up, had the breathing tube removed, and moved to the recovery room in good condition.
    - SARI=39.28  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 7.8, 18 words, 3 edits): The patient woke up, had the breathing tube removed, and moved to the recovery room in good condition.
    - SARI=39.28  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 63 - `721`

- **ORIGINAL**  (FKGL 15.4, 10 words): PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily aroused.
- **REFERENCE** (FKGL 6.7, 8 words): The patient was asleep, but easily woken up.
- **naive** (FKGL 5.2, 8 words, 0 edits): The patient was asleep but woke up easily.
    - SARI=62.05  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 7.4, 7 words, 1 edits): The patient was asleep, but easily woken.
    - SARI=88.89  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 15.4, 10 words, 1 edits): PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily woken.
    - SARI=80.25  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 64 - `725`

- **ORIGINAL**  (FKGL 10.9, 26 words): He is to follow up in approximately 10 days for recheck as well as prescription for intended AFOs, which he will need up to 6 months.
- **REFERENCE** (FKGL 11.5, 28 words): He is to come back in approximately 10 days for recheck as well as prescription for intended foot-drop braces, which he will need up to 6 months.
- **naive** (FKGL 3.9, 32 words, 0 edits): He should come back in about 10 days for a checkup and to get a prescription for the AFOs he needs. He will need to use them for up to 6 months.
    - SARI=28.71  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 10.7, 27 words, 2 edits): He is to follow up in about 10 days for recheck as well as prescription for intended ankle braces, which he will need up to 6 months.
    - SARI=54.83  crit=0.00  NLIf=0.38  copyjrg=0.00
- **grounded** (FKGL 11.2, 29 words, 2 edits): He is to follow up in about 10 days for recheck as well as prescription for intended ankle and foot braces, which he will need up to 6 months.
    - SARI=55.69  crit=0.00  NLIf=0.61  copyjrg=0.00

### Note 65 - `726`

- **ORIGINAL**  (FKGL 14.1, 8 words): Genitourinary : The external genitalia appeared to be normal.
- **REFERENCE** (FKGL 12.3, 8 words): The penis/vagina/genitals appeared to be normal.
- **naive** (FKGL 5.2, 8 words, 0 edits): The outside parts of the genitals looked normal.
    - SARI=28.00  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 9.7, 8 words, 1 edits): Genitourinary system: The outside sex organs looked normal.
    - SARI=24.48  crit=0.00  NLIf=0.95  copyjrg=0.25
- **grounded** (FKGL 9.1, 7 words, 1 edits): Genitourinary: The outside sex organs looked normal.
    - SARI=23.89  crit=0.00  NLIf=0.96  copyjrg=0.25

### Note 66 - `727`

- **ORIGINAL**  (FKGL 12.2, 13 words): She is postop day 21 of an exploratory laparotomy with ovarian cancer staging.
- **REFERENCE** (FKGL 12.6, 17 words): She is 21 days after an open abdominal operation which explored how widespread the ovarian cancer was.
- **naive** (FKGL 12.0, 16 words, 0 edits): She is 21 days past surgery, which was an exploratory laparotomy to stage her ovarian cancer.
    - SARI=51.80  crit=0.00  NLIf=0.99  copyjrg=0.25
- **termonly** (FKGL 9.1, 16 words, 2 edits): She is 21 days after surgery to look inside her belly and check for ovarian cancer.
    - SARI=54.53  crit=0.00  NLIf=0.73  copyjrg=0.00
- **grounded** (FKGL 8.5, 18 words, 2 edits): She is 21 days after surgery to check her belly and see how far ovarian cancer has spread.
    - SARI=54.77  crit=0.00  NLIf=0.25  copyjrg=0.00

### Note 67 - `732`

- **ORIGINAL**  (FKGL 8.5, 13 words): Prescription for prednisone as part of his chemotherapy has been given to him.
- **REFERENCE** (FKGL 7.6, 15 words): Prescription for steroid tablets as part of his cancer treatment has been given to him.
- **naive** (FKGL 8.8, 12 words, 0 edits): He was given a prescription for prednisone as part of his chemotherapy.
    - SARI=25.39  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 5.8, 12 words, 0 edits): He was given a medicine that is part of his cancer treatment.
    - SARI=35.39  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 8.4, 16 words, 1 edits): He was given a medicine that lowers immune response as part of his cancer drug treatment.
    - SARI=41.28  crit=0.00  NLIf=0.55  copyjrg=0.00

### Note 68 - `738`

- **ORIGINAL**  (FKGL 9.1, 12 words): Photic stimulation was performed, but no clear-cut photic driving was seen.
- **REFERENCE** (FKGL 12.8, 17 words): Visual stimulation was performed, but no clear-cut changes in electrical activity of the brain was seen.
- **naive** (FKGL 7.0, 20 words, 0 edits): The patient was exposed to flashing lights, but there was no clear sign that the brain was responding to them.
    - SARI=27.23  crit=0.00  NLIf=0.38  copyjrg=0.00
- **termonly** (FKGL 4.0, 13 words, 2 edits): The patient was shown flashing lights, but no clear brain response was seen.
    - SARI=34.26  crit=0.00  NLIf=0.19  copyjrg=0.00
- **grounded** (FKGL 2.6, 11 words, 0 edits): Light flashes were used, but no clear brain response was seen.
    - SARI=32.97  crit=0.00  NLIf=0.82  copyjrg=0.00

### Note 69 - `739`

- **ORIGINAL**  (FKGL 15.6, 8 words): FAMILY HISTORY : Both parents died with myocardial infarctions.
- **REFERENCE** (FKGL 8.2, 8 words): Family history: Both parents died with heart attacks.
- **naive** (FKGL 3.7, 10 words, 0 edits): Both of the patient's parents died from heart attacks.
    - SARI=25.93  crit=0.00  NLIf=0.91  copyjrg=0.00
- **termonly** (FKGL 8.2, 8 words, 1 edits): FAMILY HISTORY : Both parents died with heart attacks.
    - SARI=100.00  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 8.2, 8 words, 1 edits): FAMILY HISTORY: Both parents died with heart attacks.
    - SARI=100.00  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 70 - `740`

- **ORIGINAL**  (FKGL 11.2, 11 words): Extremities : 2+ bilateral pitting edema to the level of the knees.
- **REFERENCE** (FKGL 10.1, 28 words): Hands and feet: There is swelling in both feet up to the level of the knees (when pressed, causes an indentation in the skin for a few seconds)
- **naive** (FKGL 6.7, 19 words, 0 edits): The patient has moderate swelling in both legs that leaves a dent when pressed, reaching up to the knees.
    - SARI=38.47  crit=1.00  NLIf=0.60  copyjrg=0.00
- **termonly** (FKGL 3.2, 16 words, 1 edits): Arms and legs: 2+ swelling on both sides that leaves a dent, up to the knees.
    - SARI=34.55  crit=0.00  NLIf=0.57  copyjrg=0.00
- **grounded** (FKGL 3.9, 18 words, 1 edits): Arms and legs: 2+ swelling on both sides that leaves a dent when pressed, up to the knees.
    - SARI=35.79  crit=0.00  NLIf=0.39  copyjrg=0.00

### Note 71 - `741`

- **ORIGINAL**  (FKGL 14.3, 10 words): Following questions are mostly involved in a psychosocial donor evaluation.
- **REFERENCE** (FKGL 13.9, 15 words): Following questions are mostly involved in a donor evaluation of their psychological or social states.
- **naive** (FKGL 12.3, 11 words, 0 edits): The following questions are mostly used in a psychosocial donor evaluation.
    - SARI=21.16  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 7.2, 10 words, 1 edits): The questions mostly involve a social and mental donor check.
    - SARI=16.45  crit=0.00  NLIf=0.85  copyjrg=0.00
- **grounded** (FKGL 7.8, 12 words, 1 edits): The questions mostly involve a donor check of mental and social factors.
    - SARI=18.37  crit=0.00  NLIf=0.91  copyjrg=0.00

### Note 72 - `742`

- **ORIGINAL**  (FKGL 24.1, 5 words): Mild nonmobile descending aortic atherosclerosis.
- **REFERENCE** (FKGL 11.1, 22 words): Mild non-moving hardening of the part of aorta (the largest artery of the body) that goes down the chest and abdomen.
- **naive** (FKGL 10.4, 13 words, 0 edits): The patient has mild atherosclerosis in the descending aorta that does not move.
    - SARI=39.50  crit=0.00  NLIf=0.98  copyjrg=0.25
- **termonly** (FKGL 4.2, 14 words, 0 edits): Mild plaque in the lower part of the main artery that does not move.
    - SARI=45.65  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 3.7, 11 words, 1 edits): Mild clogging in the main chest artery that does not move.
    - SARI=44.23  crit=0.00  NLIf=0.90  copyjrg=0.00

### Note 73 - `750`

- **ORIGINAL**  (FKGL 6.7, 8 words): The eustachian tube was obstructed with bone wax.
- **REFERENCE** (FKGL 3.1, 13 words): The passage between the nose and the ears was blocked with bone wax.
- **naive** (FKGL 3.8, 8 words, 0 edits): The eustachian tube was blocked with bone wax.
    - SARI=59.31  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL 4.8, 11 words, 3 edits): The tube to the ear was blocked with a waxy material.
    - SARI=34.89  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 6.0, 15 words, 2 edits): The tube from the middle ear to the throat was blocked with a waxy material.
    - SARI=34.18  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 74 - `752`

- **ORIGINAL**  (FKGL 6.3, 9 words): He was placed supine on the operating room table.
- **REFERENCE** (FKGL 7.2, 10 words): He was placed facing upwards on the operating room table.
- **naive** (FKGL 4.8, 11 words, 0 edits): He was placed on his back on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 4.8, 10 words, 1 edits): He lay on his back on the operating room table.
    - SARI=50.81  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 4.8, 10 words, 1 edits): He lay on his back on the operating room table.
    - SARI=50.81  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 75 - `755`

- **ORIGINAL**  (FKGL 7.4, 7 words): A urinalysis was not performed this time.
- **REFERENCE** (FKGL 2.3, 8 words): A urine test was not performed this time.
- **naive** (FKGL 3.7, 11 words, 0 edits): The doctors did not test the patient's urine this time.
    - SARI=25.51  crit=0.00  NLIf=0.54  copyjrg=0.00
- **termonly** (FKGL 0.8, 8 words, 2 edits): A urine test was not done this time.
    - SARI=51.60  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 0.8, 8 words, 2 edits): A urine test was not done this time.
    - SARI=51.60  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 76 - `766`

- **ORIGINAL**  (FKGL 12.3, 21 words): Vision and hearing appeared to be adequate for testing, although she did indicate that she needed to update her eyeglass prescription.
- **REFERENCE** (FKGL 11.7, 21 words): Vision and hearing appeared to be okay for testing, although she did indicate that she needed to update her glasses prescription.
- **naive** (FKGL 8.7, 20 words, 0 edits): Her vision and hearing were good enough for the tests, but she said she needed to update her eyeglass prescription.
    - SARI=22.43  crit=0.00  NLIf=0.99  copyjrg=0.67
- **termonly** (FKGL 6.1, 16 words, 1 edits): Her sight and hearing were good enough for testing, though she said she needed new glasses.
    - SARI=17.45  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 8.4, 17 words, 3 edits): Vision and hearing seemed good enough for testing, although she said she needed to update her glasses.
    - SARI=38.72  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 77 - `771`

- **ORIGINAL**  (FKGL 8.0, 24 words): I have talked to him several times about a colonoscopy, which he has refused, and so we have been doing stools for occult blood.
- **REFERENCE** (FKGL 17.5, 46 words): I have talked to him several times about a procedure to have a look inside the bowels (colonoscopy), which he has refused, and so we have been testing some stool samples in the lab to look for blood (which may be invisible to the naked eye).
- **naive** (FKGL 4.0, 26 words, 0 edits): The doctor has talked to him several times about a colonoscopy, but he has refused it. So, they have been testing his stool for hidden blood.
    - SARI=37.72  crit=0.00  NLIf=0.92  copyjrg=0.00
- **termonly** (FKGL 12.4, 32 words, 3 edits): I have talked to him several times about a test to look inside the large intestine, which he has refused, and so we have been checking his bowel movements for hidden blood.
    - SARI=63.73  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 11.6, 32 words, 3 edits): I have talked to him several times about a test to check the inside of the large intestine, which he has refused, and so we have been testing poop for hidden blood.
    - SARI=63.38  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 78 - `783`

- **ORIGINAL**  (FKGL 8.4, 10 words): The knee was copiously irrigated and suction dried once again.
- **REFERENCE** (FKGL 7.6, 16 words): The knee was washed out thoroughly and dried with a suction (or mini-vacuum) once again
- **naive** (FKGL 4.7, 16 words, 0 edits): The knee was washed out with a lot of fluid and then dried with suction again.
    - SARI=61.54  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 4.0, 13 words, 2 edits): The knee was washed with lots of fluid and dried with suction again.
    - SARI=59.15  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 4.0, 13 words, 2 edits): The knee was washed with lots of fluid and dried with suction again.
    - SARI=59.15  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 79 - `784`

- **ORIGINAL**  (FKGL 10.9, 14 words): She is not having painful urination, any blood in the urine, frequency or hesitancy.
- **REFERENCE** (FKGL 11.1, 20 words): She is not having painful peeing, any blood in the pee, needing to pee very often or having difficulty peeing.
- **naive** (FKGL 10.4, 18 words, 0 edits): She does not have pain when urinating, blood in her urine, frequent urination, or trouble starting to urinate.
    - SARI=25.38  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 9.8, 18 words, 2 edits): She is not having painful urination, any blood in the urine, needing to go often, or trouble starting.
    - SARI=63.87  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 9.9, 20 words, 2 edits): She is not having painful urination, any blood in the urine, needing to pee often, or trouble starting to pee.
    - SARI=66.66  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 80 - `789`

- **ORIGINAL**  (FKGL 14.8, 19 words): Cardiovascular : Chest pain in the retrosternal area, Occasional anginal pain and patient describes it as a sensation of tightness.
- **REFERENCE** (FKGL 14.6, 30 words): Heart and blood vessels: Chest pain just behind the breastbone, occasional chest pain when exercising or exerting themselves, which gets better with rest and patient describes it as feeling 'tightness'.
- **naive** (FKGL 5.4, 21 words, 0 edits): The patient has chest pain behind the breastbone. They sometimes have angina pain and describe it as a feeling of tightness.
    - SARI=40.06  crit=0.00  NLIf=0.79  copyjrg=0.00
- **termonly** (FKGL 9.2, 19 words, 2 edits): Heart: Chest pain behind the breastbone, occasional heart pain, and the patient describes it as a feeling of tightness.
    - SARI=60.23  crit=0.00  NLIf=0.92  copyjrg=0.00
- **grounded** (FKGL 10.2, 22 words, 2 edits): Heart and blood vessels: Chest pain behind the breastbone, occasional heart pain, and the patient describes it as a feeling of tightness.
    - SARI=65.77  crit=0.00  NLIf=0.90  copyjrg=0.00

### Note 81 - `790`

- **ORIGINAL**  (FKGL 4.8, 11 words): We excised a good bit of his synovium and synovial pouch.
- **REFERENCE** (FKGL 1.9, 12 words): We cut out a bit of the soft tissue of the joint.
- **naive** (FKGL 5.8, 12 words, 0 edits): The doctors removed a large part of his synovium and synovial pouch.
    - SARI=32.05  crit=0.00  NLIf=0.96  copyjrg=0.80
- **termonly** (FKGL 1.6, 11 words, 2 edits): We cut out much of his joint lining and joint pouch.
    - SARI=40.61  crit=0.00  NLIf=0.99  copyjrg=0.20
- **grounded** (FKGL 2.6, 11 words, 2 edits): We cut out much of his joint lining and joint pocket.
    - SARI=41.09  crit=0.00  NLIf=0.92  copyjrg=0.00

### Note 82 - `801`

- **ORIGINAL**  (FKGL 13.4, 11 words): An inflammatory process such as infection or ischemia must be considered.
- **REFERENCE** (FKGL 10.4, 13 words): An inflammatory process such as infection or reduced blood flow must be considered.
- **naive** (FKGL 12.8, 16 words, 0 edits): Doctors must consider whether an inflammatory process, such as an infection or ischemia, is the cause.
    - SARI=34.50  crit=0.00  NLIf=0.23  copyjrg=1.00
- **termonly** (FKGL 5.9, 11 words, 2 edits): A problem like infection or poor blood flow must be considered.
    - SARI=35.22  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 7.8, 12 words, 2 edits): A body reaction like infection or low blood flow must be considered.
    - SARI=34.26  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 83 - `804`

- **ORIGINAL**  (FKGL 2.9, 12 words): I have asked her to increase her prednisone when she goes home.
- **REFERENCE** (FKGL 2.9, 12 words): I have asked her to increase her steroid when she goes home.
- **naive** (FKGL 2.9, 12 words, 0 edits): The doctor asked her to take more prednisone when she goes home.
    - SARI=26.98  crit=0.00  NLIf=0.57  copyjrg=1.00
- **termonly** (FKGL 4.9, 13 words, 1 edits): I have asked her to increase her steroid medicine when she goes home.
    - SARI=79.79  crit=0.00  NLIf=0.02  copyjrg=0.00
- **grounded** (FKGL 4.9, 13 words, 1 edits): I have asked her to increase her steroid medicine when she goes home.
    - SARI=79.79  crit=0.00  NLIf=0.02  copyjrg=0.00

### Note 84 - `844`

- **ORIGINAL**  (FKGL 10.2, 9 words): She may need other neuropathic pain medications as needed.
- **REFERENCE** (FKGL 6.3, 9 words): She may need other nerve pain medications as needed.
- **naive** (FKGL 4.8, 10 words, 0 edits): She may need other medicines for nerve pain as needed.
    - SARI=52.10  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 6.3, 9 words, 1 edits): She may need other nerve pain medications as needed.
    - SARI=100.00  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 6.3, 9 words, 1 edits): She may need other nerve pain medications as needed.
    - SARI=100.00  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 85 - `852`

- **ORIGINAL**  (FKGL 12.4, 7 words): A prophylactic dose of antibiotics was given.
- **REFERENCE** (FKGL 10.7, 7 words): A prevention dose of antibiotics was given.
- **naive** (FKGL 10.2, 11 words, 0 edits): The patient was given a dose of antibiotics to prevent infection.
    - SARI=41.87  crit=0.00  NLIf=0.93  copyjrg=0.00
- **termonly** (FKGL 7.2, 11 words, 2 edits): A dose of germ-fighting medicine was given to prevent illness.
    - SARI=28.96  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 6.7, 9 words, 2 edits): A preventive dose of germ-killing medicine was given.
    - SARI=28.96  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 86 - `854`

- **ORIGINAL**  (FKGL 16.2, 6 words): Chronic hypokalemia secondary to chronic diarrhea.
- **REFERENCE** (FKGL 7.6, 9 words): Long term low potassium due to long term diarrhea.
- **naive** (FKGL 11.2, 13 words, 0 edits): The patient has long-term low potassium levels caused by long-term diarrhea.
    - SARI=49.19  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 6.7, 10 words, 0 edits): Long-term low potassium caused by long-term loose stools.
    - SARI=42.52  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 9.6, 12 words, 0 edits): Long-term low blood potassium caused by long-term runny bowel movements.
    - SARI=37.94  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 87 - `859`

- **ORIGINAL**  (FKGL 6.6, 4 words): No hepatosplenomegaly or tenderness.
- **REFERENCE** (FKGL 2.3, 9 words): No enlarged liver or spleen or pain when pushed.
- **naive** (FKGL 5.8, 14 words, 0 edits): The patient's liver and spleen are not enlarged, and there is no tenderness.
    - SARI=36.27  crit=0.00  NLIf=0.93  copyjrg=0.50
- **termonly** (FKGL 3.4, 14 words, 0 edits): The liver and spleen are not enlarged, and there is no pain when touched.
    - SARI=41.53  crit=0.00  NLIf=0.12  copyjrg=0.00
- **grounded** (FKGL 2.5, 10 words, 2 edits): No enlarged liver or spleen, and no pain when touched.
    - SARI=58.88  crit=0.00  NLIf=0.08  copyjrg=0.00

### Note 88 - `881`

- **ORIGINAL**  (FKGL 9.1, 11 words): He did not experience his left anterior chest pain with exercise.
- **REFERENCE** (FKGL 5.9, 11 words): He did not experience his left front chest pain with exercise.
- **naive** (FKGL 3.9, 16 words, 0 edits): He did not have pain in the front left side of his chest when he exercised.
    - SARI=25.89  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 2.6, 11 words, 2 edits): He did not feel his left front chest pain with exercise.
    - SARI=62.40  crit=1.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 2.6, 11 words, 2 edits): He did not feel his left front chest pain with exercise.
    - SARI=62.40  crit=1.00  NLIf=0.97  copyjrg=0.00

### Note 89 - `891`

- **ORIGINAL**  (FKGL 7.6, 9 words): Also, would use it to control the atrial fibrillation.
- **REFERENCE** (FKGL 6.0, 10 words): Also, would use it to control the irregular heart beat
- **naive** (FKGL 7.2, 10 words, 0 edits): Also, it would be used to control the atrial fibrillation.
    - SARI=12.08  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 7.6, 9 words, 1 edits): Also, would use it to control the irregular heartbeat.
    - SARI=80.00  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 7.6, 9 words, 1 edits): Also, would use it to control the irregular heartbeat.
    - SARI=80.00  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 90 - `900`

- **ORIGINAL**  (FKGL 11.1, 8 words): Overall the patient is a seemingly good historian.
- **REFERENCE** (FKGL 11.9, 10 words): Overall the patient is seemingly good at remembering their history
- **naive** (FKGL 8.4, 14 words, 0 edits): The patient seems to give a clear and accurate account of their medical history.
    - SARI=27.31  crit=0.00  NLIf=0.00  copyjrg=0.00
- **termonly** (FKGL 3.8, 8 words, 0 edits): The patient seems to give a clear history.
    - SARI=26.94  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 3.8, 8 words, 0 edits): The patient seems to give a clear history.
    - SARI=26.94  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 91 - `933`

- **ORIGINAL**  (FKGL 3.7, 10 words): No active Crohn 's disease was found during the colonoscopy.
- **REFERENCE** (FKGL 5.9, 14 words): No active Crohn 's disease was found during the camera test through the gut.
- **naive** (FKGL 3.7, 10 words, 0 edits): The colonoscopy did not show any active Crohn's disease.
    - SARI=18.58  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 5.8, 13 words, 2 edits): No signs of ongoing Crohn's disease were seen during the scope exam.
    - SARI=19.15  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 6.0, 11 words, 1 edits): No current Crohn's disease was found during the colon exam.
    - SARI=41.10  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 92 - `935`

- **ORIGINAL**  (FKGL 16.4, 28 words): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have mounting exhaustion and respiratory distress.
- **REFERENCE** (FKGL 15.5, 28 words): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have worsening exhaustion and breathing distress.
- **naive** (FKGL 6.7, 28 words, 0 edits): Soon after the first check-up, the patient started to complain of chest pain. The nurse saw that the patient was getting very tired and having trouble breathing.
    - SARI=21.73  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 15.0, 28 words, 2 edits): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have growing tiredness and trouble breathing.
    - SARI=63.09  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 16.4, 29 words, 2 edits): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have growing extreme tiredness and difficulty breathing.
    - SARI=62.70  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 93 - `968`

- **ORIGINAL**  (FKGL 8.2, 8 words): She has been referred for a pacemaker implantation.
- **REFERENCE** (FKGL 7.6, 9 words): She has been referred for a pacemaker fitting surgery.
- **naive** (FKGL 2.5, 10 words, 0 edits): She has been sent to have a pacemaker put in.
    - SARI=23.47  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 2.5, 10 words, 2 edits): She has been sent to get a pacemaker put in.
    - SARI=23.47  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 2.3, 9 words, 2 edits): She was sent to have a pacemaker put in.
    - SARI=13.49  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 94 - `116`

- **ORIGINAL**  (FKGL -0.7, 8 words): There was some hematoma at the cath site.
- **REFERENCE** (FKGL 5.8, 13 words): There was some swelling due to collection of blood at the catheter site.
- **naive** (FKGL 2.3, 8 words, 0 edits): There was a bruise at the catheter site.
    - SARI=48.98  crit=0.00  NLIf=0.13  copyjrg=0.00
- **termonly** (FKGL 0.8, 8 words, 2 edits): There was some bruising at the tube site.
    - SARI=58.33  crit=0.00  NLIf=0.44  copyjrg=0.00
- **grounded** (FKGL 3.8, 8 words, 2 edits): There was some bruising at the catheter spot.
    - SARI=58.86  crit=0.00  NLIf=0.84  copyjrg=0.00

### Note 95 - `592`

- **ORIGINAL**  (FKGL 6.3, 9 words): The necrotic tissue was lifted out of the abdomen.
- **REFERENCE** (FKGL 3.7, 9 words): The dead flesh was lifted out of the abdomen.
- **naive** (FKGL 3.8, 8 words, 0 edits): The dead tissue was removed from the belly.
    - SARI=20.96  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 5.0, 9 words, 1 edits): The dead tissue was lifted out of the abdomen.
    - SARI=72.13  crit=0.00  NLIf=0.99  copyjrg=0.33
- **grounded** (FKGL 5.0, 9 words, 1 edits): The dead tissue was lifted out of the abdomen.
    - SARI=72.13  crit=0.00  NLIf=0.99  copyjrg=0.33

### Note 96 - `249`

- **ORIGINAL**  (FKGL 6.7, 8 words): Pressure was held and the area was hemostatic.
- **REFERENCE** (FKGL 5.2, 8 words): Pressure was held and the area stopped bleeding.
- **naive** (FKGL 4.0, 7 words, 0 edits): Pressure was applied, and the bleeding stopped.
    - SARI=30.32  crit=0.00  NLIf=0.58  copyjrg=0.00
- **termonly** (FKGL 5.2, 8 words, 1 edits): Pressure was held and the area stopped bleeding.
    - SARI=100.00  crit=0.00  NLIf=0.52  copyjrg=0.00
- **grounded** (FKGL 5.2, 8 words, 1 edits): Pressure was held and the area stopped bleeding.
    - SARI=100.00  crit=0.00  NLIf=0.52  copyjrg=0.00

### Note 97 - `701`

- **ORIGINAL**  (FKGL 3.7, 9 words): The area was lavaged with some saline and cleared.
- **REFERENCE** (FKGL 3.7, 11 words): The area was washed out with some salt water and cleared.
- **naive** (FKGL 3.7, 9 words, 0 edits): The area was washed with some saline and cleared.
    - SARI=59.43  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL 3.7, 9 words, 2 edits): The area was washed with salt water and cleared.
    - SARI=69.70  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 3.7, 9 words, 2 edits): The area was washed with salt water and cleared.
    - SARI=69.70  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 98 - `826`

- **ORIGINAL**  (FKGL 8.2, 8 words): Pain and inability to ambulate brought him in.
- **REFERENCE** (FKGL 6.3, 9 words): Pain and inability to move around brought him in.
- **naive** (FKGL 2.9, 12 words, 0 edits): He came in because of pain and because he could not walk.
    - SARI=23.06  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 2.3, 7 words, 1 edits): Pain and trouble walking brought him in.
    - SARI=35.97  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 2.5, 10 words, 1 edits): Pain and not being able to walk brought him in.
    - SARI=38.11  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 99 - `751`

- **ORIGINAL**  (FKGL 2.3, 8 words): There is a hernia on the left side.
- **REFERENCE** (FKGL 2.9, 12 words): The gut sticks out through the abdomen wall on the left side.
- **naive** (FKGL 3.7, 9 words, 0 edits): The patient has a hernia on the left side.
    - SARI=55.97  crit=0.00  NLIf=0.97  copyjrg=1.00
- **termonly** (FKGL -0.7, 8 words, 1 edits): There is a bulge on the left side.
    - SARI=60.64  crit=0.00  NLIf=0.75  copyjrg=0.00
- **grounded** (FKGL -0.7, 8 words, 1 edits): There is a bulge on the left side.
    - SARI=60.64  crit=0.00  NLIf=0.75  copyjrg=0.00

### Note 100 - `496`

- **ORIGINAL**  (FKGL 8.4, 10 words): Other systems were reviewed and were found to be unremarkable.
- **REFERENCE** (FKGL 4.8, 10 words): Other systems were reviewed and were found to be normal.
- **naive** (FKGL 3.8, 12 words, 0 edits): The doctor checked the rest of the body and found nothing wrong.
    - SARI=7.23  crit=1.00  NLIf=0.06  copyjrg=0.00
- **termonly** (FKGL 4.0, 7 words, 1 edits): Other systems were checked and seemed normal.
    - SARI=20.38  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 4.0, 7 words, 1 edits): Other systems were checked and seemed normal.
    - SARI=20.38  crit=1.00  NLIf=0.99  copyjrg=0.00
