# together-deepseek-pro - run `run100_20260815_222318`

- model: `deepseek-ai/DeepSeek-V4-Pro` (together, together_chat backend)
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
| **human edit recall** | 99 |  |  | 0.784 | 0.995 | 0.997 | higher is better | > 0.85 | of the jargon the human replaced, how much did we replace |

### 4 faithfulness

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **NLI faithfulness** | 100 |  |  | 0.792 | 0.794 | 0.768 | higher is better | > 0.70 | general-domain MNLI head; absolute values are compressed |
| **NLI completeness** | 100 |  |  | 0.842 | 0.782 | 0.769 | higher is better | > 0.60 | omission is the dominant clinical failure mode, which is why this direction is reported separately |

### 4 readability

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **FKGL drop vs input** | 100 |  |  | 3.73 | 3.69 | 3.33 | higher is better | > +4 grades | gameable by chopping sentences - read with length ratio |
| **Coleman-Liau drop** | 100 |  |  | 4.88 | 4.93 | 5.16 | higher is better | > +4 | none - this is the robustness check on FKGL |
| **length ratio vs reference** | 100 |  |  | 1.13 | 1.09 | 1.13 | descriptive | 0.9-1.3 | descriptive, not a quality score; >1.4 means the model is glossing everything |

### 4 safety

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **critical-error rate** | 100 |  |  | 0.100 | 0.120 | 0.090 | LOWER is better | 0.00 - any value > 0 needs review | fraction of outputs that lost a high-risk slot: negation, uncertainty, laterality, a number/unit, or a drug name |

### 5 attribution

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **attributable rate** | 0.653 | higher is better | > 0.50 | of the edits retrieval demonstrably caused, the fraction with a trustworthy explanation (held-out LDS >= 0.4, clear winner) |
| **held-out LDS (median)** | 0.669 | higher is better | > 0.60 (paper reports 0.6-0.85) | Spearman between the surrogate's predictions and the true log-probs on masks it never saw - how trustworthy the attributions are |
| **helped rate** | 0.446 | descriptive | descriptive - the split is the finding | fraction of edits retrieval made more likely (effect >= 0.10 nats) |
| **hurt rate** | 0.030 | LOWER is better | < 0.10 | fraction of edits retrieval made LESS likely - glossary actively harming the rewrite |
| **top-1 log-prob drop (helped edits)** | 1.45 | higher is better | > 0.5 nats | the paper reports roughly 0.43-0.75 for top-1 across three benchmarks, so this is the number to compare against |
| **winning source is the right term** | 0.960 | higher is better | > 0.80 | the complement is cross-term contamination - the definition of a DIFFERENT word in the same sentence winning the attribution and changing the meaning. Needs no gold labels, which is what makes it the closest thing this family has to a precision score |

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
| **copy-jargon rate** | 99 |  |  | 0.215 | 0.005 | 0.003 | LOWER is better | < 0.10 | exactly 1 - human_edit_recall, by construction: every gold term is either recalled or copied. Report it as a restatement, not as separate evidence, and keep it out of the significance family or one result consumes two FDR slots |
| **reference-vocabulary hit (NOT a precision)** | 91 |  |  | 0.659 | 0.780 | 0.747 | higher is better | descriptive only - see caveat | BROKEN AS NAMED, measured 2026-08-15. The support test is `ref_added & sys_content_words`, and `ref_added` is derived from (reference, original) only - it does not depend on the term being scored. So the same verdict is applied to every changed term in a note and the per-note value can only be 0 or 1. Verified on CLEAN93/qwen3p7-plus: 265 of 265 note-arm values are exactly 0.0 or 1.0, and no note has two terms that disagree. One incidental shared word credits every replacement in the sentence. Making this a real precision needs term-to-replacement span alignment, which does not exist yet. Do not quote it as evidence that replacements were correct |
| **definition borrowing** | 91 |  |  | 0.473 | 0.500 | 0.564 | descriptive | descriptive - the arm gap IS the finding | the mechanism behind the grounded-vs-termonly result, measured per note instead of only in analysis/conditional_grounding.py. Deliberately DESCRIPTIVE: grounded is shown the definitions and the other arms are not, so a difference here is expected by construction and testing it would burn an FDR slot to confirm something guaranteed. Read it as 'how much of the glossary's wording ended up in the output', then read what that cost in human_edit_recall and NLI |
| **replacement F1 (inherits a broken precision)** | 99 |  |  | 0.550 | 0.785 | 0.756 | higher is better | descriptive only - see caveat | DEMOTED from paper tier 2026-08-15. Half of it is replacement_precision, which is not per-term (see its caveat), so this cannot support a claim that the system replaced jargon CORRECTLY. Quote human_edit_recall instead - that half is genuinely per-term and is unaffected |
| **rewrite aggressiveness** | 100 |  |  | 0.368 | 0.157 | 0.147 | descriptive | descriptive | NOT an error rate - legitimate restructuring scores here |

### 4 quality

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **SARI** | 100 |  |  | 31.75 | 43.44 | 44.11 | higher is better | 40-60 typical | the references are MINIMAL-EDIT, so SARI rewards not editing. Measured: a perfect rewrite scored 25.97 vs 22.64 for doing nothing. Report, do not lead with it |
| **BERTScore F1** | 100 |  |  | 0.591 | 0.668 | 0.665 | higher is better | 0.4-0.7 rescaled | read the RESCALED value. Until bug 42 the baseline lookup was silently failing for a local model directory, so raw scores were reported and everything landed in 0.90-0.96 - which is why this metric was demoted for having no dynamic range. Rescaled, the same 5 notes span 0.556-0.620, a gap six times wider. The demotion should be re-examined on the full run |

### 4 readability

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **FKGL (absolute)** | 100 | 10.51 | 8.54 | 6.78 | 6.82 | 7.18 | LOWER is better | 6-8 (US grade) | absolute grade is dominated by sentence length; the DROP is the honest number |
| **Coleman-Liau (absolute)** | 100 | 12.78 | 9.80 | 7.90 | 7.85 | 7.63 | LOWER is better | 6-8 | character-based grade level |
| **Flesch Reading Ease** | 100 | 41.1 | 60.0 | 72.6 | 73.0 | 72.2 | higher is better | 60-80 (plain English) | uses the SAME two inputs as FKGL; not independent evidence |
| **FRE gain** | 100 |  |  | 31.6 | 31.9 | 31.1 | higher is better | > +20 | redundant with fkgl_drop |
| **SMOG** | 100 | 11.49 | 9.83 | 7.64 | 7.90 | 8.19 | LOWER is better | 6-8 | calibrated for 30+ sentence passages; very jumpy on one sentence |
| **SMOG drop** | 100 |  |  | 3.85 | 3.59 | 3.30 | higher is better | > +3 | same single-sentence calibration problem |
| **words out** | 100 | 12.2 | 14.8 | 16.0 | 15.6 | 16.3 | descriptive | close to the reference | output length |

### 4 safety

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **drug-name preservation** | 2 |  |  | 1.000 | 0.000 | 0.000 | higher is better | 1.00 - nothing less is acceptable | APPENDIX because of the DENOMINATOR, not the metric: only 2 of the 93 laymaker notes contain a detected drug name, so the mean is two observations wearing a percentage. Report the cases, not the rate. Also read it against tag_policy - under `replace` the pipeline is INSTRUCTED to drop drug names |
| **diagnostic-identity preservation** | 5 |  |  | 1.000 | 0.800 | 1.000 | higher is better | 1.00 - nothing less is acceptable | scored only over a closed curated table of conditions, and only 4 of 93 notes contain one, so the mean is four observations. An unlisted diagnosis is not scored rather than guessed at, so this under-reports rather than over-reports. Report the cases |
| **severity downgrade rate** | 10 |  |  | 0.200 | 0.200 | 0.100 | LOWER is better | 0.00 | 3-tier ordinal lexicon; lay renderings ('very bad') sit at the same tier as their clinical equivalent so correct paraphrase is not penalised. Appendix on denominator: 10 of 93 notes state a severity at all |
| **number/unit preservation** | 14 |  |  | 0.821 | 0.893 | 0.893 | higher is better | 1.00 | all doses and units survive (spelled-out numbers and expanded unit abbreviations count) |
| **negation preservation** | 24 |  |  | 0.917 | 0.875 | 0.917 | higher is better | 1.00 | type-level, so it cannot see WHICH negation was lost |
| **laterality preservation** | 8 |  |  | 0.812 | 0.812 | 0.812 | higher is better | 1.00 | left/right/bilateral/basal survive (instance-level) |
| **uncertainty preservation** | 9 |  |  | 0.667 | 0.667 | 0.667 | higher is better | 1.00 | hedging survives - 'cannot be excluded' must not become 'is present' |

### 5 attribution

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **LDS optimism gap** | 0.150 | LOWER is better | < 0.15 | a methodological result in its own right, not a quality score |
| **top-1 log-prob drop (all edits)** | 0.25 | higher is better | descriptive | NOT comparable to the paper's Figure 4a. Most edits have no source effect at all, so there is nothing to remove and the drop is ~0 by construction; the median over all edits therefore reads as a failure when the method is working. Quote `top1_drop_median_helped` instead |
| **ablation success rate** | 0.990 | higher is better | 1.00 | scoring calls that returned usable log-probs - a transport health check, not a quality metric |

## Attribution detail (stage 5)

`source_effect = log p(edit | full glossary) - log p(edit | no glossary)`. This is the only measurement in the suite that says whether retrieval *caused* an edit.

| quantity | value | meaning |
|---|---:|---|
| edits attributed | 178 | |
| ranked fits | 168 | a source could be ranked |
| flat fits | 0 | scoring worked, no source mattered - a RESULT, not a failure |
| measurement failures | 10 | aim for 0 |
| **helped** | 75 | retrieval made the edit more likely |
| **neutral** | 88 | the model knew it anyway |
| **hurt** | 5 | retrieval made it LESS likely |
| attributable rate | 0.6533 | of helped edits, those with a trustworthy explanation |
| **winning source is the right term** | 0.96 | of 75 caused edits; the rest are cross-term contamination |
| held-out LDS (median) | 0.669 | aim > 0.60 |
| in-sample LDS (median) | 0.8191 | for contrast only |
| **LDS optimism gap** | 0.1501 | how much an in-sample number would overstate faithfulness |
| edits with no LDS | 49 | glossary too small for a genuinely unseen held-out block |
| **top-1 drop, helped edits** | 1.4454 | paper Eq. 1 over the 75 edits where a source mattered - the number comparable to the paper's Fig. 4a |
| **top-3 drop, helped edits** | 3.3821 | same, removing the top three |
| top-1 drop, ALL edits | 0.2482 | ~0 by construction on the 88 edits with no source effect; do NOT quote this against the paper |
| ablation success | 0.9897 | transport health |

> Surrogate target: **logit-scaled probability**, per ContextCite Algorithm 1 line 4. Bucketing uses the log-probability difference, which answers "would the model have produced this anyway?". Both are stored per edit.

**Threshold sensitivity** (the helped/hurt split depends on an arbitrary cut-off, so it is swept):

| eps (nats) | helped | neutral | hurt | attributable |
|---:|---:|---:|---:|---:|
| 0.05 | 105 | 43 | 20 | 0.581 |
| 0.1 | 98 | 52 | 18 | 0.5918 |
| 0.25 | 87 | 70 | 11 | 0.6322 |
| 0.693 | 75 | 88 | 5 | 0.6533 |
| 1.0 | 67 | 97 | 4 | 0.6716 |

### Does grounding help more on rare terms?

| Zipf stratum | edits | helped | neutral | hurt | helped rate | mean effect (nats) |
|---|---:|---:|---:|---:|---:|---:|
| very_rare | 47 | 23 | 19 | 2 | 0.5227 | 1.7142 |
| rare | 63 | 27 | 30 | 1 | 0.4655 | 2.5215 |
| uncommon | 55 | 22 | 29 | 1 | 0.4231 | 1.802 |
| common | 12 | 2 | 9 | 1 | 0.1667 | 0.5365 |
| unknown | 2 | 1 | 1 | 0 | 0.5 | 3.4588 |

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

179 rationales audited.

| metric | value | direction | target |
|---|---:|---|---|
| rationale fabrications | 0.028 | LOWER is better | < 0.05 |
| rationale slot omissions | 0.006 | LOWER is better | < 0.40 |
| rationale fact recall | 0.984 | higher is better | > 0.85 |
| rationale source correct | 0.961 | higher is better | > 0.95 |
| rationale quote verified | 1.000 | higher is better | 1.00 |
| templated rationales | 0.000 | LOWER is better | < 0.30 |

> **grounding errors** (wrong source, invented quote, wrong number) and **omissions** (a statistic simply not mentioned) are reported separately. v7 merged them into one 42.3% 'hallucination rate' that was almost entirely omissions.

## Paired comparisons

