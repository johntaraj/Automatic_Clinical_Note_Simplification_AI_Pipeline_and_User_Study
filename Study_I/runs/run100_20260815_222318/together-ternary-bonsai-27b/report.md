# together-ternary-bonsai-27b - run `run100`

- model: `Prism-ML/Ternary-Bonsai-27B` (together, fireworks backend)
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
| **human edit recall** | 99 |  |  | 0.787 | 0.987 | 0.975 | higher is better | > 0.85 | of the jargon the human replaced, how much did we replace |

### 4 faithfulness

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **NLI faithfulness** | 100 |  |  | 0.796 | 0.816 | 0.813 | higher is better | > 0.70 | general-domain MNLI head; absolute values are compressed |
| **NLI completeness** | 100 |  |  | 0.903 | 0.748 | 0.755 | higher is better | > 0.60 | omission is the dominant clinical failure mode, which is why this direction is reported separately |

### 4 readability

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **FKGL drop vs input** | 100 |  |  | 2.88 | 3.58 | 3.15 | higher is better | > +4 grades | gameable by chopping sentences - read with length ratio |
| **Coleman-Liau drop** | 100 |  |  | 4.30 | 4.46 | 3.91 | higher is better | > +4 | none - this is the robustness check on FKGL |
| **length ratio vs reference** | 100 |  |  | 1.20 | 0.97 | 1.03 | descriptive | 0.9-1.3 | descriptive, not a quality score; >1.4 means the model is glossing everything |

### 4 safety

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **critical-error rate** | 100 |  |  | 0.100 | 0.090 | 0.070 | LOWER is better | 0.00 - any value > 0 needs review | fraction of outputs that lost a high-risk slot: negation, uncertainty, laterality, a number/unit, or a drug name |

### 5 attribution

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **attributable rate** | 0.677 | higher is better | > 0.50 | of the edits retrieval demonstrably caused, the fraction with a trustworthy explanation (held-out LDS >= 0.4, clear winner) |
| **held-out LDS (median)** | 0.797 | higher is better | > 0.60 (paper reports 0.6-0.85) | Spearman between the surrogate's predictions and the true log-probs on masks it never saw - how trustworthy the attributions are |
| **helped rate** | 0.482 | descriptive | descriptive - the split is the finding | fraction of edits retrieval made more likely (effect >= 0.10 nats) |
| **hurt rate** | 0.141 | LOWER is better | < 0.10 | fraction of edits retrieval made LESS likely - glossary actively harming the rewrite |
| **top-1 log-prob drop (helped edits)** | 1.48 | higher is better | > 0.5 nats | the paper reports roughly 0.43-0.75 for top-1 across three benchmarks, so this is the number to compare against |
| **winning source is the right term** | 0.917 | higher is better | > 0.80 | the complement is cross-term contamination - the definition of a DIFFERENT word in the same sentence winning the attribution and changing the meaning. Needs no gold labels, which is what makes it the closest thing this family has to a precision score |

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
| **first-attempt success rate** | 100 |  |  | 1.000 | 0.980 | 0.980 | higher is better | > 0.95 | the honest measure of how stable a model is on this task. Reported separately from output_valid_rate because retrying HIDES instability: a model that needs three attempts on a third of the corpus can still finish at output_valid_rate 1.000. Quote both, and remember the retries cost real money |
| **mean generation attempts** | 100 |  |  | 1.000 | 1.020 | 1.030 | LOWER is better | 1.00 | descriptive. Reads as a cost multiplier for the arm: 1.30 means 30% more generation calls than the ideal |
| **copy-jargon rate** | 99 |  |  | 0.213 | 0.013 | 0.025 | LOWER is better | < 0.10 | exactly 1 - human_edit_recall, by construction: every gold term is either recalled or copied. Report it as a restatement, not as separate evidence, and keep it out of the significance family or one result consumes two FDR slots |
| **reference-vocabulary hit (NOT a precision)** | 89 |  |  | 0.663 | 0.742 | 0.730 | higher is better | descriptive only - see caveat | BROKEN AS NAMED, measured 2026-08-15. The support test is `ref_added & sys_content_words`, and `ref_added` is derived from (reference, original) only - it does not depend on the term being scored. So the same verdict is applied to every changed term in a note and the per-note value can only be 0 or 1. Verified on CLEAN93/qwen3p7-plus: 265 of 265 note-arm values are exactly 0.0 or 1.0, and no note has two terms that disagree. One incidental shared word credits every replacement in the sentence. Making this a real precision needs term-to-replacement span alignment, which does not exist yet. Do not quote it as evidence that replacements were correct |
| **definition borrowing** | 89 |  |  | 0.477 | 0.484 | 0.587 | descriptive | descriptive - the arm gap IS the finding | the mechanism behind the grounded-vs-termonly result, measured per note instead of only in analysis/conditional_grounding.py. Deliberately DESCRIPTIVE: grounded is shown the definitions and the other arms are not, so a difference here is expected by construction and testing it would burn an FDR slot to confirm something guaranteed. Read it as 'how much of the glossary's wording ended up in the output', then read what that cost in human_edit_recall and NLI |
| **replacement F1 (inherits a broken precision)** | 99 |  |  | 0.559 | 0.735 | 0.715 | higher is better | descriptive only - see caveat | DEMOTED from paper tier 2026-08-15. Half of it is replacement_precision, which is not per-term (see its caveat), so this cannot support a claim that the system replaced jargon CORRECTLY. Quote human_edit_recall instead - that half is genuinely per-term and is unaffected |
| **rewrite aggressiveness** | 100 |  |  | 0.296 | 0.050 | 0.019 | descriptive | descriptive | NOT an error rate - legitimate restructuring scores here |

### 4 quality

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **SARI** | 100 |  |  | 32.31 | 51.24 | 53.23 | higher is better | 40-60 typical | the references are MINIMAL-EDIT, so SARI rewards not editing. Measured: a perfect rewrite scored 25.97 vs 22.64 for doing nothing. Report, do not lead with it |
| **BERTScore F1** | 100 |  |  | 0.591 | 0.717 | 0.728 | higher is better | 0.4-0.7 rescaled | read the RESCALED value. Until bug 42 the baseline lookup was silently failing for a local model directory, so raw scores were reported and everything landed in 0.90-0.96 - which is why this metric was demoted for having no dynamic range. Rescaled, the same 5 notes span 0.556-0.620, a gap six times wider. The demotion should be re-examined on the full run |

### 4 readability

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **FKGL (absolute)** | 100 | 10.51 | 8.54 | 7.63 | 6.93 | 7.37 | LOWER is better | 6-8 (US grade) | absolute grade is dominated by sentence length; the DROP is the honest number |
| **Coleman-Liau (absolute)** | 100 | 12.78 | 9.80 | 8.48 | 8.33 | 8.87 | LOWER is better | 6-8 | character-based grade level |
| **Flesch Reading Ease** | 100 | 41.1 | 60.0 | 69.2 | 70.1 | 68.0 | higher is better | 60-80 (plain English) | uses the SAME two inputs as FKGL; not independent evidence |
| **FRE gain** | 100 |  |  | 28.1 | 29.0 | 26.9 | higher is better | > +20 | redundant with fkgl_drop |
| **SMOG** | 100 | 11.49 | 9.83 | 8.44 | 8.46 | 8.76 | LOWER is better | 6-8 | calibrated for 30+ sentence passages; very jumpy on one sentence |
| **SMOG drop** | 100 |  |  | 3.05 | 3.03 | 2.73 | higher is better | > +3 | same single-sentence calibration problem |
| **words out** | 100 | 12.2 | 14.8 | 16.4 | 14.0 | 14.8 | descriptive | close to the reference | output length |

### 4 safety

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **drug-name preservation** | 2 |  |  | 1.000 | 0.000 | 0.000 | higher is better | 1.00 - nothing less is acceptable | APPENDIX because of the DENOMINATOR, not the metric: only 2 of the 93 laymaker notes contain a detected drug name, so the mean is two observations wearing a percentage. Report the cases, not the rate. Also read it against tag_policy - under `replace` the pipeline is INSTRUCTED to drop drug names |
| **diagnostic-identity preservation** | 5 |  |  | 1.000 | 1.000 | 1.000 | higher is better | 1.00 - nothing less is acceptable | scored only over a closed curated table of conditions, and only 4 of 93 notes contain one, so the mean is four observations. An unlisted diagnosis is not scored rather than guessed at, so this under-reports rather than over-reports. Report the cases |
| **severity downgrade rate** | 10 |  |  | 0.300 | 0.200 | 0.100 | LOWER is better | 0.00 | 3-tier ordinal lexicon; lay renderings ('very bad') sit at the same tier as their clinical equivalent so correct paraphrase is not penalised. Appendix on denominator: 10 of 93 notes state a severity at all |
| **number/unit preservation** | 14 |  |  | 0.893 | 0.821 | 0.893 | higher is better | 1.00 | all doses and units survive (spelled-out numbers and expanded unit abbreviations count) |
| **negation preservation** | 24 |  |  | 0.875 | 0.917 | 0.958 | higher is better | 1.00 | type-level, so it cannot see WHICH negation was lost |
| **laterality preservation** | 8 |  |  | 0.938 | 0.688 | 0.812 | higher is better | 1.00 | left/right/bilateral/basal survive (instance-level) |
| **uncertainty preservation** | 9 |  |  | 0.667 | 0.778 | 0.778 | higher is better | 1.00 | hedging survives - 'cannot be excluded' must not become 'is present' |

### 5 attribution

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **LDS optimism gap** | 0.080 | LOWER is better | < 0.15 | a methodological result in its own right, not a quality score |
| **top-1 log-prob drop (all edits)** | 0.49 | higher is better | descriptive | NOT comparable to the paper's Figure 4a. Most edits have no source effect at all, so there is nothing to remove and the drop is ~0 by construction; the median over all edits therefore reads as a failure when the method is working. Quote `top1_drop_median_helped` instead |
| **ablation success rate** | 1.000 | higher is better | 1.00 | scoring calls that returned usable log-probs - a transport health check, not a quality metric |

## Attribution detail (stage 5)

`source_effect = log p(edit | full glossary) - log p(edit | no glossary)`. This is the only measurement in the suite that says whether retrieval *caused* an edit.

| quantity | value | meaning |
|---|---:|---|
| edits attributed | 199 | |
| ranked fits | 198 | a source could be ranked |
| flat fits | 1 | scoring worked, no source mattered - a RESULT, not a failure |
| measurement failures | 0 | aim for 0 |
| **helped** | 96 | retrieval made the edit more likely |
| **neutral** | 75 | the model knew it anyway |
| **hurt** | 28 | retrieval made it LESS likely |
| attributable rate | 0.6771 | of helped edits, those with a trustworthy explanation |
| **winning source is the right term** | 0.9167 | of 96 caused edits; the rest are cross-term contamination |
| held-out LDS (median) | 0.7973 | aim > 0.60 |
| in-sample LDS (median) | 0.8772 | for contrast only |
| **LDS optimism gap** | 0.0799 | how much an in-sample number would overstate faithfulness |
| edits with no LDS | 61 | glossary too small for a genuinely unseen held-out block |
| **top-1 drop, helped edits** | 1.4845 | paper Eq. 1 over the 96 edits where a source mattered - the number comparable to the paper's Fig. 4a |
| **top-3 drop, helped edits** | 2.5331 | same, removing the top three |
| top-1 drop, ALL edits | 0.4864 | ~0 by construction on the 75 edits with no source effect; do NOT quote this against the paper |
| ablation success | 1.0 | transport health |

> Surrogate target: **logit-scaled probability**, per ContextCite Algorithm 1 line 4. Bucketing uses the log-probability difference, which answers "would the model have produced this anyway?". Both are stored per edit.

**Threshold sensitivity** (the helped/hurt split depends on an arbitrary cut-off, so it is swept):

| eps (nats) | helped | neutral | hurt | attributable |
|---:|---:|---:|---:|---:|
| 0.05 | 138 | 18 | 43 | 0.5942 |
| 0.1 | 131 | 27 | 41 | 0.6183 |
| 0.25 | 120 | 42 | 37 | 0.6333 |
| 0.693 | 96 | 75 | 28 | 0.6771 |
| 1.0 | 79 | 98 | 22 | 0.6709 |

### Does grounding help more on rare terms?

