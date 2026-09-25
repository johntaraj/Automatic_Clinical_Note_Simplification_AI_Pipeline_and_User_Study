# together-qwen3.5-9b - run `run100_20260815_222318`

- model: `Qwen/Qwen3.5-9B` (together, fireworks backend)
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
| **human edit recall** | 99 |  |  | 0.706 | 0.955 | 0.987 | higher is better | > 0.85 | of the jargon the human replaced, how much did we replace |

### 4 faithfulness

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **NLI faithfulness** | 100 |  |  | 0.844 | 0.804 | 0.789 | higher is better | > 0.70 | general-domain MNLI head; absolute values are compressed |
| **NLI completeness** | 100 |  |  | 0.895 | 0.760 | 0.738 | higher is better | > 0.60 | omission is the dominant clinical failure mode, which is why this direction is reported separately |

### 4 readability

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **FKGL drop vs input** | 100 |  |  | 3.30 | 4.47 | 4.33 | higher is better | > +4 grades | gameable by chopping sentences - read with length ratio |
| **Coleman-Liau drop** | 100 |  |  | 4.38 | 5.05 | 4.92 | higher is better | > +4 | none - this is the robustness check on FKGL |
| **length ratio vs reference** | 100 |  |  | 1.05 | 0.94 | 0.98 | descriptive | 0.9-1.3 | descriptive, not a quality score; >1.4 means the model is glossing everything |

### 4 safety

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **critical-error rate** | 100 |  |  | 0.100 | 0.120 | 0.110 | LOWER is better | 0.00 - any value > 0 needs review | fraction of outputs that lost a high-risk slot: negation, uncertainty, laterality, a number/unit, or a drug name |

### 5 attribution

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **attributable rate** | 0.645 | higher is better | > 0.50 | of the edits retrieval demonstrably caused, the fraction with a trustworthy explanation (held-out LDS >= 0.4, clear winner) |
| **held-out LDS (median)** | 0.772 | higher is better | > 0.60 (paper reports 0.6-0.85) | Spearman between the surrogate's predictions and the true log-probs on masks it never saw - how trustworthy the attributions are |
| **helped rate** | 0.439 | descriptive | descriptive - the split is the finding | fraction of edits retrieval made more likely (effect >= 0.10 nats) |
| **hurt rate** | 0.012 | LOWER is better | < 0.10 | fraction of edits retrieval made LESS likely - glossary actively harming the rewrite |
| **top-1 log-prob drop (helped edits)** | 1.22 | higher is better | > 0.5 nats | the paper reports roughly 0.43-0.75 for top-1 across three benchmarks, so this is the number to compare against |
| **winning source is the right term** | 0.921 | higher is better | > 0.80 | the complement is cross-term contamination - the definition of a DIFFERENT word in the same sentence winning the attribution and changing the meaning. Needs no gold labels, which is what makes it the closest thing this family has to a precision score |

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
| **copy-jargon rate** | 99 |  |  | 0.294 | 0.045 | 0.013 | LOWER is better | < 0.10 | exactly 1 - human_edit_recall, by construction: every gold term is either recalled or copied. Report it as a restatement, not as separate evidence, and keep it out of the significance family or one result consumes two FDR slots |
| **reference-vocabulary hit (NOT a precision)** | 84 |  |  | 0.643 | 0.655 | 0.679 | higher is better | descriptive only - see caveat | BROKEN AS NAMED, measured 2026-08-15. The support test is `ref_added & sys_content_words`, and `ref_added` is derived from (reference, original) only - it does not depend on the term being scored. So the same verdict is applied to every changed term in a note and the per-note value can only be 0 or 1. Verified on CLEAN93/qwen3p7-plus: 265 of 265 note-arm values are exactly 0.0 or 1.0, and no note has two terms that disagree. One incidental shared word credits every replacement in the sentence. Making this a real precision needs term-to-replacement span alignment, which does not exist yet. Do not quote it as evidence that replacements were correct |
| **definition borrowing** | 84 |  |  | 0.458 | 0.435 | 0.524 | descriptive | descriptive - the arm gap IS the finding | the mechanism behind the grounded-vs-termonly result, measured per note instead of only in analysis/conditional_grounding.py. Deliberately DESCRIPTIVE: grounded is shown the definitions and the other arms are not, so a difference here is expected by construction and testing it would burn an FDR slot to confirm something guaranteed. Read it as 'how much of the glossary's wording ended up in the output', then read what that cost in human_edit_recall and NLI |
| **replacement F1 (inherits a broken precision)** | 99 |  |  | 0.496 | 0.670 | 0.692 | higher is better | descriptive only - see caveat | DEMOTED from paper tier 2026-08-15. Half of it is replacement_precision, which is not per-term (see its caveat), so this cannot support a claim that the system replaced jargon CORRECTLY. Quote human_edit_recall instead - that half is genuinely per-term and is unaffected |
| **rewrite aggressiveness** | 100 |  |  | 0.365 | 0.194 | 0.204 | descriptive | descriptive | NOT an error rate - legitimate restructuring scores here |

### 4 quality

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **SARI** | 100 |  |  | 32.90 | 42.12 | 40.90 | higher is better | 40-60 typical | the references are MINIMAL-EDIT, so SARI rewards not editing. Measured: a perfect rewrite scored 25.97 vs 22.64 for doing nothing. Report, do not lead with it |
| **BERTScore F1** | 100 |  |  | 0.605 | 0.670 | 0.649 | higher is better | 0.4-0.7 rescaled | read the RESCALED value. Until bug 42 the baseline lookup was silently failing for a local model directory, so raw scores were reported and everything landed in 0.90-0.96 - which is why this metric was demoted for having no dynamic range. Rescaled, the same 5 notes span 0.556-0.620, a gap six times wider. The demotion should be re-examined on the full run |

### 4 readability

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **FKGL (absolute)** | 100 | 10.51 | 8.54 | 7.21 | 6.04 | 6.19 | LOWER is better | 6-8 (US grade) | absolute grade is dominated by sentence length; the DROP is the honest number |
| **Coleman-Liau (absolute)** | 100 | 12.78 | 9.80 | 8.40 | 7.73 | 7.87 | LOWER is better | 6-8 | character-based grade level |
| **Flesch Reading Ease** | 100 | 41.1 | 60.0 | 69.1 | 74.9 | 74.7 | higher is better | 60-80 (plain English) | uses the SAME two inputs as FKGL; not independent evidence |
| **FRE gain** | 100 |  |  | 28.0 | 33.9 | 33.6 | higher is better | > +20 | redundant with fkgl_drop |
| **SMOG** | 100 | 11.49 | 9.83 | 8.58 | 7.07 | 7.45 | LOWER is better | 6-8 | calibrated for 30+ sentence passages; very jumpy on one sentence |
| **SMOG drop** | 100 |  |  | 2.91 | 4.42 | 4.04 | higher is better | > +3 | same single-sentence calibration problem |
| **words out** | 100 | 12.2 | 14.8 | 14.7 | 13.4 | 13.8 | descriptive | close to the reference | output length |

### 4 safety

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **drug-name preservation** | 2 |  |  | 1.000 | 0.500 | 0.500 | higher is better | 1.00 - nothing less is acceptable | APPENDIX because of the DENOMINATOR, not the metric: only 2 of the 93 laymaker notes contain a detected drug name, so the mean is two observations wearing a percentage. Report the cases, not the rate. Also read it against tag_policy - under `replace` the pipeline is INSTRUCTED to drop drug names |
| **diagnostic-identity preservation** | 5 |  |  | 1.000 | 1.000 | 0.800 | higher is better | 1.00 - nothing less is acceptable | scored only over a closed curated table of conditions, and only 4 of 93 notes contain one, so the mean is four observations. An unlisted diagnosis is not scored rather than guessed at, so this under-reports rather than over-reports. Report the cases |
| **severity downgrade rate** | 10 |  |  | 0.200 | 0.300 | 0.200 | LOWER is better | 0.00 | 3-tier ordinal lexicon; lay renderings ('very bad') sit at the same tier as their clinical equivalent so correct paraphrase is not penalised. Appendix on denominator: 10 of 93 notes state a severity at all |
| **number/unit preservation** | 14 |  |  | 0.857 | 0.821 | 0.893 | higher is better | 1.00 | all doses and units survive (spelled-out numbers and expanded unit abbreviations count) |
| **negation preservation** | 24 |  |  | 0.917 | 0.917 | 0.917 | higher is better | 1.00 | type-level, so it cannot see WHICH negation was lost |
| **laterality preservation** | 8 |  |  | 0.812 | 0.625 | 0.812 | higher is better | 1.00 | left/right/bilateral/basal survive (instance-level) |
| **uncertainty preservation** | 9 |  |  | 0.778 | 0.667 | 0.667 | higher is better | 1.00 | hedging survives - 'cannot be excluded' must not become 'is present' |

### 5 attribution

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **LDS optimism gap** | 0.102 | LOWER is better | < 0.15 | a methodological result in its own right, not a quality score |
| **top-1 log-prob drop (all edits)** | 0.30 | higher is better | descriptive | NOT comparable to the paper's Figure 4a. Most edits have no source effect at all, so there is nothing to remove and the drop is ~0 by construction; the median over all edits therefore reads as a failure when the method is working. Quote `top1_drop_median_helped` instead |
| **ablation success rate** | 1.000 | higher is better | 1.00 | scoring calls that returned usable log-probs - a transport health check, not a quality metric |

## Attribution detail (stage 5)

`source_effect = log p(edit | full glossary) - log p(edit | no glossary)`. This is the only measurement in the suite that says whether retrieval *caused* an edit.

| quantity | value | meaning |
|---|---:|---|
| edits attributed | 173 | |
| ranked fits | 173 | a source could be ranked |
| flat fits | 0 | scoring worked, no source mattered - a RESULT, not a failure |
| measurement failures | 0 | aim for 0 |
| **helped** | 76 | retrieval made the edit more likely |
| **neutral** | 95 | the model knew it anyway |
| **hurt** | 2 | retrieval made it LESS likely |
| attributable rate | 0.6447 | of helped edits, those with a trustworthy explanation |
| **winning source is the right term** | 0.9211 | of 76 caused edits; the rest are cross-term contamination |
| held-out LDS (median) | 0.7716 | aim > 0.60 |
| in-sample LDS (median) | 0.8736 | for contrast only |
| **LDS optimism gap** | 0.102 | how much an in-sample number would overstate faithfulness |
| edits with no LDS | 52 | glossary too small for a genuinely unseen held-out block |
| **top-1 drop, helped edits** | 1.2196 | paper Eq. 1 over the 76 edits where a source mattered - the number comparable to the paper's Fig. 4a |
| **top-3 drop, helped edits** | 2.3761 | same, removing the top three |
| top-1 drop, ALL edits | 0.2959 | ~0 by construction on the 95 edits with no source effect; do NOT quote this against the paper |
| ablation success | 1.0 | transport health |

> Surrogate target: **logit-scaled probability**, per ContextCite Algorithm 1 line 4. Bucketing uses the log-probability difference, which answers "would the model have produced this anyway?". Both are stored per edit.

**Threshold sensitivity** (the helped/hurt split depends on an arbitrary cut-off, so it is swept):

| eps (nats) | helped | neutral | hurt | attributable |
|---:|---:|---:|---:|---:|
| 0.05 | 115 | 21 | 37 | 0.5739 |
| 0.1 | 108 | 35 | 30 | 0.5926 |
| 0.25 | 97 | 58 | 18 | 0.5979 |
| 0.693 | 76 | 95 | 2 | 0.6447 |
| 1.0 | 66 | 107 | 0 | 0.6515 |

### Does grounding help more on rare terms?

| Zipf stratum | edits | helped | neutral | hurt | helped rate | mean effect (nats) |
|---|---:|---:|---:|---:|---:|---:|
| very_rare | 45 | 20 | 23 | 1 | 0.4545 | 1.2889 |
| rare | 63 | 29 | 34 | 0 | 0.4603 | 1.231 |
| uncommon | 51 | 22 | 28 | 1 | 0.4314 | 1.6049 |
| common | 12 | 4 | 8 | 0 | 0.3333 | 0.849 |
| unknown | 3 | 1 | 2 | 0 | 0.3333 | 0.4296 |

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

174 rationales audited.