```

====================================================================================================
  PAIRED COMPARISON   termonly  vs  naive
====================================================================================================
  Wilcoxon one-sided ('termonly' better), paired bootstrap 95% CI, rank-biserial effect size.
  14 tests -> Benjamini-Hochberg FDR at alpha=0.05. Report p_adj, not p.

  metric                       n  dir  termonly     naive     diff              95% CI        p    p_adj    rbc
  ------------------------------------------------------------------------------------------------
  sari                       100   +1    43.445    31.745  +11.699     [+8.26, +15.30]   0.0000  0.0000*  +0.72
  bertscore_f1               100   +1     0.668     0.591   +0.077      [+0.05, +0.10]   0.0000  0.0000*  +0.65
  fkgl_drop                  100   +1     3.694     3.732   -0.038      [-0.61, +0.53]   0.3145   0.5504  +0.05
  smog_drop                  100   +1     3.594     3.850   -0.256      [-0.98, +0.47]   0.6982   0.9546  -0.12
  coleman_liau_drop          100   +1     4.932     4.884   +0.048      [-0.53, +0.63]   0.2899   0.5504  +0.06
  nli_faithfulness           100   +1     0.794     0.792   +0.002      [-0.05, +0.06]   0.8386   0.9783  -0.11
  nli_completeness           100   +1     0.782     0.842   -0.060      [-0.12, +0.00]   0.9854   1.0000  -0.25
  human_edit_recall           99   +1     0.995     0.785   +0.210      [+0.14, +0.29]   0.0000  0.0000*  +1.00
  replacement_precision       91   +1     0.780     0.659   +0.121      [+0.04, +0.20]   0.0240   0.0673  +0.73
  replacement_f1              99   +1     0.785     0.550   +0.235      [+0.15, +0.32]   0.0000  0.0000*  +0.85
  critical_error             100   -1     0.120     0.100   +0.020      [-0.02, +0.06]   0.6491   0.9546  -0.50
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.821   +0.071      [+0.00, +0.21]   0.3138   0.5504  +1.00
  diagnostic_identity_preservation   5   +1     0.800     1.000   -0.200      [-0.60, +0.00]   1.0000   1.0000  -1.00
  severity_downgrade          10   -1     0.200     0.200   +0.000      [-0.30, +0.30]   0.7500   0.9546  +0.00

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

```

====================================================================================================
  PAIRED COMPARISON   grounded  vs  termonly
====================================================================================================
  Wilcoxon one-sided ('grounded' better), paired bootstrap 95% CI, rank-biserial effect size.
  13 tests -> Benjamini-Hochberg FDR at alpha=0.05. Report p_adj, not p.

  metric                       n  dir  grounded  termonly     diff              95% CI        p    p_adj    rbc
  ------------------------------------------------------------------------------------------------
  sari                       100   +1    44.110    43.445   +0.665      [-0.93, +2.50]   0.2591   0.9164  +0.10
  bertscore_f1               100   +1     0.665     0.668   -0.003      [-0.02, +0.01]   0.6935   0.9164  -0.06
  fkgl_drop                  100   +1     3.331     3.694   -0.363      [-0.67, -0.08]   0.9920   0.9920  -0.30
  smog_drop                  100   +1     3.298     3.594   -0.296      [-0.70, +0.09]   0.8800   0.9534  -0.38
  coleman_liau_drop          100   +1     5.156     4.932   +0.224      [-0.16, +0.60]   0.2069   0.9164  +0.11
  nli_faithfulness           100   +1     0.768     0.794   -0.025      [-0.07, +0.01]   0.7383   0.9164  -0.09
  nli_completeness           100   +1     0.769     0.782   -0.013      [-0.05, +0.02]   0.7754   0.9164  -0.10
  human_edit_recall           99   +1     0.997     0.995   +0.002      [+0.00, +0.01]   0.4215   0.9164  +1.00
  replacement_precision      100   +1     0.750     0.780   -0.030      [-0.10, +0.04]   0.7019   0.9164  -0.23
  replacement_f1              99   +1     0.756     0.785   -0.029      [-0.10, +0.04]   0.6431   0.9164  -0.22
  critical_error             100   -1     0.090     0.120   -0.030      [-0.07, +0.00]   0.2810   0.9164  +1.00
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.893   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  diagnostic_identity_preservation   5   +1     1.000     0.800   +0.200      [+0.00, +0.60]   0.5000   0.9164  +1.00
  severity_downgrade          10   -1     0.100     0.200   -0.100      [-0.30, +0.00]   0.5000   0.9164  +1.00

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
  sari                       100   +1    44.110    31.745  +12.364     [+8.69, +16.31]   0.0000  0.0000*  +0.74
  bertscore_f1               100   +1     0.665     0.591   +0.074      [+0.05, +0.10]   0.0000  0.0000*  +0.61
  fkgl_drop                  100   +1     3.331     3.732   -0.401      [-0.96, +0.15]   0.8088   0.9604  -0.10
  smog_drop                  100   +1     3.298     3.850   -0.551      [-1.27, +0.16]   0.8865   0.9604  -0.22
  coleman_liau_drop          100   +1     5.156     4.884   +0.272      [-0.29, +0.83]   0.1766   0.3827  +0.11
  nli_faithfulness           100   +1     0.768     0.792   -0.023      [-0.07, +0.03]   0.8735   0.9604  -0.13
  nli_completeness           100   +1     0.769     0.842   -0.073      [-0.14, -0.00]   0.9794   0.9794  -0.23
  human_edit_recall           99   +1     0.997     0.785   +0.212      [+0.14, +0.29]   0.0000  0.0000*  +1.00
  replacement_precision       91   +1     0.747     0.659   +0.088      [+0.01, +0.16]   0.0734   0.1908  +0.57
  replacement_f1              99   +1     0.756     0.550   +0.206      [+0.12, +0.29]   0.0000  0.0002*  +0.76
  critical_error             100   -1     0.090     0.100   -0.010      [-0.03, +0.00]   0.4219   0.6856  +1.00
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.821   +0.071      [+0.00, +0.21]   0.3138   0.5828  +1.00
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.100     0.200   -0.100      [-0.30, +0.00]   0.5000   0.7222  +1.00

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

## Clinical-safety flags

- note 2 / `termonly` / **negation** (critical): lost ['can not be excluded', 'excluded', 'not']
- note 5 / `naive` / **temporality** (warning): lost ['chronic', 'history of']
- note 9 / `naive` / **number_unit** (critical): lost ['1']
- note 9 / `termonly` / **number_unit** (critical): lost ['1']
- note 9 / `grounded` / **number_unit** (critical): lost ['1']
- note 10 / `naive` / **temporality** (warning): lost ['new onset']
- note 10 / `termonly` / **temporality** (warning): lost ['new onset']
- note 10 / `grounded` / **temporality** (warning): lost ['new onset']
- note 17 / `naive` / **severity** (warning): lost ['mild']
- note 24 / `naive` / **severity** (warning): lost ['obvious']
- note 26 / `naive` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `termonly` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `termonly` / **temporality** (warning): lost ['acute']
- note 26 / `grounded` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `grounded` / **temporality** (warning): lost ['acute']
- note 27 / `naive` / **temporality** (warning): lost ['past']
- note 28 / `naive` / **uncertainty** (critical): lost ['consideration']
- note 28 / `termonly` / **uncertainty** (critical): lost ['consideration']
- note 28 / `grounded` / **uncertainty** (critical): lost ['consideration']
- note 36 / `naive` / **temporality** (warning): lost ['status post']
- note 36 / `termonly` / **temporality** (warning): lost ['status post']
- note 36 / `grounded` / **temporality** (warning): lost ['status post']
- note 38 / `naive` / **severity** (warning): lost ['severe']
- note 38 / `termonly` / **severity** (warning): lost ['severe']
- note 38 / `termonly` / **severity_downgrade** (critical): lost ['grave severity stated as mild or absent']
- note 39 / `naive` / **severity** (warning): lost ['significant']
- note 39 / `naive` / **severity_downgrade** (warning): lost ['tier 2']
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
- note 45 / `termonly` / **severity** (warning): lost ['slight']
- note 51 / `naive` / **laterality** (critical): lost ['lateral']
- note 51 / `termonly` / **laterality** (critical): lost ['lateral']
- note 51 / `grounded` / **laterality** (critical): lost ['lateral']
- note 56 / `naive` / **uncertainty** (critical): lost ['possible']
- note 56 / `termonly` / **uncertainty** (critical): lost ['possible']
- note 56 / `grounded` / **uncertainty** (critical): lost ['possible']
- note 60 / `naive` / **temporality** (warning): lost ['now']
- note 60 / `termonly` / **temporality** (warning): lost ['now']
- note 60 / `grounded` / **temporality** (warning): lost ['now']
- note 67 / `termonly` / **drug** (policy): lost ['prednisone']
- note 67 / `grounded` / **drug** (policy): lost ['prednisone']
- note 70 / `naive` / **number_unit** (critical): lost ['2']
- note 70 / `termonly` / **number_unit** (critical): lost ['2']
- note 70 / `grounded` / **number_unit** (critical): lost ['2']
- note 78 / `naive` / **number_unit** (critical): lost ['1']
- note 82 / `termonly` / **diagnostic_identity** (critical): lost ['ischemia']
- note 83 / `termonly` / **drug** (policy): lost ['prednisone']
- note 83 / `grounded` / **drug** (policy): lost ['prednisone']
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
- **naive** (FKGL 6.4, 31 words, 0 edits): He lost interest in things he used to enjoy and did not want to be around other people. He also had trouble sleeping because he woke up often and felt restless.
    - SARI=10.76  crit=0.00  NLIf=0.88  copyjrg=0.00
- **termonly** (FKGL 12.7, 26 words, 2 edits): He lost the ability to feel pleasure and did not care about social activities, and had trouble sleeping because he often woke up and felt restless.
    - SARI=24.34  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 13.2, 26 words, 2 edits): He lost the ability to feel pleasure and was not interested in social activities, and had trouble sleeping because he often woke up and felt restless.
    - SARI=28.47  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 2 - `18`

- **ORIGINAL**  (FKGL 14.3, 6 words): Myocardial infarction can not be excluded.
- **REFERENCE** (FKGL 4.5, 6 words): Heart attack can not be excluded.
- **naive** (FKGL 2.3, 7 words, 0 edits): A heart attack cannot be ruled out.
    - SARI=25.97  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 4.5, 6 words, 1 edits): A heart attack is still possible.
    - SARI=22.38  crit=1.00  NLIf=0.81  copyjrg=0.00
- **grounded** (FKGL 2.3, 7 words, 2 edits): A heart attack cannot be ruled out.
    - SARI=25.97  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 3 - `21`

- **ORIGINAL**  (FKGL 6.0, 10 words): There was marked hematoma and swelling within the subdeltoid bursa.
- **REFERENCE** (FKGL 7.6, 14 words): There was obvious collection of blood and swelling within the side of the shoulder.
- **naive** (FKGL 5.9, 11 words, 0 edits): There was a large bruise and swelling inside the subdeltoid bursa.
    - SARI=34.23  crit=0.00  NLIf=0.98  copyjrg=0.50
- **termonly** (FKGL 7.6, 16 words, 3 edits): There was a large bruise and swelling inside the fluid-filled sac under the shoulder muscle.
    - SARI=40.94  crit=0.00  NLIf=0.76  copyjrg=0.00
- **grounded** (FKGL 7.6, 16 words, 3 edits): There was a large bruise and swelling inside the fluid-filled sac under the shoulder muscle.
    - SARI=40.94  crit=0.00  NLIf=0.76  copyjrg=0.00

### Note 4 - `26`

- **ORIGINAL**  (FKGL 19.4, 5 words): Smoking history, hypertension, and hyperlipidemia.
- **REFERENCE** (FKGL 4.8, 11 words): Smoking history, high blood pressure, and high fat in the blood.
- **naive** (FKGL 7.8, 12 words, 0 edits): She has a history of smoking, high blood pressure, and high cholesterol.
    - SARI=51.08  crit=0.00  NLIf=0.95  copyjrg=0.00
- **termonly** (FKGL 7.8, 12 words, 2 edits): She has a history of smoking, high blood pressure, and high cholesterol.
    - SARI=51.08  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 8.9, 9 words, 2 edits): History of smoking, high blood pressure, and high cholesterol.
    - SARI=53.56  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 5 - `31`

- **ORIGINAL**  (FKGL 8.9, 21 words): She did complain of bladder spasms when she urinated and she did say that she has a history of chronic UTIs.
- **REFERENCE** (FKGL 11.8, 23 words): She did complain of bladder spasms when she urinated and she did say that she has a history of chronic urinary tract infections
- **naive** (FKGL 8.3, 21 words, 0 edits): She said it hurt when she peed because her bladder cramped up, and she also said she often gets bladder infections.
    - SARI=8.98  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 12.9, 28 words, 3 edits): She did complain of sudden painful tightening in her bladder when she passed urine, and she did say that she has a history of long-lasting urine infections.
    - SARI=32.03  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 12.2, 29 words, 3 edits): She did complain of sudden, painful tightening in her pee sac when she passed urine, and she did say that she has a history of long-lasting pee infections.
    - SARI=31.19  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 6 - `32`