| Zipf stratum | edits | helped | neutral | hurt | helped rate | mean effect (nats) |
|---|---:|---:|---:|---:|---:|---:|
| very_rare | 56 | 26 | 19 | 10 | 0.4727 | 1.7839 |
| rare | 69 | 37 | 25 | 7 | 0.5362 | 2.1554 |
| uncommon | 58 | 28 | 22 | 8 | 0.4828 | 0.9069 |
| common | 15 | 4 | 9 | 2 | 0.2667 | 0.9524 |
| unknown | 2 | 1 | 0 | 1 | 0.5 | 0.5213 |

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

200 rationales audited.

| metric | value | direction | target |
|---|---:|---|---|
| rationale fabrications | 0.100 | LOWER is better | < 0.05 |
| rationale slot omissions | 0.000 | LOWER is better | < 0.40 |
| rationale fact recall | 1.000 | higher is better | > 0.85 |
| rationale source correct | 1.000 | higher is better | > 0.95 |
| rationale quote verified | 0.995 | higher is better | 1.00 |
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
  sari                       100   +1    51.239    32.309  +18.930    [+14.76, +23.23]   0.0000  0.0000*  +0.83
  bertscore_f1               100   +1     0.717     0.591   +0.125      [+0.10, +0.15]   0.0000  0.0000*  +0.79
  fkgl_drop                  100   +1     3.583     2.885   +0.697      [+0.25, +1.15]   0.0018  0.0047*  +0.34
  smog_drop                  100   +1     3.032     3.048   -0.017      [-0.76, +0.73]   0.6017   0.7111  -0.01
  coleman_liau_drop          100   +1     4.455     4.297   +0.158      [-0.46, +0.75]   0.2105   0.3910  +0.09
  nli_faithfulness           100   +1     0.816     0.796   +0.020      [-0.04, +0.08]   0.4284   0.6188  +0.02
  nli_completeness           100   +1     0.747     0.903   -0.155      [-0.22, -0.10]   1.0000   1.0000  -0.60
  human_edit_recall           99   +1     0.987     0.787   +0.199      [+0.12, +0.28]   0.0000  0.0002*  +0.90
  replacement_precision       89   +1     0.742     0.663   +0.079      [-0.01, +0.18]   0.1107   0.2400  +0.37
  replacement_f1              99   +1     0.735     0.559   +0.176      [+0.07, +0.28]   0.0006  0.0021*  +0.58
  critical_error             100   -1     0.090     0.100   -0.010      [-0.05, +0.03]   0.4248   0.6188  +0.20
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.821     0.893   -0.071      [-0.21, +0.00]   0.6862   0.7434  -1.00
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.200     0.300   -0.100      [-0.40, +0.20]   0.5000   0.6500  +0.33

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
  sari                       100   +1    53.231    51.239   +1.993      [-0.63, +4.67]   0.0307   0.3992  +0.26
  bertscore_f1               100   +1     0.728     0.717   +0.012      [-0.01, +0.03]   0.1616   0.7543  +0.14
  fkgl_drop                  100   +1     3.145     3.583   -0.437      [-0.84, -0.02]   0.9960   0.9987  -0.37
  smog_drop                  100   +1     2.733     3.032   -0.299      [-0.90, +0.30]   0.9448   0.9987  -0.17
  coleman_liau_drop          100   +1     3.912     4.455   -0.543      [-1.10, +0.06]   0.9987   0.9987  -0.37
  nli_faithfulness           100   +1     0.813     0.816   -0.004      [-0.05, +0.04]   0.3205   0.7543  +0.04
  nli_completeness           100   +1     0.755     0.747   +0.008      [-0.03, +0.04]   0.3266   0.7543  +0.06
  human_edit_recall           99   +1     0.975     0.987   -0.012      [-0.03, +0.00]   0.6525   0.8483  -1.00
  replacement_precision       98   +1     0.724     0.735   -0.010      [-0.08, +0.07]   0.5694   0.8483  -0.07
  replacement_f1              99   +1     0.715     0.735   -0.020      [-0.10, +0.06]   0.6352   0.8483  -0.12
  critical_error             100   -1     0.070     0.090   -0.020      [-0.05, +0.00]   0.3481   0.7543  +1.00
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.821   +0.071      [+0.00, +0.21]   0.3138   0.7543  +1.00
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.100     0.200   -0.100      [-0.30, +0.00]   0.5000   0.8483  +1.00

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
  sari                       100   +1    53.231    32.309  +20.923    [+16.73, +25.23]   0.0000  0.0000*  +0.89
  bertscore_f1               100   +1     0.728     0.591   +0.137      [+0.11, +0.16]   0.0000  0.0000*  +0.84
  fkgl_drop                  100   +1     3.145     2.885   +0.260      [-0.26, +0.78]   0.1247   0.3242  +0.14
  smog_drop                  100   +1     2.733     3.048   -0.316      [-1.15, +0.54]   0.8494   0.9202  -0.08
  coleman_liau_drop          100   +1     3.912     4.297   -0.385      [-1.02, +0.26]   0.8238   0.9202  -0.11
  nli_faithfulness           100   +1     0.813     0.796   +0.016      [-0.04, +0.07]   0.4056   0.5858  +0.04
  nli_completeness           100   +1     0.755     0.903   -0.147      [-0.21, -0.08]   1.0000   1.0000  -0.55
  human_edit_recall           99   +1     0.975     0.787   +0.187      [+0.11, +0.27]   0.0001  0.0003*  +0.89
  replacement_precision       89   +1     0.730     0.663   +0.067      [-0.03, +0.17]   0.1537   0.3331  +0.27
  replacement_f1              99   +1     0.715     0.559   +0.156      [+0.05, +0.26]   0.0027  0.0087*  +0.51
  critical_error             100   -1     0.070     0.100   -0.030      [-0.08, +0.02]   0.2882   0.4683  +0.43
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.893   +0.000      [-0.21, +0.21]   0.5000   0.6500  +0.00
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.100     0.300   -0.200      [-0.50, +0.00]   0.2500   0.4643  +1.00

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

## Clinical-safety flags

- note 2 / `naive` / **uncertainty** (critical): lost ['can not be excluded']
- note 2 / `termonly` / **negation** (critical): lost ['can not be excluded', 'excluded', 'not']
- note 3 / `termonly` / **severity** (warning): lost ['marked']
- note 3 / `termonly` / **severity_downgrade** (warning): lost ['tier 2']
- note 5 / `naive` / **temporality** (warning): lost ['chronic', 'history of']
- note 9 / `naive` / **number_unit** (critical): lost ['1']
- note 9 / `termonly` / **number_unit** (critical): lost ['1']
- note 9 / `grounded` / **number_unit** (critical): lost ['1']
- note 10 / `naive` / **temporality** (warning): lost ['new onset']
- note 10 / `termonly` / **temporality** (warning): lost ['new onset']
- note 10 / `grounded` / **temporality** (warning): lost ['new onset']
- note 17 / `naive` / **severity** (warning): lost ['mild']
- note 21 / `naive` / **negation** (critical): lost ['no']
- note 24 / `naive` / **severity** (warning): lost ['obvious']
- note 26 / `naive` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `termonly` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `termonly` / **temporality** (warning): lost ['acute']
- note 26 / `grounded` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `grounded` / **temporality** (warning): lost ['acute']
- note 28 / `naive` / **uncertainty** (critical): lost ['consideration']
- note 28 / `termonly` / **uncertainty** (critical): lost ['consideration']
- note 28 / `grounded` / **uncertainty** (critical): lost ['consideration']
- note 36 / `naive` / **temporality** (warning): lost ['status post']
- note 38 / `naive` / **severity** (warning): lost ['severe']
- note 38 / `naive` / **severity_downgrade** (critical): lost ['grave severity stated as mild or absent']
- note 39 / `naive` / **severity** (warning): lost ['significant']
- note 39 / `naive` / **severity_downgrade** (warning): lost ['tier 2']
- note 42 / `naive` / **temporality** (warning): lost ['now']
- note 44 / `naive` / **negation** (critical): lost ['not']
- note 44 / `naive` / **severity** (warning): lost ['significant']
- note 44 / `naive` / **severity_downgrade** (warning): lost ['tier 2']
- note 44 / `termonly` / **severity** (warning): lost ['significant']
- note 44 / `termonly` / **severity_downgrade** (warning): lost ['tier 2']
- note 44 / `grounded` / **severity** (warning): lost ['significant']
- note 44 / `grounded` / **severity_downgrade** (warning): lost ['tier 2']
- note 45 / `naive` / **severity** (warning): lost ['slight']
- note 51 / `termonly` / **laterality** (critical): lost ['lateral']
- note 51 / `grounded` / **laterality** (critical): lost ['lateral']
- note 60 / `naive` / **temporality** (warning): lost ['now']
- note 67 / `termonly` / **drug** (policy): lost ['prednisone']
- note 67 / `grounded` / **drug** (policy): lost ['prednisone']
- note 70 / `termonly` / **laterality** (critical): lost ['bilateral']
- note 70 / `termonly` / **number_unit** (critical): lost ['2']
- note 70 / `grounded` / **number_unit** (critical): lost ['2']
- note 78 / `naive` / **number_unit** (critical): lost ['1']
- note 78 / `termonly` / **number_unit** (critical): lost ['1']
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
- **naive** (FKGL 12.7, 26 words, 0 edits): He lost the ability to feel pleasure and lost interest in social activities, and he had trouble sleeping because he woke up often and felt restless.
    - SARI=25.30  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 15.2, 20 words, 2 edits): He became unable to feel pleasure and uninterested in social activities, and had difficulty sleeping for frequent waking and restlessness.
    - SARI=74.23  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 14.5, 21 words, 2 edits): He became unable to feel pleasure and not interested in social activities, and had difficulty sleeping for frequent waking and restlessness.
    - SARI=72.24  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 2 - `18`

- **ORIGINAL**  (FKGL 14.3, 6 words): Myocardial infarction can not be excluded.
- **REFERENCE** (FKGL 4.5, 6 words): Heart attack can not be excluded.
- **naive** (FKGL 4.8, 11 words, 0 edits): Doctors cannot rule out that the patient has a heart attack.
    - SARI=19.79  crit=1.00  NLIf=0.80  copyjrg=0.00
- **termonly** (FKGL 4.0, 7 words, 1 edits): A heart attack might still be happening.
    - SARI=25.97  crit=1.00  NLIf=0.63  copyjrg=0.00
- **grounded** (FKGL 2.3, 7 words, 2 edits): A heart attack cannot be ruled out.
    - SARI=25.97  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 3 - `21`

- **ORIGINAL**  (FKGL 6.0, 10 words): There was marked hematoma and swelling within the subdeltoid bursa.
- **REFERENCE** (FKGL 7.6, 14 words): There was obvious collection of blood and swelling within the side of the shoulder.
- **naive** (FKGL 7.7, 17 words, 0 edits): The patient had a large collection of blood and swelling inside the small sac under the shoulder.
    - SARI=42.12  crit=0.00  NLIf=0.64  copyjrg=0.00
- **termonly** (FKGL 7.6, 14 words, 3 edits): There was clear blood collection and swelling within the fluid sac under the shoulder.
    - SARI=71.44  crit=0.00  NLIf=0.82  copyjrg=0.00
- **grounded** (FKGL 5.9, 11 words, 3 edits): There was severe bruise and swelling within the shoulder fluid pouch.
    - SARI=69.29  crit=0.00  NLIf=0.69  copyjrg=0.00

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
- **naive** (FKGL 6.3, 18 words, 0 edits): She said she gets bladder cramps when she pees and that she has had long-term bladder infections.
    - SARI=11.95  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 9.2, 20 words, 3 edits): She complained of bladder cramps when she peed and she said she has a history of long-lasting bladder infections.
    - SARI=19.15  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 13.7, 28 words, 3 edits): She did complain of sudden painful bladder tightness when she emptied her bladder and she did say that she has a history of long-lasting urinary tract infections.
    - SARI=37.43  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 6 - `32`

- **ORIGINAL**  (FKGL 7.2, 10 words): There was no instability of the knee and no effusion.
- **REFERENCE** (FKGL 8.0, 11 words): There was no instability of the knee and no fluid collection.
- **naive** (FKGL 3.6, 16 words, 0 edits): The patient's knee did not feel loose or give way, and there was no swelling.
    - SARI=18.91  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 3.8, 12 words, 2 edits): There was no giving way of the knee and no fluid buildup.
    - SARI=45.00  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 4.8, 11 words, 2 edits): There was no wobbling of the knee and no fluid buildup.
    - SARI=46.48  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 7 - `64`