| metric | value | direction | target |
|---|---:|---|---|
| rationale fabrications | 0.092 | LOWER is better | < 0.05 |
| rationale slot omissions | 0.000 | LOWER is better | < 0.40 |
| rationale fact recall | 1.000 | higher is better | > 0.85 |
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
  sari                       100   +1    42.123    32.898   +9.225     [+5.58, +13.17]   0.0000  0.0000*  +0.51
  bertscore_f1               100   +1     0.670     0.605   +0.065      [+0.04, +0.09]   0.0000  0.0001*  +0.48
  fkgl_drop                  100   +1     4.470     3.301   +1.169      [+0.65, +1.71]   0.0000  0.0000*  +0.56
  smog_drop                  100   +1     4.423     2.907   +1.516      [+0.77, +2.28]   0.0001  0.0003*  +0.58
  coleman_liau_drop          100   +1     5.049     4.380   +0.669      [+0.03, +1.31]   0.0045  0.0084*  +0.31
  nli_faithfulness           100   +1     0.804     0.844   -0.040      [-0.10, +0.03]   0.9758   1.0000  -0.23
  nli_completeness           100   +1     0.760     0.895   -0.135      [-0.19, -0.08]   1.0000   1.0000  -0.62
  human_edit_recall           99   +1     0.955     0.706   +0.250      [+0.17, +0.34]   0.0000  0.0000*  +0.92
  replacement_precision       84   +1     0.655     0.643   +0.012      [-0.10, +0.12]   0.4307   0.6998  +0.05
  replacement_f1              99   +1     0.670     0.496   +0.173      [+0.07, +0.28]   0.0010  0.0022*  +0.51
  critical_error             100   -1     0.120     0.100   +0.020      [-0.02, +0.06]   0.6491   0.8439  -0.50
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.821     0.857   -0.036      [-0.21, +0.11]   0.5135   0.7417  -0.33
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.300     0.200   +0.100      [+0.00, +0.30]   1.0000   1.0000  -1.00

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

```

====================================================================================================
  PAIRED COMPARISON   grounded  vs  termonly
====================================================================================================
  Wilcoxon one-sided ('grounded' better), paired bootstrap 95% CI, rank-biserial effect size.
  14 tests -> Benjamini-Hochberg FDR at alpha=0.05. Report p_adj, not p.

  metric                       n  dir  grounded  termonly     diff              95% CI        p    p_adj    rbc
  ------------------------------------------------------------------------------------------------
  sari                       100   +1    40.895    42.123   -1.228      [-3.27, +0.75]   0.8973   1.0000  -0.17
  bertscore_f1               100   +1     0.649     0.670   -0.021      [-0.04, -0.01]   0.9942   1.0000  -0.33
  fkgl_drop                  100   +1     4.328     4.470   -0.142      [-0.52, +0.28]   0.9337   1.0000  -0.20
  smog_drop                  100   +1     4.039     4.423   -0.384      [-0.88, +0.09]   0.8784   1.0000  -0.33
  coleman_liau_drop          100   +1     4.915     5.049   -0.134      [-0.58, +0.47]   0.9567   1.0000  -0.23
  nli_faithfulness           100   +1     0.789     0.804   -0.015      [-0.06, +0.03]   0.9889   1.0000  -0.30
  nli_completeness           100   +1     0.738     0.760   -0.022      [-0.07, +0.03]   0.9079   1.0000  -0.21
  human_edit_recall           99   +1     0.987     0.955   +0.031      [+0.00, +0.07]   0.2811   1.0000  +0.87
  replacement_precision       98   +1     0.694     0.684   +0.010      [-0.07, +0.09]   0.4317   1.0000  +0.06
  replacement_f1              99   +1     0.692     0.670   +0.022      [-0.06, +0.10]   0.3599   1.0000  +0.17
  critical_error             100   -1     0.110     0.120   -0.010      [-0.05, +0.02]   0.4234   1.0000  +0.33
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.821   +0.071      [+0.00, +0.21]   0.3138   1.0000  +1.00
  diagnostic_identity_preservation   5   +1     0.800     1.000   -0.200      [-0.60, +0.00]   1.0000   1.0000  -1.00
  severity_downgrade          10   -1     0.200     0.300   -0.100      [-0.30, +0.00]   0.5000   1.0000  +1.00

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

```

====================================================================================================
  PAIRED COMPARISON   grounded  vs  naive
====================================================================================================
  Wilcoxon one-sided ('grounded' better), paired bootstrap 95% CI, rank-biserial effect size.
  13 tests -> Benjamini-Hochberg FDR at alpha=0.05. Report p_adj, not p.

  metric                       n  dir  grounded     naive     diff              95% CI        p    p_adj    rbc
  ------------------------------------------------------------------------------------------------
  sari                       100   +1    40.895    32.898   +7.998     [+4.16, +12.21]   0.0002  0.0008*  +0.42
  bertscore_f1               100   +1     0.649     0.605   +0.044      [+0.02, +0.07]   0.0024  0.0063*  +0.33
  fkgl_drop                  100   +1     4.328     3.301   +1.028      [+0.53, +1.53]   0.0000  0.0001*  +0.50
  smog_drop                  100   +1     4.039     2.907   +1.132      [+0.39, +1.88]   0.0034  0.0073*  +0.42
  coleman_liau_drop          100   +1     4.915     4.380   +0.535      [-0.10, +1.17]   0.0150  0.0279*  +0.26
  nli_faithfulness           100   +1     0.789     0.844   -0.055      [-0.12, +0.01]   0.9921   1.0000  -0.28
  nli_completeness           100   +1     0.738     0.895   -0.157      [-0.22, -0.10]   1.0000   1.0000  -0.65
  human_edit_recall           99   +1     0.987     0.706   +0.281      [+0.20, +0.36]   0.0000  0.0000*  +1.00
  replacement_precision       85   +1     0.671     0.635   +0.035      [-0.07, +0.14]   0.3008   0.4533  +0.14
  replacement_f1              99   +1     0.692     0.496   +0.195      [+0.09, +0.30]   0.0003  0.0010*  +0.60
  critical_error             100   -1     0.110     0.100   +0.010      [-0.02, +0.05]   0.5766   0.7496  -0.33
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.857   +0.036      [+0.00, +0.11]   0.3138   0.4533  +1.00
  diagnostic_identity_preservation   5   +1     0.800     1.000   -0.200      [-0.60, +0.00]   1.0000   1.0000  -1.00
  severity_downgrade          10   -1     0.200     0.200   +0.000      [+0.00, +0.00]      n/a      n/a    n/a

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

## Clinical-safety flags

- note 3 / `termonly` / **severity** (warning): lost ['marked']
- note 3 / `grounded` / **severity** (warning): lost ['marked']
- note 5 / `termonly` / **temporality** (warning): lost ['chronic', 'history of']
- note 5 / `grounded` / **temporality** (warning): lost ['chronic', 'history of']
- note 8 / `grounded` / **diagnostic_identity** (critical): lost ['sepsis']
- note 9 / `naive` / **temporality** (warning): lost ['currently']
- note 9 / `naive` / **number_unit** (critical): lost ['1']
- note 9 / `termonly` / **number_unit** (critical): lost ['1']
- note 9 / `grounded` / **number_unit** (critical): lost ['1']
- note 10 / `naive` / **temporality** (warning): lost ['new onset']
- note 10 / `termonly` / **temporality** (warning): lost ['new onset']
- note 10 / `grounded` / **temporality** (warning): lost ['new onset']
- note 11 / `naive` / **temporality** (warning): lost ['history of']
- note 11 / `grounded` / **temporality** (warning): lost ['history of']
- note 26 / `naive` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `termonly` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `termonly` / **temporality** (warning): lost ['acute']
- note 26 / `grounded` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `grounded` / **temporality** (warning): lost ['acute']
- note 27 / `naive` / **temporality** (warning): lost ['past']
- note 28 / `naive` / **uncertainty** (critical): lost ['consideration']
- note 28 / `termonly` / **uncertainty** (critical): lost ['consideration']
- note 28 / `grounded` / **uncertainty** (critical): lost ['consideration']
- note 34 / `termonly` / **temporality** (warning): lost ['history of']
- note 34 / `grounded` / **temporality** (warning): lost ['history of']
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
- note 45 / `naive` / **severity** (warning): lost ['slight']
- note 51 / `naive` / **laterality** (critical): lost ['lateral']
- note 51 / `termonly` / **laterality** (critical): lost ['lateral']
- note 51 / `grounded` / **laterality** (critical): lost ['lateral']
- note 54 / `termonly` / **laterality** (critical): lost ['upper']
- note 56 / `termonly` / **uncertainty** (critical): lost ['possible']
- note 56 / `grounded` / **uncertainty** (critical): lost ['possible']
- note 60 / `naive` / **temporality** (warning): lost ['now']
- note 60 / `termonly` / **temporality** (warning): lost ['now']
- note 60 / `grounded` / **temporality** (warning): lost ['now']
- note 66 / `naive` / **number_unit** (critical): lost ['21']
- note 70 / `termonly` / **laterality** (critical): lost ['bilateral']
- note 70 / `termonly` / **number_unit** (critical): lost ['2']
- note 78 / `naive` / **number_unit** (critical): lost ['1']
- note 78 / `termonly` / **number_unit** (critical): lost ['1']
- note 78 / `grounded` / **number_unit** (critical): lost ['1']
- note 83 / `termonly` / **drug** (policy): lost ['prednisone']
- note 83 / `grounded` / **drug** (policy): lost ['prednisone']
- note 86 / `naive` / **temporality** (warning): lost ['chronic']
- note 86 / `termonly` / **temporality** (warning): lost ['chronic']
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
- **naive** (FKGL 10.8, 23 words, 0 edits): He felt no pleasure and lost interest in social activities, and he had trouble sleeping because he woke up often and felt restless.
    - SARI=20.69  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 10.5, 20 words, 1 edits): He felt no joy and lost interest in social activities, and had trouble sleeping due to frequent waking and restlessness.
    - SARI=30.85  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 11.1, 20 words, 0 edits): He felt no pleasure and lost interest in social activities, and had trouble sleeping due to frequent waking and restlessness.
    - SARI=33.22  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 2 - `18`

- **ORIGINAL**  (FKGL 14.3, 6 words): Myocardial infarction can not be excluded.
- **REFERENCE** (FKGL 4.5, 6 words): Heart attack can not be excluded.
- **naive** (FKGL 3.7, 10 words, 0 edits): It is not possible to rule out a heart attack.
    - SARI=24.27  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 2.3, 7 words, 2 edits): A heart attack cannot be ruled out.
    - SARI=25.97  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 0.8, 8 words, 2 edits): A heart attack might not be ruled out.
    - SARI=34.03  crit=0.00  NLIf=0.71  copyjrg=0.00

### Note 3 - `21`

- **ORIGINAL**  (FKGL 6.0, 10 words): There was marked hematoma and swelling within the subdeltoid bursa.
- **REFERENCE** (FKGL 7.6, 14 words): There was obvious collection of blood and swelling within the side of the shoulder.
- **naive** (FKGL 7.6, 16 words, 0 edits): There was a large collection of blood and swelling inside the sac under the shoulder muscle.
    - SARI=49.87  crit=0.00  NLIf=0.71  copyjrg=0.00
- **termonly** (FKGL 5.0, 14 words, 3 edits): There was a big bruise and swelling inside the sac under the shoulder blade.
    - SARI=41.17  crit=0.00  NLIf=0.71  copyjrg=0.00
- **grounded** (FKGL 4.2, 14 words, 3 edits): There was a big bruise and swelling in the fluid sac near the shoulder.
    - SARI=41.17  crit=0.00  NLIf=0.72  copyjrg=0.00

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
- **naive** (FKGL 8.4, 17 words, 0 edits): She complained of bladder spasms when she urinated and said she has a history of chronic UTIs.
    - SARI=22.80  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 8.0, 20 words, 3 edits): She said her bladder muscles twitched when she peed and she said she has had many long-term bladder infections.
    - SARI=10.35  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 9.9, 21 words, 3 edits): She complained of her pee bladder squeezing tight when she peed and said she has had long-lasting urinary tract infections.
    - SARI=14.31  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 6 - `32`

- **ORIGINAL**  (FKGL 7.2, 10 words): There was no instability of the knee and no effusion.
- **REFERENCE** (FKGL 8.0, 11 words): There was no instability of the knee and no fluid collection.
- **naive** (FKGL 2.3, 9 words, 0 edits): The knee was stable and there was no swelling.
    - SARI=20.32  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.8, 12 words, 2 edits): There was no loose movement in the knee and no fluid buildup.
    - SARI=36.98  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.7, 9 words, 2 edits): The knee was stable and had no fluid buildup.
    - SARI=18.25  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 7 - `64`