- **ORIGINAL**  (FKGL 7.2, 10 words): There was no instability of the knee and no effusion.
- **REFERENCE** (FKGL 8.0, 11 words): There was no instability of the knee and no fluid collection.
- **naive** (FKGL 2.3, 8 words, 0 edits): The knee was stable and had no swelling.
    - SARI=13.62  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 1.0, 9 words, 2 edits): The knee was not loose and had no swelling.
    - SARI=13.62  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 4.8, 10 words, 2 edits): The knee was not wobbly and had no fluid buildup.
    - SARI=17.67  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 7 - `64`

- **ORIGINAL**  (FKGL 4.9, 13 words): Two days later, the pain resolved and she has not had a recurrence.
- **REFERENCE** (FKGL 5.0, 14 words): Two days later, the pain got better and she has not had a recurrence.
- **naive** (FKGL 3.1, 13 words, 0 edits): Two days later, her pain went away and it has not come back.
    - SARI=20.91  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.6, 15 words, 2 edits): Two days later, the pain went away and she has not had it come back.
    - SARI=46.29  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.6, 15 words, 2 edits): Two days later, the pain went away and she has not had it come back.
    - SARI=46.29  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 8 - `81`

- **ORIGINAL**  (FKGL 14.1, 7 words): Description : Fever, otitis media, and possible sepsis.
- **REFERENCE** (FKGL 15.6, 8 words): Description : Fever, ear infection, and possible general infection.
- **naive** (FKGL 10.9, 15 words, 0 edits): The patient has a fever, an ear infection, and possibly a serious body-wide infection.
    - SARI=37.79  crit=0.00  NLIf=0.91  copyjrg=0.00
- **termonly** (FKGL 14.1, 10 words, 2 edits): Description: Fever, middle ear infection, and possible body-wide infection.
    - SARI=60.71  crit=0.00  NLIf=0.69  copyjrg=0.00
- **grounded** (FKGL 11.5, 9 words, 2 edits): Description: Fever, an ear infection, and possible blood infection.
    - SARI=61.87  crit=0.00  NLIf=0.70  copyjrg=0.00

### Note 9 - `101`

- **ORIGINAL**  (FKGL 7.6, 13 words): Currently, primary complaint is one of fatigue that she feels throughout the day.
- **REFERENCE** (FKGL 8.4, 14 words): Currently, primary complaint is one of feeling tired that she feels throughout the day.
- **naive** (FKGL 3.7, 10 words, 0 edits): Her main complaint right now is feeling tired all day.
    - SARI=16.25  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 4.8, 11 words, 2 edits): Right now, her main issue is feeling very tired all day.
    - SARI=13.16  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.7, 10 words, 2 edits): Right now, her main issue is feeling tired all day.
    - SARI=14.86  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 10 - `108`

- **ORIGINAL**  (FKGL 12.3, 19 words): He has noted some stool irregularity with occasional loose stools and new onset of pain predominantly in left neck.
- **REFERENCE** (FKGL 12.3, 19 words): He has noted some poop irregularity with occasional loose poop and new onset of pain predominantly in left neck.
- **naive** (FKGL 7.8, 25 words, 0 edits): He has had some changes in his bowel habits, with loose stools at times, and new pain mostly on the left side of his neck.
    - SARI=18.79  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 10.0, 26 words, 3 edits): He has noticed some change in his bowel pattern with sometimes watery stools and pain that just started, mostly in the left side of his neck.
    - SARI=16.71  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 8.9, 27 words, 3 edits): He has noticed some changes in his poop, with watery poop at times and a new start of pain mostly in the left side of his neck.
    - SARI=21.19  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 11 - `143`

- **ORIGINAL**  (FKGL 11.7, 12 words): Description : The patient presents for a followup for history of erythema nodosum.
- **REFERENCE** (FKGL 12.6, 17 words): Description : The patient presents for a followup for history of red, painful tender lumps around fatty areas.
- **naive** (FKGL 10.7, 23 words, 0 edits): The patient comes in for a follow-up visit about a past problem with red, tender bumps under the skin called erythema nodosum.
    - SARI=13.30  crit=0.00  NLIf=0.08  copyjrg=1.00
- **termonly** (FKGL 7.7, 18 words, 1 edits): The patient comes in for a follow-up for a history of tender red lumps under the skin.
    - SARI=23.09  crit=0.00  NLIf=0.37  copyjrg=0.00
- **grounded** (FKGL 6.9, 17 words, 1 edits): The patient comes for a follow-up for a history of tender red bumps on the shins.
    - SARI=22.19  crit=0.00  NLIf=0.19  copyjrg=0.00

### Note 12 - `144`

- **ORIGINAL**  (FKGL 7.5, 22 words): She was iron deficient last year, and with her multiple surgeries and poor p. o. intake, may have become iron deficient again.
- **REFERENCE** (FKGL 12.4, 23 words): She was iron deficient last year, and with her multiple surgeries and poor food and fluid intake, may have become iron deficient again.
- **naive** (FKGL 5.5, 29 words, 0 edits): She did not have enough iron in her body last year. Because she had several surgeries and did not eat much by mouth, she may have low iron again.
    - SARI=15.41  crit=0.00  NLIf=0.50  copyjrg=0.00
- **termonly** (FKGL 9.7, 25 words, 3 edits): She was low on iron last year, and with her many surgeries and poor intake by mouth, she may have become low on iron again.
    - SARI=29.35  crit=0.00  NLIf=0.05  copyjrg=0.00
- **grounded** (FKGL 10.2, 25 words, 1 edits): She did not have enough iron last year, and with her many surgeries and poor intake by mouth, she may not have enough iron again.
    - SARI=25.31  crit=0.00  NLIf=0.21  copyjrg=0.00

### Note 13 - `150`

- **ORIGINAL**  (FKGL 9.1, 15 words): We will schedule him for the Holter monitor and refer him back to his cardiologist.
- **REFERENCE** (FKGL 10.6, 16 words): We will schedule him for the continuous heart monitor and refer him back to his cardiologist.
- **naive** (FKGL 8.3, 25 words, 0 edits): We will set up a time for him to wear a Holter monitor, which tracks his heartbeat, and send him back to his heart doctor.
    - SARI=22.73  crit=0.00  NLIf=0.80  copyjrg=1.00
- **termonly** (FKGL 6.1, 17 words, 2 edits): We will schedule him for the heart-rhythm recorder and refer him back to his heart doctor.
    - SARI=50.10  crit=0.00  NLIf=0.91  copyjrg=0.00
- **grounded** (FKGL 8.0, 23 words, 2 edits): We will set up a time for him to wear a portable heart-beat recorder and send him back to his heart doctor.
    - SARI=24.96  crit=0.00  NLIf=0.84  copyjrg=0.00

### Note 14 - `161`

- **ORIGINAL**  (FKGL 11.1, 8 words): The patient wished to proceed with operative intervention.
- **REFERENCE** (FKGL 6.7, 8 words): The patient wished to proceed with an operation
- **naive** (FKGL 6.4, 6 words, 0 edits): The patient wanted to have surgery.
    - SARI=20.56  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.2, 8 words, 2 edits): The patient wished to go ahead with surgery.
    - SARI=41.60  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.2, 8 words, 2 edits): The patient wished to go forward with surgery.
    - SARI=41.60  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 15 - `178`

- **ORIGINAL**  (FKGL 7.2, 10 words): A KUB was obtained showing an abnormal bowel gas pattern.
- **REFERENCE** (FKGL 8.4, 17 words): An x-ray of the kidney, ureter and bladder was obtained showing an abnormal bowel gas pattern.
- **naive** (FKGL 6.9, 17 words, 0 edits): A KUB X‑ray was taken and it showed an unusual pattern of gas in the bowel.
    - SARI=16.39  crit=0.00  NLIf=0.18  copyjrg=1.00
- **termonly** (FKGL 7.0, 18 words, 2 edits): An X-ray of the belly was taken and showed an unusual pattern of gas in the gut.
    - SARI=24.99  crit=0.00  NLIf=0.84  copyjrg=0.00
- **grounded** (FKGL 8.4, 18 words, 3 edits): An x-ray of the belly was taken and showed an unusual pattern of air in the intestines.
    - SARI=23.36  crit=0.00  NLIf=0.41  copyjrg=0.00

### Note 16 - `185`

- **ORIGINAL**  (FKGL 12.3, 19 words): She has been sedated with Ativan and came into the emergency room obtunded and unable to give any history.
- **REFERENCE** (FKGL 12.3, 20 words): She has been sedated with Ativan and came into the emergency room very drowsy and unable to give any history.
- **naive** (FKGL 14.5, 25 words, 0 edits): She was given a calming medicine called Ativan and arrived at the emergency room very drowsy and unable to share any information about her health.
    - SARI=27.95  crit=0.00  NLIf=0.90  copyjrg=0.00
- **termonly** (FKGL 12.8, 22 words, 2 edits): She has been given a calming medicine called lorazepam and came into the emergency room drowsy and unable to give any history.
    - SARI=43.39  crit=0.00  NLIf=0.54  copyjrg=0.00
- **grounded** (FKGL 13.3, 27 words, 2 edits): She was given a medicine to calm her and make her sleepy, and came into the emergency room not fully alert and unable to give any history.
    - SARI=34.60  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 17 - `202`

- **ORIGINAL**  (FKGL 4.4, 15 words): He has no edema now, but has had some mild leg swelling in the past.
- **REFERENCE** (FKGL 3.6, 15 words): He has no swelling now, but has had some mild leg swelling in the past.
- **naive** (FKGL 5.2, 15 words, 0 edits): He does not have swelling now, but his legs have been a little puffy before.
    - SARI=13.88  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 4.7, 16 words, 1 edits): He has no fluid buildup now, but has had some mild leg swelling in the past.
    - SARI=66.67  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.6, 15 words, 1 edits): He has no swelling now, but has had some mild leg swelling in the past.
    - SARI=91.67  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 18 - `231`

- **ORIGINAL**  (FKGL 21.0, 3 words): Mild secondary hyperparathyroidism.
- **REFERENCE** (FKGL 14.7, 5 words): Mild secondary hyperactive parathyroid gland
- **naive** (FKGL 8.9, 9 words, 0 edits): The patient has a mild form of secondary hyperparathyroidism.
    - SARI=15.00  crit=0.00  NLIf=0.97  copyjrg=1.00
- **termonly** (FKGL 9.1, 11 words, 1 edits): Mild overactivity of the parathyroid glands caused by another health problem.
    - SARI=23.50  crit=0.00  NLIf=0.86  copyjrg=0.00
- **grounded** (FKGL 9.1, 7 words, 1 edits): Mild overactive parathyroid glands from another cause.
    - SARI=24.07  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 19 - `248`

- **ORIGINAL**  (FKGL 10.6, 16 words): Otherwise, a complete review of systems was obtained and was negative except for as mentioned above.
- **REFERENCE** (FKGL 9.8, 16 words): Otherwise, a complete review of systems was obtained and was normal except for as mentioned above.
- **naive** (FKGL 10.6, 17 words, 0 edits): Otherwise, the patient's review of all body systems was normal except for what was already mentioned.
    - SARI=23.16  crit=0.00  NLIf=0.34  copyjrg=0.00
- **termonly** (FKGL 9.1, 19 words, 3 edits): Otherwise, a full head-to-toe symptom check was done and was normal except for what was noted above.
    - SARI=23.35  crit=0.00  NLIf=0.16  copyjrg=0.00
- **grounded** (FKGL 8.5, 19 words, 3 edits): Otherwise, the full set of body-part questions was asked and was normal except for what was noted above.
    - SARI=22.23  crit=0.00  NLIf=0.30  copyjrg=0.00

### Note 20 - `277`

- **ORIGINAL**  (FKGL 7.6, 16 words): Symptoms are worse when sitting for any length of time, such as driving a motor vehicle.
- **REFERENCE** (FKGL 5.2, 15 words): Symptoms are worse when sitting for any length of time, such as driving a car.
- **naive** (FKGL 4.7, 17 words, 0 edits): The patient's symptoms get worse when she sits for a while, like when driving a car.
    - SARI=16.46  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.2, 15 words, 1 edits): Symptoms are worse when sitting for any length of time, such as driving a car.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.2, 15 words, 1 edits): Symptoms are worse when sitting for any length of time, such as driving a car.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 21 - `290`

- **ORIGINAL**  (FKGL 12.8, 9 words): Forearm, elbow and shoulder exams reveal no neurologic compromise.
- **REFERENCE** (FKGL 7.6, 9 words): Forearm, elbow and shoulder exams reveal no nerve problems
- **naive** (FKGL 5.8, 12 words, 0 edits): The exams of the forearm, elbow, and shoulder show no nerve problems.
    - SARI=46.66  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.9, 11 words, 1 edits): Forearm, elbow and shoulder exams show no nerve or muscle damage.
    - SARI=48.68  crit=0.00  NLIf=0.15  copyjrg=0.00