- **ORIGINAL**  (FKGL 4.9, 13 words): Two days later, the pain resolved and she has not had a recurrence.
- **REFERENCE** (FKGL 5.0, 14 words): Two days later, the pain got better and she has not had a recurrence.
- **naive** (FKGL 3.1, 13 words, 0 edits): Two days later, the pain stopped and she did not get it again.
    - SARI=32.27  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.6, 15 words, 2 edits): Two days later, the pain went away and she has not had it come back.
    - SARI=46.29  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.6, 15 words, 2 edits): Two days later, the pain went away and she has not had it come back.
    - SARI=46.29  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 8 - `81`

- **ORIGINAL**  (FKGL 14.1, 7 words): Description : Fever, otitis media, and possible sepsis.
- **REFERENCE** (FKGL 15.6, 8 words): Description : Fever, ear infection, and possible general infection.
- **naive** (FKGL 8.8, 12 words, 0 edits): The patient has a fever, a middle ear infection, and possible sepsis.
    - SARI=48.02  crit=0.00  NLIf=0.77  copyjrg=0.50
- **termonly** (FKGL 14.1, 10 words, 2 edits): Description : Fever, middle ear infection, and possible whole-body infection.
    - SARI=60.71  crit=0.00  NLIf=0.67  copyjrg=0.00
- **grounded** (FKGL 14.1, 9 words, 2 edits): Description: Fever, ear infection, and possible serious blood infection.
    - SARI=68.98  crit=0.00  NLIf=0.68  copyjrg=0.00

### Note 9 - `101`

- **ORIGINAL**  (FKGL 7.6, 13 words): Currently, primary complaint is one of fatigue that she feels throughout the day.
- **REFERENCE** (FKGL 8.4, 14 words): Currently, primary complaint is one of feeling tired that she feels throughout the day.
- **naive** (FKGL 4.0, 13 words, 0 edits): Right now, her main problem is fatigue that she feels throughout the day.
    - SARI=29.50  crit=1.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 6.8, 12 words, 2 edits): Currently, the main problem is tiredness that she feels throughout the day.
    - SARI=35.71  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.8, 12 words, 2 edits): Currently, her main problem is tiredness that she feels throughout the day.
    - SARI=35.71  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 10 - `108`

- **ORIGINAL**  (FKGL 12.3, 19 words): He has noted some stool irregularity with occasional loose stools and new onset of pain predominantly in left neck.
- **REFERENCE** (FKGL 12.3, 19 words): He has noted some poop irregularity with occasional loose poop and new onset of pain predominantly in left neck.
- **naive** (FKGL 12.5, 24 words, 0 edits): He has noticed irregular bowel movements with occasional loose stools, and he recently started feeling pain mostly in the left side of his neck.
    - SARI=18.57  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 11.1, 18 words, 4 edits): He has noted some irregular bowel movements with occasional runny stools and sudden pain mostly in left neck.
    - SARI=27.99  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 11.8, 22 words, 4 edits): He has noted some irregular bowel movements with occasional watery poop and a recent start of pain mostly in the left neck.
    - SARI=31.64  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 11 - `143`

- **ORIGINAL**  (FKGL 11.7, 12 words): Description : The patient presents for a followup for history of erythema nodosum.
- **REFERENCE** (FKGL 12.6, 17 words): Description : The patient presents for a followup for history of red, painful tender lumps around fatty areas.
- **naive** (FKGL 8.4, 17 words, 0 edits): The patient comes in for a follow-up visit because of a past case of erythema nodosum.
    - SARI=10.55  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 7.6, 15 words, 1 edits): Description : The patient comes in for a followup for a history of red skin bumps.
    - SARI=38.10  crit=0.00  NLIf=0.57  copyjrg=0.00
- **grounded** (FKGL 8.8, 12 words, 1 edits): Description : The patient presents for a followup for history of red skin.
    - SARI=74.07  crit=0.00  NLIf=0.60  copyjrg=0.00

### Note 12 - `144`

- **ORIGINAL**  (FKGL 7.5, 22 words): She was iron deficient last year, and with her multiple surgeries and poor p. o. intake, may have become iron deficient again.
- **REFERENCE** (FKGL 12.4, 23 words): She was iron deficient last year, and with her multiple surgeries and poor food and fluid intake, may have become iron deficient again.
- **naive** (FKGL 10.4, 26 words, 0 edits): She did not have enough iron last year, and because she had many surgeries and did not eat well, she might not have enough iron again.
    - SARI=15.64  crit=0.00  NLIf=0.17  copyjrg=0.00
- **termonly** (FKGL 10.0, 24 words, 3 edits): She was low on iron last year, and with her multiple surgeries and poor intake by mouth, may have become low on iron again.
    - SARI=37.42  crit=0.00  NLIf=0.08  copyjrg=0.00
- **grounded** (FKGL 10.7, 22 words, 3 edits): She was lacking iron last year, and with her multiple surgeries and poor intake by mouth, may have become lacking iron again.
    - SARI=37.42  crit=0.00  NLIf=0.06  copyjrg=0.00

### Note 13 - `150`

- **ORIGINAL**  (FKGL 9.1, 15 words): We will schedule him for the Holter monitor and refer him back to his cardiologist.
- **REFERENCE** (FKGL 10.6, 16 words): We will schedule him for the continuous heart monitor and refer him back to his cardiologist.
- **naive** (FKGL 8.0, 22 words, 0 edits): We will set up an appointment for him to wear a Holter monitor and send him back to see his heart doctor.
    - SARI=18.58  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 6.1, 16 words, 2 edits): We will schedule him for the heart recorder and refer him back to his heart doctor.
    - SARI=50.65  crit=0.00  NLIf=0.90  copyjrg=0.00
- **grounded** (FKGL 8.7, 20 words, 2 edits): We will schedule him for a portable machine for recording heart beats and refer him back to his heart doctor.
    - SARI=43.95  crit=0.00  NLIf=0.74  copyjrg=0.00

### Note 14 - `161`

- **ORIGINAL**  (FKGL 11.1, 8 words): The patient wished to proceed with operative intervention.
- **REFERENCE** (FKGL 6.7, 8 words): The patient wished to proceed with an operation
- **naive** (FKGL 6.7, 8 words, 0 edits): The patient wanted to go ahead with surgery.
    - SARI=22.50  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.4, 6 words, 1 edits): The patient wanted to have surgery.
    - SARI=20.56  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.2, 8 words, 2 edits): The patient wished to go forward with surgery.
    - SARI=41.60  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 15 - `178`

- **ORIGINAL**  (FKGL 7.2, 10 words): A KUB was obtained showing an abnormal bowel gas pattern.
- **REFERENCE** (FKGL 8.4, 17 words): An x-ray of the kidney, ureter and bladder was obtained showing an abnormal bowel gas pattern.
- **naive** (FKGL 9.7, 13 words, 0 edits): An abdominal X-ray was taken and showed unusual gas in the intestines.
    - SARI=17.74  crit=0.00  NLIf=0.88  copyjrg=0.00
- **termonly** (FKGL 7.6, 10 words, 2 edits): A stomach X-ray was taken showing unusual gas spots.
    - SARI=15.18  crit=0.00  NLIf=0.69  copyjrg=0.00
- **grounded** (FKGL 9.1, 16 words, 2 edits): A kidney and bladder x-ray was done showing an unusual gas pattern in the intestines.
    - SARI=25.66  crit=0.00  NLIf=0.48  copyjrg=0.00

### Note 16 - `185`

- **ORIGINAL**  (FKGL 12.3, 19 words): She has been sedated with Ativan and came into the emergency room obtunded and unable to give any history.
- **REFERENCE** (FKGL 12.3, 20 words): She has been sedated with Ativan and came into the emergency room very drowsy and unable to give any history.
- **naive** (FKGL 13.0, 25 words, 0 edits): She was given a sedative called Ativan and went to the emergency room feeling very confused and unable to tell the doctors what happened before.
    - SARI=18.51  crit=0.00  NLIf=0.74  copyjrg=0.00
- **termonly** (FKGL 11.8, 23 words, 3 edits): She has been put to sleep with a sleeping medicine and came into the emergency room confused and unable to give any history.
    - SARI=39.08  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 12.9, 24 words, 3 edits): She has been made sleepy with a calming medicine and came into the emergency room not fully alert and unable to give any history.
    - SARI=39.08  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 17 - `202`

- **ORIGINAL**  (FKGL 4.4, 15 words): He has no edema now, but has had some mild leg swelling in the past.
- **REFERENCE** (FKGL 3.6, 15 words): He has no swelling now, but has had some mild leg swelling in the past.
- **naive** (FKGL 6.4, 20 words, 0 edits): He does not have any swelling now, but he did have a little swelling in his legs in the past.
    - SARI=20.62  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.6, 15 words, 1 edits): He has no swelling now, but has had some mild leg swelling in the past.
    - SARI=91.67  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.6, 15 words, 1 edits): He has no swelling now, but has had some mild leg swelling in the past.
    - SARI=91.67  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 18 - `231`

- **ORIGINAL**  (FKGL 21.0, 3 words): Mild secondary hyperparathyroidism.
- **REFERENCE** (FKGL 14.7, 5 words): Mild secondary hyperactive parathyroid gland
- **naive** (FKGL 11.6, 25 words, 0 edits): The patient has a mild overactivity of the parathyroid glands that is caused by another health issue rather than a problem with the glands themselves.
    - SARI=22.95  crit=0.00  NLIf=0.73  copyjrg=0.00
- **termonly** (FKGL 10.4, 6 words, 1 edits): Mild high calcium from another condition.
    - SARI=22.22  crit=0.00  NLIf=0.10  copyjrg=0.00
- **grounded** (FKGL 9.1, 7 words, 1 edits): Mild second condition where blood calcium rises.
    - SARI=22.22  crit=0.00  NLIf=0.30  copyjrg=0.00

### Note 19 - `248`

- **ORIGINAL**  (FKGL 10.6, 16 words): Otherwise, a complete review of systems was obtained and was negative except for as mentioned above.
- **REFERENCE** (FKGL 9.8, 16 words): Otherwise, a complete review of systems was obtained and was normal except for as mentioned above.
- **naive** (FKGL 10.4, 19 words, 0 edits): Otherwise, the patient's body systems were checked and found to be normal, except for the problems already mentioned.
    - SARI=15.32  crit=0.00  NLIf=0.04  copyjrg=0.00
- **termonly** (FKGL 7.7, 17 words, 3 edits): Otherwise, a full body check was done and showed no problems except for what was mentioned above.
    - SARI=16.30  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 9.1, 17 words, 3 edits): Otherwise, a complete body symptom check was asked and was nothing wrong except for as mentioned above.
    - SARI=29.64  crit=0.00  NLIf=0.77  copyjrg=0.00

### Note 20 - `277`

- **ORIGINAL**  (FKGL 7.6, 16 words): Symptoms are worse when sitting for any length of time, such as driving a motor vehicle.
- **REFERENCE** (FKGL 5.2, 15 words): Symptoms are worse when sitting for any length of time, such as driving a car.
- **naive** (FKGL 6.7, 20 words, 0 edits): The patient's symptoms get worse when they sit for any amount of time, such as when driving a car.
    - SARI=28.35  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.2, 15 words, 1 edits): Symptoms are worse when sitting for any length of time, such as driving a car.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.2, 15 words, 1 edits): Symptoms are worse when sitting for any length of time, such as driving a car.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 21 - `290`

- **ORIGINAL**  (FKGL 12.8, 9 words): Forearm, elbow and shoulder exams reveal no neurologic compromise.
- **REFERENCE** (FKGL 7.6, 9 words): Forearm, elbow and shoulder exams reveal no nerve problems
- **naive** (FKGL 8.4, 17 words, 0 edits): The exams of the forearm, elbow, and shoulder show that the patient's nerves are working normally.
    - SARI=34.76  crit=1.00  NLIf=0.72  copyjrg=0.00
- **termonly** (FKGL 7.6, 9 words, 1 edits): Forearm, elbow and shoulder exams reveal no nerve damage.
    - SARI=83.33  crit=0.00  NLIf=0.90  copyjrg=0.00
- **grounded** (FKGL 7.6, 9 words, 1 edits): Forearm, elbow and shoulder exams reveal no nerve damage.
    - SARI=83.33  crit=0.00  NLIf=0.90  copyjrg=0.00

### Note 22 - `296`

- **ORIGINAL**  (FKGL 13.7, 12 words): Thereafter, the local anesthesia was injected into the area around the tumor.
- **REFERENCE** (FKGL 11.7, 12 words): Thereafter, the numbing agent was injected into the area around the tumor.
- **naive** (FKGL 11.3, 13 words, 0 edits): After that, the numbing medicine was injected into the area around the tumor.
    - SARI=65.67  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 10.4, 13 words, 2 edits): After that, the numbing medicine was injected into the area around the lump.
    - SARI=56.27  crit=0.00  NLIf=0.80  copyjrg=0.00