- **ORIGINAL**  (FKGL 4.9, 13 words): Two days later, the pain resolved and she has not had a recurrence.
- **REFERENCE** (FKGL 5.0, 14 words): Two days later, the pain got better and she has not had a recurrence.
- **naive** (FKGL 3.6, 15 words, 0 edits): Two days later, the pain went away and she has not had it come back.
    - SARI=46.29  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.1, 14 words, 2 edits): Two days later, the pain stopped and she has not had a flare-up.
    - SARI=53.86  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 2.5, 14 words, 2 edits): Two days later, the pain stopped and she has not had it come back.
    - SARI=46.29  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 8 - `81`

- **ORIGINAL**  (FKGL 14.1, 7 words): Description : Fever, otitis media, and possible sepsis.
- **REFERENCE** (FKGL 15.6, 8 words): Description : Fever, ear infection, and possible general infection.
- **naive** (FKGL 5.8, 12 words, 0 edits): The patient has a fever, an ear infection, and might have sepsis.
    - SARI=37.05  crit=0.00  NLIf=0.82  copyjrg=0.50
- **termonly** (FKGL 10.7, 7 words, 2 edits): Fever, ear infection, and possible blood infection.
    - SARI=61.09  crit=0.00  NLIf=0.70  copyjrg=0.00
- **grounded** (FKGL 12.6, 8 words, 2 edits): Fever, ear infection, and possible severe bloodstream infection.
    - SARI=59.09  crit=1.00  NLIf=0.88  copyjrg=0.00

### Note 9 - `101`

- **ORIGINAL**  (FKGL 7.6, 13 words): Currently, primary complaint is one of fatigue that she feels throughout the day.
- **REFERENCE** (FKGL 8.4, 14 words): Currently, primary complaint is one of feeling tired that she feels throughout the day.
- **naive** (FKGL 0.5, 6 words, 0 edits): She is tired all day long.
    - SARI=14.49  crit=1.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 5.9, 11 words, 2 edits): Currently, her main issue is tiredness that she feels all day.
    - SARI=18.88  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 8.4, 14 words, 2 edits): Currently, her main reason for seeing the doctor is feeling very tired all day.
    - SARI=14.87  crit=1.00  NLIf=0.06  copyjrg=0.00

### Note 10 - `108`

- **ORIGINAL**  (FKGL 12.3, 19 words): He has noted some stool irregularity with occasional loose stools and new onset of pain predominantly in left neck.
- **REFERENCE** (FKGL 12.3, 19 words): He has noted some poop irregularity with occasional loose poop and new onset of pain predominantly in left neck.
- **naive** (FKGL 11.5, 24 words, 0 edits): He has noticed some changes in his bowel movements, including occasional loose stools, and he has started feeling pain mostly in his left neck.
    - SARI=17.02  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 7.8, 18 words, 3 edits): He has noticed some bowel problems with occasional loose stools and new pain mostly in the left neck.
    - SARI=19.78  crit=0.00  NLIf=0.99  copyjrg=0.33
- **grounded** (FKGL 11.1, 18 words, 4 edits): He has noticed some poop irregularity with occasional watery poop and new pain mostly in the left neck.
    - SARI=34.64  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 11 - `143`

- **ORIGINAL**  (FKGL 11.7, 12 words): Description : The patient presents for a followup for history of erythema nodosum.
- **REFERENCE** (FKGL 12.6, 17 words): Description : The patient presents for a followup for history of red, painful tender lumps around fatty areas.
- **naive** (FKGL 9.1, 17 words, 0 edits): The patient is coming back for a checkup because she has had a condition called erythema nodosum.
    - SARI=11.78  crit=0.00  NLIf=0.97  copyjrg=1.00
- **termonly** (FKGL 7.0, 17 words, 1 edits): The patient comes back for a checkup because of a history of red lumps under the skin.
    - SARI=23.58  crit=0.00  NLIf=0.60  copyjrg=0.00
- **grounded** (FKGL 3.7, 11 words, 1 edits): The patient comes back for a checkup about red skin lumps.
    - SARI=18.29  crit=0.00  NLIf=0.52  copyjrg=0.00

### Note 12 - `144`

- **ORIGINAL**  (FKGL 7.5, 22 words): She was iron deficient last year, and with her multiple surgeries and poor p. o. intake, may have become iron deficient again.
- **REFERENCE** (FKGL 12.4, 23 words): She was iron deficient last year, and with her multiple surgeries and poor food and fluid intake, may have become iron deficient again.
- **naive** (FKGL 11.8, 22 words, 0 edits): She was iron deficient last year, and because of her many surgeries and poor eating, she may have become iron deficient again.
    - SARI=39.88  crit=0.00  NLIf=0.03  copyjrg=0.00
- **termonly** (FKGL 10.0, 24 words, 3 edits): She was low in iron last year, and with her multiple surgeries and poor eating by mouth, may have become low in iron again.
    - SARI=36.35  crit=0.00  NLIf=0.07  copyjrg=0.00
- **grounded** (FKGL 9.5, 21 words, 3 edits): She lacked iron last year, and with her many surgeries and poor eating by mouth, may have become iron lacking again.
    - SARI=29.63  crit=0.00  NLIf=0.09  copyjrg=0.00

### Note 13 - `150`

- **ORIGINAL**  (FKGL 9.1, 15 words): We will schedule him for the Holter monitor and refer him back to his cardiologist.
- **REFERENCE** (FKGL 10.6, 16 words): We will schedule him for the continuous heart monitor and refer him back to his cardiologist.
- **naive** (FKGL 8.4, 15 words, 0 edits): We will schedule him for the Holter monitor and send him back to his cardiologist.
    - SARI=27.81  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 5.6, 17 words, 2 edits): We will schedule him for a heart rhythm check and refer him back to his heart doctor.
    - SARI=44.48  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 7.7, 17 words, 2 edits): We will schedule him for a portable heart recorder and refer him back to his heart doctor.
    - SARI=44.48  crit=0.00  NLIf=0.80  copyjrg=0.00

### Note 14 - `161`

- **ORIGINAL**  (FKGL 11.1, 8 words): The patient wished to proceed with operative intervention.
- **REFERENCE** (FKGL 6.7, 8 words): The patient wished to proceed with an operation
- **naive** (FKGL 6.4, 6 words, 0 edits): The patient wanted to have surgery.
    - SARI=20.56  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.4, 6 words, 1 edits): The patient wanted to have surgery.
    - SARI=20.56  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.4, 6 words, 1 edits): The patient wanted to have surgery.
    - SARI=20.56  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 15 - `178`

- **ORIGINAL**  (FKGL 7.2, 10 words): A KUB was obtained showing an abnormal bowel gas pattern.
- **REFERENCE** (FKGL 8.4, 17 words): An x-ray of the kidney, ureter and bladder was obtained showing an abnormal bowel gas pattern.
- **naive** (FKGL 5.0, 14 words, 0 edits): A KUB was taken and showed that the bowel gas pattern was not normal.
    - SARI=15.87  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 5.0, 14 words, 3 edits): A test of the belly was done, showing too much gas in the intestines.
    - SARI=14.59  crit=0.00  NLIf=0.78  copyjrg=0.00
- **grounded** (FKGL 8.4, 11 words, 1 edits): A belly x-ray of the intestines showed unusual air pockets.
    - SARI=16.41  crit=0.00  NLIf=0.32  copyjrg=0.00

### Note 16 - `185`

- **ORIGINAL**  (FKGL 12.3, 19 words): She has been sedated with Ativan and came into the emergency room obtunded and unable to give any history.
- **REFERENCE** (FKGL 12.3, 20 words): She has been sedated with Ativan and came into the emergency room very drowsy and unable to give any history.
- **naive** (FKGL 12.2, 28 words, 0 edits): She has been given Ativan to help her relax, and when she arrived at the emergency room, she was very confused and could not tell anyone what happened.
    - SARI=18.16  crit=0.00  NLIf=0.90  copyjrg=0.00
- **termonly** (FKGL 11.7, 21 words, 2 edits): She was given a calming medicine by vein and came to the emergency room confused and unable to give any history.
    - SARI=27.45  crit=0.00  NLIf=0.52  copyjrg=0.00
- **grounded** (FKGL 11.1, 21 words, 2 edits): She was given Ativan by mouth and came to the emergency room not fully alert and unable to give any history.
    - SARI=27.97  crit=0.00  NLIf=0.42  copyjrg=0.00

### Note 17 - `202`

- **ORIGINAL**  (FKGL 4.4, 15 words): He has no edema now, but has had some mild leg swelling in the past.
- **REFERENCE** (FKGL 3.6, 15 words): He has no swelling now, but has had some mild leg swelling in the past.
- **naive** (FKGL 5.8, 20 words, 0 edits): He does not have swelling in his legs now, but he has had some mild swelling in his legs before.
    - SARI=26.06  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.6, 15 words, 1 edits): He has no swelling now, but has had some mild leg swelling in the past.
    - SARI=91.67  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.8, 12 words, 1 edits): He has no swelling now, but had some mild leg swelling before.
    - SARI=47.71  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 18 - `231`

- **ORIGINAL**  (FKGL 21.0, 3 words): Mild secondary hyperparathyroidism.
- **REFERENCE** (FKGL 14.7, 5 words): Mild secondary hyperactive parathyroid gland
- **naive** (FKGL 12.3, 6 words, 0 edits): The patient has mild secondary hyperparathyroidism.
    - SARI=12.22  crit=0.00  NLIf=0.94  copyjrg=1.00
- **termonly** (FKGL 21.0, 3 words, 0 edits): Mild secondary hyperparathyroidism.
    - SARI=12.22  crit=0.00  NLIf=0.99  copyjrg=1.00
- **grounded** (FKGL 8.2, 10 words, 0 edits): A mild flare-up of the parathyroid gland's overactivity.
    - SARI=26.39  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 19 - `248`

- **ORIGINAL**  (FKGL 10.6, 16 words): Otherwise, a complete review of systems was obtained and was negative except for as mentioned above.
- **REFERENCE** (FKGL 9.8, 16 words): Otherwise, a complete review of systems was obtained and was normal except for as mentioned above.
- **naive** (FKGL 12.3, 21 words, 0 edits): Otherwise, the doctor checked the patient's entire body for other problems, and found nothing except for the issues mentioned above.
    - SARI=13.45  crit=0.00  NLIf=0.14  copyjrg=0.00
- **termonly** (FKGL 9.8, 16 words, 0 edits): Otherwise, the doctor asked about many body parts and found no problems except as mentioned above.
    - SARI=14.98  crit=0.00  NLIf=0.06  copyjrg=0.00
- **grounded** (FKGL 8.5, 13 words, 2 edits): Otherwise, the doctor asked about all body symptoms and found no other problems.
    - SARI=8.02  crit=0.00  NLIf=0.04  copyjrg=0.00

### Note 20 - `277`

- **ORIGINAL**  (FKGL 7.6, 16 words): Symptoms are worse when sitting for any length of time, such as driving a motor vehicle.
- **REFERENCE** (FKGL 5.2, 15 words): Symptoms are worse when sitting for any length of time, such as driving a car.
- **naive** (FKGL 5.2, 15 words, 0 edits): The patient feels worse after sitting for a long time, like when driving a car.
    - SARI=17.94  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.2, 15 words, 1 edits): Symptoms are worse when sitting for any length of time, such as driving a car.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.2, 15 words, 1 edits): Symptoms are worse when sitting for any length of time, such as driving a car.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 21 - `290`

- **ORIGINAL**  (FKGL 12.8, 9 words): Forearm, elbow and shoulder exams reveal no neurologic compromise.
- **REFERENCE** (FKGL 7.6, 9 words): Forearm, elbow and shoulder exams reveal no nerve problems
- **naive** (FKGL 5.8, 13 words, 0 edits): Exams of the forearm, elbow, and shoulder show no problems with the nerves.
    - SARI=38.98  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 7.6, 9 words, 1 edits): Forearm, elbow and shoulder exams reveal no nerve damage.
    - SARI=83.33  crit=0.00  NLIf=0.90  copyjrg=0.00
- **grounded** (FKGL 7.6, 9 words, 1 edits): Forearm, elbow and shoulder exams reveal no nerve problems.
    - SARI=100.00  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 22 - `296`

- **ORIGINAL**  (FKGL 13.7, 12 words): Thereafter, the local anesthesia was injected into the area around the tumor.
- **REFERENCE** (FKGL 11.7, 12 words): Thereafter, the numbing agent was injected into the area around the tumor.
- **naive** (FKGL 12.6, 14 words, 0 edits): After that, the doctor injected the local anesthesia into the area around the tumor.
    - SARI=37.17  crit=0.00  NLIf=0.50  copyjrg=1.00