- **grounded** (FKGL 6.3, 9 words, 1 edits): Forearm, elbow and shoulder exams show no nerve problems.
    - SARI=59.22  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 22 - `296`

- **ORIGINAL**  (FKGL 13.7, 12 words): Thereafter, the local anesthesia was injected into the area around the tumor.
- **REFERENCE** (FKGL 11.7, 12 words): Thereafter, the numbing agent was injected into the area around the tumor.
- **naive** (FKGL 12.2, 13 words, 0 edits): After that, the doctor injected numbing medicine into the area around the tumor.
    - SARI=48.56  crit=0.00  NLIf=0.90  copyjrg=0.00
- **termonly** (FKGL 8.5, 13 words, 3 edits): After that, the numbing medicine was shot into the area around the lump.
    - SARI=42.76  crit=0.00  NLIf=0.84  copyjrg=0.00
- **grounded** (FKGL 8.5, 13 words, 2 edits): After that, the numbing drug was injected into the area around the growth.
    - SARI=56.27  crit=0.00  NLIf=0.98  copyjrg=0.00

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
- **naive** (FKGL 6.1, 19 words, 0 edits): I do not think she has a clear, active abscess right now, but there is some fluid coming out.
    - SARI=36.14  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 7.8, 18 words, 2 edits): I do not think she has an obvious current pocket of pus, although there is some fluid leaking.
    - SARI=69.74  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 9.2, 19 words, 2 edits): I do not think she has an obvious current pocket of infection, although there is some fluid leaking out.
    - SARI=58.94  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 25 - `358`

- **ORIGINAL**  (FKGL 9.1, 11 words): At this time, we would rehydrate with intravenous fluids and reassess.
- **REFERENCE** (FKGL 5.8, 13 words): At this time, we would rehydrate with fluids through the vein and reassess.
- **naive** (FKGL 6.1, 21 words, 0 edits): At this time, the care team would give the patient fluids through a vein and then check how she is doing.
    - SARI=30.25  crit=0.00  NLIf=0.49  copyjrg=0.00
- **termonly** (FKGL 6.1, 16 words, 2 edits): At this time, we would give fluids by vein to restore body water and check again.
    - SARI=43.48  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 5.2, 15 words, 0 edits): Right now, we would give fluids by vein to restore water and then check again.
    - SARI=19.87  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 26 - `380`

- **ORIGINAL**  (FKGL 14.3, 6 words): Findings are compatible with acute appendicitis.
- **REFERENCE** (FKGL 12.8, 9 words): Findings are compatible with acute inflammation of the appendix
- **naive** (FKGL 8.9, 9 words, 0 edits): The test results suggest the patient has acute appendicitis.
    - SARI=8.91  crit=1.00  NLIf=0.86  copyjrg=1.00
- **termonly** (FKGL 5.9, 11 words, 2 edits): The test results point to a sudden swelling of the appendix.
    - SARI=15.15  crit=1.00  NLIf=0.67  copyjrg=0.00
- **grounded** (FKGL 6.8, 12 words, 2 edits): The test results point to a sudden, painful swelling of the appendix.
    - SARI=14.66  crit=1.00  NLIf=0.71  copyjrg=0.00

### Note 27 - `391`

- **ORIGINAL**  (FKGL 10.5, 18 words): She denies weight loss, but acknowledged decreased appetite and increased generalized fatigue for the past 3-4 months.
- **REFERENCE** (FKGL 10.5, 18 words): She denies weight loss, but acknowledged reduced appetite and more generalized tiredness for the past 3-4 months.
- **naive** (FKGL 10.2, 25 words, 0 edits): She said she has not lost weight, but she has noticed a smaller appetite and more overall tiredness over the last 3 to 4 months.
    - SARI=27.33  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 8.5, 27 words, 3 edits): She says she has not lost weight, but she agreed she has been less hungry and more tired all over for the past 3 to 4 months.
    - SARI=35.57  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 8.6, 26 words, 3 edits): She says she has not lost weight, but admitted she has been less hungry and more tired all over for the past 3 to 4 months.
    - SARI=35.60  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 28 - `392`

- **ORIGINAL**  (FKGL 21.8, 5 words): Consideration given to completion thyroidectomy.
- **REFERENCE** (FKGL 11.5, 9 words): Consideration given to remove remaining parts of the thyroid
- **naive** (FKGL 8.5, 18 words, 0 edits): The doctor thought about whether the patient should have surgery to remove the rest of the thyroid gland.
    - SARI=32.65  crit=1.00  NLIf=0.27  copyjrg=0.00
- **termonly** (FKGL 6.0, 10 words, 0 edits): The doctors thought about removing the rest of the thyroid.
    - SARI=28.37  crit=1.00  NLIf=0.44  copyjrg=0.00
- **grounded** (FKGL 6.7, 13 words, 0 edits): Doctors thought about doing surgery to take out the rest of the thyroid.
    - SARI=32.16  crit=1.00  NLIf=0.55  copyjrg=0.00

### Note 29 - `394`

- **ORIGINAL**  (FKGL 10.5, 19 words): She notes that she had epistaxis a few days ago, requiring nasal packing and fortunately that had resolved now.
- **REFERENCE** (FKGL 9.5, 21 words): She notes that she had a nose bleed a few days ago, requiring nose packing and fortunately that had resolved now.
- **naive** (FKGL 8.0, 22 words, 0 edits): She says she had a nosebleed a few days ago that needed packing in her nose, and luckily it has stopped now.
    - SARI=30.86  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 7.7, 23 words, 3 edits): She says she had a nosebleed a few days ago that needed gauze put in her nose, and luckily that has stopped now.
    - SARI=30.04  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 8.8, 25 words, 3 edits): She says she had a nosebleed a few days ago, needed something put in her nose to stop it, and luckily that has healed now.
    - SARI=29.58  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 30 - `396`

- **ORIGINAL**  (FKGL 8.9, 9 words): I also explained to the patient about conscious sedation.
- **REFERENCE** (FKGL 8.9, 9 words): I also explained to the patient about awake sedation.
- **naive** (FKGL 11.8, 22 words, 0 edits): I also told the patient about conscious sedation, which is medicine that helps a person stay calm and relaxed during a procedure.
    - SARI=13.30  crit=0.00  NLIf=0.00  copyjrg=1.00
- **termonly** (FKGL 8.4, 14 words, 1 edits): I also explained to the patient about medicine to make her relaxed and sleepy.
    - SARI=61.94  crit=0.00  NLIf=0.42  copyjrg=0.00
- **grounded** (FKGL 9.2, 19 words, 1 edits): I also explained to the patient about getting medicine to make them sleepy but still able to wake up.
    - SARI=61.94  crit=0.00  NLIf=0.05  copyjrg=0.00

### Note 31 - `762`

- **ORIGINAL**  (FKGL 5.2, 8 words): Palpation of her right knee reveals no crepitus.
- **REFERENCE** (FKGL 5.0, 9 words): Feeling of her right knee reveals no crunchy feeling.
- **naive** (FKGL 3.8, 8 words, 0 edits): Palpation of her right knee shows no crepitus.
    - SARI=25.06  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 2.3, 7 words, 1 edits): Feeling her right knee shows no crackling.
    - SARI=32.26  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 3.7, 9 words, 1 edits): Feeling her right knee finds no grinding or crackling.
    - SARI=31.31  crit=0.00  NLIf=0.87  copyjrg=0.00

### Note 32 - `427`

- **ORIGINAL**  (FKGL 10.1, 14 words): She stepped on ideas, concerns and expectations the evening prior and twisted her ankle.
- **REFERENCE** (FKGL 4.8, 11 words): She stepped on ice the evening prior and twisted her ankle.
- **naive** (FKGL 9.8, 16 words, 0 edits): She talked about her ideas, concerns, and expectations the night before, and she twisted her ankle.
    - SARI=18.55  crit=0.00  NLIf=0.93
- **termonly** (FKGL 9.3, 14 words, 1 edits): She stepped on ideas, concerns and expectations the night before and twisted her ankle.
    - SARI=21.81  crit=0.00  NLIf=0.99
- **grounded** (FKGL 9.3, 14 words, 1 edits): She stepped on ideas, concerns and expectations the night before and twisted her ankle.
    - SARI=21.81  crit=0.00  NLIf=0.99

### Note 33 - `439`

- **ORIGINAL**  (FKGL 14.1, 9 words): Modifying Factors : Patient 's condition is aggravated by throwing.
- **REFERENCE** (FKGL 9.6, 10 words): Modifying Factors : Patient 's condition is made worse by throwing.
- **naive** (FKGL 3.8, 9 words, 0 edits): The patient's condition gets worse when she throws.
    - SARI=26.63  crit=0.00  NLIf=0.94  copyjrg=0.00
- **termonly** (FKGL 6.8, 13 words, 1 edits): Things that change the condition: The patient's condition gets worse from throwing.
    - SARI=27.69  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.8, 13 words, 1 edits): Things that change the problem: The patient's condition gets worse from throwing.
    - SARI=27.50  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 34 - `451`

- **ORIGINAL**  (FKGL 21.3, 10 words): History of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis and kidney stones.
- **REFERENCE** (FKGL 14.9, 13 words): History of joint inflammation, bone degeneration, underactive thyroid, hay fever and kidney stones.
- **naive** (FKGL 17.7, 14 words, 0 edits): The patient has a history of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis, and kidney stones.
    - SARI=11.57  crit=0.00  NLIf=0.96  copyjrg=1.00
- **termonly** (FKGL 10.5, 22 words, 5 edits): She has a history of joint wear-and-tear, weak bones, an underactive thyroid, nose allergies, and hard deposits in the kidneys.
    - SARI=41.87  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 12.3, 24 words, 5 edits): She has a history of joint wear-and-tear arthritis, weak bones, an underactive thyroid, hay fever, and hard mineral deposits in the kidneys.
    - SARI=47.07  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 35 - `465`

- **ORIGINAL**  (FKGL 15.8, 7 words): The ultrasound was negative for intracranial hemorrhage.
- **REFERENCE** (FKGL 6.3, 9 words): The ultrasound was negative for bleeding in the brain.
- **naive** (FKGL 3.8, 8 words, 0 edits): The ultrasound showed no bleeding in the brain.
    - SARI=38.70  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 5.2, 8 words, 1 edits): The ultrasound found no bleeding inside the skull.
    - SARI=24.35  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 5.2, 8 words, 1 edits): The ultrasound found no bleeding inside the brain.
    - SARI=28.10  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 36 - `466`

- **ORIGINAL**  (FKGL 14.7, 12 words): He is status post laparoscopic appendicectomy, and he is tolerating oral diet.
- **REFERENCE** (FKGL 12.3, 15 words): He is status after keyhole surgery to remove appendix, and he is tolerating oral diet.
- **naive** (FKGL 10.0, 24 words, 0 edits): He had surgery to remove his appendix through small cuts in his belly, and he is able to eat food by mouth without problems.
    - SARI=34.97  crit=0.00  NLIf=0.25  copyjrg=0.00
- **termonly** (FKGL 8.9, 21 words, 0 edits): He had surgery to remove his appendix through small cuts, and he is able to eat food by mouth without problems.
    - SARI=35.43  crit=0.00  NLIf=0.54  copyjrg=0.00
- **grounded** (FKGL 7.0, 17 words, 0 edits): He had surgery to remove his appendix through small cuts, and he is handling food by mouth.
    - SARI=36.28  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 37 - `478`

- **ORIGINAL**  (FKGL 8.4, 14 words): We believe that her walking is most likely not being affected by the hydrocephalus.
- **REFERENCE** (FKGL 8.5, 18 words): We believe that her walking is most likely not being affected by the excess fluid in the brain.
- **naive** (FKGL 7.6, 14 words, 0 edits): We think the fluid buildup in her brain is probably not affecting her walking.
    - SARI=14.28  crit=0.00  NLIf=0.75  copyjrg=0.00
- **termonly** (FKGL 8.5, 18 words, 1 edits): We believe that her walking is most likely not being affected by the fluid buildup in her brain.
    - SARI=72.92  crit=0.00  NLIf=0.43  copyjrg=0.00
- **grounded** (FKGL 8.5, 18 words, 1 edits): We believe that her walking is most likely not being affected by the fluid buildup in her brain.
    - SARI=72.92  crit=0.00  NLIf=0.43  copyjrg=0.00

### Note 38 - `505`

- **ORIGINAL**  (FKGL 12.3, 11 words): She noted complaints of fatigue, lightheadedness, and severe dyspnea on exertion.
- **REFERENCE** (FKGL 13.1, 15 words): She noted complaints of tiredness, lightheadedness, and severe shortness of breath on doing anything physical.
- **naive** (FKGL 8.4, 16 words, 0 edits): She said she felt very tired, dizzy, and had serious trouble breathing when she was active.
    - SARI=23.12  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 4.9, 13 words, 3 edits): She said she felt tired, dizzy, and very short of breath when active.
    - SARI=26.59  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.9, 16 words, 4 edits): She said she felt very tired, dizzy, and had severe trouble breathing when she worked hard.
    - SARI=24.68  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 39 - `516`