- **grounded** (FKGL 10.4, 13 words, 3 edits): After that, a numbing medicine was injected into the area around the lump.
    - SARI=54.00  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 23 - `307`

- **ORIGINAL**  (FKGL 3.7, 11 words): There is no numbness or paresthesias in the hand or arm.
- **REFERENCE** (FKGL 5.8, 12 words): There is no numbness or abnormal sensation in the hand or arm.
- **naive** (FKGL 4.8, 12 words, 0 edits): The patient has no numbness or tingling in the hand or arm.
    - SARI=44.27  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 3.7, 11 words, 1 edits): There is no numbness or tingling in the hand or arm.
    - SARI=66.67  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 3.7, 11 words, 1 edits): There is no numbness or tingling in the hand or arm.
    - SARI=66.67  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 24 - `357`

- **ORIGINAL**  (FKGL 7.6, 16 words): I do not think she has an obvious current abscessed lesion, although there is some drainage.
- **REFERENCE** (FKGL 7.7, 17 words): I do not think she has an obvious current collection of pus, although there is some drainage.
- **naive** (FKGL 6.4, 20 words, 0 edits): I do not think she has a clear pocket of pus right now, although some fluid is still coming out.
    - SARI=36.42  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 7.8, 19 words, 2 edits): I do not think she has an obvious current pus-filled sore, although there is some fluid coming out.
    - SARI=58.94  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 7.8, 19 words, 2 edits): I do not think she has an obvious current pus-filled sore, although there is some fluid leaking out.
    - SARI=58.94  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 25 - `358`

- **ORIGINAL**  (FKGL 9.1, 11 words): At this time, we would rehydrate with intravenous fluids and reassess.
- **REFERENCE** (FKGL 5.8, 13 words): At this time, we would rehydrate with fluids through the vein and reassess.
- **naive** (FKGL 9.8, 20 words, 0 edits): At this time, the medical team would give IV fluids to restore hydration and check the patient's condition again.
    - SARI=26.90  crit=0.00  NLIf=0.41  copyjrg=0.00
- **termonly** (FKGL 5.2, 15 words, 3 edits): At this time, we would restore water with fluids through a vein and check again.
    - SARI=51.04  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 6.1, 16 words, 3 edits): At this time, we would restore fluids with fluids given through a vein and check again.
    - SARI=48.75  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 26 - `380`

- **ORIGINAL**  (FKGL 14.3, 6 words): Findings are compatible with acute appendicitis.
- **REFERENCE** (FKGL 12.8, 9 words): Findings are compatible with acute inflammation of the appendix
- **naive** (FKGL 8.4, 10 words, 0 edits): The test results match what doctors expect for acute appendicitis.
    - SARI=8.63  crit=1.00  NLIf=0.29  copyjrg=1.00
- **termonly** (FKGL 7.4, 7 words, 1 edits): The test results suggest an inflamed appendix.
    - SARI=10.95  crit=1.00  NLIf=0.92  copyjrg=0.00
- **grounded** (FKGL 8.4, 6 words, 1 edits): The results suggest a swollen appendix.
    - SARI=11.25  crit=1.00  NLIf=0.88  copyjrg=0.00

### Note 27 - `391`

- **ORIGINAL**  (FKGL 10.5, 18 words): She denies weight loss, but acknowledged decreased appetite and increased generalized fatigue for the past 3-4 months.
- **REFERENCE** (FKGL 10.5, 18 words): She denies weight loss, but acknowledged reduced appetite and more generalized tiredness for the past 3-4 months.
- **naive** (FKGL 9.4, 28 words, 0 edits): She says she has not lost any weight, but she admits she has been eating less and feeling more tired all over for the past 3-4 months.
    - SARI=43.06  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.2, 24 words, 3 edits): She says she did not have weight loss, but said she was eating less and felt more tired for the past 3-4 months.
    - SARI=47.57  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 7.5, 25 words, 4 edits): She says she did not have weight loss, but admitted she wants less food and feels tired all over for the past 3-4 months.
    - SARI=46.38  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 28 - `392`

- **ORIGINAL**  (FKGL 21.8, 5 words): Consideration given to completion thyroidectomy.
- **REFERENCE** (FKGL 11.5, 9 words): Consideration given to remove remaining parts of the thyroid
- **naive** (FKGL 7.6, 14 words, 0 edits): The doctors are thinking about removing the rest of the patient's thyroid gland.
    - SARI=25.04  crit=1.00  NLIf=0.34  copyjrg=0.00
- **termonly** (FKGL 11.1, 8 words, 1 edits): The doctors are thinking about finishing thyroid surgery.
    - SARI=23.77  crit=1.00  NLIf=0.60  copyjrg=0.00
- **grounded** (FKGL 7.6, 13 words, 1 edits): The doctors are thinking about surgery to remove the rest of the thyroid.
    - SARI=34.31  crit=1.00  NLIf=0.14  copyjrg=0.00

### Note 29 - `394`

- **ORIGINAL**  (FKGL 10.5, 19 words): She notes that she had epistaxis a few days ago, requiring nasal packing and fortunately that had resolved now.
- **REFERENCE** (FKGL 9.5, 21 words): She notes that she had a nose bleed a few days ago, requiring nose packing and fortunately that had resolved now.
- **naive** (FKGL 8.8, 23 words, 0 edits): She mentions that she had a nosebleed a few days ago that needed packing in her nose, and luckily it has stopped now.
    - SARI=33.64  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 8.3, 21 words, 4 edits): She notes that she had a nosebleed a few days ago, needing packing in the nose and fortunately that stopped now.
    - SARI=46.80  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 8.5, 22 words, 4 edits): She notes that she had a nosebleed a few days ago, needing packing in her nose and fortunately that had gone now.
    - SARI=50.21  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 30 - `396`

- **ORIGINAL**  (FKGL 8.9, 9 words): I also explained to the patient about conscious sedation.
- **REFERENCE** (FKGL 8.9, 9 words): I also explained to the patient about awake sedation.
- **naive** (FKGL 9.6, 10 words, 0 edits): The doctor also explained to the patient about conscious sedation.
    - SARI=25.32  crit=0.00  NLIf=0.39  copyjrg=1.00
- **termonly** (FKGL 8.9, 9 words, 1 edits): I also explained to the patient about calming medicine.
    - SARI=61.94  crit=0.00  NLIf=0.92  copyjrg=0.00
- **grounded** (FKGL 6.7, 14 words, 1 edits): I also explained to the patient about light sedation where they wake when touched.
    - SARI=66.67  crit=0.00  NLIf=0.00  copyjrg=0.00

### Note 31 - `762`

- **ORIGINAL**  (FKGL 5.2, 8 words): Palpation of her right knee reveals no crepitus.
- **REFERENCE** (FKGL 5.0, 9 words): Feeling of her right knee reveals no crunchy feeling.
- **naive** (FKGL 3.7, 10 words, 0 edits): Touching her right knee shows no grinding or clicking sound.
    - SARI=28.93  crit=0.00  NLIf=0.77  copyjrg=0.00
- **termonly** (FKGL 3.8, 8 words, 1 edits): Touching her right knee reveals no cracking sounds.
    - SARI=51.01  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 3.8, 8 words, 1 edits): Feeling her right knee reveals no popping sound.
    - SARI=54.35  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 32 - `427`

- **ORIGINAL**  (FKGL 10.1, 14 words): She stepped on ideas, concerns and expectations the evening prior and twisted her ankle.
- **REFERENCE** (FKGL 4.8, 11 words): She stepped on ice the evening prior and twisted her ankle.
- **naive** (FKGL 9.8, 17 words, 0 edits): She was distracted by her thoughts, worries, and expectations the evening before, so she twisted her ankle.
    - SARI=27.34  crit=0.00  NLIf=0.93
- **termonly** (FKGL 10.1, 14 words, 1 edits): She stepped on ideas, concerns and expectations the evening before and twisted her ankle.
    - SARI=19.14  crit=0.00  NLIf=0.99
- **grounded** (FKGL 10.1, 14 words, 1 edits): She stepped on ideas, concerns and expectations the evening before and twisted her ankle.
    - SARI=19.14  crit=0.00  NLIf=0.99

### Note 33 - `439`

- **ORIGINAL**  (FKGL 14.1, 9 words): Modifying Factors : Patient 's condition is aggravated by throwing.
- **REFERENCE** (FKGL 9.6, 10 words): Modifying Factors : Patient 's condition is made worse by throwing.
- **naive** (FKGL 3.8, 9 words, 0 edits): The patient's condition gets worse when they throw.
    - SARI=26.63  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.9, 12 words, 2 edits): What affects it : The patient's condition is made worse by throwing.
    - SARI=60.75  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 4.8, 13 words, 1 edits): Things that change it : The patient's condition is made worse by throwing.
    - SARI=58.98  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 34 - `451`

- **ORIGINAL**  (FKGL 21.3, 10 words): History of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis and kidney stones.
- **REFERENCE** (FKGL 14.9, 13 words): History of joint inflammation, bone degeneration, underactive thyroid, hay fever and kidney stones.
- **naive** (FKGL 9.9, 20 words, 0 edits): The patient has a history of joint wear and tear, weak bones, an underactive thyroid, allergic nose, and kidney stones.
    - SARI=61.91  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 6.8, 15 words, 5 edits): History of stiff joints, weak bones, slow thyroid, nose allergies and stones in the kidneys.
    - SARI=41.27  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 8.4, 17 words, 5 edits): History of worn-out joints, weak bones, an underactive thyroid, hay fever, and stones in the kidneys.
    - SARI=49.73  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 35 - `465`

- **ORIGINAL**  (FKGL 15.8, 7 words): The ultrasound was negative for intracranial hemorrhage.
- **REFERENCE** (FKGL 6.3, 9 words): The ultrasound was negative for bleeding in the brain.
- **naive** (FKGL 6.0, 10 words, 0 edits): The ultrasound did not show any bleeding inside the skull.
    - SARI=23.93  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 3.8, 8 words, 1 edits): The ultrasound showed no bleeding in the brain.
    - SARI=38.70  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 7.6, 9 words, 1 edits): The ultrasound was negative for bleeding inside the brain.
    - SARI=80.56  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 36 - `466`

- **ORIGINAL**  (FKGL 14.7, 12 words): He is status post laparoscopic appendicectomy, and he is tolerating oral diet.
- **REFERENCE** (FKGL 12.3, 15 words): He is status after keyhole surgery to remove appendix, and he is tolerating oral diet.
- **naive** (FKGL 9.1, 18 words, 0 edits): He had a keyhole surgery to remove his appendix, and he can eat and drink without any problems.
    - SARI=31.93  crit=0.00  NLIf=0.60  copyjrg=0.00
- **termonly** (FKGL 8.8, 12 words, 3 edits): He is after keyhole appendix surgery, and he can eat food normally.
    - SARI=32.99  crit=0.00  NLIf=0.65  copyjrg=0.00
- **grounded** (FKGL 9.1, 17 words, 3 edits): He is after appendix removal with a small camera, and he is eating and drinking by mouth.
    - SARI=33.61  crit=0.00  NLIf=0.82  copyjrg=0.00

### Note 37 - `478`

- **ORIGINAL**  (FKGL 8.4, 14 words): We believe that her walking is most likely not being affected by the hydrocephalus.
- **REFERENCE** (FKGL 8.5, 18 words): We believe that her walking is most likely not being affected by the excess fluid in the brain.
- **naive** (FKGL 9.3, 14 words, 0 edits): The doctors think that her walking is probably not being affected by the hydrocephalus.
    - SARI=20.83  crit=0.00  NLIf=0.24  copyjrg=1.00
- **termonly** (FKGL 8.5, 18 words, 1 edits): We believe that her walking is most likely not being affected by the fluid buildup in the brain.
    - SARI=77.92  crit=0.00  NLIf=0.71  copyjrg=0.00
- **grounded** (FKGL 8.4, 17 words, 1 edits): We believe that her walking is most likely not being affected by excess fluid in the brain.
    - SARI=76.30  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 38 - `505`

- **ORIGINAL**  (FKGL 12.3, 11 words): She noted complaints of fatigue, lightheadedness, and severe dyspnea on exertion.
- **REFERENCE** (FKGL 13.1, 15 words): She noted complaints of tiredness, lightheadedness, and severe shortness of breath on doing anything physical.
- **naive** (FKGL 6.8, 15 words, 0 edits): She said she felt very tired, dizzy, and had trouble breathing when she got active.
    - SARI=23.12  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.9, 14 words, 3 edits): She said she felt tired, dizzy, and had severe trouble breathing when she moved.
    - SARI=24.68  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 12.3, 11 words, 4 edits): She reported tiredness, dizziness, and severe shortness of breath with activity.
    - SARI=40.39  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 39 - `516`