- **termonly** (FKGL 10.4, 13 words, 2 edits): After that, the numbing medicine was injected into the area around the growth.
    - SARI=56.27  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 10.4, 13 words, 2 edits): After that, the numbing medicine was injected into the area around the lump.
    - SARI=56.27  crit=0.00  NLIf=0.80  copyjrg=0.00

### Note 23 - `307`

- **ORIGINAL**  (FKGL 3.7, 11 words): There is no numbness or paresthesias in the hand or arm.
- **REFERENCE** (FKGL 5.8, 12 words): There is no numbness or abnormal sensation in the hand or arm.
- **naive** (FKGL 3.7, 11 words, 0 edits): There is no numbness or tingling in the hand or arm.
    - SARI=66.67  crit=0.00  NLIf=0.95  copyjrg=0.00
- **termonly** (FKGL 3.7, 11 words, 1 edits): There is no numbness or tingling in the hand or arm.
    - SARI=66.67  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 3.7, 11 words, 1 edits): There is no numbness or tingling in the hand or arm.
    - SARI=66.67  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 24 - `357`

- **ORIGINAL**  (FKGL 7.6, 16 words): I do not think she has an obvious current abscessed lesion, although there is some drainage.
- **REFERENCE** (FKGL 7.7, 17 words): I do not think she has an obvious current collection of pus, although there is some drainage.
- **naive** (FKGL 6.1, 16 words, 0 edits): I do not think she has an obvious abscess right now, although there is some drainage.
    - SARI=57.08  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 7.8, 19 words, 2 edits): I do not think she has an obvious current pus-filled sore, although there is some fluid coming out.
    - SARI=58.94  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 8.5, 18 words, 2 edits): I do not think she has an obvious current infected sore, although there is some fluid leaking out.
    - SARI=57.08  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 25 - `358`

- **ORIGINAL**  (FKGL 9.1, 11 words): At this time, we would rehydrate with intravenous fluids and reassess.
- **REFERENCE** (FKGL 5.8, 13 words): At this time, we would rehydrate with fluids through the vein and reassess.
- **naive** (FKGL 3.1, 13 words, 0 edits): At this time, we would give fluids through an IV and check again.
    - SARI=45.22  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 2.9, 12 words, 2 edits): At this time, we would give fluids by vein and check again.
    - SARI=45.56  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 2.9, 12 words, 2 edits): At this time, we would give fluids by vein and check again.
    - SARI=45.56  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 26 - `380`

- **ORIGINAL**  (FKGL 14.3, 6 words): Findings are compatible with acute appendicitis.
- **REFERENCE** (FKGL 12.8, 9 words): Findings are compatible with acute inflammation of the appendix
- **naive** (FKGL 8.4, 10 words, 0 edits): The test results match what is expected for acute appendicitis.
    - SARI=8.63  crit=1.00  NLIf=0.97  copyjrg=1.00
- **termonly** (FKGL 8.9, 9 words, 1 edits): The signs show a sudden attack of appendix inflammation.
    - SARI=13.04  crit=1.00  NLIf=0.46  copyjrg=0.00
- **grounded** (FKGL 7.2, 11 words, 3 edits): The test results show a sudden flare-up of swollen appendix.
    - SARI=11.25  crit=1.00  NLIf=0.49  copyjrg=0.00

### Note 27 - `391`

- **ORIGINAL**  (FKGL 10.5, 18 words): She denies weight loss, but acknowledged decreased appetite and increased generalized fatigue for the past 3-4 months.
- **REFERENCE** (FKGL 10.5, 18 words): She denies weight loss, but acknowledged reduced appetite and more generalized tiredness for the past 3-4 months.
- **naive** (FKGL 10.8, 30 words, 0 edits): She says she has not lost weight, but she admitted she has had less of an appetite and more tiredness all over her body for the last 3-4 months.
    - SARI=32.16  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 8.0, 23 words, 1 edits): She says she has not lost weight, but admitted feeling very tired and not wanting to eat for the past 3-4 months.
    - SARI=42.08  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 8.0, 23 words, 3 edits): She says she did not lose weight, but admitted feeling tired all over and wanting less food for the past 3-4 months.
    - SARI=42.08  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 28 - `392`

- **ORIGINAL**  (FKGL 21.8, 5 words): Consideration given to completion thyroidectomy.
- **REFERENCE** (FKGL 11.5, 9 words): Consideration given to remove remaining parts of the thyroid
- **naive** (FKGL 10.2, 9 words, 0 edits): The doctors are thinking about finishing the thyroid removal.
    - SARI=24.96  crit=1.00  NLIf=0.61  copyjrg=0.00
- **termonly** (FKGL 8.0, 11 words, 0 edits): The doctors thought about finishing the removal of the thyroid gland.
    - SARI=27.92  crit=1.00  NLIf=0.48  copyjrg=0.00
- **grounded** (FKGL 8.8, 12 words, 0 edits): The doctors thought about finishing the surgery to remove the thyroid gland.
    - SARI=31.68  crit=1.00  NLIf=0.42  copyjrg=0.00

### Note 29 - `394`

- **ORIGINAL**  (FKGL 10.5, 19 words): She notes that she had epistaxis a few days ago, requiring nasal packing and fortunately that had resolved now.
- **REFERENCE** (FKGL 9.5, 21 words): She notes that she had a nose bleed a few days ago, requiring nose packing and fortunately that had resolved now.
- **naive** (FKGL 6.6, 21 words, 0 edits): She says she had a nosebleed a few days ago that needed packing in her nose, but it is now gone.
    - SARI=30.14  crit=0.00  NLIf=0.95  copyjrg=0.00
- **termonly** (FKGL 5.5, 19 words, 3 edits): She had a nosebleed a few days ago, needed a cloth to stop it, and it is now stopped.
    - SARI=27.49  crit=0.00  NLIf=0.90  copyjrg=0.00
- **grounded** (FKGL 6.1, 21 words, 3 edits): She had a nosebleed a few days ago, needed help with her nose to stop it, and it is now stopped.
    - SARI=28.63  crit=0.00  NLIf=0.85  copyjrg=0.00

### Note 30 - `396`

- **ORIGINAL**  (FKGL 8.9, 9 words): I also explained to the patient about conscious sedation.
- **REFERENCE** (FKGL 8.9, 9 words): I also explained to the patient about awake sedation.
- **naive** (FKGL 8.2, 8 words, 0 edits): I also told the patient about conscious sedation.
    - SARI=13.30  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 4.8, 10 words, 1 edits): I also explained to the patient about a light sleep.
    - SARI=61.94  crit=0.00  NLIf=0.26  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 1 edits): I also explained to the patient about light sleep.
    - SARI=61.94  crit=0.00  NLIf=0.04  copyjrg=0.00

### Note 31 - `762`

- **ORIGINAL**  (FKGL 5.2, 8 words): Palpation of her right knee reveals no crepitus.
- **REFERENCE** (FKGL 5.0, 9 words): Feeling of her right knee reveals no crunchy feeling.
- **naive** (FKGL 3.7, 9 words, 0 edits): Palpation of her right knee shows no crackling sounds.
    - SARI=33.10  crit=0.00  NLIf=0.79  copyjrg=0.50
- **termonly** (FKGL 2.3, 8 words, 1 edits): Touching her right knee shows no crackling sound.
    - SARI=28.93  crit=0.00  NLIf=0.92  copyjrg=0.00
- **grounded** (FKGL 2.3, 8 words, 1 edits): Feeling her right knee shows no crackling sound.
    - SARI=31.71  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 32 - `427`

- **ORIGINAL**  (FKGL 10.1, 14 words): She stepped on ideas, concerns and expectations the evening prior and twisted her ankle.
- **REFERENCE** (FKGL 4.8, 11 words): She stepped on ice the evening prior and twisted her ankle.
- **naive** (FKGL 10.1, 14 words, 0 edits): She stepped on ideas, concerns, and expectations the evening before and twisted her ankle.
    - SARI=19.14  crit=0.00  NLIf=0.99
- **termonly** (FKGL 9.3, 14 words, 1 edits): She stepped on ideas, concerns and expectations the night before and twisted her ankle.
    - SARI=21.81  crit=0.00  NLIf=0.99
- **grounded** (FKGL 9.3, 14 words, 1 edits): She stepped on ideas, concerns and expectations the night before and twisted her ankle.
    - SARI=21.81  crit=0.00  NLIf=0.99

### Note 33 - `439`

- **ORIGINAL**  (FKGL 14.1, 9 words): Modifying Factors : Patient 's condition is aggravated by throwing.
- **REFERENCE** (FKGL 9.6, 10 words): Modifying Factors : Patient 's condition is made worse by throwing.
- **naive** (FKGL 3.8, 9 words, 0 edits): The patient's condition gets worse when they throw.
    - SARI=26.63  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.7, 10 words, 1 edits): The patient's condition gets worse when they throw up.
    - SARI=26.40  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.8, 13 words, 0 edits): Things that change the patient's condition get worse when they throw up.
    - SARI=25.93  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 34 - `451`

- **ORIGINAL**  (FKGL 21.3, 10 words): History of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis and kidney stones.
- **REFERENCE** (FKGL 14.9, 13 words): History of joint inflammation, bone degeneration, underactive thyroid, hay fever and kidney stones.
- **naive** (FKGL 17.7, 14 words, 0 edits): The patient has a history of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis, and kidney stones.
    - SARI=11.57  crit=0.00  NLIf=0.96  copyjrg=1.00
- **termonly** (FKGL 6.3, 17 words, 5 edits): She has had joint pain, weak bones, slow thyroid, runny nose allergies, and stones in her kidneys.
    - SARI=32.60  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 9.8, 23 words, 4 edits): She has had joint pain from worn joints, weak bones that break easily, low thyroid hormone, and hard mineral deposits in her kidneys.
    - SARI=29.70  crit=0.00  NLIf=0.70  copyjrg=0.00

### Note 35 - `465`

- **ORIGINAL**  (FKGL 15.8, 7 words): The ultrasound was negative for intracranial hemorrhage.
- **REFERENCE** (FKGL 6.3, 9 words): The ultrasound was negative for bleeding in the brain.
- **naive** (FKGL 5.2, 8 words, 0 edits): The ultrasound showed no bleeding inside the skull.
    - SARI=24.35  crit=0.00  NLIf=0.93  copyjrg=0.00
- **termonly** (FKGL 5.2, 8 words, 1 edits): The ultrasound showed no bleeding inside the skull.
    - SARI=24.35  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 5.2, 8 words, 1 edits): The ultrasound showed no bleeding inside the brain.
    - SARI=28.10  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 36 - `466`

- **ORIGINAL**  (FKGL 14.7, 12 words): He is status post laparoscopic appendicectomy, and he is tolerating oral diet.
- **REFERENCE** (FKGL 12.3, 15 words): He is status after keyhole surgery to remove appendix, and he is tolerating oral diet.
- **naive** (FKGL 9.9, 15 words, 0 edits): He had his appendix removed using a keyhole surgery, and he is eating food normally.
    - SARI=34.24  crit=0.00  NLIf=0.56  copyjrg=0.00
- **termonly** (FKGL 8.4, 14 words, 0 edits): He had surgery to remove his appendix through small cuts and is eating normally.
    - SARI=27.75  crit=0.00  NLIf=0.77  copyjrg=0.00
- **grounded** (FKGL 8.4, 15 words, 0 edits): He had surgery to remove his appendix through small holes, and he is eating normally.
    - SARI=36.93  crit=0.00  NLIf=0.77  copyjrg=0.00

### Note 37 - `478`

- **ORIGINAL**  (FKGL 8.4, 14 words): We believe that her walking is most likely not being affected by the hydrocephalus.
- **REFERENCE** (FKGL 8.5, 18 words): We believe that her walking is most likely not being affected by the excess fluid in the brain.
- **naive** (FKGL 8.0, 11 words, 0 edits): We think her walking is probably not affected by the hydrocephalus.
    - SARI=12.36  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 7.6, 14 words, 1 edits): We believe her walking is likely not affected by fluid buildup in the brain.
    - SARI=28.03  crit=0.00  NLIf=0.81  copyjrg=0.00
- **grounded** (FKGL 6.8, 15 words, 1 edits): We believe her walking is likely not affected by too much fluid in her brain.
    - SARI=24.08  crit=0.00  NLIf=0.51  copyjrg=0.00

### Note 38 - `505`