- **ORIGINAL**  (FKGL 10.9, 14 words): No significant amount of edema associated with these in the dorsum of the hand.
- **REFERENCE** (FKGL 9.3, 14 words): No significant amount of swelling associated with these in the back of the hand.
- **naive** (FKGL 3.4, 14 words, 0 edits): There was no major swelling on the back of the hand linked to these.
    - SARI=36.58  crit=0.00  NLIf=0.93  copyjrg=0.00
- **termonly** (FKGL 2.2, 13 words, 2 edits): There is no large swelling on the back of the hand with these.
    - SARI=40.41  crit=0.00  NLIf=0.91  copyjrg=0.00
- **grounded** (FKGL 1.9, 12 words, 3 edits): No big swelling linked to these on the back of the hand.
    - SARI=38.22  crit=0.00  NLIf=0.57  copyjrg=0.00

### Note 40 - `523`

- **ORIGINAL**  (FKGL 12.3, 5 words): No cardio or pulmonary complaints.
- **REFERENCE** (FKGL 0.5, 5 words): No heart or lung complaints.
- **naive** (FKGL 2.3, 8 words, 0 edits): The patient has no heart or lung complaints.
    - SARI=62.81  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 0.5, 5 words, 2 edits): No heart or lung complaints.
    - SARI=75.00  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 0.5, 5 words, 2 edits): No heart or lung complaints.
    - SARI=75.00  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 41 - `553`

- **ORIGINAL**  (FKGL 6.9, 11 words): At that time, the Coreg had been held secondary to hypotension.
- **REFERENCE** (FKGL 3.1, 13 words): At that time, the Coreg had been held because of low blood pressure
- **naive** (FKGL 4.2, 15 words, 0 edits): At that time, the patient's Coreg had been stopped because of low blood pressure.
    - SARI=58.63  crit=0.00  NLIf=0.77  copyjrg=0.00
- **termonly** (FKGL 6.0, 15 words, 3 edits): At that time, the blood pressure medicine had been held because of low blood pressure.
    - SARI=66.79  crit=0.00  NLIf=0.77  copyjrg=0.00
- **grounded** (FKGL 6.0, 15 words, 3 edits): At that time, the blood pressure medicine had been held because of low blood pressure.
    - SARI=66.79  crit=0.00  NLIf=0.77  copyjrg=0.00

### Note 42 - `554`

- **ORIGINAL**  (FKGL 12.8, 16 words): Her diarrhea now has settled down and she is having less urinary incontinence, less pedal edema.
- **REFERENCE** (FKGL 8.4, 17 words): Her watery poop now has settled down and she is having less uncontrolled peeing, less foot swelling.
- **naive** (FKGL 9.3, 20 words, 0 edits): Her diarrhea has calmed down, and she is having fewer problems with urine leaking and less swelling in her feet.
    - SARI=43.59  crit=0.00  NLIf=0.80  copyjrg=0.33
- **termonly** (FKGL 6.1, 19 words, 3 edits): Her loose stools have calmed down and she is having less leaking of urine, less swelling in her feet.
    - SARI=48.79  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 7.2, 21 words, 3 edits): Her runny poop has calmed down, and she is having less trouble holding her pee and less swelling in her feet.
    - SARI=51.20  crit=0.00  NLIf=0.87  copyjrg=0.00

### Note 43 - `556`

- **ORIGINAL**  (FKGL 19.4, 13 words): Description : Nausea and abdominal pain after eating - Gall bladder disease - Laparoscopic cholecystectomy scheduled.
- **REFERENCE** (FKGL 14.4, 18 words): Description : Nausea and abdominal pain after eating - Gall bladder disease - keyhole surgery to remove the gall bladder scheduled.
- **naive** (FKGL 7.1, 27 words, 0 edits): The patient feels sick to the stomach and has belly pain after eating. This is caused by gall bladder disease. A surgery called laparoscopic cholecystectomy is planned.
    - SARI=23.97  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 4.8, 32 words, 5 edits): She has an upset stomach and belly pain after eating. This is from a problem with the organ that stores bile. A surgery using small cuts to remove that organ is planned.
    - SARI=21.44  crit=0.00  NLIf=0.63  copyjrg=0.00
- **grounded** (FKGL 12.4, 23 words, 3 edits): Feeling sick and belly pain after eating – a problem with the gallbladder – surgery to remove the gallbladder with a small camera is planned.
    - SARI=25.72  crit=0.00  NLIf=0.64  copyjrg=0.00

### Note 44 - `618`

- **ORIGINAL**  (FKGL 12.3, 20 words): She states that she has underlying history of heart disease but is not able to elaborate to any significant extent.
- **REFERENCE** (FKGL 12.3, 22 words): She states that she has underlying history of heart disease but is not able to go into detail to any significant extent.
- **naive** (FKGL 7.0, 17 words, 0 edits): She says she has a history of heart disease, but she cannot explain much more about it.
    - SARI=19.50  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.9, 14 words, 0 edits): She says she has a history of heart disease but cannot give more detail.
    - SARI=21.35  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 7.6, 16 words, 1 edits): She says she has a history of heart disease but cannot give many details about it.
    - SARI=19.50  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 45 - `661`

- **ORIGINAL**  (FKGL 6.5, 18 words): There was some slight edema of the fourth digit, on which he still is wearing his wedding band.
- **REFERENCE** (FKGL 5.9, 18 words): There was some slight swelling of the fourth finger, on which he still is wearing his wedding band.
- **naive** (FKGL 6.7, 19 words, 0 edits): There was a little swelling on his fourth finger, and he still has his wedding ring on that finger.
    - SARI=24.51  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.4, 16 words, 1 edits): The ring finger was a little swollen, and he still has his wedding band on it.
    - SARI=23.69  crit=0.00  NLIf=0.27  copyjrg=0.00
- **grounded** (FKGL 5.9, 18 words, 2 edits): There was some slight swelling of the ring finger, on which he still is wearing his wedding band.
    - SARI=81.51  crit=0.00  NLIf=0.24  copyjrg=0.00

### Note 46 - `669`

- **ORIGINAL**  (FKGL 12.8, 21 words): Parents do state that she does appear to breathe rapidly, tires somewhat with the feeding with increased respiratory effort and diaphoresis.
- **REFERENCE** (FKGL 10.0, 21 words): Parents do state that she does appear to breathe quickly, tires somewhat with the feeding with increased breathing effort and sweating.
- **naive** (FKGL 8.0, 19 words, 0 edits): The parents say that she seems to breathe fast and gets tired during feeding, with harder breathing and sweating.
    - SARI=23.66  crit=0.00  NLIf=0.79  copyjrg=0.00
- **termonly** (FKGL 8.1, 20 words, 4 edits): Parents do say that she seems to breathe fast, gets a bit tired during feeding with harder breathing and sweating.
    - SARI=24.14  crit=0.00  NLIf=0.62  copyjrg=0.00
- **grounded** (FKGL 8.3, 23 words, 4 edits): Her parents do say she seems to breathe quickly, gets a bit tired while feeding with more work to breathe and heavy sweating.
    - SARI=22.82  crit=0.00  NLIf=0.14  copyjrg=0.00

### Note 47 - `673`

- **ORIGINAL**  (FKGL 11.3, 26 words): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had onset of chest pain this evening.
- **REFERENCE** (FKGL 10.5, 24 words): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had chest pain this evening.
- **naive** (FKGL 8.8, 23 words, 0 edits): The patient said he has not used amphetamines for at least four to five months, but he started having chest pain this evening.
    - SARI=37.20  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 10.9, 28 words, 2 edits): The patient has not used stimulant drugs for at least four to five months, according to the patient; however, he had a start of chest pain this evening.
    - SARI=46.93  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 10.9, 28 words, 2 edits): The patient has not used stimulant drugs for at least four to five months, according to the patient; however, he had the start of chest pain this evening.
    - SARI=46.93  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 48 - `675`

- **ORIGINAL**  (FKGL 8.4, 10 words): Orogastric suction carried out with only scant clear stomach contents.
- **REFERENCE** (FKGL 7.6, 16 words): Suction of stomach through the mouth carried out with only a small amount clear stomach contents
- **naive** (FKGL 5.2, 15 words, 0 edits): A tube was used to remove a small amount of clear fluid from the stomach.
    - SARI=27.94  crit=0.00  NLIf=0.89  copyjrg=0.00
- **termonly** (FKGL 9.0, 25 words, 2 edits): A tube was put through the mouth into the stomach to pull out fluid, but only a tiny amount of see-through liquid came out.
    - SARI=28.94  crit=0.00  NLIf=0.67  copyjrg=0.00
- **grounded** (FKGL 10.0, 26 words, 0 edits): A tube was put through the mouth into the stomach to pull out fluid, but only a very small amount of thin stomach liquid came out.
    - SARI=29.85  crit=0.00  NLIf=0.66  copyjrg=0.00

### Note 49 - `680`

- **ORIGINAL**  (FKGL 11.5, 9 words): Probably there is some restrictive element because of fibrosis.
- **REFERENCE** (FKGL 10.2, 11 words): Probably there is some restrictive element because of scarring of tissues.
- **naive** (FKGL 6.0, 10 words, 0 edits): The patient may have some restriction because of scar tissue.
    - SARI=11.79  crit=0.00  NLIf=0.72  copyjrg=0.00
- **termonly** (FKGL 8.2, 8 words, 2 edits): Probably there is some stiffening because of scarring.
    - SARI=37.67  crit=0.00  NLIf=0.86  copyjrg=0.00
- **grounded** (FKGL 7.2, 10 words, 2 edits): Probably there is some limiting part because of scarred tissue.
    - SARI=28.34  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 50 - `681`

- **ORIGINAL**  (FKGL 10.2, 9 words): The uterus was placed back into the abdominal cavity.
- **REFERENCE** (FKGL 3.8, 8 words): The womb was placed back into the abdomen
- **naive** (FKGL 7.6, 9 words, 0 edits): The uterus was put back into the belly area.
    - SARI=34.72  crit=0.00  NLIf=0.98  copyjrg=0.50
- **termonly** (FKGL 2.3, 9 words, 2 edits): The womb was placed back into the belly space.
    - SARI=84.29  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 2 edits): The womb was placed back into the belly area.
    - SARI=84.29  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 51 - `682`

- **ORIGINAL**  (FKGL 5.0, 9 words): This was viewed on the AP and lateral projections.
- **REFERENCE** (FKGL -0.7, 8 words): This was viewed from the front and sides.
- **naive** (FKGL 4.8, 15 words, 0 edits): The doctors looked at this on the front-to-back and side-view X‑rays.
    - SARI=34.19  crit=1.00  NLIf=0.08  copyjrg=0.00
- **termonly** (FKGL 2.3, 11 words, 2 edits): This was viewed on the front-to-back and side views.
    - SARI=54.23  crit=1.00  NLIf=0.91  copyjrg=0.00
- **grounded** (FKGL 2.3, 11 words, 2 edits): This was seen on the front-to-back and side views.
    - SARI=42.64  crit=1.00  NLIf=0.91  copyjrg=0.00

### Note 52 - `686`

- **ORIGINAL**  (FKGL 8.2, 8 words): The cords move normally with phonation and ventilation.
- **REFERENCE** (FKGL 5.2, 8 words): The cords move normally when speaking and breathing
- **naive** (FKGL 3.6, 15 words, 0 edits): The vocal cords move the way they should when the person makes sound and breathes.
    - SARI=36.99  crit=0.00  NLIf=0.95  copyjrg=0.00
- **termonly** (FKGL 5.9, 11 words, 2 edits): The vocal folds move normally with breathing and making voice sounds.
    - SARI=34.07  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 6.3, 9 words, 1 edits): The vocal folds move normally with speaking and breathing.
    - SARI=41.98  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 53 - `688`

- **ORIGINAL**  (FKGL 7.6, 13 words): Once the abdomen was opened, there was noted to be gross purulent drainage.
- **REFERENCE** (FKGL 6.0, 15 words): Once the abdomen was opened, there was noted to be a lot of pus draining.
- **naive** (FKGL 7.6, 14 words, 0 edits): Once the abdomen was opened, the doctors saw thick, pus-like fluid draining out.
    - SARI=34.84  crit=0.00  NLIf=0.40  copyjrg=0.00
- **termonly** (FKGL 5.8, 14 words, 2 edits): Once the belly was opened, there was a thick, pus-like fluid leaking out.
    - SARI=31.61  crit=0.00  NLIf=0.88  copyjrg=0.00
- **grounded** (FKGL 5.0, 14 words, 2 edits): Once the belly was opened, there was a large amount of pus leaking out.
    - SARI=34.08  crit=0.00  NLIf=0.88  copyjrg=0.00

### Note 54 - `692`