- **ORIGINAL**  (FKGL 10.9, 14 words): No significant amount of edema associated with these in the dorsum of the hand.
- **REFERENCE** (FKGL 9.3, 14 words): No significant amount of swelling associated with these in the back of the hand.
- **naive** (FKGL 7.6, 15 words, 0 edits): The patient had no noticeable swelling on the top of the hand related to these.
    - SARI=28.98  crit=0.00  NLIf=0.92  copyjrg=0.00
- **termonly** (FKGL 3.4, 14 words, 2 edits): No large amount of swelling linked to these on the back of the hand.
    - SARI=42.37  crit=0.00  NLIf=0.54  copyjrg=0.00
- **grounded** (FKGL 3.4, 14 words, 2 edits): No large amount of swelling linked to these in the back of the hand.
    - SARI=52.43  crit=0.00  NLIf=0.42  copyjrg=0.00

### Note 40 - `523`

- **ORIGINAL**  (FKGL 12.3, 5 words): No cardio or pulmonary complaints.
- **REFERENCE** (FKGL 0.5, 5 words): No heart or lung complaints.
- **naive** (FKGL 2.3, 8 words, 0 edits): The patient has no heart or lung symptoms.
    - SARI=52.02  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 0.5, 5 words, 2 edits): No heart or lung complaints.
    - SARI=75.00  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 0.5, 5 words, 2 edits): No heart or lung complaints.
    - SARI=75.00  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 41 - `553`

- **ORIGINAL**  (FKGL 6.9, 11 words): At that time, the Coreg had been held secondary to hypotension.
- **REFERENCE** (FKGL 3.1, 13 words): At that time, the Coreg had been held because of low blood pressure
- **naive** (FKGL 5.0, 14 words, 0 edits): At that time, the patient was not given Coreg because of low blood pressure.
    - SARI=49.19  crit=0.00  NLIf=0.68  copyjrg=0.00
- **termonly** (FKGL 7.6, 14 words, 3 edits): At that time, the diabetes medicine had been held because of low blood pressure.
    - SARI=66.91  crit=0.00  NLIf=0.48  copyjrg=0.00
- **grounded** (FKGL 5.8, 13 words, 3 edits): At that time, the medication had been stopped because of low blood pressure.
    - SARI=54.48  crit=0.00  NLIf=0.59  copyjrg=0.00

### Note 42 - `554`

- **ORIGINAL**  (FKGL 12.8, 16 words): Her diarrhea now has settled down and she is having less urinary incontinence, less pedal edema.
- **REFERENCE** (FKGL 8.4, 17 words): Her watery poop now has settled down and she is having less uncontrolled peeing, less foot swelling.
- **naive** (FKGL 10.2, 22 words, 0 edits): Her diarrhea has gotten better, and she is losing control of her bladder less often and has less swelling in her feet.
    - SARI=29.60  crit=0.00  NLIf=0.84  copyjrg=0.33
- **termonly** (FKGL 8.6, 19 words, 3 edits): Her loose stools now have settled down and she is having less accidental urination, less swelling in her feet.
    - SARI=56.27  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 8.1, 20 words, 3 edits): Her loose, watery poop now has settled down and she is having less loss of bladder control, less swollen feet.
    - SARI=74.15  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 43 - `556`

- **ORIGINAL**  (FKGL 19.4, 13 words): Description : Nausea and abdominal pain after eating - Gall bladder disease - Laparoscopic cholecystectomy scheduled.
- **REFERENCE** (FKGL 14.4, 18 words): Description : Nausea and abdominal pain after eating - Gall bladder disease - keyhole surgery to remove the gall bladder scheduled.
- **naive** (FKGL 15.3, 32 words, 0 edits): The patient felt sick to their stomach and had pain in their belly after eating because of gallbladder disease, and they have a scheduled surgery to remove the gallbladder using small incisions.
    - SARI=22.22  crit=0.00  NLIf=0.35  copyjrg=0.00
- **termonly** (FKGL 12.3, 22 words, 3 edits): The patient has an upset stomach and belly pain after eating because of a sick gallbladder, and a gallbladder removal is scheduled.
    - SARI=20.55  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 14.5, 25 words, 4 edits): Description : feeling like they want to throw up and stomach ache after eating - illness of the gallbladder - surgery to remove the gallbladder via camera scheduled.
    - SARI=22.39  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 44 - `618`

- **ORIGINAL**  (FKGL 12.3, 20 words): She states that she has underlying history of heart disease but is not able to elaborate to any significant extent.
- **REFERENCE** (FKGL 12.3, 22 words): She states that she has underlying history of heart disease but is not able to go into detail to any significant extent.
- **naive** (FKGL 7.8, 18 words, 0 edits): She says she has a history of heart disease, but she cannot give any more details about it.
    - SARI=19.98  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 8.7, 20 words, 3 edits): She says that she has an existing history of heart disease but is not able to explain it in detail.
    - SARI=34.66  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 7.0, 20 words, 3 edits): She says that she has a past history of heart disease but is not able to give details at all.
    - SARI=32.99  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 45 - `661`

- **ORIGINAL**  (FKGL 6.5, 18 words): There was some slight edema of the fourth digit, on which he still is wearing his wedding band.
- **REFERENCE** (FKGL 5.9, 18 words): There was some slight swelling of the fourth finger, on which he still is wearing his wedding band.
- **naive** (FKGL 7.2, 21 words, 0 edits): There was a little bit of swelling on his fourth finger, and he is still wearing his wedding ring on it.
    - SARI=28.10  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.9, 18 words, 2 edits): There was some slight swelling of the fourth finger, on which he still is wearing his wedding band.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.9, 18 words, 2 edits): There was some slight swelling of the fourth finger, on which he still is wearing his wedding band.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 46 - `669`

- **ORIGINAL**  (FKGL 12.8, 21 words): Parents do state that she does appear to breathe rapidly, tires somewhat with the feeding with increased respiratory effort and diaphoresis.
- **REFERENCE** (FKGL 10.0, 21 words): Parents do state that she does appear to breathe quickly, tires somewhat with the feeding with increased breathing effort and sweating.
- **naive** (FKGL 7.0, 20 words, 0 edits): Parents say that she appears to breathe fast, gets a bit tired while feeding, works harder to breathe, and sweats.
    - SARI=17.50  crit=0.00  NLIf=0.17  copyjrg=0.00
- **termonly** (FKGL 9.3, 23 words, 4 edits): Parents do say that she does appear to breathe fast, tires somewhat with the feeding with increased working hard to breathe and sweating.
    - SARI=54.63  crit=0.00  NLIf=0.61  copyjrg=0.00
- **grounded** (FKGL 9.5, 21 words, 4 edits): Parents do say that she does appear to breathe quickly, tires somewhat with the feeding with increased breathing work and sweating.
    - SARI=71.04  crit=0.00  NLIf=0.59  copyjrg=0.00

### Note 47 - `673`

- **ORIGINAL**  (FKGL 11.3, 26 words): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had onset of chest pain this evening.
- **REFERENCE** (FKGL 10.5, 24 words): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had chest pain this evening.
- **naive** (FKGL 11.0, 24 words, 0 edits): According to the patient, he has not used amphetamines for at least four to five months; however, he started having chest pain this evening.
    - SARI=43.48  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 11.3, 26 words, 0 edits): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had onset of chest pain this evening.
    - SARI=30.69  crit=0.00  NLIf=0.99  copyjrg=1.00
- **grounded** (FKGL 11.3, 26 words, 0 edits): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had onset of chest pain this evening.
    - SARI=30.69  crit=0.00  NLIf=0.99  copyjrg=1.00

### Note 48 - `675`

- **ORIGINAL**  (FKGL 8.4, 10 words): Orogastric suction carried out with only scant clear stomach contents.
- **REFERENCE** (FKGL 7.6, 16 words): Suction of stomach through the mouth carried out with only a small amount clear stomach contents
- **naive** (FKGL 9.3, 23 words, 0 edits): The patient had a suction performed from the mouth to the stomach, but there was only a small amount of clear liquid inside.
    - SARI=32.38  crit=0.00  NLIf=0.91  copyjrg=0.00
- **termonly** (FKGL 5.2, 15 words, 0 edits): A stomach tube was used, but only a small amount of clear fluid came out.
    - SARI=32.48  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 6.0, 15 words, 0 edits): A mouth tube pull was done with only very little plain liquid in the stomach.
    - SARI=28.85  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 49 - `680`

- **ORIGINAL**  (FKGL 11.5, 9 words): Probably there is some restrictive element because of fibrosis.
- **REFERENCE** (FKGL 10.2, 11 words): Probably there is some restrictive element because of scarring of tissues.
- **naive** (FKGL 11.5, 9 words, 0 edits): Probably there is some restrictive element because of fibrosis.
    - SARI=30.89  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 6.3, 9 words, 2 edits): Probably there is some tightness because of scar tissue.
    - SARI=28.34  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 8.0, 11 words, 2 edits): Probably there is some limiting factor because of thick, scarred tissue.
    - SARI=28.34  crit=0.00  NLIf=0.74  copyjrg=0.00

### Note 50 - `681`

- **ORIGINAL**  (FKGL 10.2, 9 words): The uterus was placed back into the abdominal cavity.
- **REFERENCE** (FKGL 3.8, 8 words): The womb was placed back into the abdomen
- **naive** (FKGL 5.2, 8 words, 0 edits): The uterus was moved back inside the belly.
    - SARI=22.73  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL 5.0, 9 words, 2 edits): The womb was put back into the belly area.
    - SARI=48.55  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 2.3, 8 words, 2 edits): The womb was placed back into the belly.
    - SARI=87.50  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 51 - `682`

- **ORIGINAL**  (FKGL 5.0, 9 words): This was viewed on the AP and lateral projections.
- **REFERENCE** (FKGL -0.7, 8 words): This was viewed from the front and sides.
- **naive** (FKGL 5.0, 9 words, 0 edits): This was viewed on the AP and lateral projections.
    - SARI=11.37  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL -0.3, 10 words, 2 edits): This was viewed on the front and side X-rays.
    - SARI=58.01  crit=1.00  NLIf=0.38  copyjrg=0.00
- **grounded** (FKGL -0.3, 9 words, 2 edits): This was viewed on the front and side views.
    - SARI=58.96  crit=1.00  NLIf=0.97  copyjrg=0.00

### Note 52 - `686`

- **ORIGINAL**  (FKGL 8.2, 8 words): The cords move normally with phonation and ventilation.
- **REFERENCE** (FKGL 5.2, 8 words): The cords move normally when speaking and breathing
- **naive** (FKGL 4.8, 11 words, 0 edits): The vocal cords move normally when the patient speaks and breathes.
    - SARI=55.14  crit=0.00  NLIf=0.90  copyjrg=0.00
- **termonly** (FKGL 6.3, 9 words, 2 edits): The vocal cords move normally when speaking and breathing.
    - SARI=76.03  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.3, 9 words, 2 edits): The vocal cords move normally with speaking and breathing.
    - SARI=55.49  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 53 - `688`

- **ORIGINAL**  (FKGL 7.6, 13 words): Once the abdomen was opened, there was noted to be gross purulent drainage.
- **REFERENCE** (FKGL 6.0, 15 words): Once the abdomen was opened, there was noted to be a lot of pus draining.
- **naive** (FKGL 7.6, 17 words, 0 edits): Once the patient's abdomen was opened, the doctors found a large amount of thick, yellow pus.
    - SARI=26.45  crit=0.00  NLIf=0.07  copyjrg=0.00
- **termonly** (FKGL 4.2, 14 words, 2 edits): Once the belly was opened, there was noted to be a lot of pus.
    - SARI=71.08  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 5.9, 11 words, 2 edits): Once the belly was opened, there was visible pus leaking out.
    - SARI=30.71  crit=0.00  NLIf=0.88  copyjrg=0.00

### Note 54 - `692`

- **ORIGINAL**  (FKGL 4.0, 13 words): Once all four ports were placed, the right upper quadrant was then explored.
- **REFERENCE** (FKGL 5.4, 16 words): Once all four tubes were placed, the top right corner of her abdomen was then explored.
- **naive** (FKGL 4.0, 13 words, 0 edits): Once all four ports were placed, the right upper quadrant was then explored.
    - SARI=16.37  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 4.2, 14 words, 3 edits): Once all four tubes were placed, the upper right area was then looked at.
    - SARI=58.97  crit=0.00  NLIf=0.88  copyjrg=0.00