- **ORIGINAL**  (FKGL 12.3, 11 words): She noted complaints of fatigue, lightheadedness, and severe dyspnea on exertion.
- **REFERENCE** (FKGL 13.1, 15 words): She noted complaints of tiredness, lightheadedness, and severe shortness of breath on doing anything physical.
- **naive** (FKGL 5.9, 14 words, 0 edits): She said she felt tired, dizzy, and very short of breath when she exercised.
    - SARI=26.55  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 4.9, 13 words, 3 edits): She said she felt very tired, dizzy, and out of breath when active.
    - SARI=26.59  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 4.4, 15 words, 3 edits): She said she felt very tired, dizzy, and out of breath when she worked hard.
    - SARI=26.45  crit=1.00  NLIf=0.97  copyjrg=0.00

### Note 39 - `516`

- **ORIGINAL**  (FKGL 10.9, 14 words): No significant amount of edema associated with these in the dorsum of the hand.
- **REFERENCE** (FKGL 9.3, 14 words): No significant amount of swelling associated with these in the back of the hand.
- **naive** (FKGL 6.7, 14 words, 0 edits): There was no significant swelling on the back of the hand related to these.
    - SARI=39.55  crit=0.00  NLIf=0.90  copyjrg=0.00
- **termonly** (FKGL 0.8, 8 words, 1 edits): No swelling on the back of the hand.
    - SARI=42.30  crit=0.00  NLIf=0.33  copyjrg=0.00
- **grounded** (FKGL 1.0, 9 words, 2 edits): No big swelling on the back of the hand.
    - SARI=40.39  crit=0.00  NLIf=0.66  copyjrg=0.00

### Note 40 - `523`

- **ORIGINAL**  (FKGL 12.3, 5 words): No cardio or pulmonary complaints.
- **REFERENCE** (FKGL 0.5, 5 words): No heart or lung complaints.
- **naive** (FKGL 2.5, 10 words, 0 edits): The patient has no problems with their heart or lungs.
    - SARI=40.17  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 0.5, 5 words, 2 edits): No heart or lung problems.
    - SARI=59.86  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 0.5, 5 words, 2 edits): No heart or lung complaints.
    - SARI=75.00  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 41 - `553`

- **ORIGINAL**  (FKGL 6.9, 11 words): At that time, the Coreg had been held secondary to hypotension.
- **REFERENCE** (FKGL 3.1, 13 words): At that time, the Coreg had been held because of low blood pressure
- **naive** (FKGL 4.4, 15 words, 0 edits): At that time, the Coreg was not used because the patient had low blood pressure.
    - SARI=49.48  crit=0.00  NLIf=0.69  copyjrg=0.00
- **termonly** (FKGL 4.9, 13 words, 3 edits): At that time, the medicine had been stopped because of low blood pressure.
    - SARI=54.48  crit=0.00  NLIf=0.56  copyjrg=0.00
- **grounded** (FKGL 2.6, 11 words, 2 edits): At that time, Coreg was stopped because of low blood pressure.
    - SARI=43.07  crit=0.00  NLIf=0.88  copyjrg=0.00

### Note 42 - `554`

- **ORIGINAL**  (FKGL 12.8, 16 words): Her diarrhea now has settled down and she is having less urinary incontinence, less pedal edema.
- **REFERENCE** (FKGL 8.4, 17 words): Her watery poop now has settled down and she is having less uncontrolled peeing, less foot swelling.
- **naive** (FKGL 10.5, 17 words, 0 edits): Her diarrhea has stopped, and she is having less urinary incontinence and less swelling in her feet.
    - SARI=36.43  crit=0.00  NLIf=0.70  copyjrg=0.67
- **termonly** (FKGL 7.2, 18 words, 3 edits): Her stomach upset has calmed, and she is having less urine leakage and less swelling in her feet.
    - SARI=44.05  crit=0.00  NLIf=0.88  copyjrg=0.00
- **grounded** (FKGL 6.7, 19 words, 3 edits): Her loose stools have settled down, and she is having less trouble holding her pee and less swollen feet.
    - SARI=53.65  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 43 - `556`

- **ORIGINAL**  (FKGL 19.4, 13 words): Description : Nausea and abdominal pain after eating - Gall bladder disease - Laparoscopic cholecystectomy scheduled.
- **REFERENCE** (FKGL 14.4, 18 words): Description : Nausea and abdominal pain after eating - Gall bladder disease - keyhole surgery to remove the gall bladder scheduled.
- **naive** (FKGL 12.3, 19 words, 0 edits): The patient has nausea and abdominal pain after eating, which suggests gall bladder disease. A laparoscopic cholecystectomy is scheduled.
    - SARI=38.81  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 4.1, 27 words, 2 edits): She feels sick and has tummy pain after eating. She has gall bladder disease. The doctor plans a surgery to remove her gall bladder through small cuts.
    - SARI=31.03  crit=0.00  NLIf=0.68  copyjrg=0.00
- **grounded** (FKGL 5.3, 28 words, 0 edits): She feels sick and hurts her belly after eating. She has a problem with her gallbladder. The doctor plans a surgery to remove it using a small camera.
    - SARI=18.01  crit=0.00  NLIf=0.66  copyjrg=0.00

### Note 44 - `618`

- **ORIGINAL**  (FKGL 12.3, 20 words): She states that she has underlying history of heart disease but is not able to elaborate to any significant extent.
- **REFERENCE** (FKGL 12.3, 22 words): She states that she has underlying history of heart disease but is not able to go into detail to any significant extent.
- **naive** (FKGL 6.9, 16 words, 0 edits): She says she has a history of heart disease, but she cannot explain much about it.
    - SARI=19.50  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.8, 12 words, 3 edits): She says she has a past heart problem but cannot explain much.
    - SARI=9.23  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.8, 12 words, 3 edits): She says she has a past heart problem but cannot explain much.
    - SARI=9.23  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 45 - `661`

- **ORIGINAL**  (FKGL 6.5, 18 words): There was some slight edema of the fourth digit, on which he still is wearing his wedding band.
- **REFERENCE** (FKGL 5.9, 18 words): There was some slight swelling of the fourth finger, on which he still is wearing his wedding band.
- **naive** (FKGL 5.4, 16 words, 0 edits): There was a little swelling on his fourth finger, where he still wears his wedding ring.
    - SARI=25.04  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 4.4, 15 words, 2 edits): There was slight swelling on his fourth finger, where he still wears his wedding ring.
    - SARI=27.91  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 4.4, 15 words, 2 edits): There was slight swelling on his fourth finger, where he still wears his wedding band.
    - SARI=32.21  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 46 - `669`

- **ORIGINAL**  (FKGL 12.8, 21 words): Parents do state that she does appear to breathe rapidly, tires somewhat with the feeding with increased respiratory effort and diaphoresis.
- **REFERENCE** (FKGL 10.0, 21 words): Parents do state that she does appear to breathe quickly, tires somewhat with the feeding with increased breathing effort and sweating.
- **naive** (FKGL 8.5, 24 words, 0 edits): Parents say that she seems to breathe quickly, gets tired a bit while eating, and shows signs of working hard to breathe and sweating.
    - SARI=20.64  crit=0.00  NLIf=0.84  copyjrg=0.00
- **termonly** (FKGL 4.9, 13 words, 3 edits): Parents say she breathes fast, gets tired feeding, and sweats while breathing hard.
    - SARI=14.75  crit=0.00  NLIf=0.13  copyjrg=0.00
- **grounded** (FKGL 7.6, 15 words, 2 edits): Parents say she breathes quickly, gets tired while eating, and sweats heavily while breathing hard.
    - SARI=15.01  crit=0.00  NLIf=0.04  copyjrg=0.00

### Note 47 - `673`

- **ORIGINAL**  (FKGL 11.3, 26 words): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had onset of chest pain this evening.
- **REFERENCE** (FKGL 10.5, 24 words): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had chest pain this evening.
- **naive** (FKGL 8.8, 23 words, 0 edits): The patient says he has not used amphetamines for at least four to five months, but he started having chest pain this evening.
    - SARI=37.20  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 11.3, 26 words, 0 edits): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had onset of chest pain this evening.
    - SARI=30.69  crit=0.00  NLIf=0.99  copyjrg=1.00
- **grounded** (FKGL 10.9, 28 words, 2 edits): The patient has not used a stimulant for at least four to five months, according to the patient; however, he had the start of chest pain this evening.
    - SARI=46.93  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 48 - `675`

- **ORIGINAL**  (FKGL 8.4, 10 words): Orogastric suction carried out with only scant clear stomach contents.
- **REFERENCE** (FKGL 7.6, 16 words): Suction of stomach through the mouth carried out with only a small amount clear stomach contents
- **naive** (FKGL 8.7, 21 words, 0 edits): A tube was placed in the patient's mouth to remove stomach contents, but there was very little clear liquid inside.
    - SARI=28.31  crit=0.00  NLIf=0.79  copyjrg=0.00
- **termonly** (FKGL 5.8, 13 words, 0 edits): A tube through the mouth removed very little clear liquid from the stomach.
    - SARI=27.67  crit=0.00  NLIf=0.92  copyjrg=0.00
- **grounded** (FKGL 5.0, 14 words, 0 edits): A tube through the mouth pulled out very little clear liquid from the stomach.
    - SARI=29.08  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 49 - `680`

- **ORIGINAL**  (FKGL 11.5, 9 words): Probably there is some restrictive element because of fibrosis.
- **REFERENCE** (FKGL 10.2, 11 words): Probably there is some restrictive element because of scarring of tissues.
- **naive** (FKGL 8.9, 9 words, 0 edits): There is likely a restrictive problem because of fibrosis.
    - SARI=10.67  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 6.8, 12 words, 2 edits): Probably there is some trouble breathing because of scarring in the lungs.
    - SARI=33.61  crit=0.00  NLIf=0.18  copyjrg=0.00
- **grounded** (FKGL 5.8, 12 words, 1 edits): Probably there is some thick, scarred tissue limiting how the lungs work.
    - SARI=24.17  crit=0.00  NLIf=0.07  copyjrg=0.00

### Note 50 - `681`

- **ORIGINAL**  (FKGL 10.2, 9 words): The uterus was placed back into the abdominal cavity.
- **REFERENCE** (FKGL 3.8, 8 words): The womb was placed back into the abdomen
- **naive** (FKGL 6.3, 9 words, 0 edits): The doctor put the uterus back inside the belly.
    - SARI=22.22  crit=0.00  NLIf=0.62  copyjrg=0.50
- **termonly** (FKGL 2.3, 8 words, 2 edits): The womb was put back into the belly.
    - SARI=49.80  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 2 edits): The womb was placed back into the belly area.
    - SARI=84.29  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 51 - `682`

- **ORIGINAL**  (FKGL 5.0, 9 words): This was viewed on the AP and lateral projections.
- **REFERENCE** (FKGL -0.7, 8 words): This was viewed from the front and sides.
- **naive** (FKGL 1.3, 11 words, 0 edits): The X-rays were taken from the front and side views.
    - SARI=41.28  crit=1.00  NLIf=0.34  copyjrg=0.00
- **termonly** (FKGL -0.3, 9 words, 2 edits): This was viewed on the front and side views.
    - SARI=58.96  crit=1.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 2.3, 11 words, 2 edits): This was viewed on the front-to-back and side views.
    - SARI=54.23  crit=1.00  NLIf=0.91  copyjrg=0.00

### Note 52 - `686`

- **ORIGINAL**  (FKGL 8.2, 8 words): The cords move normally with phonation and ventilation.
- **REFERENCE** (FKGL 5.2, 8 words): The cords move normally when speaking and breathing
- **naive** (FKGL 4.8, 11 words, 0 edits): The vocal cords move normally when the patient speaks or breathes.
    - SARI=51.90  crit=0.00  NLIf=0.92  copyjrg=0.00
- **termonly** (FKGL 6.0, 10 words, 2 edits): The vocal cords move normally when breathing and making sound.
    - SARI=57.60  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 6.3, 9 words, 2 edits): The vocal cords move normally when speaking and breathing.
    - SARI=76.03  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 53 - `688`

- **ORIGINAL**  (FKGL 7.6, 13 words): Once the abdomen was opened, there was noted to be gross purulent drainage.
- **REFERENCE** (FKGL 6.0, 15 words): Once the abdomen was opened, there was noted to be a lot of pus draining.
- **naive** (FKGL 6.8, 16 words, 0 edits): Once the abdomen was opened, there was a lot of thick, pus-like fluid coming out.
    - SARI=51.00  crit=0.00  NLIf=0.87  copyjrg=0.00