- **ORIGINAL**  (FKGL 4.0, 13 words): Once all four ports were placed, the right upper quadrant was then explored.
- **REFERENCE** (FKGL 5.4, 16 words): Once all four tubes were placed, the top right corner of her abdomen was then explored.
- **naive** (FKGL 5.9, 18 words, 0 edits): Once all four ports were in place, the doctor looked around the right upper part of the belly.
    - SARI=30.63  crit=0.00  NLIf=0.30  copyjrg=0.50
- **termonly** (FKGL 5.9, 18 words, 3 edits): Once all four small openings were put in, the upper right side of the belly was then checked.
    - SARI=42.65  crit=0.00  NLIf=0.66  copyjrg=0.00
- **grounded** (FKGL 7.3, 19 words, 3 edits): Once all four small openings were placed, the upper right part of the belly was then looked at carefully.
    - SARI=51.37  crit=0.00  NLIf=0.55  copyjrg=0.00

### Note 55 - `693`

- **ORIGINAL**  (FKGL 15.4, 15 words): Options such as watchful waiting, robotic prostatectomy, seed implantation with and without radiation were discussed.
- **REFERENCE** (FKGL 11.8, 23 words): Options such as watch and wait, removing the prostate with the help of a robot, seed implantation with and without radiation were discussed.
- **naive** (FKGL 12.9, 19 words, 0 edits): Options like watchful waiting, robotic surgery to remove the prostate, and seed implants with or without radiation were discussed.
    - SARI=32.68  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 16.4, 30 words, 4 edits): Options such as close follow-up without treatment right away, surgery to remove the prostate with a robot, placing tiny radioactive seeds with and without high-energy rays were discussed.
    - SARI=39.54  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 16.7, 32 words, 4 edits): Options such as close monitoring without treatment right away, surgery with a robot to remove the prostate, placing tiny devices with and without high-energy rays to kill cancer cells were discussed.
    - SARI=38.55  crit=0.00  NLIf=0.85  copyjrg=0.00

### Note 56 - `695`

- **ORIGINAL**  (FKGL 14.3, 10 words): He also reportedly was on Lasix prior to hospitalization, possible
- **REFERENCE** (FKGL 11.5, 15 words): He also was reportedly on water pills (lasix) before his admission to the hospital, possible
- **naive** (FKGL 8.1, 20 words, 0 edits): He was also taking a water pill called Lasix before he went to the hospital, but that is not certain.
    - SARI=39.09  crit=1.00  NLIf=0.08  copyjrg=0.00
- **termonly** (FKGL 5.9, 14 words, 3 edits): He also was said to be on a water pill before his hospital stay.
    - SARI=49.24  crit=1.00  NLIf=0.00  copyjrg=0.00
- **grounded** (FKGL 6.7, 13 words, 2 edits): He also, people say, was on a water pill before his hospital stay.
    - SARI=43.78  crit=1.00  NLIf=0.00  copyjrg=0.00

### Note 57 - `697`

- **ORIGINAL**  (FKGL 10.2, 9 words): The four cardiac chambers dimensions are within normal limits.
- **REFERENCE** (FKGL 4.9, 13 words): The sizes of the four parts of the heart are within normal limits.
- **naive** (FKGL 2.5, 10 words, 0 edits): The four chambers of the heart are normal in size.
    - SARI=41.72  crit=0.00  NLIf=0.98  copyjrg=0.25
- **termonly** (FKGL 2.3, 8 words, 2 edits): The four heart spaces are normal in size.
    - SARI=34.74  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 0.8, 8 words, 2 edits): The four heart rooms are normal in size.
    - SARI=34.74  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 58 - `698`

- **ORIGINAL**  (FKGL 11.5, 9 words): Digital rectal examination was performed, which showed no masses.
- **REFERENCE** (FKGL 6.9, 11 words): Examination of the back passage was performed, which showed no lumps.
- **naive** (FKGL 5.0, 15 words, 0 edits): A doctor checked the patient's rectum with a gloved finger and found no lumps.
    - SARI=22.68  crit=0.00  NLIf=0.05  copyjrg=0.00
- **termonly** (FKGL 6.0, 16 words, 1 edits): A doctor checked inside the patient's rectum with a gloved finger and found no lumps.
    - SARI=22.54  crit=0.00  NLIf=0.08  copyjrg=0.00
- **grounded** (FKGL 4.0, 13 words, 2 edits): The doctor did a finger check of the rectum and felt no lumps.
    - SARI=24.97  crit=0.00  NLIf=0.22  copyjrg=0.00

### Note 59 - `699`

- **ORIGINAL**  (FKGL 11.2, 23 words): He then had a problem with seizures, hemiparesis, has been to the hospital, developed C-diff, and is in the nursing home currently.
- **REFERENCE** (FKGL 12.0, 29 words): He then had a problem with fits, weakness on one side, has been to the hospital, developed an infection in the gut, and is in the nursing home currently.
- **naive** (FKGL 6.1, 33 words, 0 edits): He then had a problem with seizures and weakness on one side of his body. He has been to the hospital, got a C-diff infection, and is now in a nursing home.
    - SARI=48.23  crit=0.00  NLIf=0.95  copyjrg=0.67
- **termonly** (FKGL 13.9, 36 words, 3 edits): He then had a problem with sudden body shakes, weakness on one side of the body, has been to the hospital, got a gut infection that causes loose stools, and is in the nursing home now.
    - SARI=63.15  crit=0.00  NLIf=0.70  copyjrg=0.00
- **grounded** (FKGL 13.4, 33 words, 3 edits): He then had a problem with fits, weakness on one side of his body, has been to the hospital, got a gut infection that causes diarrhea, and is in the nursing home now.
    - SARI=68.70  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 60 - `700`

- **ORIGINAL**  (FKGL 12.3, 22 words): He has been on continuous positive airway pressure now for several months, and returns for followup to review his response to treatment.
- **REFERENCE** (FKGL 9.7, 25 words): He has been using a breathing mask now for several months, and returns for follow up to review how he is doing with the treatment.
- **naive** (FKGL 13.5, 29 words, 0 edits): He has been using a continuous positive airway pressure machine for several months and is back for a follow-up visit to check how well the treatment is working.
    - SARI=50.87  crit=0.00  NLIf=0.95  copyjrg=0.83
- **termonly** (FKGL 8.3, 25 words, 2 edits): He has been on a steady air pressure mask for several months, and comes back for a checkup to see how well it is working.
    - SARI=47.11  crit=0.00  NLIf=0.93  copyjrg=0.17
- **grounded** (FKGL 9.9, 30 words, 2 edits): He has been on a steady stream of air through a mask for several months, and comes back for a checkup to see how he is doing with the treatment.
    - SARI=56.39  crit=0.00  NLIf=0.60  copyjrg=0.00

### Note 61 - `709`

- **ORIGINAL**  (FKGL 8.5, 18 words): The patient to take small bite and small sips to help decrease the risk of aspiration and penetration.
- **REFERENCE** (FKGL 9.9, 30 words): The patient is to take small bite and small sips to help decrease the risk of having the food or drink going down the wrong pipe and piercing the pipe.
- **naive** (FKGL 7.2, 23 words, 0 edits): The patient should take small bites and small sips to help lower the chance of food or liquid going down the wrong way.
    - SARI=39.20  crit=0.00  NLIf=0.67  copyjrg=0.00
- **termonly** (FKGL 10.0, 26 words, 2 edits): The patient should take small bites and small sips to help lower the risk of food or liquid going into the airway and entering the lungs.
    - SARI=38.74  crit=0.00  NLIf=0.70  copyjrg=0.00
- **grounded** (FKGL 8.5, 24 words, 0 edits): The patient should take small bites and small sips to help lower the risk of food or liquid going into the airway or lungs.
    - SARI=38.85  crit=0.00  NLIf=0.73  copyjrg=0.00

### Note 62 - `714`

- **ORIGINAL**  (FKGL 12.3, 15 words): The patient was awakened and extubated and moved to the recovery room in satisfactory condition.
- **REFERENCE** (FKGL 11.1, 20 words): The patient was awakened and tube was removed from the airway and moved to the recovery room in satisfactory condition.
- **naive** (FKGL 9.3, 20 words, 0 edits): The patient was woken up, had her breathing tube removed, and was taken to the recovery room in good condition.
    - SARI=33.74  crit=0.00  NLIf=0.93  copyjrg=0.00
- **termonly** (FKGL 8.9, 21 words, 3 edits): The patient was woken up, had the breathing tube taken out, and was moved to the recovery room in good condition.
    - SARI=37.26  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 9.6, 22 words, 3 edits): The patient was woken up, had the breathing tube taken out, and was moved to the recovery room in good enough condition.
    - SARI=37.15  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 63 - `721`

- **ORIGINAL**  (FKGL 15.4, 10 words): PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily aroused.
- **REFERENCE** (FKGL 6.7, 8 words): The patient was asleep, but easily woken up.
- **naive** (FKGL 6.0, 15 words, 0 edits): The patient was asleep, but she woke up easily when someone tried to rouse her.
    - SARI=59.40  crit=0.00  NLIf=0.35  copyjrg=0.00
- **termonly** (FKGL 14.4, 11 words, 1 edits): PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily woken up.
    - SARI=91.36  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 14.4, 11 words, 1 edits): PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily woken up.
    - SARI=91.36  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 64 - `725`

- **ORIGINAL**  (FKGL 10.9, 26 words): He is to follow up in approximately 10 days for recheck as well as prescription for intended AFOs, which he will need up to 6 months.
- **REFERENCE** (FKGL 11.5, 28 words): He is to come back in approximately 10 days for recheck as well as prescription for intended foot-drop braces, which he will need up to 6 months.
- **naive** (FKGL 4.8, 34 words, 0 edits): He should come back in about 10 days for a check-up and to get a prescription for the leg braces he will need. He will use those braces for up to 6 months.
    - SARI=30.46  crit=0.00  NLIf=0.68  copyjrg=0.00
- **termonly** (FKGL 10.1, 29 words, 2 edits): He is to come back in about 10 days for a recheck and a prescription for planned ankle-foot braces, which he will need for up to 6 months.
    - SARI=43.50  crit=0.00  NLIf=0.67  copyjrg=0.00
- **grounded** (FKGL 10.1, 29 words, 2 edits): He is to come back in about 10 days for a recheck and a prescription for planned ankle-foot braces, which he will need for up to 6 months.
    - SARI=43.50  crit=0.00  NLIf=0.67  copyjrg=0.00

### Note 65 - `726`

- **ORIGINAL**  (FKGL 14.1, 8 words): Genitourinary : The external genitalia appeared to be normal.
- **REFERENCE** (FKGL 12.3, 8 words): The penis/vagina/genitals appeared to be normal.
- **naive** (FKGL 4.5, 6 words, 0 edits): The outside sex organs looked normal.
    - SARI=25.91  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 7.2, 10 words, 0 edits): Urinary and sex organs: The outer sex parts looked normal.
    - SARI=25.91  crit=0.00  NLIf=0.77  copyjrg=0.00
- **grounded** (FKGL 7.2, 10 words, 1 edits): Urinary and sex organs: The outside sex parts looked normal.
    - SARI=25.91  crit=0.00  NLIf=0.72  copyjrg=0.00

### Note 66 - `727`

- **ORIGINAL**  (FKGL 12.2, 13 words): She is postop day 21 of an exploratory laparotomy with ovarian cancer staging.
- **REFERENCE** (FKGL 12.6, 17 words): She is 21 days after an open abdominal operation which explored how widespread the ovarian cancer was.
- **naive** (FKGL 13.5, 14 words, 0 edits): She is 21 days past surgery from an exploratory laparotomy with ovarian cancer staging.
    - SARI=48.37  crit=0.00  NLIf=0.99  copyjrg=0.75
- **termonly** (FKGL 9.2, 19 words, 2 edits): She is 21 days after surgery to look inside the belly and check how far ovarian cancer has spread.
    - SARI=55.21  crit=0.00  NLIf=0.46  copyjrg=0.00
- **grounded** (FKGL 8.1, 20 words, 2 edits): She is 21 days after surgery to check her belly and find out how far her ovary cancer has spread.
    - SARI=49.02  crit=0.00  NLIf=0.11  copyjrg=0.00

### Note 67 - `732`

- **ORIGINAL**  (FKGL 8.5, 13 words): Prescription for prednisone as part of his chemotherapy has been given to him.
- **REFERENCE** (FKGL 7.6, 15 words): Prescription for steroid tablets as part of his cancer treatment has been given to him.
- **naive** (FKGL 8.5, 13 words, 0 edits): A prescription for prednisone was given to him as part of his chemotherapy.
    - SARI=37.37  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 8.4, 17 words, 2 edits): He has been given a prescription for a steroid medicine as part of his cancer drug treatment.
    - SARI=54.69  crit=0.00  NLIf=0.40  copyjrg=0.00
- **grounded** (FKGL 10.6, 22 words, 2 edits): He was given a prescription for a medicine that lowers the body's immune response as part of his cancer drug treatment.
    - SARI=43.78  crit=0.00  NLIf=0.56  copyjrg=0.00