- **grounded** (FKGL 4.0, 13 words, 0 edits): Once all four ports were placed, the right upper quadrant was then explored.
    - SARI=16.37  crit=0.00  NLIf=0.99  copyjrg=1.00

### Note 55 - `693`

- **ORIGINAL**  (FKGL 15.4, 15 words): Options such as watchful waiting, robotic prostatectomy, seed implantation with and without radiation were discussed.
- **REFERENCE** (FKGL 11.8, 23 words): Options such as watch and wait, removing the prostate with the help of a robot, seed implantation with and without radiation were discussed.
- **naive** (FKGL 14.3, 28 words, 0 edits): Options like waiting to see how it goes, surgery to remove the prostate using robots, and putting tiny seeds into the prostate with or without radiation were discussed.
    - SARI=36.64  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 11.1, 21 words, 4 edits): Options such as waiting to see, surgery to remove the prostate, placing small seeds with and without energy treatment were discussed.
    - SARI=36.79  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 15.6, 23 words, 4 edits): Options such as close monitoring without treatment, robot-assisted prostate surgery, placing small seeds inside with and without high-energy rays were discussed.
    - SARI=36.92  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 56 - `695`

- **ORIGINAL**  (FKGL 14.3, 10 words): He also reportedly was on Lasix prior to hospitalization, possible
- **REFERENCE** (FKGL 11.5, 15 words): He also was reportedly on water pills (lasix) before his admission to the hospital, possible
- **naive** (FKGL 7.8, 18 words, 0 edits): He was also said to be taking Lasix before he went to the hospital, which could be possible.
    - SARI=40.75  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 11.8, 14 words, 4 edits): He also, according to reports, was on a diuretic before his hospital stay, possible
    - SARI=45.89  crit=0.00  NLIf=0.80  copyjrg=0.00
- **grounded** (FKGL 8.5, 13 words, 4 edits): He also people say took a water pill before a hospital stay, possible
    - SARI=43.38  crit=0.00  NLIf=0.01  copyjrg=0.00

### Note 57 - `697`

- **ORIGINAL**  (FKGL 10.2, 9 words): The four cardiac chambers dimensions are within normal limits.
- **REFERENCE** (FKGL 4.9, 13 words): The sizes of the four parts of the heart are within normal limits.
- **naive** (FKGL 3.7, 10 words, 0 edits): The patient's four heart chambers are a normal size.
    - SARI=29.14  crit=0.00  NLIf=0.89  copyjrg=0.25
- **termonly** (FKGL -0.7, 8 words, 2 edits): The four heart rooms are the right size.
    - SARI=32.80  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL -0.7, 9 words, 0 edits): The heart's four rooms are the right size.
    - SARI=29.75  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 58 - `698`

- **ORIGINAL**  (FKGL 11.5, 9 words): Digital rectal examination was performed, which showed no masses.
- **REFERENCE** (FKGL 6.9, 11 words): Examination of the back passage was performed, which showed no lumps.
- **naive** (FKGL 4.0, 13 words, 0 edits): The patient had a finger check of the rectum, which showed no lumps.
    - SARI=43.85  crit=0.00  NLIf=0.20  copyjrg=0.00
- **termonly** (FKGL 2.9, 12 words, 3 edits): A finger check of the rectum was done, which showed no lumps.
    - SARI=46.35  crit=0.00  NLIf=0.20  copyjrg=0.00
- **grounded** (FKGL 2.9, 12 words, 3 edits): A finger check of the rectum was done, which showed no lumps.
    - SARI=46.35  crit=0.00  NLIf=0.20  copyjrg=0.00

### Note 59 - `699`

- **ORIGINAL**  (FKGL 11.2, 23 words): He then had a problem with seizures, hemiparesis, has been to the hospital, developed C-diff, and is in the nursing home currently.
- **REFERENCE** (FKGL 12.0, 29 words): He then had a problem with fits, weakness on one side, has been to the hospital, developed an infection in the gut, and is in the nursing home currently.
- **naive** (FKGL 10.2, 26 words, 0 edits): He then had seizures and weakness on one side of his body, went to the hospital, developed C-diff, and is now in a nursing home.
    - SARI=31.07  crit=0.00  NLIf=0.94  copyjrg=0.67
- **termonly** (FKGL 12.6, 28 words, 3 edits): He then had a problem with fits, weakness on one side, has been to the hospital, developed a dangerous gut infection, and is in the nursing home currently.
    - SARI=87.13  crit=0.00  NLIf=0.80  copyjrg=0.00
- **grounded** (FKGL 13.3, 28 words, 3 edits): He then had a problem with sudden jerky movements, one-sided weakness, has been to the hospital, developed a gut infection, and is in the nursing home currently.
    - SARI=70.83  crit=0.00  NLIf=0.90  copyjrg=0.00

### Note 60 - `700`

- **ORIGINAL**  (FKGL 12.3, 22 words): He has been on continuous positive airway pressure now for several months, and returns for followup to review his response to treatment.
- **REFERENCE** (FKGL 9.7, 25 words): He has been using a breathing mask now for several months, and returns for follow up to review how he is doing with the treatment.
- **naive** (FKGL 14.4, 32 words, 0 edits): He has been using a continuous positive airway pressure machine for several months, and he is coming back for a follow-up visit to see how well the treatment is helping him.
    - SARI=50.67  crit=0.00  NLIf=0.95  copyjrg=0.83
- **termonly** (FKGL 8.5, 25 words, 2 edits): He has been on a mask that blows air now for several months, and returns for a check-up to review his response to treatment.
    - SARI=62.84  crit=0.00  NLIf=0.62  copyjrg=0.00
- **grounded** (FKGL 9.1, 22 words, 2 edits): He has been on steady air pressure now for several months, and returns for a checkup to review his response to treatment.
    - SARI=58.67  crit=0.00  NLIf=0.99  copyjrg=0.17

### Note 61 - `709`

- **ORIGINAL**  (FKGL 8.5, 18 words): The patient to take small bite and small sips to help decrease the risk of aspiration and penetration.
- **REFERENCE** (FKGL 9.9, 30 words): The patient is to take small bite and small sips to help decrease the risk of having the food or drink going down the wrong pipe and piercing the pipe.
- **naive** (FKGL 10.1, 28 words, 0 edits): The patient should take small bites and small sips to help decrease the risk of swallowing food or liquid into the lungs or going down the wrong way.
    - SARI=54.78  crit=0.00  NLIf=0.77  copyjrg=0.00
- **termonly** (FKGL 8.8, 25 words, 2 edits): The patient should take small bites and small sips to help decrease the risk of swallowing into the lungs and going down the wrong tube.
    - SARI=53.41  crit=0.00  NLIf=0.53  copyjrg=0.00
- **grounded** (FKGL 8.6, 26 words, 2 edits): The patient to take small bite and small sips to help decrease the risk of breathing food into the lungs and going down the wrong way.
    - SARI=72.25  crit=0.00  NLIf=0.28  copyjrg=0.00

### Note 62 - `714`

- **ORIGINAL**  (FKGL 12.3, 15 words): The patient was awakened and extubated and moved to the recovery room in satisfactory condition.
- **REFERENCE** (FKGL 11.1, 20 words): The patient was awakened and tube was removed from the airway and moved to the recovery room in satisfactory condition.
- **naive** (FKGL 8.0, 19 words, 0 edits): The patient woke up, had the breathing tube removed, and was moved to the recovery room in good condition.
    - SARI=36.87  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 9.1, 22 words, 3 edits): The patient was woken up and had the tube removed from their airway and moved to the recovery room in good condition.
    - SARI=47.71  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 8.7, 20 words, 3 edits): The patient was woken up and had the breathing tube removed and moved to the recovery room in good condition.
    - SARI=42.49  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 63 - `721`

- **ORIGINAL**  (FKGL 15.4, 10 words): PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily aroused.
- **REFERENCE** (FKGL 6.7, 8 words): The patient was asleep, but easily woken up.
- **naive** (FKGL 10.7, 15 words, 0 edits): Physical examination: General: The patient was asleep, but it was easy to wake them up.
    - SARI=39.42  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 5.2, 8 words, 1 edits): The patient was asleep, but easily woke up.
    - SARI=70.83  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.2, 8 words, 1 edits): The patient was asleep, but easily woke up.
    - SARI=70.83  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 64 - `725`

- **ORIGINAL**  (FKGL 10.9, 26 words): He is to follow up in approximately 10 days for recheck as well as prescription for intended AFOs, which he will need up to 6 months.
- **REFERENCE** (FKGL 11.5, 28 words): He is to come back in approximately 10 days for recheck as well as prescription for intended foot-drop braces, which he will need up to 6 months.
- **naive** (FKGL 10.6, 32 words, 0 edits): He needs to see the doctor again in about 10 days for a check-up and to get a prescription for his AFOs, which he will need for up to 6 months.
    - SARI=26.71  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 11.2, 29 words, 2 edits): He is to follow up in about 10 days for recheck as well as prescription for intended ankle and foot braces, which he will need up to 6 months.
    - SARI=55.69  crit=0.00  NLIf=0.61  copyjrg=0.00
- **grounded** (FKGL 11.1, 28 words, 2 edits): He is to follow up in about 10 days for recheck as well as prescription for intended ankle-foot braces, which he will need up to 6 months.
    - SARI=56.24  crit=0.00  NLIf=0.63  copyjrg=0.00

### Note 65 - `726`

- **ORIGINAL**  (FKGL 14.1, 8 words): Genitourinary : The external genitalia appeared to be normal.
- **REFERENCE** (FKGL 12.3, 8 words): The penis/vagina/genitals appeared to be normal.
- **naive** (FKGL 14.4, 12 words, 0 edits): Urinary and reproductive system: The patient's outside genital organs looked normal.
    - SARI=25.91  crit=0.00  NLIf=0.72  copyjrg=0.00
- **termonly** (FKGL 15.5, 9 words, 0 edits): Urinary and reproductive: The outside reproductive parts appeared normal.
    - SARI=28.23  crit=0.00  NLIf=0.71  copyjrg=0.00
- **grounded** (FKGL 5.9, 14 words, 1 edits): Body parts for peeing and sex : The outside sex parts appeared to be normal.
    - SARI=66.67  crit=0.00  NLIf=0.77  copyjrg=0.00

### Note 66 - `727`

- **ORIGINAL**  (FKGL 12.2, 13 words): She is postop day 21 of an exploratory laparotomy with ovarian cancer staging.
- **REFERENCE** (FKGL 12.6, 17 words): She is 21 days after an open abdominal operation which explored how widespread the ovarian cancer was.
- **naive** (FKGL 9.8, 19 words, 0 edits): She is day 21 after surgery to open her abdomen and check how far the ovarian cancer has spread.
    - SARI=49.63  crit=0.00  NLIf=0.70  copyjrg=0.00
- **termonly** (FKGL 7.7, 17 words, 2 edits): She is after surgery day 21 of a belly surgery to check how far the cancer spread.
    - SARI=41.30  crit=0.00  NLIf=0.14  copyjrg=0.00
- **grounded** (FKGL 10.6, 21 words, 3 edits): She is after surgery day 21 of a surgery to check her belly with checking how far the ovarian cancer spread.
    - SARI=46.41  crit=0.00  NLIf=0.62  copyjrg=0.00

### Note 67 - `732`

- **ORIGINAL**  (FKGL 8.5, 13 words): Prescription for prednisone as part of his chemotherapy has been given to him.
- **REFERENCE** (FKGL 7.6, 15 words): Prescription for steroid tablets as part of his cancer treatment has been given to him.
- **naive** (FKGL 8.8, 12 words, 0 edits): He was given a prescription for prednisone as part of his chemotherapy.
    - SARI=25.39  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 8.4, 16 words, 2 edits): Prescription for a steroid medicine as part of his cancer treatment has been given to him.
    - SARI=84.38  crit=0.00  NLIf=0.39  copyjrg=0.00
- **grounded** (FKGL 10.5, 20 words, 2 edits): Prescription for a medicine that lowers inflammation as part of his treatment with cancer drugs has been given to him.
    - SARI=69.23  crit=0.00  NLIf=0.68  copyjrg=0.00

### Note 68 - `738`