- **termonly** (FKGL 4.9, 14 words, 2 edits): Once the belly was opened, there was a lot of thick, pus-like fluid.
    - SARI=37.67  crit=0.00  NLIf=0.88  copyjrg=0.00
- **grounded** (FKGL 3.7, 9 words, 2 edits): Once the belly was opened, pus was leaking out.
    - SARI=20.84  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 54 - `692`

- **ORIGINAL**  (FKGL 4.0, 13 words): Once all four ports were placed, the right upper quadrant was then explored.
- **REFERENCE** (FKGL 5.4, 16 words): Once all four tubes were placed, the top right corner of her abdomen was then explored.
- **naive** (FKGL 5.6, 17 words, 0 edits): Once all four ports were placed, the doctor looked inside the right upper part of the belly.
    - SARI=37.24  crit=0.00  NLIf=0.25  copyjrg=0.50
- **termonly** (FKGL 5.2, 18 words, 3 edits): Once all four tubes were placed, the area on the right side of the belly was then checked.
    - SARI=59.05  crit=1.00  NLIf=0.88  copyjrg=0.00
- **grounded** (FKGL 5.9, 18 words, 1 edits): Once all four ports were placed, the doctor then looked inside the upper right part of the belly.
    - SARI=41.39  crit=0.00  NLIf=0.22  copyjrg=0.25

### Note 55 - `693`

- **ORIGINAL**  (FKGL 15.4, 15 words): Options such as watchful waiting, robotic prostatectomy, seed implantation with and without radiation were discussed.
- **REFERENCE** (FKGL 11.8, 23 words): Options such as watch and wait, removing the prostate with the help of a robot, seed implantation with and without radiation were discussed.
- **naive** (FKGL 15.6, 28 words, 0 edits): The doctor talked about different choices, like watching and waiting, having a robotic surgery to remove the prostate, or putting seeds in the prostate with or without radiation.
    - SARI=22.50  crit=0.00  NLIf=0.44  copyjrg=0.00
- **termonly** (FKGL 10.1, 14 words, 3 edits): The doctor talked about waiting, surgery, and putting seeds in, with or without radiation.
    - SARI=21.17  crit=0.00  NLIf=0.27  copyjrg=0.00
- **grounded** (FKGL 14.3, 29 words, 4 edits): Options like waiting to see if symptoms change, a surgery to remove the prostate, and placing small devices inside the body with or without high-energy rays were discussed.
    - SARI=24.40  crit=0.00  NLIf=0.91  copyjrg=0.00

### Note 56 - `695`

- **ORIGINAL**  (FKGL 14.3, 10 words): He also reportedly was on Lasix prior to hospitalization, possible
- **REFERENCE** (FKGL 11.5, 15 words): He also was reportedly on water pills (lasix) before his admission to the hospital, possible
- **naive** (FKGL 11.3, 13 words, 0 edits): He also reportedly took Lasix before he was admitted to the hospital, possibly.
    - SARI=48.61  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 13.7, 12 words, 2 edits): He also reportedly took a diuretic before being admitted to the hospital.
    - SARI=44.49  crit=1.00  NLIf=0.42  copyjrg=0.00
- **grounded** (FKGL 10.7, 12 words, 2 edits): He also reportedly was on Lasix before being admitted to the hospital.
    - SARI=48.79  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 57 - `697`

- **ORIGINAL**  (FKGL 10.2, 9 words): The four cardiac chambers dimensions are within normal limits.
- **REFERENCE** (FKGL 4.9, 13 words): The sizes of the four parts of the heart are within normal limits.
- **naive** (FKGL 3.7, 9 words, 0 edits): The sizes of the four heart chambers are normal.
    - SARI=47.28  crit=0.00  NLIf=0.97  copyjrg=0.25
- **termonly** (FKGL 2.3, 7 words, 2 edits): The four heart room sizes are normal.
    - SARI=37.42  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL -0.7, 8 words, 2 edits): The four heart rooms are the right size.
    - SARI=32.80  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 58 - `698`

- **ORIGINAL**  (FKGL 11.5, 9 words): Digital rectal examination was performed, which showed no masses.
- **REFERENCE** (FKGL 6.9, 11 words): Examination of the back passage was performed, which showed no lumps.
- **naive** (FKGL 5.8, 14 words, 0 edits): A doctor checked inside the patient's rectum and did not find any lumps.
    - SARI=19.02  crit=0.00  NLIf=0.68  copyjrg=0.00
- **termonly** (FKGL 3.7, 10 words, 2 edits): A doctor felt inside the rectum and found no lumps.
    - SARI=23.48  crit=0.00  NLIf=0.81  copyjrg=0.00
- **grounded** (FKGL 3.7, 10 words, 2 edits): A doctor felt inside the rectum and found no lumps.
    - SARI=23.48  crit=0.00  NLIf=0.81  copyjrg=0.00

### Note 59 - `699`

- **ORIGINAL**  (FKGL 11.2, 23 words): He then had a problem with seizures, hemiparesis, has been to the hospital, developed C-diff, and is in the nursing home currently.
- **REFERENCE** (FKGL 12.0, 29 words): He then had a problem with fits, weakness on one side, has been to the hospital, developed an infection in the gut, and is in the nursing home currently.
- **naive** (FKGL 11.0, 25 words, 0 edits): He then had seizures, weakness on one side of his body, went to the hospital, developed C-diff, and is currently in the nursing home.
    - SARI=36.00  crit=0.00  NLIf=0.98  copyjrg=0.67
- **termonly** (FKGL 13.5, 32 words, 3 edits): He then had a problem with shaking fits, weakness on one side of his body, has been to the hospital, developed a bad gut infection, and is in the nursing home currently.
    - SARI=77.63  crit=0.00  NLIf=0.84  copyjrg=0.00
- **grounded** (FKGL 13.6, 31 words, 3 edits): He then had a problem with jerky movements, weakness on one side of the body, has been to the hospital, developed a gut infection, and is in the nursing home currently.
    - SARI=75.82  crit=0.00  NLIf=0.91  copyjrg=0.00

### Note 60 - `700`

- **ORIGINAL**  (FKGL 12.3, 22 words): He has been on continuous positive airway pressure now for several months, and returns for followup to review his response to treatment.
- **REFERENCE** (FKGL 9.7, 25 words): He has been using a breathing mask now for several months, and returns for follow up to review how he is doing with the treatment.
- **naive** (FKGL 11.6, 25 words, 0 edits): He has been using continuous positive airway pressure for several months and is back for a checkup to see how well the treatment is working.
    - SARI=48.42  crit=0.00  NLIf=0.99  copyjrg=0.83
- **termonly** (FKGL 8.7, 20 words, 2 edits): He has used a breathing machine for several months and returns for a checkup to review his response to treatment.
    - SARI=53.10  crit=0.00  NLIf=0.86  copyjrg=0.00
- **grounded** (FKGL 10.9, 26 words, 2 edits): He has used a breathing machine that pushes air into his lungs for several months, and returns for a checkup to review his response to treatment.
    - SARI=52.45  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 61 - `709`

- **ORIGINAL**  (FKGL 8.5, 18 words): The patient to take small bite and small sips to help decrease the risk of aspiration and penetration.
- **REFERENCE** (FKGL 9.9, 30 words): The patient is to take small bite and small sips to help decrease the risk of having the food or drink going down the wrong pipe and piercing the pipe.
- **naive** (FKGL 8.5, 18 words, 0 edits): The patient should take small bites and small sips to help decrease the risk of aspiration and penetration.
    - SARI=32.39  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 7.0, 20 words, 1 edits): The patient should take small bites and sips to lower the risk of food going into the lungs or airway.
    - SARI=27.56  crit=0.00  NLIf=0.62  copyjrg=0.00
- **grounded** (FKGL 8.0, 22 words, 1 edits): The patient should take small bites and sips to lower the risk of food or liquid going into the lungs by mistake.
    - SARI=27.83  crit=0.00  NLIf=0.56  copyjrg=0.00

### Note 62 - `714`

- **ORIGINAL**  (FKGL 12.3, 15 words): The patient was awakened and extubated and moved to the recovery room in satisfactory condition.
- **REFERENCE** (FKGL 11.1, 20 words): The patient was awakened and tube was removed from the airway and moved to the recovery room in satisfactory condition.
- **naive** (FKGL 8.0, 19 words, 0 edits): The patient woke up, had the breathing tube removed, and was moved to the recovery room in good condition.
    - SARI=36.87  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 7.6, 15 words, 3 edits): The patient woke up, had the breathing tube removed, and went to recovery feeling okay.
    - SARI=16.13  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 7.6, 15 words, 3 edits): The patient woke up, had the breathing tube removed, and went to recovery feeling okay.
    - SARI=16.13  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 63 - `721`

- **ORIGINAL**  (FKGL 15.4, 10 words): PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily aroused.
- **REFERENCE** (FKGL 6.7, 8 words): The patient was asleep, but easily woken up.
- **naive** (FKGL 5.8, 13 words, 0 edits): The patient was asleep but woke up easily when someone called their name.
    - SARI=59.74  crit=0.00  NLIf=0.08  copyjrg=0.00
- **termonly** (FKGL 5.2, 8 words, 1 edits): The patient was asleep, but easily woke up.
    - SARI=70.83  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.2, 8 words, 1 edits): The patient was asleep, but woke up easily.
    - SARI=62.05  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 64 - `725`

- **ORIGINAL**  (FKGL 10.9, 26 words): He is to follow up in approximately 10 days for recheck as well as prescription for intended AFOs, which he will need up to 6 months.
- **REFERENCE** (FKGL 11.5, 28 words): He is to come back in approximately 10 days for recheck as well as prescription for intended foot-drop braces, which he will need up to 6 months.
- **naive** (FKGL 9.1, 29 words, 0 edits): He will come back in about 10 days for a checkup and to get a prescription for the AFOs he will need to use for up to 6 months.
    - SARI=29.34  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 8.3, 23 words, 1 edits): He will return in about 10 days for a checkup and new medicine orders, which he will need for up to 6 months.
    - SARI=27.87  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 8.0, 24 words, 2 edits): He will return in about 10 days for a checkup and a prescription for a brace he will need for up to 6 months.
    - SARI=25.97  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 65 - `726`

- **ORIGINAL**  (FKGL 14.1, 8 words): Genitourinary : The external genitalia appeared to be normal.
- **REFERENCE** (FKGL 12.3, 8 words): The penis/vagina/genitals appeared to be normal.
- **naive** (FKGL 8.9, 9 words, 0 edits): Genitourinary: The outside parts of the genitals looked normal.
    - SARI=25.97  crit=0.00  NLIf=0.99  copyjrg=0.25
- **termonly** (FKGL 8.9, 9 words, 1 edits): Genitourinary: The outside parts of the genitals looked normal.
    - SARI=25.97  crit=0.00  NLIf=0.99  copyjrg=0.25
- **grounded** (FKGL 7.4, 7 words, 1 edits): Genitourinary: The outside sex parts looked normal.
    - SARI=23.89  crit=0.00  NLIf=0.98  copyjrg=0.25

### Note 66 - `727`

- **ORIGINAL**  (FKGL 12.2, 13 words): She is postop day 21 of an exploratory laparotomy with ovarian cancer staging.
- **REFERENCE** (FKGL 12.6, 17 words): She is 21 days after an open abdominal operation which explored how widespread the ovarian cancer was.
- **naive** (FKGL 9.4, 14 words, 0 edits): She is on her twenty-first day after surgery to check for ovarian cancer.
    - SARI=46.48  crit=1.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 6.7, 13 words, 1 edits): She is 21 days after her surgery to check her ovaries for cancer.
    - SARI=50.01  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 8.5, 13 words, 2 edits): She is 21 days after surgery to check her belly for ovarian cancer.
    - SARI=55.35  crit=0.00  NLIf=0.56  copyjrg=0.00

### Note 67 - `732`

- **ORIGINAL**  (FKGL 8.5, 13 words): Prescription for prednisone as part of his chemotherapy has been given to him.
- **REFERENCE** (FKGL 7.6, 15 words): Prescription for steroid tablets as part of his cancer treatment has been given to him.
- **naive** (FKGL 9.1, 16 words, 0 edits): A doctor has given him a prescription for prednisone to use as part of his chemotherapy.
    - SARI=32.84  crit=0.00  NLIf=0.60  copyjrg=1.00
- **termonly** (FKGL 6.7, 13 words, 1 edits): A medicine called prednisone for his cancer treatment has been given to him.
    - SARI=57.33  crit=0.00  NLIf=0.98  copyjrg=0.50