### Note 68 - `738`

- **ORIGINAL**  (FKGL 9.1, 12 words): Photic stimulation was performed, but no clear-cut photic driving was seen.
- **REFERENCE** (FKGL 12.8, 17 words): Visual stimulation was performed, but no clear-cut changes in electrical activity of the brain was seen.
- **naive** (FKGL 7.6, 15 words, 0 edits): Photic stimulation was done, but no clear brainwave response to the flashing light was seen.
    - SARI=31.65  crit=0.00  NLIf=0.03  copyjrg=0.50
- **termonly** (FKGL 4.8, 12 words, 0 edits): Flashing lights were used, but no clear brain-wave following was seen.
    - SARI=32.89  crit=0.00  NLIf=0.64  copyjrg=0.00
- **grounded** (FKGL 3.6, 15 words, 0 edits): Flashing lights were used, but no strong brain wave response to the lights was seen.
    - SARI=27.18  crit=0.00  NLIf=0.24  copyjrg=0.00

### Note 69 - `739`

- **ORIGINAL**  (FKGL 15.6, 8 words): FAMILY HISTORY : Both parents died with myocardial infarctions.
- **REFERENCE** (FKGL 8.2, 8 words): Family history: Both parents died with heart attacks.
- **naive** (FKGL 2.3, 8 words, 0 edits): Both of her parents died from heart attacks.
    - SARI=27.40  crit=0.00  NLIf=0.87  copyjrg=0.00
- **termonly** (FKGL 8.2, 8 words, 1 edits): FAMILY HISTORY: Both parents died from heart attacks.
    - SARI=61.01  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 8.2, 8 words, 1 edits): FAMILY HISTORY: Both parents died from heart attacks.
    - SARI=61.01  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 70 - `740`

- **ORIGINAL**  (FKGL 11.2, 11 words): Extremities : 2+ bilateral pitting edema to the level of the knees.
- **REFERENCE** (FKGL 10.1, 28 words): Hands and feet: There is swelling in both feet up to the level of the knees (when pressed, causes an indentation in the skin for a few seconds)
- **naive** (FKGL 5.3, 22 words, 0 edits): Her legs and feet have swelling that leaves a dent when pressed, and it goes up to her knees on both sides.
    - SARI=27.57  crit=1.00  NLIf=0.19  copyjrg=0.00
- **termonly** (FKGL 1.9, 12 words, 1 edits): Both legs have swelling that leaves a dent, up to the knees.
    - SARI=35.45  crit=1.00  NLIf=0.90  copyjrg=0.00
- **grounded** (FKGL 3.5, 17 words, 0 edits): Her legs and feet are swollen with pits when pressed, up to the knees on both sides.
    - SARI=36.88  crit=1.00  NLIf=0.25  copyjrg=0.00

### Note 71 - `741`

- **ORIGINAL**  (FKGL 14.3, 10 words): Following questions are mostly involved in a psychosocial donor evaluation.
- **REFERENCE** (FKGL 13.9, 15 words): Following questions are mostly involved in a donor evaluation of their psychological or social states.
- **naive** (FKGL 9.1, 15 words, 0 edits): The questions that come next are mostly part of a psychosocial evaluation of a donor.
    - SARI=19.23  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 7.6, 16 words, 1 edits): Following questions are mostly part of a check on a donor's mental and social health.
    - SARI=36.06  crit=0.00  NLIf=0.88  copyjrg=0.00
- **grounded** (FKGL 11.8, 20 words, 1 edits): The following questions are mostly part of an evaluation that looks at a donor's mental and social well-being.
    - SARI=36.75  crit=0.00  NLIf=0.80  copyjrg=0.00

### Note 72 - `742`

- **ORIGINAL**  (FKGL 24.1, 5 words): Mild nonmobile descending aortic atherosclerosis.
- **REFERENCE** (FKGL 11.1, 22 words): Mild non-moving hardening of the part of aorta (the largest artery of the body) that goes down the chest and abdomen.
- **naive** (FKGL 9.3, 25 words, 0 edits): The patient has mild hardening of the arteries in the part of the aorta that goes down through the chest, and it does not move.
    - SARI=51.08  crit=0.00  NLIf=0.87  copyjrg=0.00
- **termonly** (FKGL 7.6, 9 words, 2 edits): Mild, not moving, hardening of the lower main artery.
    - SARI=48.83  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 5.9, 11 words, 2 edits): Mild, not moving, hardening of the main artery in the chest.
    - SARI=49.66  crit=0.00  NLIf=0.88  copyjrg=0.00

### Note 73 - `750`

- **ORIGINAL**  (FKGL 6.7, 8 words): The eustachian tube was obstructed with bone wax.
- **REFERENCE** (FKGL 3.1, 13 words): The passage between the nose and the ears was blocked with bone wax.
- **naive** (FKGL 3.8, 8 words, 0 edits): The eustachian tube was blocked with bone wax.
    - SARI=59.31  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL 6.5, 18 words, 3 edits): The tube that connects the ear to the throat was blocked with a waxy material used on bone.
    - SARI=36.31  crit=0.00  NLIf=0.85  copyjrg=0.00
- **grounded** (FKGL 8.1, 20 words, 3 edits): The tube that links the middle ear to the throat was blocked with a hard, waxy material used in surgery.
    - SARI=33.53  crit=0.00  NLIf=0.25  copyjrg=0.00

### Note 74 - `752`

- **ORIGINAL**  (FKGL 6.3, 9 words): He was placed supine on the operating room table.
- **REFERENCE** (FKGL 7.2, 10 words): He was placed facing upwards on the operating room table.
- **naive** (FKGL 4.8, 11 words, 0 edits): He lay flat on his back on the operating room table.
    - SARI=50.81  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 4.8, 12 words, 1 edits): He was placed flat on his back on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 5.8, 12 words, 1 edits): He was placed lying on his back on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 75 - `755`

- **ORIGINAL**  (FKGL 7.4, 7 words): A urinalysis was not performed this time.
- **REFERENCE** (FKGL 2.3, 8 words): A urine test was not performed this time.
- **naive** (FKGL 0.8, 8 words, 0 edits): A urine test was not done this time.
    - SARI=51.60  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 0.8, 8 words, 2 edits): A urine test was not done this time.
    - SARI=51.60  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL -0.7, 8 words, 1 edits): A pee test was not done this time.
    - SARI=36.23  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 76 - `766`

- **ORIGINAL**  (FKGL 12.3, 21 words): Vision and hearing appeared to be adequate for testing, although she did indicate that she needed to update her eyeglass prescription.
- **REFERENCE** (FKGL 11.7, 21 words): Vision and hearing appeared to be okay for testing, although she did indicate that she needed to update her glasses prescription.
- **naive** (FKGL 8.1, 20 words, 0 edits): Her eyesight and hearing seemed good enough for the tests, but she did say she needed a new glasses prescription.
    - SARI=18.42  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 7.7, 17 words, 3 edits): Vision and hearing seemed good enough for testing, although she did say that she needed new glasses.
    - SARI=31.06  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 9.2, 19 words, 3 edits): Vision and hearing seemed good enough for testing, although she did say she needed to update her glasses order.
    - SARI=41.39  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 77 - `771`

- **ORIGINAL**  (FKGL 8.0, 24 words): I have talked to him several times about a colonoscopy, which he has refused, and so we have been doing stools for occult blood.
- **REFERENCE** (FKGL 17.5, 46 words): I have talked to him several times about a procedure to have a look inside the bowels (colonoscopy), which he has refused, and so we have been testing some stool samples in the lab to look for blood (which may be invisible to the naked eye).
- **naive** (FKGL 9.5, 26 words, 0 edits): The doctor has talked to the patient several times about a colonoscopy, which he has refused, so they have been checking his stool for hidden blood.
    - SARI=33.49  crit=0.00  NLIf=0.94  copyjrg=0.00
- **termonly** (FKGL 12.6, 34 words, 2 edits): I have talked to him several times about a test that looks inside the large bowel with a camera, which he has refused, and so we have been checking his poop for hidden blood.
    - SARI=61.87  crit=0.00  NLIf=0.69  copyjrg=0.00
- **grounded** (FKGL 11.9, 33 words, 3 edits): I have talked to him several times about a test that checks the inside of his large intestine, which he has refused, and so we have been checking his poop for hidden blood.
    - SARI=61.54  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 78 - `783`

- **ORIGINAL**  (FKGL 8.4, 10 words): The knee was copiously irrigated and suction dried once again.
- **REFERENCE** (FKGL 7.6, 16 words): The knee was washed out thoroughly and dried with a suction (or mini-vacuum) once again
- **naive** (FKGL 4.4, 15 words, 0 edits): The knee was washed out with a lot of fluid and then suctioned dry again.
    - SARI=57.01  crit=1.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 4.7, 16 words, 2 edits): The knee was washed with a lot of fluid and then dried with suction once again.
    - SARI=65.03  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.1, 21 words, 2 edits): The knee was washed with a lot of fluid and then the fluid was pulled out to dry it once again.
    - SARI=58.53  crit=0.00  NLIf=0.88  copyjrg=0.00

### Note 79 - `784`

- **ORIGINAL**  (FKGL 10.9, 14 words): She is not having painful urination, any blood in the urine, frequency or hesitancy.
- **REFERENCE** (FKGL 11.1, 20 words): She is not having painful peeing, any blood in the pee, needing to pee very often or having difficulty peeing.
- **naive** (FKGL 6.9, 22 words, 0 edits): She does not have pain when she pees, any blood in her pee, or a need to go often or trouble starting.
    - SARI=35.73  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 9.8, 18 words, 2 edits): She is not having painful urination, any blood in the urine, needing to go often, or trouble starting.
    - SARI=63.87  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 9.9, 20 words, 2 edits): She is not having painful urination, any blood in the urine, needing to pee often, or trouble starting to pee.
    - SARI=66.66  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 80 - `789`

- **ORIGINAL**  (FKGL 14.8, 19 words): Cardiovascular : Chest pain in the retrosternal area, Occasional anginal pain and patient describes it as a sensation of tightness.
- **REFERENCE** (FKGL 14.6, 30 words): Heart and blood vessels: Chest pain just behind the breastbone, occasional chest pain when exercising or exerting themselves, which gets better with rest and patient describes it as feeling 'tightness'.
- **naive** (FKGL 4.8, 24 words, 0 edits): The patient has chest pain behind the breastbone. Sometimes it feels like a squeezing or tightness, which is a type of heart-related pain.
    - SARI=38.01  crit=0.00  NLIf=0.77  copyjrg=0.00
- **termonly** (FKGL 10.7, 23 words, 2 edits): Heart and blood vessels: Chest pain behind the breastbone, occasional heart-related chest pain, and the patient describes it as a tight feeling.
    - SARI=64.71  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 11.3, 24 words, 2 edits): Heart and blood vessels: Chest pain behind the breastbone, occasional heart-related chest pain, and the patient describes it as a feeling of tightness.
    - SARI=65.33  crit=0.00  NLIf=0.91  copyjrg=0.00

### Note 81 - `790`

- **ORIGINAL**  (FKGL 4.8, 11 words): We excised a good bit of his synovium and synovial pouch.
- **REFERENCE** (FKGL 1.9, 12 words): We cut out a bit of the soft tissue of the joint.
- **naive** (FKGL 5.9, 18 words, 0 edits): We removed a large part of the tissue lining his joint and the small sac attached to it.
    - SARI=40.09  crit=0.00  NLIf=0.94  copyjrg=0.00
- **termonly** (FKGL 4.5, 18 words, 2 edits): We cut out a good bit of the lining of his joint and the small sac around it.
    - SARI=53.01  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 5.6, 17 words, 3 edits): We removed a good bit of the soft lining of his joint and the pocket around it.
    - SARI=50.09  crit=0.00  NLIf=0.87  copyjrg=0.00

### Note 82 - `801`

- **ORIGINAL**  (FKGL 13.4, 11 words): An inflammatory process such as infection or ischemia must be considered.
- **REFERENCE** (FKGL 10.4, 13 words): An inflammatory process such as infection or reduced blood flow must be considered.
- **naive** (FKGL 9.8, 17 words, 0 edits): Doctors must think about whether an infection or poor blood flow is causing the swelling and irritation.
    - SARI=19.56  crit=0.00  NLIf=0.42  copyjrg=0.00
- **termonly** (FKGL 5.8, 12 words, 2 edits): A problem like an infection or blocked blood flow must be considered.
    - SARI=35.60  crit=1.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 6.7, 19 words, 2 edits): An illness with redness, warmth, and swelling, such as an infection or poor blood flow, must be thought of.
    - SARI=29.22  crit=0.00  NLIf=0.36  copyjrg=0.00

### Note 83 - `804`