- **ORIGINAL**  (FKGL 9.1, 12 words): Photic stimulation was performed, but no clear-cut photic driving was seen.
- **REFERENCE** (FKGL 12.8, 17 words): Visual stimulation was performed, but no clear-cut changes in electrical activity of the brain was seen.
- **naive** (FKGL 6.7, 20 words, 0 edits): Light was used to stimulate the patient's eyes, but no clear eye movements that followed the light were seen.
    - SARI=30.82  crit=0.00  NLIf=0.63  copyjrg=0.00
- **termonly** (FKGL 4.8, 12 words, 0 edits): Flashing lights were used, but no obvious brain wave syncing was seen.
    - SARI=26.37  crit=0.00  NLIf=0.45  copyjrg=0.00
- **grounded** (FKGL 6.9, 11 words, 2 edits): Light stimulation was performed, but no clear light reaction was seen.
    - SARI=56.89  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 69 - `739`

- **ORIGINAL**  (FKGL 15.6, 8 words): FAMILY HISTORY : Both parents died with myocardial infarctions.
- **REFERENCE** (FKGL 8.2, 8 words): Family history: Both parents died with heart attacks.
- **naive** (FKGL 3.7, 10 words, 0 edits): Both of the patient's parents died from heart attacks.
    - SARI=25.93  crit=0.00  NLIf=0.91  copyjrg=0.00
- **termonly** (FKGL 8.2, 8 words, 1 edits): FAMILY HISTORY : Both parents died with heart attacks.
    - SARI=100.00  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 8.2, 8 words, 1 edits): FAMILY HISTORY : Both parents died with heart attacks.
    - SARI=100.00  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 70 - `740`

- **ORIGINAL**  (FKGL 11.2, 11 words): Extremities : 2+ bilateral pitting edema to the level of the knees.
- **REFERENCE** (FKGL 10.1, 28 words): Hands and feet: There is swelling in both feet up to the level of the knees (when pressed, causes an indentation in the skin for a few seconds)
- **naive** (FKGL 6.6, 21 words, 0 edits): The patient has 2+ swelling on both arms and legs that leaves a dent when pressed, extending up to the knees.
    - SARI=36.00  crit=0.00  NLIf=0.34  copyjrg=0.00
- **termonly** (FKGL 7.6, 14 words, 1 edits): The patient has swollen legs that leave indentations when pressed, extending to the knees.
    - SARI=34.08  crit=1.00  NLIf=0.57  copyjrg=0.00
- **grounded** (FKGL 1.9, 24 words, 1 edits): The arms and legs have a swelling that leaves a dent when you press down. It reaches up to the knees on both sides.
    - SARI=35.83  crit=1.00  NLIf=0.53  copyjrg=0.00

### Note 71 - `741`

- **ORIGINAL**  (FKGL 14.3, 10 words): Following questions are mostly involved in a psychosocial donor evaluation.
- **REFERENCE** (FKGL 13.9, 15 words): Following questions are mostly involved in a donor evaluation of their psychological or social states.
- **naive** (FKGL 9.9, 16 words, 0 edits): The questions listed below are usually used to check a donor's mental and social background.
    - SARI=16.75  crit=0.00  NLIf=0.78  copyjrg=0.00
- **termonly** (FKGL 11.3, 13 words, 1 edits): The following questions are mostly used in a mental and social donor evaluation.
    - SARI=41.06  crit=0.00  NLIf=0.82  copyjrg=0.00
- **grounded** (FKGL 12.7, 12 words, 1 edits): Following questions are mostly involved in a mental and social donor evaluation.
    - SARI=68.52  crit=0.00  NLIf=0.84  copyjrg=0.00

### Note 72 - `742`

- **ORIGINAL**  (FKGL 24.1, 5 words): Mild nonmobile descending aortic atherosclerosis.
- **REFERENCE** (FKGL 11.1, 22 words): Mild non-moving hardening of the part of aorta (the largest artery of the body) that goes down the chest and abdomen.
- **naive** (FKGL 6.1, 16 words, 0 edits): The patient has a slight, fixed plaque buildup in the lower part of the main artery.
    - SARI=34.84  crit=0.00  NLIf=0.85  copyjrg=0.00
- **termonly** (FKGL 5.0, 9 words, 3 edits): Mild fixed plaque buildup in the lower main artery.
    - SARI=43.06  crit=0.00  NLIf=0.91  copyjrg=0.00
- **grounded** (FKGL 2.3, 7 words, 2 edits): Mild fixed clogged artery in the chest.
    - SARI=44.58  crit=0.00  NLIf=0.79  copyjrg=0.00

### Note 73 - `750`

- **ORIGINAL**  (FKGL 6.7, 8 words): The eustachian tube was obstructed with bone wax.
- **REFERENCE** (FKGL 3.1, 13 words): The passage between the nose and the ears was blocked with bone wax.
- **naive** (FKGL 3.8, 8 words, 0 edits): The eustachian tube was blocked by bone wax.
    - SARI=36.51  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL -0.3, 9 words, 3 edits): The ear tube was blocked by a hard paste.
    - SARI=30.70  crit=0.00  NLIf=0.72  copyjrg=0.00
- **grounded** (FKGL -0.3, 9 words, 3 edits): The ear throat tube was blocked with ear wax.
    - SARI=37.85  crit=0.00  NLIf=0.08  copyjrg=0.00

### Note 74 - `752`

- **ORIGINAL**  (FKGL 6.3, 9 words): He was placed supine on the operating room table.
- **REFERENCE** (FKGL 7.2, 10 words): He was placed facing upwards on the operating room table.
- **naive** (FKGL 4.8, 11 words, 0 edits): He was placed on his back on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 4.8, 11 words, 1 edits): He was placed on his back on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 4.8, 11 words, 1 edits): He was placed on his back on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 75 - `755`

- **ORIGINAL**  (FKGL 7.4, 7 words): A urinalysis was not performed this time.
- **REFERENCE** (FKGL 2.3, 8 words): A urine test was not performed this time.
- **naive** (FKGL 2.6, 11 words, 0 edits): The patient did not have a urine test done this time.
    - SARI=31.48  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 0.8, 8 words, 2 edits): A urine test was not done this time.
    - SARI=51.60  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 0.8, 8 words, 2 edits): A urine test was not done this time.
    - SARI=51.60  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 76 - `766`

- **ORIGINAL**  (FKGL 12.3, 21 words): Vision and hearing appeared to be adequate for testing, although she did indicate that she needed to update her eyeglass prescription.
- **REFERENCE** (FKGL 11.7, 21 words): Vision and hearing appeared to be okay for testing, although she did indicate that she needed to update her glasses prescription.
- **naive** (FKGL 8.3, 21 words, 0 edits): Her vision and hearing were good enough for the test, but she said she needed to get a new eyeglass prescription.
    - SARI=18.83  crit=0.00  NLIf=0.99  copyjrg=0.67
- **termonly** (FKGL 9.1, 18 words, 3 edits): Vision and hearing seemed good enough for testing, although she said she needed to update her glasses fitting.
    - SARI=38.16  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 10.0, 21 words, 3 edits): Vision and hearing appeared to be good enough for testing, although she said that she needed to update her glasses order.
    - SARI=51.51  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 77 - `771`

- **ORIGINAL**  (FKGL 8.0, 24 words): I have talked to him several times about a colonoscopy, which he has refused, and so we have been doing stools for occult blood.
- **REFERENCE** (FKGL 17.5, 46 words): I have talked to him several times about a procedure to have a look inside the bowels (colonoscopy), which he has refused, and so we have been testing some stool samples in the lab to look for blood (which may be invisible to the naked eye).
- **naive** (FKGL 9.5, 26 words, 0 edits): The doctor has talked to him several times about a colonoscopy, which he has refused, so the doctors have been testing his stool for hidden blood.
    - SARI=41.73  crit=0.00  NLIf=0.83  copyjrg=0.00
- **termonly** (FKGL 12.1, 31 words, 3 edits): I have talked to him several times about a test to look inside the large intestine, which he has refused, and so we have been testing bowel movements for hidden blood.
    - SARI=65.62  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 12.0, 29 words, 2 edits): The doctor has talked to him several times about a large intestine exam, which he has refused, and so the team has been doing bowel movements for hidden blood.
    - SARI=41.51  crit=0.00  NLIf=0.89  copyjrg=0.00

### Note 78 - `783`

- **ORIGINAL**  (FKGL 8.4, 10 words): The knee was copiously irrigated and suction dried once again.
- **REFERENCE** (FKGL 7.6, 16 words): The knee was washed out thoroughly and dried with a suction (or mini-vacuum) once again
- **naive** (FKGL 5.8, 12 words, 0 edits): The knee was washed thoroughly with fluid and dried with suction again.
    - SARI=60.96  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.6, 15 words, 2 edits): The knee was washed out with a lot of fluid and dried with a vacuum.
    - SARI=62.05  crit=1.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 6.9, 16 words, 2 edits): The knee was washed thoroughly with fluid and made dry with a suction machine once again.
    - SARI=63.17  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 79 - `784`

- **ORIGINAL**  (FKGL 10.9, 14 words): She is not having painful urination, any blood in the urine, frequency or hesitancy.
- **REFERENCE** (FKGL 11.1, 20 words): She is not having painful peeing, any blood in the pee, needing to pee very often or having difficulty peeing.
- **naive** (FKGL 7.0, 20 words, 0 edits): She does not have pain when she pees, blood in her urine, frequent bathroom trips, or trouble starting to pee.
    - SARI=27.73  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 9.9, 20 words, 2 edits): She is not having painful urination, any blood in the urine, needing to pee often or trouble starting to pee.
    - SARI=66.66  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 10.5, 20 words, 2 edits): She is not having painful urination, any blood in the urine, how often she pees or difficulty starting to pee.
    - SARI=63.83  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 80 - `789`

- **ORIGINAL**  (FKGL 14.8, 19 words): Cardiovascular : Chest pain in the retrosternal area, Occasional anginal pain and patient describes it as a sensation of tightness.
- **REFERENCE** (FKGL 14.6, 30 words): Heart and blood vessels: Chest pain just behind the breastbone, occasional chest pain when exercising or exerting themselves, which gets better with rest and patient describes it as feeling 'tightness'.
- **naive** (FKGL 12.3, 21 words, 0 edits): Cardiovascular: The patient has occasional chest pain behind the breastbone, which is related to the heart and feels like a tightness.
    - SARI=39.81  crit=0.00  NLIf=0.90  copyjrg=0.33
- **termonly** (FKGL 11.3, 23 words, 2 edits): Heart and blood vessels : Chest pain behind the breastbone, occasional heart muscle pain and the patient describes it as a sensation of tightness.
    - SARI=60.10  crit=0.00  NLIf=0.85  copyjrg=0.00
- **grounded** (FKGL 12.1, 25 words, 2 edits): Heart and blood vessels: Chest pain in the area behind the breastbone, occasional chest pain and the patient describes it as a sensation of tightness.
    - SARI=59.82  crit=0.00  NLIf=0.86  copyjrg=0.00

### Note 81 - `790`

- **ORIGINAL**  (FKGL 4.8, 11 words): We excised a good bit of his synovium and synovial pouch.
- **REFERENCE** (FKGL 1.9, 12 words): We cut out a bit of the soft tissue of the joint.
- **naive** (FKGL 5.8, 12 words, 0 edits): The surgeons removed a large part of his synovium and synovial pouch.
    - SARI=32.05  crit=0.00  NLIf=0.87  copyjrg=0.80
- **termonly** (FKGL 4.0, 13 words, 2 edits): We removed a good bit of his joint lining and joint fluid sac.
    - SARI=44.24  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 4.2, 14 words, 2 edits): We cut out a good bit of his joint lining and joint lining pocket.
    - SARI=52.89  crit=0.00  NLIf=0.73  copyjrg=0.00

### Note 82 - `801`

- **ORIGINAL**  (FKGL 13.4, 11 words): An inflammatory process such as infection or ischemia must be considered.
- **REFERENCE** (FKGL 10.4, 13 words): An inflammatory process such as infection or reduced blood flow must be considered.
- **naive** (FKGL 9.1, 17 words, 0 edits): The patient's condition should be checked for inflammation, such as an infection or reduced blood flow.
    - SARI=30.79  crit=0.00  NLIf=0.93  copyjrg=0.00
- **termonly** (FKGL 5.9, 11 words, 1 edits): Swelling, such as infection or poor blood flow, must be considered.
    - SARI=50.57  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 7.8, 12 words, 2 edits): An inflammation such as infection or low blood flow must be considered.
    - SARI=51.00  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 83 - `804`

- **ORIGINAL**  (FKGL 2.9, 12 words): I have asked her to increase her prednisone when she goes home.
- **REFERENCE** (FKGL 2.9, 12 words): I have asked her to increase her steroid when she goes home.
- **naive** (FKGL 3.8, 12 words, 0 edits): The doctor asked her to increase her prednisone when she goes home.
    - SARI=23.35  crit=0.00  NLIf=0.31  copyjrg=1.00