- **grounded** (FKGL 6.8, 15 words, 1 edits): A medicine called prednisone, given with drugs to treat cancer, has been prescribed for him.
    - SARI=23.59  crit=0.00  NLIf=0.97  copyjrg=0.50

### Note 68 - `738`

- **ORIGINAL**  (FKGL 9.1, 12 words): Photic stimulation was performed, but no clear-cut photic driving was seen.
- **REFERENCE** (FKGL 12.8, 17 words): Visual stimulation was performed, but no clear-cut changes in electrical activity of the brain was seen.
- **naive** (FKGL 8.3, 22 words, 0 edits): They shined a flashing light in the patient's eyes, but the patient did not show any clear reaction to the flashing.
    - SARI=18.75  crit=0.00  NLIf=0.12  copyjrg=0.00
- **termonly** (FKGL 4.8, 11 words, 0 edits): Light flashes were used, but no obvious brain response was seen.
    - SARI=26.44  crit=0.00  NLIf=0.81  copyjrg=0.00
- **grounded** (FKGL 5.8, 13 words, 3 edits): They flashed lights at the patient, but no obvious strong reaction was seen.
    - SARI=26.31  crit=0.00  NLIf=0.17  copyjrg=0.00

### Note 69 - `739`

- **ORIGINAL**  (FKGL 15.6, 8 words): FAMILY HISTORY : Both parents died with myocardial infarctions.
- **REFERENCE** (FKGL 8.2, 8 words): Family history: Both parents died with heart attacks.
- **naive** (FKGL 2.5, 6 words, 0 edits): Both parents died from heart attacks.
    - SARI=36.98  crit=0.00  NLIf=0.93  copyjrg=0.00
- **termonly** (FKGL 2.5, 6 words, 1 edits): Both parents died from heart attacks.
    - SARI=36.98  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 2.5, 6 words, 1 edits): Both parents died from heart attacks.
    - SARI=36.98  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 70 - `740`

- **ORIGINAL**  (FKGL 11.2, 11 words): Extremities : 2+ bilateral pitting edema to the level of the knees.
- **REFERENCE** (FKGL 10.1, 28 words): Hands and feet: There is swelling in both feet up to the level of the knees (when pressed, causes an indentation in the skin for a few seconds)
- **naive** (FKGL 5.2, 15 words, 0 edits): The patient has 2+ pitting edema in both legs that goes up to the knees.
    - SARI=31.40  crit=0.00  NLIf=0.88  copyjrg=0.25
- **termonly** (FKGL 1.9, 12 words, 2 edits): Her arms and legs had swollen, soft spots down to the knees.
    - SARI=32.61  crit=1.00  NLIf=0.65  copyjrg=0.00
- **grounded** (FKGL 2.5, 14 words, 1 edits): Both arms and legs have 2+ swelling that leaves a dent to the knees.
    - SARI=33.22  crit=0.00  NLIf=0.62  copyjrg=0.00

### Note 71 - `741`

- **ORIGINAL**  (FKGL 14.3, 10 words): Following questions are mostly involved in a psychosocial donor evaluation.
- **REFERENCE** (FKGL 13.9, 15 words): Following questions are mostly involved in a donor evaluation of their psychological or social states.
- **naive** (FKGL 11.2, 11 words, 0 edits): The questions below are mostly used for a psychosocial donor evaluation.
    - SARI=13.45  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 6.0, 11 words, 1 edits): The questions mostly check the donor's social and mental health.
    - SARI=15.19  crit=0.00  NLIf=0.54  copyjrg=0.00
- **grounded** (FKGL 9.6, 11 words, 1 edits): The questions mostly check the donor's mental and social situation.
    - SARI=15.19  crit=0.00  NLIf=0.76  copyjrg=0.00

### Note 72 - `742`

- **ORIGINAL**  (FKGL 24.1, 5 words): Mild nonmobile descending aortic atherosclerosis.
- **REFERENCE** (FKGL 11.1, 22 words): Mild non-moving hardening of the part of aorta (the largest artery of the body) that goes down the chest and abdomen.
- **naive** (FKGL 9.7, 12 words, 0 edits): The patient has mild atherosclerosis in the aorta that is not moving.
    - SARI=41.56  crit=0.00  NLIf=0.98  copyjrg=0.25
- **termonly** (FKGL 7.6, 17 words, 2 edits): A mild, non-moving plaque buildup in the lower part of the main artery to the body.
    - SARI=48.35  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 3.7, 11 words, 0 edits): Mild plaque buildup in the chest artery that does not move.
    - SARI=44.79  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 73 - `750`

- **ORIGINAL**  (FKGL 6.7, 8 words): The eustachian tube was obstructed with bone wax.
- **REFERENCE** (FKGL 3.1, 13 words): The passage between the nose and the ears was blocked with bone wax.
- **naive** (FKGL 3.8, 8 words, 0 edits): The eustachian tube was blocked with bone wax.
    - SARI=59.31  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL 1.3, 13 words, 3 edits): The tube in the ear was blocked with a paste made of bone.
    - SARI=37.04  crit=0.00  NLIf=0.90  copyjrg=0.00
- **grounded** (FKGL 2.9, 12 words, 3 edits): The tube in the ear was blocked with a hard, sticky substance.
    - SARI=34.66  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 74 - `752`

- **ORIGINAL**  (FKGL 6.3, 9 words): He was placed supine on the operating room table.
- **REFERENCE** (FKGL 7.2, 10 words): He was placed facing upwards on the operating room table.
- **naive** (FKGL 4.8, 11 words, 0 edits): He lay flat on his back on the operating room table.
    - SARI=50.81  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 4.8, 10 words, 1 edits): He was placed face up on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.22  copyjrg=0.00
- **grounded** (FKGL 4.8, 11 words, 1 edits): He was placed on his back on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 75 - `755`

- **ORIGINAL**  (FKGL 7.4, 7 words): A urinalysis was not performed this time.
- **REFERENCE** (FKGL 2.3, 8 words): A urine test was not performed this time.
- **naive** (FKGL 5.7, 7 words, 0 edits): A urinalysis was not done this time.
    - SARI=13.89  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 0.8, 8 words, 2 edits): A urine test was not done this time.
    - SARI=51.60  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 0.8, 8 words, 2 edits): A urine test was not done this time.
    - SARI=51.60  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 76 - `766`

- **ORIGINAL**  (FKGL 12.3, 21 words): Vision and hearing appeared to be adequate for testing, although she did indicate that she needed to update her eyeglass prescription.
- **REFERENCE** (FKGL 11.7, 21 words): Vision and hearing appeared to be okay for testing, although she did indicate that she needed to update her glasses prescription.
- **naive** (FKGL 9.3, 20 words, 0 edits): Her vision and hearing were good enough for the test, but she said she needed to update her eyeglasses prescription.
    - SARI=27.09  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.7, 19 words, 1 edits): Her sight and hearing were good enough for the test, though she said she needed to update her glasses.
    - SARI=28.52  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 8.5, 18 words, 3 edits): Vision and hearing seemed good enough for testing, though she said she needed to update her glasses order.
    - SARI=32.70  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 77 - `771`

- **ORIGINAL**  (FKGL 8.0, 24 words): I have talked to him several times about a colonoscopy, which he has refused, and so we have been doing stools for occult blood.
- **REFERENCE** (FKGL 17.5, 46 words): I have talked to him several times about a procedure to have a look inside the bowels (colonoscopy), which he has refused, and so we have been testing some stool samples in the lab to look for blood (which may be invisible to the naked eye).
- **naive** (FKGL 8.8, 25 words, 0 edits): I have talked to him several times about getting a colonoscopy, but he has refused, so we have been testing his stools for hidden blood.
    - SARI=44.47  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 9.5, 26 words, 3 edits): I have talked to him several times about a colon exam, which he has refused, and so we have been checking his poop for hidden blood.
    - SARI=60.35  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 10.4, 29 words, 3 edits): I have talked to him several times about a test for his large intestine, which he has refused, and so we have been checking his poop for hidden blood.
    - SARI=60.35  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 78 - `783`

- **ORIGINAL**  (FKGL 8.4, 10 words): The knee was copiously irrigated and suction dried once again.
- **REFERENCE** (FKGL 7.6, 16 words): The knee was washed out thoroughly and dried with a suction (or mini-vacuum) once again
- **naive** (FKGL 4.8, 11 words, 0 edits): The knee was washed out thoroughly and dried with suction again.
    - SARI=72.22  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.1, 13 words, 2 edits): The knee was washed with lots of water and dried with a vacuum.
    - SARI=59.65  crit=1.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 3.1, 13 words, 2 edits): The knee was washed with lots of water and cleaned with a vacuum.
    - SARI=54.27  crit=1.00  NLIf=0.87  copyjrg=0.00

### Note 79 - `784`

- **ORIGINAL**  (FKGL 10.9, 14 words): She is not having painful urination, any blood in the urine, frequency or hesitancy.
- **REFERENCE** (FKGL 11.1, 20 words): She is not having painful peeing, any blood in the pee, needing to pee very often or having difficulty peeing.
- **naive** (FKGL 8.1, 20 words, 0 edits): She does not have painful urination, blood in her urine, or the need to go often or have trouble starting.
    - SARI=28.69  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 10.5, 20 words, 2 edits): She is not having painful urination, any blood in the urine, or needing to go often or having trouble starting.
    - SARI=65.25  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 9.1, 18 words, 2 edits): She is not having painful urination, blood in the urine, or peeing too often or with trouble starting.
    - SARI=54.30  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 80 - `789`

- **ORIGINAL**  (FKGL 14.8, 19 words): Cardiovascular : Chest pain in the retrosternal area, Occasional anginal pain and patient describes it as a sensation of tightness.
- **REFERENCE** (FKGL 14.6, 30 words): Heart and blood vessels: Chest pain just behind the breastbone, occasional chest pain when exercising or exerting themselves, which gets better with rest and patient describes it as feeling 'tightness'.
- **naive** (FKGL 14.5, 21 words, 0 edits): Cardiovascular: The patient has chest pain in the area behind the breastbone, occasional anginal pain, and describes the sensation as tightness.
    - SARI=37.54  crit=0.00  NLIf=0.97  copyjrg=0.67
- **termonly** (FKGL 6.8, 12 words, 0 edits): The patient has heart pain behind the breastbone, sometimes feeling like tightness.
    - SARI=33.93  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 8.4, 14 words, 3 edits): The patient has heart and blood vessel pain behind the breastbone, with occasional tightness.
    - SARI=38.20  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 81 - `790`

- **ORIGINAL**  (FKGL 4.8, 11 words): We excised a good bit of his synovium and synovial pouch.
- **REFERENCE** (FKGL 1.9, 12 words): We cut out a bit of the soft tissue of the joint.
- **naive** (FKGL 4.8, 11 words, 0 edits): We removed a large part of his synovium and synovial pouch.
    - SARI=33.06  crit=0.00  NLIf=0.99  copyjrg=0.80
- **termonly** (FKGL 4.4, 15 words, 2 edits): We removed a good bit of his joint lining and the bag inside the joint.
    - SARI=46.38  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 5.2, 15 words, 2 edits): We removed a good bit of the joint lining and the small pocket inside it.
    - SARI=49.80  crit=0.00  NLIf=0.55  copyjrg=0.00

### Note 82 - `801`

- **ORIGINAL**  (FKGL 13.4, 11 words): An inflammatory process such as infection or ischemia must be considered.
- **REFERENCE** (FKGL 10.4, 13 words): An inflammatory process such as infection or reduced blood flow must be considered.
- **naive** (FKGL 9.1, 15 words, 0 edits): An inflammatory process, like an infection or a lack of blood flow, must be considered.
    - SARI=42.04  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.8, 13 words, 2 edits): A flare-up from infection or lack of blood flow must be considered.
    - SARI=33.44  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 4.8, 10 words, 2 edits): An infection or lack of blood flow must be considered.
    - SARI=37.95  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 83 - `804`

- **ORIGINAL**  (FKGL 2.9, 12 words): I have asked her to increase her prednisone when she goes home.
- **REFERENCE** (FKGL 2.9, 12 words): I have asked her to increase her steroid when she goes home.
- **naive** (FKGL 1.9, 12 words, 0 edits): I have asked her to take more prednisone when she goes home.
    - SARI=38.27  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 4.9, 13 words, 1 edits): I have asked her to increase her steroid medicine when she goes home.
    - SARI=79.79  crit=0.00  NLIf=0.02  copyjrg=0.00