- **ORIGINAL**  (FKGL 2.9, 12 words): I have asked her to increase her prednisone when she goes home.
- **REFERENCE** (FKGL 2.9, 12 words): I have asked her to increase her steroid when she goes home.
- **naive** (FKGL 4.4, 15 words, 0 edits): The doctor asked her to take a higher dose of prednisone when she goes home.
    - SARI=26.98  crit=0.00  NLIf=0.60  copyjrg=1.00
- **termonly** (FKGL 4.9, 13 words, 1 edits): I have asked her to increase her steroid medicine when she goes home.
    - SARI=79.79  crit=0.00  NLIf=0.02  copyjrg=0.00
- **grounded** (FKGL 6.0, 15 words, 1 edits): I have asked her to increase her medicine that lowers swelling when she goes home.
    - SARI=66.67  crit=0.00  NLIf=0.25  copyjrg=0.00

### Note 84 - `844`

- **ORIGINAL**  (FKGL 10.2, 9 words): She may need other neuropathic pain medications as needed.
- **REFERENCE** (FKGL 6.3, 9 words): She may need other nerve pain medications as needed.
- **naive** (FKGL 7.2, 10 words, 0 edits): She might need other medicines for nerve pain if necessary.
    - SARI=25.16  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 4.8, 11 words, 1 edits): She may need other pain medicines for nerve pain as needed.
    - SARI=51.81  crit=0.00  NLIf=0.91  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 1 edits): She may need other nerve pain medicines as needed.
    - SARI=64.54  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 85 - `852`

- **ORIGINAL**  (FKGL 12.4, 7 words): A prophylactic dose of antibiotics was given.
- **REFERENCE** (FKGL 10.7, 7 words): A prevention dose of antibiotics was given.
- **naive** (FKGL 9.6, 10 words, 0 edits): A dose of antibiotics was given to help prevent infection.
    - SARI=66.67  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 12.6, 9 words, 2 edits): A preventive dose of infection-fighting medicine was given.
    - SARI=28.96  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 9.6, 10 words, 2 edits): A protective dose of medicine that kills bacteria was given.
    - SARI=28.96  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 86 - `854`

- **ORIGINAL**  (FKGL 16.2, 6 words): Chronic hypokalemia secondary to chronic diarrhea.
- **REFERENCE** (FKGL 7.6, 9 words): Long term low potassium due to long term diarrhea.
- **naive** (FKGL 13.4, 12 words, 0 edits): The patient has long-lasting low potassium levels caused by ongoing diarrhea.
    - SARI=41.27  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 9.7, 10 words, 0 edits): Long-lasting low potassium caused by long-lasting loose stools.
    - SARI=35.51  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 11.1, 9 words, 0 edits): Long-lasting low potassium caused by ongoing runny poop.
    - SARI=35.24  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 87 - `859`

- **ORIGINAL**  (FKGL 6.6, 4 words): No hepatosplenomegaly or tenderness.
- **REFERENCE** (FKGL 2.3, 9 words): No enlarged liver or spleen or pain when pushed.
- **naive** (FKGL 4.8, 11 words, 0 edits): There is no swelling or tenderness in the liver or spleen.
    - SARI=45.57  crit=0.00  NLIf=0.59  copyjrg=0.50
- **termonly** (FKGL 3.7, 9 words, 1 edits): The liver and spleen are not enlarged or painful.
    - SARI=39.68  crit=0.00  NLIf=0.89  copyjrg=0.00
- **grounded** (FKGL 5.6, 17 words, 0 edits): The liver and spleen are not enlarged, and there is no pain when the area is touched.
    - SARI=41.19  crit=0.00  NLIf=0.14  copyjrg=0.00

### Note 88 - `881`

- **ORIGINAL**  (FKGL 9.1, 11 words): He did not experience his left anterior chest pain with exercise.
- **REFERENCE** (FKGL 5.9, 11 words): He did not experience his left front chest pain with exercise.
- **naive** (FKGL 3.9, 16 words, 0 edits): He did not feel pain in the front left side of his chest when he exercised.
    - SARI=25.89  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 2.6, 11 words, 2 edits): He did not feel his left front chest pain with exercise.
    - SARI=62.40  crit=1.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 2.6, 11 words, 2 edits): He did not feel his left front chest pain with exercise.
    - SARI=62.40  crit=1.00  NLIf=0.97  copyjrg=0.00

### Note 89 - `891`

- **ORIGINAL**  (FKGL 7.6, 9 words): Also, would use it to control the atrial fibrillation.
- **REFERENCE** (FKGL 6.0, 10 words): Also, would use it to control the irregular heart beat
- **naive** (FKGL 7.2, 10 words, 0 edits): Also, she would use it to control the atrial fibrillation.
    - SARI=25.32  crit=0.00  NLIf=0.65  copyjrg=1.00
- **termonly** (FKGL 6.3, 9 words, 1 edits): Also, would use it to control the uneven heartbeat.
    - SARI=66.67  crit=0.00  NLIf=0.85  copyjrg=0.00
- **grounded** (FKGL 7.6, 9 words, 1 edits): Also, would use it to control the irregular heartbeat.
    - SARI=80.00  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 90 - `900`

- **ORIGINAL**  (FKGL 11.1, 8 words): Overall the patient is a seemingly good historian.
- **REFERENCE** (FKGL 11.9, 10 words): Overall the patient is seemingly good at remembering their history
- **naive** (FKGL 8.4, 14 words, 0 edits): The patient seems to be able to give a clear and accurate medical history.
    - SARI=26.28  crit=0.00  NLIf=0.05  copyjrg=0.00
- **termonly** (FKGL 7.6, 14 words, 2 edits): Overall the patient seems to give a clear and reliable account of their health.
    - SARI=37.72  crit=0.00  NLIf=0.06  copyjrg=0.00
- **grounded** (FKGL 7.6, 14 words, 2 edits): Overall the patient appears to give a clear and accurate account of their health.
    - SARI=37.72  crit=0.00  NLIf=0.04  copyjrg=0.00

### Note 91 - `933`

- **ORIGINAL**  (FKGL 3.7, 10 words): No active Crohn 's disease was found during the colonoscopy.
- **REFERENCE** (FKGL 5.9, 14 words): No active Crohn 's disease was found during the camera test through the gut.
- **naive** (FKGL 3.7, 12 words, 0 edits): No signs of active Crohn's disease were seen during the colonoscopy.
    - SARI=19.09  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 9.8, 17 words, 1 edits): No signs of an ongoing bowel condition were seen during the camera test of the large intestine.
    - SARI=16.78  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 9.8, 17 words, 1 edits): No signs of a currently flaring bowel condition were found during the exam of the large intestine.
    - SARI=15.51  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 92 - `935`

- **ORIGINAL**  (FKGL 16.4, 28 words): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have mounting exhaustion and respiratory distress.
- **REFERENCE** (FKGL 15.5, 28 words): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have worsening exhaustion and breathing distress.
- **naive** (FKGL 6.7, 27 words, 0 edits): Shortly after the first check-up, the patient started complaining of chest pain. The nurse noticed she seemed more and more tired and was having trouble breathing.
    - SARI=17.65  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 11.5, 28 words, 1 edits): Shortly after the first check-up, the patient seemed to start complaining of chest pain and looked to the nurse like they had growing tiredness and trouble breathing.
    - SARI=21.96  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 12.2, 31 words, 2 edits): Shortly after the first check-up, the patient seemed to start complaining of chest pain and looked to the nurse to be getting more and more tired and having trouble breathing.
    - SARI=24.00  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 93 - `968`

- **ORIGINAL**  (FKGL 8.2, 8 words): She has been referred for a pacemaker implantation.
- **REFERENCE** (FKGL 7.6, 9 words): She has been referred for a pacemaker fitting surgery.
- **naive** (FKGL 2.5, 10 words, 0 edits): She has been sent to get a pacemaker put in.
    - SARI=23.47  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 1.3, 11 words, 2 edits): She has been sent to get a heart-rhythm device placed.
    - SARI=20.09  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 4.9, 17 words, 2 edits): She has been sent to get a device put in her chest to help control her heartbeat.
    - SARI=20.09  crit=0.00  NLIf=0.86  copyjrg=0.00

### Note 94 - `116`

- **ORIGINAL**  (FKGL -0.7, 8 words): There was some hematoma at the cath site.
- **REFERENCE** (FKGL 5.8, 13 words): There was some swelling due to collection of blood at the catheter site.
- **naive** (FKGL 4.8, 11 words, 0 edits): There was some bruising and swelling where the catheter went in.
    - SARI=52.53  crit=0.00  NLIf=0.77  copyjrg=0.00
- **termonly** (FKGL 2.5, 11 words, 2 edits): There was some bruise-like swelling where the tube went in.
    - SARI=50.36  crit=0.00  NLIf=0.56  copyjrg=0.00
- **grounded** (FKGL 1.0, 9 words, 2 edits): There was some bruising where the tube went in.
    - SARI=49.17  crit=0.00  NLIf=0.53  copyjrg=0.00

### Note 95 - `592`

- **ORIGINAL**  (FKGL 6.3, 9 words): The necrotic tissue was lifted out of the abdomen.
- **REFERENCE** (FKGL 3.7, 9 words): The dead flesh was lifted out of the abdomen.
- **naive** (FKGL 3.8, 8 words, 0 edits): The dead tissue was removed from the belly.
    - SARI=20.96  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 3.7, 9 words, 1 edits): The dead tissue was lifted out of the belly.
    - SARI=53.39  crit=0.00  NLIf=0.99  copyjrg=0.33
- **grounded** (FKGL 3.7, 9 words, 1 edits): The dead tissue was lifted out of the belly.
    - SARI=53.39  crit=0.00  NLIf=0.99  copyjrg=0.33

### Note 96 - `249`

- **ORIGINAL**  (FKGL 6.7, 8 words): Pressure was held and the area was hemostatic.
- **REFERENCE** (FKGL 5.2, 8 words): Pressure was held and the area stopped bleeding.
- **naive** (FKGL 4.0, 7 words, 0 edits): Pressure was applied, and the bleeding stopped.
    - SARI=30.32  crit=0.00  NLIf=0.58  copyjrg=0.00
- **termonly** (FKGL 2.3, 7 words, 1 edits): Pressure was held and the bleeding stopped.
    - SARI=57.96  crit=0.00  NLIf=0.34  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 1 edits): Pressure was held and the area was not bleeding.
    - SARI=67.96  crit=0.00  NLIf=0.71  copyjrg=0.00

### Note 97 - `701`

- **ORIGINAL**  (FKGL 3.7, 9 words): The area was lavaged with some saline and cleared.
- **REFERENCE** (FKGL 3.7, 11 words): The area was washed out with some salt water and cleared.
- **naive** (FKGL 3.7, 9 words, 0 edits): The area was washed with saline and cleaned out.
    - SARI=52.61  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL 3.7, 10 words, 2 edits): The area was washed with some salt water and cleared.
    - SARI=81.54  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.7, 11 words, 2 edits): The area was washed out with some salt water and cleared.
    - SARI=91.67  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 98 - `826`

- **ORIGINAL**  (FKGL 8.2, 8 words): Pain and inability to ambulate brought him in.
- **REFERENCE** (FKGL 6.3, 9 words): Pain and inability to move around brought him in.
- **naive** (FKGL 2.3, 7 words, 0 edits): Pain and trouble walking brought him in.
    - SARI=35.97  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 2.5, 10 words, 1 edits): Pain and not being able to walk brought him in.
    - SARI=38.11  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 2.5, 10 words, 1 edits): Pain and not being able to walk brought him in.
    - SARI=38.11  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 99 - `751`

- **ORIGINAL**  (FKGL 2.3, 8 words): There is a hernia on the left side.
- **REFERENCE** (FKGL 2.9, 12 words): The gut sticks out through the abdomen wall on the left side.
- **naive** (FKGL 2.5, 14 words, 0 edits): There is a bulge or weak spot on the left side of the body.
    - SARI=60.64  crit=0.00  NLIf=0.94  copyjrg=0.00
- **termonly** (FKGL -0.7, 8 words, 1 edits): There is a bulge on the left side.
    - SARI=60.64  crit=0.00  NLIf=0.75  copyjrg=0.00
- **grounded** (FKGL -0.7, 8 words, 1 edits): There is a bulge on the left side.
    - SARI=60.64  crit=0.00  NLIf=0.75  copyjrg=0.00

### Note 100 - `496`

- **ORIGINAL**  (FKGL 8.4, 10 words): Other systems were reviewed and were found to be unremarkable.
- **REFERENCE** (FKGL 4.8, 10 words): Other systems were reviewed and were found to be normal.
- **naive** (FKGL 7.6, 13 words, 0 edits): The doctors checked the other parts of the body and found nothing unusual.
    - SARI=8.52  crit=1.00  NLIf=0.44  copyjrg=0.00
- **termonly** (FKGL 3.7, 9 words, 1 edits): Other systems were checked and found to be normal.
    - SARI=39.50  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.7, 9 words, 1 edits): Other systems were checked and found to be normal.
    - SARI=39.50  crit=1.00  NLIf=0.99  copyjrg=0.00