- **termonly** (FKGL 4.9, 13 words, 1 edits): I have asked her to increase her steroid medicine when she goes home.
    - SARI=79.79  crit=0.00  NLIf=0.02  copyjrg=0.00
- **grounded** (FKGL 9.4, 14 words, 1 edits): I have asked her to increase her anti-inflammatory medicine when she goes home.
    - SARI=66.67  crit=0.00  NLIf=0.53  copyjrg=0.00

### Note 84 - `844`

- **ORIGINAL**  (FKGL 10.2, 9 words): She may need other neuropathic pain medications as needed.
- **REFERENCE** (FKGL 6.3, 9 words): She may need other nerve pain medications as needed.
- **naive** (FKGL 6.0, 10 words, 0 edits): She may need other medications for nerve pain as needed.
    - SARI=58.21  crit=0.00  NLIf=0.95  copyjrg=0.00
- **termonly** (FKGL 5.0, 9 words, 1 edits): She may need other nerve pain medicines as needed.
    - SARI=64.54  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 1 edits): She may need other nerve pain medicines as needed.
    - SARI=64.54  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 85 - `852`

- **ORIGINAL**  (FKGL 12.4, 7 words): A prophylactic dose of antibiotics was given.
- **REFERENCE** (FKGL 10.7, 7 words): A prevention dose of antibiotics was given.
- **naive** (FKGL 10.2, 9 words, 0 edits): The patient was given a preventive dose of antibiotics.
    - SARI=41.87  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 11.1, 8 words, 2 edits): A preventive dose of bacterial medicines was given.
    - SARI=28.96  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 11.1, 9 words, 2 edits): A preventive dose of bacteria-killing medicine was given.
    - SARI=28.96  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 86 - `854`

- **ORIGINAL**  (FKGL 16.2, 6 words): Chronic hypokalemia secondary to chronic diarrhea.
- **REFERENCE** (FKGL 7.6, 9 words): Long term low potassium due to long term diarrhea.
- **naive** (FKGL 10.9, 16 words, 0 edits): The patient has long-term low potassium levels in the blood caused by long-lasting diarrhea.
    - SARI=45.66  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 8.9, 11 words, 2 edits): Long-lasting low blood potassium caused by long-lasting loose stools.
    - SARI=34.13  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 8.9, 11 words, 2 edits): Long-lasting low blood potassium caused by long-lasting loose stools.
    - SARI=34.13  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 87 - `859`

- **ORIGINAL**  (FKGL 6.6, 4 words): No hepatosplenomegaly or tenderness.
- **REFERENCE** (FKGL 2.3, 9 words): No enlarged liver or spleen or pain when pushed.
- **naive** (FKGL 6.1, 16 words, 0 edits): The patient had no enlarged liver or spleen, and the area did not hurt when touched.
    - SARI=52.21  crit=0.00  NLIf=0.08  copyjrg=0.00
- **termonly** (FKGL 2.3, 9 words, 2 edits): No swollen liver and spleen or pain when touched.
    - SARI=53.69  crit=0.00  NLIf=0.29  copyjrg=0.00
- **grounded** (FKGL 2.3, 9 words, 2 edits): No swollen liver and spleen or pain when touched.
    - SARI=53.69  crit=0.00  NLIf=0.29  copyjrg=0.00

### Note 88 - `881`

- **ORIGINAL**  (FKGL 9.1, 11 words): He did not experience his left anterior chest pain with exercise.
- **REFERENCE** (FKGL 5.9, 11 words): He did not experience his left front chest pain with exercise.
- **naive** (FKGL 3.6, 15 words, 0 edits): He did not feel pain in the front of his left chest when he exercised.
    - SARI=27.63  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 2.6, 11 words, 2 edits): He did not feel his left front chest pain with exercise.
    - SARI=62.40  crit=1.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 3.4, 14 words, 2 edits): He did not feel pain in the front of his left chest with exercise.
    - SARI=32.85  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 89 - `891`

- **ORIGINAL**  (FKGL 7.6, 9 words): Also, would use it to control the atrial fibrillation.
- **REFERENCE** (FKGL 6.0, 10 words): Also, would use it to control the irregular heart beat
- **naive** (FKGL 8.0, 11 words, 0 edits): Also, the doctor would use it to control the atrial fibrillation.
    - SARI=25.32  crit=0.00  NLIf=0.00  copyjrg=1.00
- **termonly** (FKGL 7.6, 9 words, 1 edits): Also, would use it to control the irregular heartbeat.
    - SARI=80.00  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 7.6, 9 words, 1 edits): Also, would use it to control the irregular heartbeat.
    - SARI=80.00  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 90 - `900`

- **ORIGINAL**  (FKGL 11.1, 8 words): Overall the patient is a seemingly good historian.
- **REFERENCE** (FKGL 11.9, 10 words): Overall the patient is seemingly good at remembering their history
- **naive** (FKGL 5.8, 12 words, 0 edits): Overall, the patient gives a clear and detailed account of their past.
    - SARI=37.92  crit=0.00  NLIf=0.18  copyjrg=0.00
- **termonly** (FKGL 6.0, 10 words, 1 edits): Overall the patient appears to be clear about their health.
    - SARI=39.85  crit=0.00  NLIf=0.12  copyjrg=0.00
- **grounded** (FKGL 9.6, 10 words, 2 edits): Overall the patient is apparently good at sharing past events.
    - SARI=63.22  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 91 - `933`

- **ORIGINAL**  (FKGL 3.7, 10 words): No active Crohn 's disease was found during the colonoscopy.
- **REFERENCE** (FKGL 5.9, 14 words): No active Crohn 's disease was found during the camera test through the gut.
- **naive** (FKGL 5.0, 15 words, 0 edits): The colonoscopy did not show any signs of active Crohn's disease in the patient.
    - SARI=18.58  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 6.0, 10 words, 2 edits): No active gut disease was found during the bowel exam.
    - SARI=33.44  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 9.7, 13 words, 2 edits): No currently happening Crohn's disease was found during the large intestine exam.
    - SARI=41.10  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 92 - `935`

- **ORIGINAL**  (FKGL 16.4, 28 words): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have mounting exhaustion and respiratory distress.
- **REFERENCE** (FKGL 15.5, 28 words): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have worsening exhaustion and breathing distress.
- **naive** (FKGL 12.0, 30 words, 0 edits): Not long after the first check-up, the patient started saying they had chest pain and looked to the nurse like they were getting very tired and having trouble breathing.
    - SARI=17.51  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 15.5, 28 words, 2 edits): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have increasing tiredness and trouble breathing.
    - SARI=63.09  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 16.4, 28 words, 2 edits): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have increasing tiredness and difficulty breathing.
    - SARI=63.09  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 93 - `968`

- **ORIGINAL**  (FKGL 8.2, 8 words): She has been referred for a pacemaker implantation.
- **REFERENCE** (FKGL 7.6, 9 words): She has been referred for a pacemaker fitting surgery.
- **naive** (FKGL 4.7, 16 words, 0 edits): She has been sent to see a doctor to have a pacemaker put in her heart.
    - SARI=23.47  crit=0.00  NLIf=0.90  copyjrg=0.00
- **termonly** (FKGL 2.5, 10 words, 2 edits): She has been sent to get a pacemaker put in.
    - SARI=23.47  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.8, 15 words, 2 edits): She has been sent to see another doctor for surgery to place a heart device.
    - SARI=23.18  crit=0.00  NLIf=0.56  copyjrg=0.00

### Note 94 - `116`

- **ORIGINAL**  (FKGL -0.7, 8 words): There was some hematoma at the cath site.
- **REFERENCE** (FKGL 5.8, 13 words): There was some swelling due to collection of blood at the catheter site.
- **naive** (FKGL 5.0, 9 words, 0 edits): The patient had some bruising at the catheter site.
    - SARI=42.43  crit=0.00  NLIf=0.76  copyjrg=0.00
- **termonly** (FKGL -0.7, 8 words, 2 edits): There was some bruise at the tube spot.
    - SARI=54.80  crit=0.00  NLIf=0.19  copyjrg=0.00
- **grounded** (FKGL 2.3, 8 words, 2 edits): There was some bruise at the catheter spot.
    - SARI=58.86  crit=0.00  NLIf=0.43  copyjrg=0.00

### Note 95 - `592`

- **ORIGINAL**  (FKGL 6.3, 9 words): The necrotic tissue was lifted out of the abdomen.
- **REFERENCE** (FKGL 3.7, 9 words): The dead flesh was lifted out of the abdomen.
- **naive** (FKGL 5.2, 8 words, 0 edits): The dead tissue was removed from the abdomen.
    - SARI=25.95  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 5.0, 9 words, 1 edits): The dead tissue was lifted out of the abdomen.
    - SARI=72.13  crit=0.00  NLIf=0.99  copyjrg=0.33
- **grounded** (FKGL 5.0, 9 words, 1 edits): The dead tissue was lifted out of the abdomen.
    - SARI=72.13  crit=0.00  NLIf=0.99  copyjrg=0.33

### Note 96 - `249`

- **ORIGINAL**  (FKGL 6.7, 8 words): Pressure was held and the area was hemostatic.
- **REFERENCE** (FKGL 5.2, 8 words): Pressure was held and the area stopped bleeding.
- **naive** (FKGL 5.9, 11 words, 0 edits): The patient kept pressure on the area and the bleeding stopped.
    - SARI=27.11  crit=0.00  NLIf=0.20  copyjrg=0.00
- **termonly** (FKGL 5.0, 9 words, 1 edits): Pressure was held and the area was not bleeding.
    - SARI=67.96  crit=0.00  NLIf=0.71  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 1 edits): Pressure was held and the area had stopped bleeding.
    - SARI=76.67  crit=0.00  NLIf=0.30  copyjrg=0.00

### Note 97 - `701`

- **ORIGINAL**  (FKGL 3.7, 9 words): The area was lavaged with some saline and cleared.
- **REFERENCE** (FKGL 3.7, 11 words): The area was washed out with some salt water and cleared.
- **naive** (FKGL 3.7, 11 words, 0 edits): The area was washed with some salt water and made clean.
    - SARI=70.03  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.7, 10 words, 2 edits): The area was rinsed with some salt water and cleared.
    - SARI=75.42  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.7, 10 words, 2 edits): The area was cleaned with some salt water and cleared.
    - SARI=75.42  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 98 - `826`

- **ORIGINAL**  (FKGL 8.2, 8 words): Pain and inability to ambulate brought him in.
- **REFERENCE** (FKGL 6.3, 9 words): Pain and inability to move around brought him in.
- **naive** (FKGL 1.9, 12 words, 0 edits): He came in because he was in pain and could not walk.
    - SARI=23.06  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.7, 9 words, 1 edits): Pain and being unable to walk brought him in.
    - SARI=38.11  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 2.5, 10 words, 1 edits): Pain and not being able to walk brought him in.
    - SARI=38.11  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 99 - `751`

- **ORIGINAL**  (FKGL 2.3, 8 words): There is a hernia on the left side.
- **REFERENCE** (FKGL 2.9, 12 words): The gut sticks out through the abdomen wall on the left side.
- **naive** (FKGL 3.7, 9 words, 0 edits): The patient has a hernia on the left side.
    - SARI=55.97  crit=0.00  NLIf=0.97  copyjrg=1.00
- **termonly** (FKGL -0.7, 8 words, 1 edits): There is a bulge on the left side.
    - SARI=60.64  crit=0.00  NLIf=0.75  copyjrg=0.00
- **grounded** (FKGL 4.0, 13 words, 1 edits): There is an organ bulging through a weak muscle on the left side.
    - SARI=64.59  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 100 - `496`

- **ORIGINAL**  (FKGL 8.4, 10 words): Other systems were reviewed and were found to be unremarkable.
- **REFERENCE** (FKGL 4.8, 10 words): Other systems were reviewed and were found to be normal.
- **naive** (FKGL 5.8, 13 words, 0 edits): The patient's other body systems were checked and found to be normal.
    - SARI=29.42  crit=1.00  NLIf=0.50  copyjrg=0.00
- **termonly** (FKGL 4.8, 10 words, 1 edits): Other systems were reviewed and were found to be normal.
    - SARI=100.00  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 7.8, 12 words, 1 edits): Other systems were reviewed and were found to be common and ordinary.
    - SARI=66.67  crit=1.00  NLIf=0.82  copyjrg=0.00