- **grounded** (FKGL 4.2, 14 words, 1 edits): I have asked her to increase the medicine she takes when she goes home.
    - SARI=58.08  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 84 - `844`

- **ORIGINAL**  (FKGL 10.2, 9 words): She may need other neuropathic pain medications as needed.
- **REFERENCE** (FKGL 6.3, 9 words): She may need other nerve pain medications as needed.
- **naive** (FKGL 4.0, 13 words, 0 edits): She might need other medicines for nerve pain if she feels like it.
    - SARI=24.25  crit=0.00  NLIf=0.90  copyjrg=0.00
- **termonly** (FKGL 5.0, 9 words, 1 edits): She may need other nerve pain medicines as needed.
    - SARI=64.54  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 1 edits): She may need other nerve pain medicines as needed.
    - SARI=64.54  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 85 - `852`

- **ORIGINAL**  (FKGL 12.4, 7 words): A prophylactic dose of antibiotics was given.
- **REFERENCE** (FKGL 10.7, 7 words): A prevention dose of antibiotics was given.
- **naive** (FKGL 9.6, 10 words, 0 edits): A small dose of antibiotics was given to prevent infection.
    - SARI=66.67  crit=0.00  NLIf=0.95  copyjrg=0.00
- **termonly** (FKGL 7.2, 10 words, 2 edits): A small dose of medicine to prevent infection was given.
    - SARI=28.96  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 9.6, 10 words, 2 edits): A preventive dose of medicine to stop bacteria was given.
    - SARI=28.96  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 86 - `854`

- **ORIGINAL**  (FKGL 16.2, 6 words): Chronic hypokalemia secondary to chronic diarrhea.
- **REFERENCE** (FKGL 7.6, 9 words): Long term low potassium due to long term diarrhea.
- **naive** (FKGL 9.9, 16 words, 0 edits): The patient has had low potassium levels for a long time because of long-term diarrhea.
    - SARI=43.80  crit=0.00  NLIf=0.95  copyjrg=0.00
- **termonly** (FKGL 10.7, 14 words, 2 edits): The patient had a long-term low potassium level caused by long-term diarrhea.
    - SARI=48.51  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 7.6, 15 words, 2 edits): The patient had low blood potassium for a long time because of ongoing loose stools.
    - SARI=33.06  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 87 - `859`

- **ORIGINAL**  (FKGL 6.6, 4 words): No hepatosplenomegaly or tenderness.
- **REFERENCE** (FKGL 2.3, 9 words): No enlarged liver or spleen or pain when pushed.
- **naive** (FKGL 2.6, 11 words, 0 edits): There was no swelling or pain in the liver or spleen.
    - SARI=49.06  crit=0.00  NLIf=0.82  copyjrg=0.00
- **termonly** (FKGL 2.6, 11 words, 1 edits): No swelling of the liver or spleen, or pain when touched.
    - SARI=58.80  crit=0.00  NLIf=0.16  copyjrg=0.00
- **grounded** (FKGL 2.9, 12 words, 1 edits): No swelling of the liver or spleen, and no pain when touched.
    - SARI=49.72  crit=0.00  NLIf=0.04  copyjrg=0.00

### Note 88 - `881`

- **ORIGINAL**  (FKGL 9.1, 11 words): He did not experience his left anterior chest pain with exercise.
- **REFERENCE** (FKGL 5.9, 11 words): He did not experience his left front chest pain with exercise.
- **naive** (FKGL 3.9, 16 words, 0 edits): He did not feel chest pain on the left side of his chest when he exercised.
    - SARI=25.55  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 4.0, 13 words, 2 edits): He did not feel chest pain on his left front side during exercise.
    - SARI=33.92  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 4.2, 14 words, 2 edits): He did not feel pain in the front of his left chest during exercise.
    - SARI=29.17  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 89 - `891`

- **ORIGINAL**  (FKGL 7.6, 9 words): Also, would use it to control the atrial fibrillation.
- **REFERENCE** (FKGL 6.0, 10 words): Also, would use it to control the irregular heart beat
- **naive** (FKGL 8.0, 11 words, 0 edits): Also, the doctor would use it to control the atrial fibrillation.
    - SARI=25.32  crit=0.00  NLIf=0.00  copyjrg=1.00
- **termonly** (FKGL 3.7, 9 words, 1 edits): Also, would use it to control the heart rhythm.
    - SARI=70.00  crit=0.00  NLIf=0.60  copyjrg=0.00
- **grounded** (FKGL 7.2, 11 words, 1 edits): Also, would use it to control the heart's irregular rhythm.
    - SARI=71.43  crit=0.00  NLIf=0.90  copyjrg=0.00

### Note 90 - `900`

- **ORIGINAL**  (FKGL 11.1, 8 words): Overall the patient is a seemingly good historian.
- **REFERENCE** (FKGL 11.9, 10 words): Overall the patient is seemingly good at remembering their history
- **naive** (FKGL 6.0, 15 words, 0 edits): Overall, the patient seems to be a good person to talk to about their health.
    - SARI=39.67  crit=0.00  NLIf=0.02  copyjrg=0.00
- **termonly** (FKGL 5.0, 9 words, 2 edits): Overall the patient seems to tell a good story.
    - SARI=38.28  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 2 edits): Overall the patient seems to tell a clear story.
    - SARI=36.53  crit=0.00  NLIf=0.81  copyjrg=0.00

### Note 91 - `933`

- **ORIGINAL**  (FKGL 3.7, 10 words): No active Crohn 's disease was found during the colonoscopy.
- **REFERENCE** (FKGL 5.9, 14 words): No active Crohn 's disease was found during the camera test through the gut.
- **naive** (FKGL 3.7, 10 words, 0 edits): No active Crohn's disease was found during the colonoscopy.
    - SARI=31.21  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 3.7, 12 words, 1 edits): No flare-up of Crohn's disease was found during the colonoscopy.
    - SARI=26.54  crit=0.00  NLIf=0.99  copyjrg=1.00
- **grounded** (FKGL 6.7, 15 words, 1 edits): The test looking inside the large intestine found no flare-up of Crohn's disease.
    - SARI=19.13  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 92 - `935`

- **ORIGINAL**  (FKGL 16.4, 28 words): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have mounting exhaustion and respiratory distress.
- **REFERENCE** (FKGL 15.5, 28 words): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have worsening exhaustion and breathing distress.
- **naive** (FKGL 11.2, 25 words, 0 edits): Shortly after the nurse first checked the patient, she started complaining of chest pain and seemed to be getting more tired and having trouble breathing.
    - SARI=20.58  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 15.5, 28 words, 2 edits): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have worsening tiredness and trouble breathing.
    - SARI=71.06  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 15.5, 28 words, 2 edits): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have worsening tiredness and trouble breathing.
    - SARI=71.06  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 93 - `968`

- **ORIGINAL**  (FKGL 8.2, 8 words): She has been referred for a pacemaker implantation.
- **REFERENCE** (FKGL 7.6, 9 words): She has been referred for a pacemaker fitting surgery.
- **naive** (FKGL 3.8, 12 words, 0 edits): She has been sent to get a pacemaker put inside her heart.
    - SARI=23.47  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 3.1, 13 words, 2 edits): She has been sent to get a small battery put in her heart.
    - SARI=20.09  crit=0.00  NLIf=0.45  copyjrg=0.00
- **grounded** (FKGL 3.4, 14 words, 2 edits): She has been sent to get a small heart device put inside her chest.
    - SARI=20.09  crit=0.00  NLIf=0.92  copyjrg=0.00

### Note 94 - `116`

- **ORIGINAL**  (FKGL -0.7, 8 words): There was some hematoma at the cath site.
- **REFERENCE** (FKGL 5.8, 13 words): There was some swelling due to collection of blood at the catheter site.
- **naive** (FKGL 6.8, 15 words, 0 edits): There was a small collection of blood at the place where the catheter was inserted.
    - SARI=50.47  crit=0.00  NLIf=0.81  copyjrg=0.00
- **termonly** (FKGL 1.0, 9 words, 2 edits): There was a bruise at the vein access site.
    - SARI=41.74  crit=0.00  NLIf=0.02  copyjrg=0.00
- **grounded** (FKGL 0.8, 8 words, 2 edits): There was a bruise at the needle spot.
    - SARI=39.44  crit=0.00  NLIf=0.02  copyjrg=0.00

### Note 95 - `592`

- **ORIGINAL**  (FKGL 6.3, 9 words): The necrotic tissue was lifted out of the abdomen.
- **REFERENCE** (FKGL 3.7, 9 words): The dead flesh was lifted out of the abdomen.
- **naive** (FKGL 5.0, 10 words, 0 edits): The dead tissue was removed from the patient's belly.
    - SARI=19.93  crit=0.00  NLIf=0.98  copyjrg=0.33
- **termonly** (FKGL 5.0, 9 words, 1 edits): The dead tissue was lifted out of the abdomen.
    - SARI=72.13  crit=0.00  NLIf=0.99  copyjrg=0.33
- **grounded** (FKGL 5.0, 9 words, 1 edits): The dead tissue was lifted out of the abdomen.
    - SARI=72.13  crit=0.00  NLIf=0.99  copyjrg=0.33

### Note 96 - `249`

- **ORIGINAL**  (FKGL 6.7, 8 words): Pressure was held and the area was hemostatic.
- **REFERENCE** (FKGL 5.2, 8 words): Pressure was held and the area stopped bleeding.
- **naive** (FKGL 2.3, 9 words, 0 edits): The pressure was kept on, and the bleeding stopped.
    - SARI=29.21  crit=0.00  NLIf=0.19  copyjrg=0.00
- **termonly** (FKGL 2.3, 7 words, 1 edits): Pressure was held and the bleeding stopped.
    - SARI=57.96  crit=0.00  NLIf=0.34  copyjrg=0.00
- **grounded** (FKGL 2.3, 7 words, 1 edits): Pressure was held and the bleeding stopped.
    - SARI=57.96  crit=0.00  NLIf=0.34  copyjrg=0.00

### Note 97 - `701`

- **ORIGINAL**  (FKGL 3.7, 9 words): The area was lavaged with some saline and cleared.
- **REFERENCE** (FKGL 3.7, 11 words): The area was washed out with some salt water and cleared.
- **naive** (FKGL 3.7, 10 words, 0 edits): The area was washed with some salt water and cleared.
    - SARI=81.54  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.7, 9 words, 2 edits): The area was flushed with salt water and cleared.
    - SARI=63.42  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 5.2, 8 words, 2 edits): The area was cleaned with saltwater and cleared.
    - SARI=52.06  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 98 - `826`

- **ORIGINAL**  (FKGL 8.2, 8 words): Pain and inability to ambulate brought him in.
- **REFERENCE** (FKGL 6.3, 9 words): Pain and inability to move around brought him in.
- **naive** (FKGL 5.0, 9 words, 0 edits): Pain and the inability to walk brought him in.
    - SARI=45.46  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.2, 8 words, 1 edits): Pain and inability to walk brought him in.
    - SARI=66.67  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 2.5, 10 words, 1 edits): Pain and not being able to walk brought him in.
    - SARI=38.11  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 99 - `751`

- **ORIGINAL**  (FKGL 2.3, 8 words): There is a hernia on the left side.
- **REFERENCE** (FKGL 2.9, 12 words): The gut sticks out through the abdomen wall on the left side.
- **naive** (FKGL 2.3, 8 words, 0 edits): There is a hernia on the left side.
    - SARI=17.50  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL -0.7, 8 words, 1 edits): There is a bulge on the left side.
    - SARI=60.64  crit=0.00  NLIf=0.75  copyjrg=0.00
- **grounded** (FKGL -0.7, 8 words, 1 edits): There is a bulge on the left side.
    - SARI=60.64  crit=0.00  NLIf=0.75  copyjrg=0.00

### Note 100 - `496`

- **ORIGINAL**  (FKGL 8.4, 10 words): Other systems were reviewed and were found to be unremarkable.
- **REFERENCE** (FKGL 4.8, 10 words): Other systems were reviewed and were found to be normal.
- **naive** (FKGL 4.0, 14 words, 0 edits): The rest of the patient's body was checked and found to be normal.
    - SARI=21.34  crit=1.00  NLIf=0.10  copyjrg=0.00
- **termonly** (FKGL 3.7, 9 words, 1 edits): Other systems were checked and found to be normal.
    - SARI=39.50  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 1 edits): Other systems were reviewed and found to be normal.
    - SARI=61.95  crit=1.00  NLIf=0.99  copyjrg=0.00
