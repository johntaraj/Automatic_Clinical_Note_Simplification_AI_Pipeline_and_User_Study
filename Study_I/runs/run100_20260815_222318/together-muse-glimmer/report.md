# together-muse-glimmer - run `run100_20260815_222318`

- model: `meta-models/Muse-Glimmer-30B` (together, fireworks backend)
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
| **human edit recall** | 99 |  |  | 0.568 | 0.995 | 0.995 | higher is better | > 0.85 | of the jargon the human replaced, how much did we replace |

### 4 faithfulness

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **NLI faithfulness** | 100 |  |  | 0.901 | 0.793 | 0.737 | higher is better | > 0.70 | general-domain MNLI head; absolute values are compressed |
| **NLI completeness** | 100 |  |  | 0.861 | 0.763 | 0.736 | higher is better | > 0.60 | omission is the dominant clinical failure mode, which is why this direction is reported separately |

### 4 readability

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **FKGL drop vs input** | 100 |  |  | 2.96 | 3.59 | 2.94 | higher is better | > +4 grades | gameable by chopping sentences - read with length ratio |
| **Coleman-Liau drop** | 100 |  |  | 3.56 | 5.16 | 4.93 | higher is better | > +4 | none - this is the robustness check on FKGL |
| **length ratio vs reference** | 100 |  |  | 0.97 | 1.10 | 1.20 | descriptive | 0.9-1.3 | descriptive, not a quality score; >1.4 means the model is glossing everything |

### 4 safety

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **critical-error rate** | 100 |  |  | 0.100 | 0.060 | 0.090 | LOWER is better | 0.00 - any value > 0 needs review | fraction of outputs that lost a high-risk slot: negation, uncertainty, laterality, a number/unit, or a drug name |

### 5 attribution

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **attributable rate** | 0.697 | higher is better | > 0.50 | of the edits retrieval demonstrably caused, the fraction with a trustworthy explanation (held-out LDS >= 0.4, clear winner) |
| **held-out LDS (median)** | 0.771 | higher is better | > 0.60 (paper reports 0.6-0.85) | Spearman between the surrogate's predictions and the true log-probs on masks it never saw - how trustworthy the attributions are |
| **helped rate** | 0.548 | descriptive | descriptive - the split is the finding | fraction of edits retrieval made more likely (effect >= 0.10 nats) |
| **hurt rate** | 0.035 | LOWER is better | < 0.10 | fraction of edits retrieval made LESS likely - glossary actively harming the rewrite |
| **top-1 log-prob drop (helped edits)** | 2.37 | higher is better | > 0.5 nats | the paper reports roughly 0.43-0.75 for top-1 across three benchmarks, so this is the number to compare against |
| **winning source is the right term** | 0.927 | higher is better | > 0.80 | the complement is cross-term contamination - the definition of a DIFFERENT word in the same sentence winning the attribution and changing the meaning. Needs no gold labels, which is what makes it the closest thing this family has to a precision score |

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
| **copy-jargon rate** | 99 |  |  | 0.432 | 0.005 | 0.005 | LOWER is better | < 0.10 | exactly 1 - human_edit_recall, by construction: every gold term is either recalled or copied. Report it as a restatement, not as separate evidence, and keep it out of the significance family or one result consumes two FDR slots |
| **reference-vocabulary hit (NOT a precision)** | 73 |  |  | 0.603 | 0.753 | 0.740 | higher is better | descriptive only - see caveat | BROKEN AS NAMED, measured 2026-08-15. The support test is `ref_added & sys_content_words`, and `ref_added` is derived from (reference, original) only - it does not depend on the term being scored. So the same verdict is applied to every changed term in a note and the per-note value can only be 0 or 1. Verified on CLEAN93/qwen3p7-plus: 265 of 265 note-arm values are exactly 0.0 or 1.0, and no note has two terms that disagree. One incidental shared word credits every replacement in the sentence. Making this a real precision needs term-to-replacement span alignment, which does not exist yet. Do not quote it as evidence that replacements were correct |
| **definition borrowing** | 73 |  |  | 0.416 | 0.466 | 0.555 | descriptive | descriptive - the arm gap IS the finding | the mechanism behind the grounded-vs-termonly result, measured per note instead of only in analysis/conditional_grounding.py. Deliberately DESCRIPTIVE: grounded is shown the definitions and the other arms are not, so a difference here is expected by construction and testing it would burn an FDR slot to confirm something guaranteed. Read it as 'how much of the glossary's wording ended up in the output', then read what that cost in human_edit_recall and NLI |
| **replacement F1 (inherits a broken precision)** | 99 |  |  | 0.388 | 0.776 | 0.734 | higher is better | descriptive only - see caveat | DEMOTED from paper tier 2026-08-15. Half of it is replacement_precision, which is not per-term (see its caveat), so this cannot support a claim that the system replaced jargon CORRECTLY. Quote human_edit_recall instead - that half is genuinely per-term and is unaffected |
| **rewrite aggressiveness** | 100 |  |  | 0.294 | 0.081 | 0.082 | descriptive | descriptive | NOT an error rate - legitimate restructuring scores here |

### 4 quality

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **SARI** | 100 |  |  | 32.84 | 50.68 | 47.62 | higher is better | 40-60 typical | the references are MINIMAL-EDIT, so SARI rewards not editing. Measured: a perfect rewrite scored 25.97 vs 22.64 for doing nothing. Report, do not lead with it |
| **BERTScore F1** | 100 |  |  | 0.647 | 0.696 | 0.661 | higher is better | 0.4-0.7 rescaled | read the RESCALED value. Until bug 42 the baseline lookup was silently failing for a local model directory, so raw scores were reported and everything landed in 0.90-0.96 - which is why this metric was demoted for having no dynamic range. Rescaled, the same 5 notes span 0.556-0.620, a gap six times wider. The demotion should be re-examined on the full run |

### 4 readability

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **FKGL (absolute)** | 100 | 10.51 | 8.54 | 7.55 | 6.92 | 7.57 | LOWER is better | 6-8 (US grade) | absolute grade is dominated by sentence length; the DROP is the honest number |
| **Coleman-Liau (absolute)** | 100 | 12.78 | 9.80 | 9.22 | 7.62 | 7.85 | LOWER is better | 6-8 | character-based grade level |
| **Flesch Reading Ease** | 100 | 41.1 | 60.0 | 63.7 | 72.7 | 71.0 | higher is better | 60-80 (plain English) | uses the SAME two inputs as FKGL; not independent evidence |
| **FRE gain** | 100 |  |  | 22.7 | 31.6 | 30.0 | higher is better | > +20 | redundant with fkgl_drop |
| **SMOG** | 100 | 11.49 | 9.83 | 8.73 | 7.96 | 8.19 | LOWER is better | 6-8 | calibrated for 30+ sentence passages; very jumpy on one sentence |
| **SMOG drop** | 100 |  |  | 2.76 | 3.53 | 3.30 | higher is better | > +3 | same single-sentence calibration problem |
| **words out** | 100 | 12.2 | 14.8 | 13.8 | 15.8 | 17.2 | descriptive | close to the reference | output length |

### 4 safety

| metric | n | ORIGINAL | REFERENCE | naive | termonly | grounded | direction | target | note |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **drug-name preservation** | 2 |  |  | 1.000 | 0.000 | 0.000 | higher is better | 1.00 - nothing less is acceptable | APPENDIX because of the DENOMINATOR, not the metric: only 2 of the 93 laymaker notes contain a detected drug name, so the mean is two observations wearing a percentage. Report the cases, not the rate. Also read it against tag_policy - under `replace` the pipeline is INSTRUCTED to drop drug names |
| **diagnostic-identity preservation** | 5 |  |  | 1.000 | 1.000 | 1.000 | higher is better | 1.00 - nothing less is acceptable | scored only over a closed curated table of conditions, and only 4 of 93 notes contain one, so the mean is four observations. An unlisted diagnosis is not scored rather than guessed at, so this under-reports rather than over-reports. Report the cases |
| **severity downgrade rate** | 10 |  |  | 0.200 | 0.300 | 0.200 | LOWER is better | 0.00 | 3-tier ordinal lexicon; lay renderings ('very bad') sit at the same tier as their clinical equivalent so correct paraphrase is not penalised. Appendix on denominator: 10 of 93 notes state a severity at all |
| **number/unit preservation** | 14 |  |  | 0.821 | 1.000 | 0.893 | higher is better | 1.00 | all doses and units survive (spelled-out numbers and expanded unit abbreviations count) |
| **negation preservation** | 24 |  |  | 0.917 | 0.875 | 0.875 | higher is better | 1.00 | type-level, so it cannot see WHICH negation was lost |
| **laterality preservation** | 8 |  |  | 0.812 | 0.812 | 0.812 | higher is better | 1.00 | left/right/bilateral/basal survive (instance-level) |
| **uncertainty preservation** | 9 |  |  | 0.778 | 0.778 | 0.778 | higher is better | 1.00 | hedging survives - 'cannot be excluded' must not become 'is present' |

### 5 attribution

| run-level metric | value | direction | target | note |
|---|---:|---|---|---|
| **LDS optimism gap** | 0.087 | LOWER is better | < 0.15 | a methodological result in its own right, not a quality score |
| **top-1 log-prob drop (all edits)** | 0.65 | higher is better | descriptive | NOT comparable to the paper's Figure 4a. Most edits have no source effect at all, so there is nothing to remove and the drop is ~0 by construction; the median over all edits therefore reads as a failure when the method is working. Quote `top1_drop_median_helped` instead |
| **ablation success rate** | 1.000 | higher is better | 1.00 | scoring calls that returned usable log-probs - a transport health check, not a quality metric |

## Attribution detail (stage 5)

`source_effect = log p(edit | full glossary) - log p(edit | no glossary)`. This is the only measurement in the suite that says whether retrieval *caused* an edit.

| quantity | value | meaning |
|---|---:|---|
| edits attributed | 199 | |
| ranked fits | 199 | a source could be ranked |
| flat fits | 0 | scoring worked, no source mattered - a RESULT, not a failure |
| measurement failures | 0 | aim for 0 |
| **helped** | 109 | retrieval made the edit more likely |
| **neutral** | 83 | the model knew it anyway |
| **hurt** | 7 | retrieval made it LESS likely |
| attributable rate | 0.6972 | of helped edits, those with a trustworthy explanation |
| **winning source is the right term** | 0.9266 | of 109 caused edits; the rest are cross-term contamination |
| held-out LDS (median) | 0.7714 | aim > 0.60 |
| in-sample LDS (median) | 0.8584 | for contrast only |
| **LDS optimism gap** | 0.087 | how much an in-sample number would overstate faithfulness |
| edits with no LDS | 60 | glossary too small for a genuinely unseen held-out block |
| **top-1 drop, helped edits** | 2.3695 | paper Eq. 1 over the 109 edits where a source mattered - the number comparable to the paper's Fig. 4a |
| **top-3 drop, helped edits** | 5.7798 | same, removing the top three |
| top-1 drop, ALL edits | 0.6542 | ~0 by construction on the 83 edits with no source effect; do NOT quote this against the paper |
| ablation success | 1.0 | transport health |

> Surrogate target: **logit-scaled probability**, per ContextCite Algorithm 1 line 4. Bucketing uses the log-probability difference, which answers "would the model have produced this anyway?". Both are stored per edit.

**Threshold sensitivity** (the helped/hurt split depends on an arbitrary cut-off, so it is swept):

| eps (nats) | helped | neutral | hurt | attributable |
|---:|---:|---:|---:|---:|
| 0.05 | 147 | 24 | 28 | 0.5986 |
| 0.1 | 139 | 34 | 26 | 0.6115 |
| 0.25 | 127 | 53 | 19 | 0.6457 |
| 0.693 | 109 | 83 | 7 | 0.6972 |
| 1.0 | 102 | 94 | 3 | 0.7059 |

### Does grounding help more on rare terms?

| Zipf stratum | edits | helped | neutral | hurt | helped rate | mean effect (nats) |
|---|---:|---:|---:|---:|---:|---:|
| very_rare | 56 | 33 | 21 | 1 | 0.6 | 3.9367 |
| rare | 69 | 43 | 25 | 1 | 0.6232 | 5.0425 |
| uncommon | 61 | 29 | 27 | 5 | 0.4754 | 4.5786 |
| common | 12 | 3 | 9 | 0 | 0.25 | 1.3649 |
| unknown | 2 | 1 | 1 | 0 | 0.5 | 10.5906 |

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
| rationale fabrications | 0.000 | LOWER is better | < 0.05 |
| rationale slot omissions | 0.190 | LOWER is better | < 0.40 |
| rationale fact recall | 0.810 | higher is better | > 0.85 |
| rationale source correct | 1.000 | higher is better | > 0.95 |
| rationale quote verified | 1.000 | higher is better | 1.00 |
| templated rationales | 0.035 | LOWER is better | < 0.30 |

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
  sari                       100   +1    50.684    32.842  +17.842    [+13.61, +22.29]   0.0000  0.0000*  +0.77
  bertscore_f1               100   +1     0.695     0.647   +0.048      [+0.02, +0.08]   0.0046  0.0121*  +0.30
  fkgl_drop                  100   +1     3.593     2.963   +0.630      [-0.19, +1.49]   0.1581   0.2284  +0.12
  smog_drop                  100   +1     3.533     2.758   +0.775      [+0.03, +1.53]   0.0317   0.0590  +0.31
  coleman_liau_drop          100   +1     5.161     3.559   +1.602      [+0.72, +2.57]   0.0003  0.0010*  +0.40
  nli_faithfulness           100   +1     0.793     0.901   -0.108      [-0.17, -0.05]   1.0000   1.0000  -0.51
  nli_completeness           100   +1     0.763     0.861   -0.098      [-0.17, -0.03]   1.0000   1.0000  -0.49
  human_edit_recall           99   +1     0.995     0.568   +0.427      [+0.34, +0.52]   0.0000  0.0000*  +1.00
  replacement_precision       73   +1     0.753     0.603   +0.151      [+0.04, +0.26]   0.0205  0.0444*  +0.58
  replacement_f1              99   +1     0.776     0.388   +0.387      [+0.28, +0.49]   0.0000  0.0000*  +0.86
  critical_error             100   -1     0.060     0.100   -0.040      [-0.09, +0.00]   0.2261   0.2939  +0.67
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     1.000     0.821   +0.179      [+0.00, +0.39]   0.0974   0.1582  +1.00
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.300     0.200   +0.100      [-0.20, +0.40]   0.8750   1.0000  -0.33

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

```

====================================================================================================
  PAIRED COMPARISON   grounded  vs  termonly
====================================================================================================
  Wilcoxon one-sided ('grounded' better), paired bootstrap 95% CI, rank-biserial effect size.
  12 tests -> Benjamini-Hochberg FDR at alpha=0.05. Report p_adj, not p.

  metric                       n  dir  grounded  termonly     diff              95% CI        p    p_adj    rbc
  ------------------------------------------------------------------------------------------------
  sari                       100   +1    47.619    50.684   -3.065      [-4.92, -1.33]   0.9998   0.9998  -0.50
  bertscore_f1               100   +1     0.661     0.695   -0.035      [-0.05, -0.02]   0.9996   0.9998  -0.42
  fkgl_drop                  100   +1     2.944     3.593   -0.648      [-1.19, -0.13]   0.9788   0.9998  -0.29
  smog_drop                  100   +1     3.297     3.533   -0.236      [-0.82, +0.36]   0.7301   0.9998  -0.13
  coleman_liau_drop          100   +1     4.929     5.161   -0.232      [-0.60, +0.14]   0.9468   0.9998  -0.18
  nli_faithfulness           100   +1     0.737     0.793   -0.056      [-0.11, +0.00]   0.9252   0.9998  -0.20
  nli_completeness           100   +1     0.736     0.763   -0.028      [-0.06, +0.01]   0.9627   0.9998  -0.23
  human_edit_recall           99   +1     0.995     0.995   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  replacement_precision      100   +1     0.730     0.770   -0.040      [-0.11, +0.03]   0.7582   0.9998  -0.29
  replacement_f1              99   +1     0.734     0.776   -0.041      [-0.11, +0.03]   0.7643   0.9998  -0.37
  critical_error             100   -1     0.090     0.060   +0.030      [+0.00, +0.07]   0.7190   0.9998  -1.00
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     1.000   -0.107      [-0.29, +0.00]   0.8197   0.9998  -1.00
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.200     0.300   -0.100      [-0.30, +0.00]   0.5000   0.9998  +1.00

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
  sari                       100   +1    47.619    32.842  +14.777    [+10.80, +18.87]   0.0000  0.0000*  +0.72
  bertscore_f1               100   +1     0.661     0.647   +0.013      [-0.02, +0.04]   0.1955   0.3630  +0.10
  fkgl_drop                  100   +1     2.944     2.963   -0.018      [-0.91, +0.93]   0.6794   0.8832  -0.05
  smog_drop                  100   +1     3.297     2.758   +0.539      [-0.30, +1.39]   0.1754   0.3630  +0.19
  coleman_liau_drop          100   +1     4.929     3.559   +1.370      [+0.44, +2.41]   0.0109  0.0353*  +0.27
  nli_faithfulness           100   +1     0.737     0.901   -0.164      [-0.23, -0.10]   1.0000   1.0000  -0.67
  nli_completeness           100   +1     0.736     0.861   -0.125      [-0.20, -0.05]   1.0000   1.0000  -0.53
  human_edit_recall           99   +1     0.995     0.568   +0.427      [+0.34, +0.52]   0.0000  0.0000*  +1.00
  replacement_precision       73   +1     0.740     0.603   +0.137      [+0.01, +0.26]   0.0358   0.0932  +0.46
  replacement_f1              99   +1     0.734     0.388   +0.346      [+0.23, +0.46]   0.0000  0.0000*  +0.73
  critical_error             100   -1     0.090     0.100   -0.010      [-0.04, +0.02]   0.4234   0.6115  +0.33
  drug_preservation           -- skipped: only 2 paired notes
  number_unit_preservation    14   +1     0.893     0.821   +0.071      [+0.00, +0.21]   0.3138   0.5100  +1.00
  diagnostic_identity_preservation   5   +1     1.000     1.000   +0.000      [+0.00, +0.00]      n/a      n/a    n/a
  severity_downgrade          10   -1     0.200     0.200   +0.000      [-0.30, +0.30]   0.7500   0.8864  +0.00

  * = survives FDR correction. Anything without a star is NOT a significant result, whatever the raw p says.
```

## Clinical-safety flags

- note 2 / `termonly` / **negation** (critical): lost ['can not be excluded', 'excluded', 'not']
- note 2 / `termonly` / **uncertainty** (critical): lost ['can not be excluded']
- note 2 / `grounded` / **negation** (critical): lost ['can not be excluded', 'excluded', 'not']
- note 3 / `termonly` / **severity** (warning): lost ['marked']
- note 3 / `termonly` / **severity_downgrade** (warning): lost ['tier 2']
- note 3 / `grounded` / **severity_downgrade** (warning): lost ['tier 2']
- note 9 / `naive` / **number_unit** (critical): lost ['1']
- note 9 / `grounded` / **number_unit** (critical): lost ['1']
- note 10 / `naive` / **temporality** (warning): lost ['new onset']
- note 10 / `termonly` / **temporality** (warning): lost ['new onset']
- note 10 / `grounded` / **temporality** (warning): lost ['new onset']
- note 24 / `naive` / **severity** (warning): lost ['obvious']
- note 26 / `naive` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `termonly` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `termonly` / **temporality** (warning): lost ['acute']
- note 26 / `grounded` / **uncertainty** (critical): lost ['compatible with']
- note 26 / `grounded` / **temporality** (warning): lost ['acute']
- note 28 / `naive` / **uncertainty** (critical): lost ['consideration']
- note 28 / `grounded` / **uncertainty** (critical): lost ['consideration']
- note 32 / `termonly` / **temporality** (warning): lost ['prior']
- note 36 / `naive` / **temporality** (warning): lost ['status post']
- note 36 / `grounded` / **temporality** (warning): lost ['status post']
- note 38 / `naive` / **severity** (warning): lost ['severe']
- note 38 / `naive` / **severity_downgrade** (critical): lost ['grave severity stated as mild or absent']
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
- note 44 / `termonly` / **temporality** (warning): lost ['history of']
- note 44 / `termonly` / **severity** (warning): lost ['significant']
- note 44 / `termonly` / **severity_downgrade** (warning): lost ['tier 2']
- note 44 / `grounded` / **negation** (critical): lost ['not']
- note 44 / `grounded` / **temporality** (warning): lost ['history of']
- note 44 / `grounded` / **severity** (warning): lost ['significant']
- note 44 / `grounded` / **severity_downgrade** (warning): lost ['tier 2']
- note 45 / `naive` / **severity** (warning): lost ['slight']
- note 51 / `naive` / **laterality** (critical): lost ['lateral']
- note 51 / `termonly` / **laterality** (critical): lost ['lateral']
- note 51 / `grounded` / **laterality** (critical): lost ['lateral']
- note 60 / `naive` / **temporality** (warning): lost ['now']
- note 67 / `termonly` / **drug** (policy): lost ['prednisone']
- note 67 / `grounded` / **drug** (policy): lost ['prednisone']
- note 70 / `naive` / **number_unit** (critical): lost ['2']
- note 70 / `grounded` / **number_unit** (critical): lost ['2']
- note 78 / `naive` / **number_unit** (critical): lost ['1']
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
- **naive** (FKGL 7.6, 28 words, 0 edits): He lost interest in things he used to enjoy and stopped caring about social activities. He also had trouble sleeping because he woke up often and felt restless.
    - SARI=13.31  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 14.4, 23 words, 2 edits): He lost the ability to feel pleasure and was not interested in social activities, and had difficulty sleeping for frequent waking and restlessness.
    - SARI=56.21  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 12.8, 21 words, 2 edits): He lost interest in things and was not interested in social activities, and had difficulty sleeping for frequent waking and restlessness.
    - SARI=46.30  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 2 - `18`

- **ORIGINAL**  (FKGL 14.3, 6 words): Myocardial infarction can not be excluded.
- **REFERENCE** (FKGL 4.5, 6 words): Heart attack can not be excluded.
- **naive** (FKGL 12.3, 6 words, 0 edits): Myocardial infarction cannot be ruled out.
    - SARI=14.19  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 2.5, 6 words, 1 edits): A heart attack can still happen.
    - SARI=32.02  crit=1.00  NLIf=0.84  copyjrg=0.00
- **grounded** (FKGL 2.3, 7 words, 1 edits): A heart attack may still be present.
    - SARI=25.97  crit=1.00  NLIf=0.77  copyjrg=0.00

### Note 3 - `21`

- **ORIGINAL**  (FKGL 6.0, 10 words): There was marked hematoma and swelling within the subdeltoid bursa.
- **REFERENCE** (FKGL 7.6, 14 words): There was obvious collection of blood and swelling within the side of the shoulder.
- **naive** (FKGL 5.9, 14 words, 0 edits): There was a large bruise and swelling in the bursa under the deltoid muscle.
    - SARI=38.10  crit=0.00  NLIf=0.92  copyjrg=0.25
- **termonly** (FKGL 7.0, 17 words, 3 edits): There was a lot of blood pooling and swelling in the fluid sac under the shoulder muscle.
    - SARI=43.53  crit=0.00  NLIf=0.73  copyjrg=0.00
- **grounded** (FKGL 7.3, 19 words, 3 edits): There was a lot of a blood pool and swelling within the small fluid sac under the shoulder muscle.
    - SARI=70.33  crit=0.00  NLIf=0.77  copyjrg=0.00

### Note 4 - `26`

- **ORIGINAL**  (FKGL 19.4, 5 words): Smoking history, hypertension, and hyperlipidemia.
- **REFERENCE** (FKGL 4.8, 11 words): Smoking history, high blood pressure, and high fat in the blood.
- **naive** (FKGL 9.7, 8 words, 0 edits): Smoking history, high blood pressure, and high cholesterol.
    - SARI=71.24  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 5.0, 9 words, 2 edits): Smoking history, high blood pressure, and high blood fats.
    - SARI=70.53  crit=0.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 9.7, 8 words, 2 edits): Smoking history, high blood pressure, and high cholesterol.
    - SARI=71.24  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 5 - `31`

- **ORIGINAL**  (FKGL 8.9, 21 words): She did complain of bladder spasms when she urinated and she did say that she has a history of chronic UTIs.
- **REFERENCE** (FKGL 11.8, 23 words): She did complain of bladder spasms when she urinated and she did say that she has a history of chronic urinary tract infections
- **naive** (FKGL 7.7, 17 words, 0 edits): She said she had bladder spasms when she urinated, and she has a history of chronic UTIs.
    - SARI=22.80  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 9.8, 24 words, 3 edits): She did complain of bladder cramps when she passed urine and she did say that she has a history of long-term bladder infections.
    - SARI=34.11  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 14.9, 36 words, 3 edits): She did complain of sudden tight, painful muscle cramps in the sac that holds pee when she passed urine and she did say that she has a history of long-lasting infections in the urinary system.
    - SARI=31.75  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 6 - `32`

- **ORIGINAL**  (FKGL 7.2, 10 words): There was no instability of the knee and no effusion.
- **REFERENCE** (FKGL 8.0, 11 words): There was no instability of the knee and no fluid collection.
- **naive** (FKGL 6.8, 12 words, 0 edits): There was no knee instability and no fluid buildup in the knee.
    - SARI=30.40  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.7, 12 words, 2 edits): There was no looseness of the knee and no fluid build-up.
    - SARI=45.00  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.7, 11 words, 2 edits): There was no wobble of the knee and no extra fluid.
    - SARI=39.24  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 7 - `64`

- **ORIGINAL**  (FKGL 4.9, 13 words): Two days later, the pain resolved and she has not had a recurrence.
- **REFERENCE** (FKGL 5.0, 14 words): Two days later, the pain got better and she has not had a recurrence.
- **naive** (FKGL 3.6, 15 words, 0 edits): Two days later, the pain went away and she has not had it come back.
    - SARI=46.29  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 4.2, 15 words, 2 edits): Two days later, the pain went away and she has not had a come-back.
    - SARI=53.86  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 4.0, 14 words, 2 edits): Two days later, the pain ended and she has not had a come-back.
    - SARI=53.86  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 8 - `81`

- **ORIGINAL**  (FKGL 14.1, 7 words): Description : Fever, otitis media, and possible sepsis.
- **REFERENCE** (FKGL 15.6, 8 words): Description : Fever, ear infection, and possible general infection.
- **naive** (FKGL 7.6, 13 words, 0 edits): Description: The patient has a fever, an ear infection, and may have sepsis.
    - SARI=39.75  crit=0.00  NLIf=0.81  copyjrg=0.50
- **termonly** (FKGL 12.6, 9 words, 2 edits): Fever, middle ear infection, and possible body-wide infection.
    - SARI=53.31  crit=0.00  NLIf=0.83  copyjrg=0.00
- **grounded** (FKGL 12.3, 12 words, 2 edits): Description: Fever, middle ear infection, and possible body-wide infection from germs.
    - SARI=58.99  crit=0.00  NLIf=0.60  copyjrg=0.00

### Note 9 - `101`

- **ORIGINAL**  (FKGL 7.6, 13 words): Currently, primary complaint is one of fatigue that she feels throughout the day.
- **REFERENCE** (FKGL 8.4, 14 words): Currently, primary complaint is one of feeling tired that she feels throughout the day.
- **naive** (FKGL 5.9, 11 words, 0 edits): Currently, the main problem is tiredness that she feels all day.
    - SARI=19.66  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.7, 14 words, 2 edits): Currently, the main issue is one of tiredness that she feels throughout the day.
    - SARI=41.44  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 8.7, 20 words, 1 edits): Currently, the main reason she went to the doctor is feeling tired all over that she feels throughout the day.
    - SARI=39.72  crit=1.00  NLIf=0.00  copyjrg=0.00

### Note 10 - `108`

- **ORIGINAL**  (FKGL 12.3, 19 words): He has noted some stool irregularity with occasional loose stools and new onset of pain predominantly in left neck.
- **REFERENCE** (FKGL 12.3, 19 words): He has noted some poop irregularity with occasional loose poop and new onset of pain predominantly in left neck.
- **naive** (FKGL 9.5, 24 words, 0 edits): He has noticed some changes in his bowel movements with occasional loose stools and new pain mostly in the left side of his neck.
    - SARI=19.62  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 10.2, 22 words, 4 edits): He has noted some change in bowel habits with occasional watery stools and a recent start of pain mostly in left neck.
    - SARI=29.30  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 9.2, 19 words, 4 edits): He has noted some bowel movement change with occasional watery poop and start of pain mostly in left neck.
    - SARI=34.50  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 11 - `143`

- **ORIGINAL**  (FKGL 11.7, 12 words): Description : The patient presents for a followup for history of erythema nodosum.
- **REFERENCE** (FKGL 12.6, 17 words): Description : The patient presents for a followup for history of red, painful tender lumps around fatty areas.
- **naive** (FKGL 8.4, 15 words, 0 edits): The patient comes back for a checkup because they have a history of erythema nodosum.
    - SARI=10.50  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 5.6, 17 words, 1 edits): The patient comes back for a check on a history of tender red bumps on the shins.
    - SARI=21.99  crit=0.00  NLIf=0.18  copyjrg=0.00
- **grounded** (FKGL 5.0, 14 words, 1 edits): The patient comes back for a check on a history of red skin nodules.
    - SARI=22.82  crit=0.00  NLIf=0.83  copyjrg=0.00

### Note 12 - `144`

- **ORIGINAL**  (FKGL 7.5, 22 words): She was iron deficient last year, and with her multiple surgeries and poor p. o. intake, may have become iron deficient again.
- **REFERENCE** (FKGL 12.4, 23 words): She was iron deficient last year, and with her multiple surgeries and poor food and fluid intake, may have become iron deficient again.
- **naive** (FKGL 9.0, 24 words, 0 edits): She was low on iron last year, and with many surgeries and poor food intake by mouth, she may be low on iron again.
    - SARI=26.89  crit=0.00  NLIf=0.14  copyjrg=0.00
- **termonly** (FKGL 11.6, 29 words, 3 edits): She had too little iron in her blood last year, and with her many operations and poor intake by mouth, may have too little iron in her blood again.
    - SARI=23.91  crit=0.00  NLIf=0.19  copyjrg=0.00
- **grounded** (FKGL 11.6, 29 words, 3 edits): She had not enough iron in her blood last year, and with her many operations and poor intake by mouth, may have not enough iron in her blood again.
    - SARI=23.91  crit=0.00  NLIf=0.20  copyjrg=0.00

### Note 13 - `150`

- **ORIGINAL**  (FKGL 9.1, 15 words): We will schedule him for the Holter monitor and refer him back to his cardiologist.
- **REFERENCE** (FKGL 10.6, 16 words): We will schedule him for the continuous heart monitor and refer him back to his cardiologist.
- **naive** (FKGL 5.6, 17 words, 0 edits): We will set up a Holter monitor for him and send him back to his heart doctor.
    - SARI=23.53  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 8.3, 23 words, 2 edits): We will schedule him for a heart rhythm recorder worn for a day or two and refer him back to his heart doctor.
    - SARI=43.61  crit=0.00  NLIf=0.11  copyjrg=0.00
- **grounded** (FKGL 8.7, 20 words, 2 edits): We will schedule him for a portable machine for recording heart beats and refer him back to his heart doctor.
    - SARI=43.95  crit=0.00  NLIf=0.74  copyjrg=0.00

### Note 14 - `161`

- **ORIGINAL**  (FKGL 11.1, 8 words): The patient wished to proceed with operative intervention.
- **REFERENCE** (FKGL 6.7, 8 words): The patient wished to proceed with an operation
- **naive** (FKGL 6.7, 8 words, 0 edits): The patient wanted to go ahead with surgery.
    - SARI=22.50  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.7, 8 words, 2 edits): The patient wanted to go ahead with surgery.
    - SARI=22.50  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.7, 8 words, 2 edits): The patient wanted to go forward with surgery.
    - SARI=22.50  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 15 - `178`

- **ORIGINAL**  (FKGL 7.2, 10 words): A KUB was obtained showing an abnormal bowel gas pattern.
- **REFERENCE** (FKGL 8.4, 17 words): An x-ray of the kidney, ureter and bladder was obtained showing an abnormal bowel gas pattern.
- **naive** (FKGL 6.9, 17 words, 0 edits): A KUB X-ray was taken and it showed an unusual pattern of gas in the bowel.
    - SARI=16.39  crit=0.00  NLIf=0.14  copyjrg=1.00
- **termonly** (FKGL 6.3, 18 words, 2 edits): A plain X-ray of the belly was done showing a bowel gas pattern that is not normal.
    - SARI=28.94  crit=0.00  NLIf=0.64  copyjrg=0.00
- **grounded** (FKGL 7.0, 18 words, 4 edits): A x-ray of the kidneys, ureters, and bladder was done showing a not normal bowel gas design.
    - SARI=26.45  crit=0.00  NLIf=0.11  copyjrg=0.00

### Note 16 - `185`

- **ORIGINAL**  (FKGL 12.3, 19 words): She has been sedated with Ativan and came into the emergency room obtunded and unable to give any history.
- **REFERENCE** (FKGL 12.3, 20 words): She has been sedated with Ativan and came into the emergency room very drowsy and unable to give any history.
- **naive** (FKGL 11.8, 22 words, 0 edits): She was given Ativan to calm her, and she arrived at the emergency room very drowsy and unable to share any history.
    - SARI=30.61  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 12.1, 25 words, 3 edits): She has been calmed with a medicine that slows the brain and came into the emergency room very drowsy and unable to give any history.
    - SARI=53.42  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 12.6, 25 words, 3 edits): She has been made sleepy with a medicine that calms and came into the emergency room not fully alert and unable to give any history.
    - SARI=39.08  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 17 - `202`

- **ORIGINAL**  (FKGL 4.4, 15 words): He has no edema now, but has had some mild leg swelling in the past.
- **REFERENCE** (FKGL 3.6, 15 words): He has no swelling now, but has had some mild leg swelling in the past.
- **naive** (FKGL 4.0, 13 words, 0 edits): He has no swelling now, but he had some mild leg swelling before.
    - SARI=45.99  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 3.6, 15 words, 1 edits): He has no swelling now, but has had some mild leg swelling in the past.
    - SARI=91.67  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.6, 15 words, 1 edits): He has no swelling now, but has had some mild leg swelling in the past.
    - SARI=91.67  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 18 - `231`

- **ORIGINAL**  (FKGL 21.0, 3 words): Mild secondary hyperparathyroidism.
- **REFERENCE** (FKGL 14.7, 5 words): Mild secondary hyperactive parathyroid gland
- **naive** (FKGL 21.0, 3 words, 0 edits): Mild secondary hyperparathyroidism.
    - SARI=12.22  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 9.1, 7 words, 1 edits): Mild overactive parathyroid glands from another cause.
    - SARI=24.07  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 4.5, 6 words, 1 edits): Mild second too much parathyroid hormone.
    - SARI=24.31  crit=0.00  NLIf=0.77  copyjrg=0.00

### Note 19 - `248`

- **ORIGINAL**  (FKGL 10.6, 16 words): Otherwise, a complete review of systems was obtained and was negative except for as mentioned above.
- **REFERENCE** (FKGL 9.8, 16 words): Otherwise, a complete review of systems was obtained and was normal except for as mentioned above.
- **naive** (FKGL 9.1, 17 words, 0 edits): Otherwise, a full review of systems was done and was negative except for what was mentioned above.
    - SARI=17.58  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 8.5, 18 words, 0 edits): Otherwise, a full check of body systems was done and showed no problems except for as mentioned above.
    - SARI=28.44  crit=0.00  NLIf=0.21  copyjrg=0.00
- **grounded** (FKGL 8.5, 18 words, 3 edits): Otherwise, a full set of symptom questions was asked and showed no problems except for as mentioned above.
    - SARI=26.81  crit=0.00  NLIf=0.64  copyjrg=0.00

### Note 20 - `277`

- **ORIGINAL**  (FKGL 7.6, 16 words): Symptoms are worse when sitting for any length of time, such as driving a motor vehicle.
- **REFERENCE** (FKGL 5.2, 15 words): Symptoms are worse when sitting for any length of time, such as driving a car.
- **naive** (FKGL 4.7, 16 words, 0 edits): Symptoms get worse when the person sits for a long time, like when driving a car.
    - SARI=17.77  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.2, 15 words, 1 edits): Symptoms are worse when sitting for any length of time, such as driving a car.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.2, 15 words, 1 edits): Symptoms are worse when sitting for any length of time, such as driving a car.
    - SARI=100.00  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 21 - `290`

- **ORIGINAL**  (FKGL 12.8, 9 words): Forearm, elbow and shoulder exams reveal no neurologic compromise.
- **REFERENCE** (FKGL 7.6, 9 words): Forearm, elbow and shoulder exams reveal no nerve problems
- **naive** (FKGL 8.4, 15 words, 0 edits): The exam of the forearm, elbow, and shoulder shows no nerve or brain-related problems.
    - SARI=39.07  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 5.9, 11 words, 1 edits): Forearm, elbow and shoulder exams show no nerve or brain problem.
    - SARI=48.68  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 5.0, 9 words, 1 edits): Forearm, elbow and shoulder exams show no nerve harm.
    - SARI=50.33  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 22 - `296`

- **ORIGINAL**  (FKGL 13.7, 12 words): Thereafter, the local anesthesia was injected into the area around the tumor.
- **REFERENCE** (FKGL 11.7, 12 words): Thereafter, the numbing agent was injected into the area around the tumor.
- **naive** (FKGL 13.7, 12 words, 0 edits): Thereafter, the local anesthesia was injected into the area around the tumor.
    - SARI=26.80  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 8.5, 13 words, 3 edits): After that, a numbing medicine was put into the area around the growth.
    - SARI=40.82  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 6.7, 13 words, 2 edits): After that, the numbing drug was put into the area around the growth.
    - SARI=42.76  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 23 - `307`

- **ORIGINAL**  (FKGL 3.7, 11 words): There is no numbness or paresthesias in the hand or arm.
- **REFERENCE** (FKGL 5.8, 12 words): There is no numbness or abnormal sensation in the hand or arm.
- **naive** (FKGL 3.7, 11 words, 0 edits): There is no numbness or tingling in the hand or arm.
    - SARI=66.67  crit=0.00  NLIf=0.95  copyjrg=0.00
- **termonly** (FKGL 3.8, 12 words, 1 edits): There is no numbness or odd tingling in the hand or arm.
    - SARI=66.67  crit=0.00  NLIf=0.88  copyjrg=0.00
- **grounded** (FKGL 3.7, 11 words, 1 edits): There is no numbness or tingling in the hand or arm.
    - SARI=66.67  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 24 - `357`

- **ORIGINAL**  (FKGL 7.6, 16 words): I do not think she has an obvious current abscessed lesion, although there is some drainage.
- **REFERENCE** (FKGL 7.7, 17 words): I do not think she has an obvious current collection of pus, although there is some drainage.
- **naive** (FKGL 6.1, 16 words, 0 edits): I do not think she has a clear current abscessed lesion, although there is some drainage.
    - SARI=29.85  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 8.0, 19 words, 2 edits): I do not think she has an obvious current pocket of pus, although there is some fluid coming out.
    - SARI=68.61  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 7.3, 19 words, 2 edits): I do not think she has an obvious current wound or sore, although there is some fluid leaking out.
    - SARI=57.08  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 25 - `358`

- **ORIGINAL**  (FKGL 9.1, 11 words): At this time, we would rehydrate with intravenous fluids and reassess.
- **REFERENCE** (FKGL 5.8, 13 words): At this time, we would rehydrate with fluids through the vein and reassess.
- **naive** (FKGL 3.6, 15 words, 0 edits): At this time, the team would give fluids through a vein and then check again.
    - SARI=31.98  crit=0.00  NLIf=0.80  copyjrg=0.00
- **termonly** (FKGL 5.6, 17 words, 2 edits): At this time, we would give fluids by vein to replace lost water and then check again.
    - SARI=43.37  crit=0.00  NLIf=0.80  copyjrg=0.00
- **grounded** (FKGL 4.7, 16 words, 2 edits): At this time, we would give fluids by vein to add water back and check again.
    - SARI=43.48  crit=0.00  NLIf=0.89  copyjrg=0.00

### Note 26 - `380`

- **ORIGINAL**  (FKGL 14.3, 6 words): Findings are compatible with acute appendicitis.
- **REFERENCE** (FKGL 12.8, 9 words): Findings are compatible with acute inflammation of the appendix
- **naive** (FKGL 10.0, 5 words, 0 edits): Findings fit with acute appendicitis.
    - SARI=11.11  crit=1.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 8.4, 10 words, 2 edits): The results match a sudden belly infection near the appendix.
    - SARI=11.76  crit=1.00  NLIf=0.60  copyjrg=0.00
- **grounded** (FKGL 7.6, 10 words, 2 edits): The test results fit a sudden, short-term appendix swelling.
    - SARI=10.30  crit=1.00  NLIf=0.94  copyjrg=0.00

### Note 27 - `391`

- **ORIGINAL**  (FKGL 10.5, 18 words): She denies weight loss, but acknowledged decreased appetite and increased generalized fatigue for the past 3-4 months.
- **REFERENCE** (FKGL 10.5, 18 words): She denies weight loss, but acknowledged reduced appetite and more generalized tiredness for the past 3-4 months.
- **naive** (FKGL 9.9, 30 words, 0 edits): She says she has not lost weight, but she says her appetite has gone down and she has felt very tired all over for the past 3 to 4 months.
    - SARI=34.75  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 6.9, 24 words, 2 edits): She says no to weight loss, but said she has had less hunger and more whole-body tiredness for the past 3-4 months.
    - SARI=51.40  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.6, 26 words, 4 edits): She says no to weight loss, but said she has less want to eat food and more whole-body tired for the past 3-4 months.
    - SARI=48.12  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 28 - `392`

- **ORIGINAL**  (FKGL 21.8, 5 words): Consideration given to completion thyroidectomy.
- **REFERENCE** (FKGL 11.5, 9 words): Consideration given to remove remaining parts of the thyroid
- **naive** (FKGL 10.7, 7 words, 0 edits): Consider thyroid removal is being thought about.
    - SARI=22.67  crit=1.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 11.9, 10 words, 1 edits): Consideration is given to finishing the removal of the thyroid.
    - SARI=49.40  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 7.6, 14 words, 1 edits): The team is thinking about finishing the surgery to take out the thyroid gland.
    - SARI=29.23  crit=1.00  NLIf=0.79  copyjrg=0.00

### Note 29 - `394`

- **ORIGINAL**  (FKGL 10.5, 19 words): She notes that she had epistaxis a few days ago, requiring nasal packing and fortunately that had resolved now.
- **REFERENCE** (FKGL 9.5, 21 words): She notes that she had a nose bleed a few days ago, requiring nose packing and fortunately that had resolved now.
- **naive** (FKGL 3.1, 21 words, 0 edits): She says she had a nosebleed a few days ago. It needed packing in the nose, and it is better now.
    - SARI=29.71  crit=0.00  NLIf=0.89  copyjrg=0.00
- **termonly** (FKGL 8.3, 23 words, 4 edits): She notes that she had a nose bleed a few days ago, needing a nose plug and fortunately that had gone away now.
    - SARI=60.29  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 13.1, 32 words, 4 edits): She notes that she had a nosebleed a few days ago, needing something put into her nose to help it heal and fortunately that had been brought to a successful solution now.
    - SARI=47.18  crit=0.00  NLIf=0.92  copyjrg=0.00

### Note 30 - `396`

- **ORIGINAL**  (FKGL 8.9, 9 words): I also explained to the patient about conscious sedation.
- **REFERENCE** (FKGL 8.9, 9 words): I also explained to the patient about awake sedation.
- **naive** (FKGL 8.2, 8 words, 0 edits): I also told the patient about conscious sedation.
    - SARI=13.30  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 8.4, 16 words, 1 edits): I also explained to the patient about a calm, sleepy medicine that lets them stay awake.
    - SARI=63.61  crit=0.00  NLIf=0.17  copyjrg=0.00
- **grounded** (FKGL 7.8, 12 words, 1 edits): I also told the patient about light sleep medicine for a procedure.
    - SARI=25.72  crit=0.00  NLIf=0.21  copyjrg=0.00

### Note 31 - `762`

- **ORIGINAL**  (FKGL 5.2, 8 words): Palpation of her right knee reveals no crepitus.
- **REFERENCE** (FKGL 5.0, 9 words): Feeling of her right knee reveals no crunchy feeling.
- **naive** (FKGL 5.2, 8 words, 0 edits): Palpation of her right knee reveals no crepitus.
    - SARI=27.00  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 2.3, 7 words, 1 edits): Feeling her right knee shows no crackling.
    - SARI=32.26  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 2.6, 11 words, 1 edits): Feeling her right knee with her hands shows no crackling sound.
    - SARI=31.01  crit=0.00  NLIf=0.62  copyjrg=0.00

### Note 32 - `427`

- **ORIGINAL**  (FKGL 10.1, 14 words): She stepped on ideas, concerns and expectations the evening prior and twisted her ankle.
- **REFERENCE** (FKGL 4.8, 11 words): She stepped on ice the evening prior and twisted her ankle.
- **naive** (FKGL 10.1, 14 words, 0 edits): She stepped on ideas, concerns and expectations the evening prior and twisted her ankle.
    - SARI=23.68  crit=0.00  NLIf=0.99
- **termonly** (FKGL 8.5, 13 words, 1 edits): She stepped on ideas, concerns and expectations last night and twisted her ankle.
    - SARI=26.24  crit=0.00  NLIf=0.99
- **grounded** (FKGL 9.3, 14 words, 1 edits): She stepped on ideas, concerns and expectations the night before and twisted her ankle.
    - SARI=21.81  crit=0.00  NLIf=0.99

### Note 33 - `439`

- **ORIGINAL**  (FKGL 14.1, 9 words): Modifying Factors : Patient 's condition is aggravated by throwing.
- **REFERENCE** (FKGL 9.6, 10 words): Modifying Factors : Patient 's condition is made worse by throwing.
- **naive** (FKGL 3.7, 11 words, 0 edits): The patient's condition gets worse when he or she throws.
    - SARI=26.21  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.2, 9 words, 1 edits): The patient’s condition is made worse by throwing.
    - SARI=69.10  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.2, 9 words, 1 edits): The patient’s condition is made worse by throwing.
    - SARI=69.10  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 34 - `451`

- **ORIGINAL**  (FKGL 21.3, 10 words): History of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis and kidney stones.
- **REFERENCE** (FKGL 14.9, 13 words): History of joint inflammation, bone degeneration, underactive thyroid, hay fever and kidney stones.
- **naive** (FKGL 21.3, 10 words, 0 edits): History of osteoarthritis, osteoporosis, hypothyroidism, allergic rhinitis and kidney stones.
    - SARI=11.57  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 5.8, 13 words, 4 edits): History of joint wear, bone loss, low thyroid, hay fever and kidney stones.
    - SARI=73.08  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 12.8, 22 words, 5 edits): History of worn-out joints, weak bones that break easily, low thyroid activity, nose allergy, and hard mineral deposits in the kidneys.
    - SARI=38.86  crit=0.00  NLIf=0.75  copyjrg=0.00

### Note 35 - `465`

- **ORIGINAL**  (FKGL 15.8, 7 words): The ultrasound was negative for intracranial hemorrhage.
- **REFERENCE** (FKGL 6.3, 9 words): The ultrasound was negative for bleeding in the brain.
- **naive** (FKGL 5.2, 8 words, 0 edits): The ultrasound showed no bleeding inside the head.
    - SARI=24.35  crit=0.00  NLIf=0.94  copyjrg=0.00
- **termonly** (FKGL 3.8, 8 words, 1 edits): The ultrasound showed no bleed inside the skull.
    - SARI=22.26  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 5.2, 8 words, 1 edits): The ultrasound showed no bleeding within the brain.
    - SARI=28.10  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 36 - `466`

- **ORIGINAL**  (FKGL 14.7, 12 words): He is status post laparoscopic appendicectomy, and he is tolerating oral diet.
- **REFERENCE** (FKGL 12.3, 15 words): He is status after keyhole surgery to remove appendix, and he is tolerating oral diet.
- **naive** (FKGL 13.7, 12 words, 0 edits): He had a laparoscopic appendectomy, and he is tolerating an oral diet.
    - SARI=45.46  crit=0.00  NLIf=0.99  copyjrg=0.25
- **termonly** (FKGL 6.3, 17 words, 2 edits): He had a keyhole appendix removal in the past, and he can keep food down by mouth.
    - SARI=23.75  crit=0.00  NLIf=0.77  copyjrg=0.00
- **grounded** (FKGL 8.0, 19 words, 2 edits): He had a keyhole surgery to remove his appendix, and he is able to eat and drink by mouth.
    - SARI=41.12  crit=0.00  NLIf=0.82  copyjrg=0.00

### Note 37 - `478`

- **ORIGINAL**  (FKGL 8.4, 14 words): We believe that her walking is most likely not being affected by the hydrocephalus.
- **REFERENCE** (FKGL 8.5, 18 words): We believe that her walking is most likely not being affected by the excess fluid in the brain.
- **naive** (FKGL 7.6, 13 words, 0 edits): We think her walking is most likely not being affected by the hydrocephalus.
    - SARI=27.30  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 8.6, 19 words, 1 edits): We believe that her walking is most likely not being affected by a buildup of fluid in the brain.
    - SARI=66.30  crit=0.00  NLIf=0.78  copyjrg=0.00
- **grounded** (FKGL 7.8, 18 words, 1 edits): We believe that her walking is most likely not being affected by too much fluid in the brain.
    - SARI=67.62  crit=0.00  NLIf=0.75  copyjrg=0.00

### Note 38 - `505`

- **ORIGINAL**  (FKGL 12.3, 11 words): She noted complaints of fatigue, lightheadedness, and severe dyspnea on exertion.
- **REFERENCE** (FKGL 13.1, 15 words): She noted complaints of tiredness, lightheadedness, and severe shortness of breath on doing anything physical.
- **naive** (FKGL 6.5, 18 words, 0 edits): She said she felt tired, dizzy, and had very hard trouble breathing when she tried to do things.
    - SARI=23.12  crit=1.00  NLIf=0.95  copyjrg=0.00
- **termonly** (FKGL 8.4, 14 words, 3 edits): She said she had tiredness, feeling faint, and severe shortness of breath with activity.
    - SARI=38.88  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 9.1, 16 words, 3 edits): She said she had tiredness, feeling dizzy or almost faint, and severe trouble breathing with effort.
    - SARI=28.85  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 39 - `516`

- **ORIGINAL**  (FKGL 10.9, 14 words): No significant amount of edema associated with these in the dorsum of the hand.
- **REFERENCE** (FKGL 9.3, 14 words): No significant amount of swelling associated with these in the back of the hand.
- **naive** (FKGL 10.9, 14 words, 0 edits): No significant amount of edema associated with these in the dorsum of the hand.
    - SARI=23.64  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 1.9, 12 words, 3 edits): No clear swelling linked to these on the back of the hand.
    - SARI=38.22  crit=0.00  NLIf=0.69  copyjrg=0.00
- **grounded** (FKGL 1.9, 12 words, 2 edits): No big swelling linked to these on the back of the hand.
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
- **naive** (FKGL 5.2, 16 words, 0 edits): At that time, the doctor had stopped Coreg because the patient’s blood pressure was low.
    - SARI=40.54  crit=0.00  NLIf=0.17  copyjrg=0.00
- **termonly** (FKGL 4.9, 13 words, 3 edits): At that time, the medicine had been held because of low blood pressure.
    - SARI=68.93  crit=0.00  NLIf=0.85  copyjrg=0.00
- **grounded** (FKGL 4.9, 13 words, 3 edits): At that time, the medicine had been held because of low blood pressure.
    - SARI=68.93  crit=0.00  NLIf=0.85  copyjrg=0.00

### Note 42 - `554`

- **ORIGINAL**  (FKGL 12.8, 16 words): Her diarrhea now has settled down and she is having less urinary incontinence, less pedal edema.
- **REFERENCE** (FKGL 8.4, 17 words): Her watery poop now has settled down and she is having less uncontrolled peeing, less foot swelling.
- **naive** (FKGL 7.7, 17 words, 0 edits): Her diarrhea has eased, and she is having less urine leakage and less swelling in her feet.
    - SARI=42.72  crit=0.00  NLIf=0.86  copyjrg=0.33
- **termonly** (FKGL 5.9, 18 words, 3 edits): Her loose stools have settled down and she is leaking urine less, with less swelling in her feet.
    - SARI=43.97  crit=0.00  NLIf=0.81  copyjrg=0.00
- **grounded** (FKGL 8.0, 19 words, 3 edits): Her loose, watery poop has settled down and she is having less loss of bladder control, less swollen feet.
    - SARI=62.90  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 43 - `556`

- **ORIGINAL**  (FKGL 19.4, 13 words): Description : Nausea and abdominal pain after eating - Gall bladder disease - Laparoscopic cholecystectomy scheduled.
- **REFERENCE** (FKGL 14.4, 18 words): Description : Nausea and abdominal pain after eating - Gall bladder disease - keyhole surgery to remove the gall bladder scheduled.
- **naive** (FKGL 9.9, 19 words, 0 edits): The patient has nausea and belly pain after eating. This is from gallbladder disease. A laparoscopic cholecystectomy is scheduled.
    - SARI=19.81  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 5.8, 27 words, 4 edits): The patient has a stomach ache after eating and feels sick to the stomach. The patient has a gallbladder problem. A planned keyhole gallbladder removal is set.
    - SARI=16.33  crit=0.00  NLIf=0.82  copyjrg=0.00
- **grounded** (FKGL 13.9, 33 words, 3 edits): The patient has a sick gallbladder and feels sick to the stomach and has a stomach ache after eating, and a planned small-tube camera surgery to take out the gallbladder is set.
    - SARI=16.48  crit=0.00  NLIf=0.84  copyjrg=0.00

### Note 44 - `618`

- **ORIGINAL**  (FKGL 12.3, 20 words): She states that she has underlying history of heart disease but is not able to elaborate to any significant extent.
- **REFERENCE** (FKGL 12.3, 22 words): She states that she has underlying history of heart disease but is not able to go into detail to any significant extent.
- **naive** (FKGL 6.0, 15 words, 0 edits): She says she has a history of heart disease, but she cannot give more details.
    - SARI=19.50  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.8, 13 words, 2 edits): She says she has long-standing heart disease but cannot give more detail.
    - SARI=14.28  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 5.8, 14 words, 2 edits): She says she has a long-standing heart disease but cannot give much detail.
    - SARI=14.13  crit=1.00  NLIf=0.99  copyjrg=0.00

### Note 45 - `661`

- **ORIGINAL**  (FKGL 6.5, 18 words): There was some slight edema of the fourth digit, on which he still is wearing his wedding band.
- **REFERENCE** (FKGL 5.9, 18 words): There was some slight swelling of the fourth finger, on which he still is wearing his wedding band.
- **naive** (FKGL 6.7, 19 words, 0 edits): There was a little swelling of the fourth finger, and he is still wearing his wedding band on it.
    - SARI=43.00  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 5.9, 18 words, 2 edits): There was some slight swelling of the ring finger, on which he still is wearing his wedding band.
    - SARI=81.51  crit=0.00  NLIf=0.24  copyjrg=0.00
- **grounded** (FKGL 5.9, 18 words, 2 edits): There was some slight swelling of the ring finger, on which he still is wearing his wedding band.
    - SARI=81.51  crit=0.00  NLIf=0.24  copyjrg=0.00

### Note 46 - `669`

- **ORIGINAL**  (FKGL 12.8, 21 words): Parents do state that she does appear to breathe rapidly, tires somewhat with the feeding with increased respiratory effort and diaphoresis.
- **REFERENCE** (FKGL 10.0, 21 words): Parents do state that she does appear to breathe quickly, tires somewhat with the feeding with increased breathing effort and sweating.
- **naive** (FKGL 6.1, 19 words, 0 edits): Parents say she seems to breathe fast, gets a bit tired during feeds, works harder to breathe, and sweats.
    - SARI=15.19  crit=0.00  NLIf=0.18  copyjrg=0.00
- **termonly** (FKGL 6.4, 20 words, 3 edits): Parents say she seems to breathe fast, gets a bit tired with feeding with more work to breathe and sweating.
    - SARI=20.18  crit=0.00  NLIf=0.73  copyjrg=0.00
- **grounded** (FKGL 7.8, 21 words, 3 edits): Parents say she seems to breathe quickly, gets a bit tired with feeding with more work to breathe and heavy sweating.
    - SARI=21.88  crit=0.00  NLIf=0.12  copyjrg=0.00

### Note 47 - `673`

- **ORIGINAL**  (FKGL 11.3, 26 words): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had onset of chest pain this evening.
- **REFERENCE** (FKGL 10.5, 24 words): The patient has not used amphetamines for at least four to five months, according to the patient ; however, he had chest pain this evening.
- **naive** (FKGL 4.3, 23 words, 0 edits): The patient says he has not used amphetamines for at least four to five months. However, he had chest pain start this evening.
    - SARI=46.12  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 11.5, 30 words, 2 edits): The patient says he has not used a medicine that raises energy and mood for at least four to five months; however, he had start of chest pain this evening.
    - SARI=31.05  crit=0.00  NLIf=0.13  copyjrg=0.00
- **grounded** (FKGL 12.6, 34 words, 2 edits): The patient says he has not used a stimulant drug that helps people stay awake and focus for at least four to five months; however, he had the start of chest pain this evening.
    - SARI=31.08  crit=0.00  NLIf=0.15  copyjrg=0.00

### Note 48 - `675`

- **ORIGINAL**  (FKGL 8.4, 10 words): Orogastric suction carried out with only scant clear stomach contents.
- **REFERENCE** (FKGL 7.6, 16 words): Suction of stomach through the mouth carried out with only a small amount clear stomach contents
- **naive** (FKGL 7.6, 15 words, 0 edits): Orogastric suction was done and only a small amount of clear stomach contents came out.
    - SARI=44.01  crit=0.00  NLIf=0.99  copyjrg=0.67
- **termonly** (FKGL 9.7, 25 words, 1 edits): A tube placed through the mouth into the stomach to remove fluid was done, with only a small amount of clear fluid from the stomach.
    - SARI=38.25  crit=0.00  NLIf=0.93  copyjrg=0.00
- **grounded** (FKGL 10.0, 28 words, 1 edits): A tube through the mouth to the stomach was used to pull out fluid, and only a very small amount of easy-to-see stomach fluid came out.
    - SARI=29.90  crit=0.00  NLIf=0.76  copyjrg=0.00

### Note 49 - `680`

- **ORIGINAL**  (FKGL 11.5, 9 words): Probably there is some restrictive element because of fibrosis.
- **REFERENCE** (FKGL 10.2, 11 words): Probably there is some restrictive element because of scarring of tissues.
- **naive** (FKGL 11.5, 9 words, 0 edits): Probably there is some restrictive element because of fibrosis.
    - SARI=30.89  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 7.2, 10 words, 2 edits): Probably there is some limiting part because of scar tissue.
    - SARI=28.34  crit=0.00  NLIf=0.91  copyjrg=0.00
- **grounded** (FKGL 9.1, 17 words, 2 edits): Probably there is some limiting part because of tissue that becomes thick and scarred due to injury.
    - SARI=28.34  crit=0.00  NLIf=0.12  copyjrg=0.00

### Note 50 - `681`

- **ORIGINAL**  (FKGL 10.2, 9 words): The uterus was placed back into the abdominal cavity.
- **REFERENCE** (FKGL 3.8, 8 words): The womb was placed back into the abdomen
- **naive** (FKGL 5.2, 8 words, 0 edits): The uterus was put back into the belly.
    - SARI=34.72  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL 2.3, 8 words, 2 edits): The womb was placed back into the belly.
    - SARI=87.50  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 9.1, 17 words, 2 edits): The womb was placed back into the belly area where the stomach and other organs are located.
    - SARI=74.72  crit=0.00  NLIf=0.32  copyjrg=0.00

### Note 51 - `682`

- **ORIGINAL**  (FKGL 5.0, 9 words): This was viewed on the AP and lateral projections.
- **REFERENCE** (FKGL -0.7, 8 words): This was viewed from the front and sides.
- **naive** (FKGL 0.1, 11 words, 0 edits): This was seen on the front and side X-ray views.
    - SARI=45.11  crit=1.00  NLIf=0.36  copyjrg=0.00
- **termonly** (FKGL -0.3, 9 words, 2 edits): This was viewed on the front and side views.
    - SARI=58.96  crit=1.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 0.5, 11 words, 2 edits): This was viewed on the front to back and side views.
    - SARI=54.23  crit=1.00  NLIf=0.89  copyjrg=0.00

### Note 52 - `686`

- **ORIGINAL**  (FKGL 8.2, 8 words): The cords move normally with phonation and ventilation.
- **REFERENCE** (FKGL 5.2, 8 words): The cords move normally when speaking and breathing
- **naive** (FKGL 4.8, 11 words, 0 edits): The vocal cords move normally when the patient speaks and breathes.
    - SARI=55.14  crit=0.00  NLIf=0.90  copyjrg=0.00
- **termonly** (FKGL 4.8, 11 words, 3 edits): The voice bands move normally with sound making and air moving.
    - SARI=32.22  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 4.8, 11 words, 3 edits): The long, thin ropes move normally with making sounds and breathing.
    - SARI=35.46  crit=0.00  NLIf=0.10  copyjrg=0.00

### Note 53 - `688`

- **ORIGINAL**  (FKGL 7.6, 13 words): Once the abdomen was opened, there was noted to be gross purulent drainage.
- **REFERENCE** (FKGL 6.0, 15 words): Once the abdomen was opened, there was noted to be a lot of pus draining.
- **naive** (FKGL 7.6, 13 words, 0 edits): Once the abdomen was opened, there was noted to be gross purulent drainage.
    - SARI=28.27  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 7.0, 18 words, 2 edits): Once the belly was opened, there was noted to be a lot of thick yellow-green pus draining.
    - SARI=63.89  crit=0.00  NLIf=0.01  copyjrg=0.00
- **grounded** (FKGL 5.4, 16 words, 2 edits): Once the belly was opened, there was noted to be a lot of pus leaking out.
    - SARI=67.45  crit=0.00  NLIf=0.91  copyjrg=0.00

### Note 54 - `692`

- **ORIGINAL**  (FKGL 4.0, 13 words): Once all four ports were placed, the right upper quadrant was then explored.
- **REFERENCE** (FKGL 5.4, 16 words): Once all four tubes were placed, the top right corner of her abdomen was then explored.
- **naive** (FKGL 4.0, 13 words, 0 edits): Once all four ports were placed, the right upper quadrant was then explored.
    - SARI=16.37  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 7.6, 16 words, 3 edits): Once all four small openings were placed, the upper right belly area was then looked into.
    - SARI=50.18  crit=0.00  NLIf=0.84  copyjrg=0.00
- **grounded** (FKGL 6.1, 16 words, 3 edits): Once all four entry points were placed, the upper right belly area was then looked at.
    - SARI=50.18  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 55 - `693`

- **ORIGINAL**  (FKGL 15.4, 15 words): Options such as watchful waiting, robotic prostatectomy, seed implantation with and without radiation were discussed.
- **REFERENCE** (FKGL 11.8, 23 words): Options such as watch and wait, removing the prostate with the help of a robot, seed implantation with and without radiation were discussed.
- **naive** (FKGL 15.4, 15 words, 0 edits): Options such as watchful waiting, robotic prostatectomy, seed implantation with and without radiation were discussed.
    - SARI=24.31  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 10.7, 22 words, 4 edits): The patient talked about waiting and watching, surgery by robot to remove the prostate, and putting seeds in with and without rays.
    - SARI=25.82  crit=0.00  NLIf=0.45  copyjrg=0.00
- **grounded** (FKGL 16.8, 34 words, 4 edits): Options such as close watch with no treatment for now, robot-assisted prostate removal, and placing tiny radioactive seeds in the prostate with and without high-energy rays to kill cancer cells were discussed.
    - SARI=38.75  crit=0.00  NLIf=0.49  copyjrg=0.00

### Note 56 - `695`

- **ORIGINAL**  (FKGL 14.3, 10 words): He also reportedly was on Lasix prior to hospitalization, possible
- **REFERENCE** (FKGL 11.5, 15 words): He also was reportedly on water pills (lasix) before his admission to the hospital, possible
- **naive** (FKGL 7.6, 14 words, 0 edits): He was also said to have been on Lasix before he was hospitalized, possibly.
    - SARI=37.24  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 11.5, 24 words, 3 edits): He also was said to be on a medicine that helps the body get rid of extra water before being in the hospital, possible.
    - SARI=49.80  crit=0.00  NLIf=0.25  copyjrg=0.00
- **grounded** (FKGL 13.0, 25 words, 4 edits): He also people say he was on a medicine that helps the body get rid of extra water before being admitted to a hospital, possible
    - SARI=45.12  crit=0.00  NLIf=0.27  copyjrg=0.00

### Note 57 - `697`

- **ORIGINAL**  (FKGL 10.2, 9 words): The four cardiac chambers dimensions are within normal limits.
- **REFERENCE** (FKGL 4.9, 13 words): The sizes of the four parts of the heart are within normal limits.
- **naive** (FKGL 2.5, 10 words, 0 edits): The four chambers of the heart are normal in size.
    - SARI=41.72  crit=0.00  NLIf=0.98  copyjrg=0.25
- **termonly** (FKGL 2.3, 7 words, 3 edits): The four heart rooms sizes are normal.
    - SARI=37.42  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 6.7, 14 words, 3 edits): The four heart rooms sizes are as expected for a person similar to you.
    - SARI=32.94  crit=0.00  NLIf=0.18  copyjrg=0.00

### Note 58 - `698`

- **ORIGINAL**  (FKGL 11.5, 9 words): Digital rectal examination was performed, which showed no masses.
- **REFERENCE** (FKGL 6.9, 11 words): Examination of the back passage was performed, which showed no lumps.
- **naive** (FKGL 5.0, 14 words, 0 edits): The doctor checked the rectum with a finger and did not feel any lumps.
    - SARI=19.11  crit=0.00  NLIf=0.06  copyjrg=0.00
- **termonly** (FKGL 3.1, 13 words, 3 edits): A finger check of the back passage was done, which showed no lumps.
    - SARI=56.51  crit=0.00  NLIf=0.36  copyjrg=0.00
- **grounded** (FKGL 2.9, 12 words, 3 edits): A finger check of the rectum was done, which showed no lumps.
    - SARI=46.35  crit=0.00  NLIf=0.20  copyjrg=0.00

### Note 59 - `699`

- **ORIGINAL**  (FKGL 11.2, 23 words): He then had a problem with seizures, hemiparesis, has been to the hospital, developed C-diff, and is in the nursing home currently.
- **REFERENCE** (FKGL 12.0, 29 words): He then had a problem with fits, weakness on one side, has been to the hospital, developed an infection in the gut, and is in the nursing home currently.
- **naive** (FKGL 4.9, 26 words, 0 edits): He then had seizures and weakness on one side of the body, went to the hospital, developed C. diff, and is now in a nursing home.
    - SARI=31.42  crit=0.00  NLIf=0.97  copyjrg=0.33
- **termonly** (FKGL 7.6, 31 words, 3 edits): He then had a problem with fits, weakness on one side of the body, has been to the hospital, developed a C. difficile infection, and is in the nursing home currently.
    - SARI=80.90  crit=0.00  NLIf=0.94  copyjrg=0.00
- **grounded** (FKGL 19.8, 46 words, 3 edits): He then had a problem with brain events that can cause loss of consciousness and jerky movements, weakness on one side of the body, has been to the hospital, developed a gut infection that causes fever, diarrhea, and cramps, and is in the nursing home currently.
    - SARI=72.45  crit=0.00  NLIf=0.61  copyjrg=0.00

### Note 60 - `700`

- **ORIGINAL**  (FKGL 12.3, 22 words): He has been on continuous positive airway pressure now for several months, and returns for followup to review his response to treatment.
- **REFERENCE** (FKGL 9.7, 25 words): He has been using a breathing mask now for several months, and returns for follow up to review how he is doing with the treatment.
- **naive** (FKGL 13.0, 26 words, 0 edits): He has been using continuous positive airway pressure for several months and is back for a follow-up visit to review how the treatment is working.
    - SARI=53.82  crit=0.00  NLIf=0.99  copyjrg=0.83
- **termonly** (FKGL 10.4, 30 words, 2 edits): He has been on a machine that keeps air pressure up in the lungs now for several months, and returns for a check-in to review his response to treatment.
    - SARI=60.97  crit=0.00  NLIf=0.90  copyjrg=0.17
- **grounded** (FKGL 11.2, 29 words, 2 edits): He has been on a machine that keeps air pressure in his breathing tube now for several months, and returns for a checkup to review his response to treatment.
    - SARI=60.25  crit=0.00  NLIf=0.81  copyjrg=0.17

### Note 61 - `709`

- **ORIGINAL**  (FKGL 8.5, 18 words): The patient to take small bite and small sips to help decrease the risk of aspiration and penetration.
- **REFERENCE** (FKGL 9.9, 30 words): The patient is to take small bite and small sips to help decrease the risk of having the food or drink going down the wrong pipe and piercing the pipe.
- **naive** (FKGL 8.5, 18 words, 0 edits): The patient should take small bites and small sips to help lower the risk of aspiration and penetration.
    - SARI=23.61  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 12.9, 35 words, 2 edits): The patient should take small bites and small sips to help lower the risk of food or liquid going into the lungs and of food or liquid going past the voice box into the airway.
    - SARI=38.48  crit=0.00  NLIf=0.38  copyjrg=0.00
- **grounded** (FKGL 12.7, 33 words, 2 edits): The patient should take small bites and small sips to help lower the risk of breathing food or liquid into the lungs by mistake and of food or liquid going into the airways.
    - SARI=38.48  crit=0.00  NLIf=0.95  copyjrg=0.00

### Note 62 - `714`

- **ORIGINAL**  (FKGL 12.3, 15 words): The patient was awakened and extubated and moved to the recovery room in satisfactory condition.
- **REFERENCE** (FKGL 11.1, 20 words): The patient was awakened and tube was removed from the airway and moved to the recovery room in satisfactory condition.
- **naive** (FKGL 8.1, 20 words, 0 edits): The patient woke up, the breathing tube was removed, and they were moved to the recovery room in good condition.
    - SARI=39.05  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 8.9, 21 words, 3 edits): The patient was woken up and the breathing tube was taken out and moved to the recovery room in good condition.
    - SARI=41.85  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 9.6, 22 words, 3 edits): The patient was woken up and the breathing tube was taken out and moved to the recovery room in good enough condition.
    - SARI=41.68  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 63 - `721`

- **ORIGINAL**  (FKGL 15.4, 10 words): PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily aroused.
- **REFERENCE** (FKGL 6.7, 8 words): The patient was asleep, but easily woken up.
- **naive** (FKGL 6.0, 10 words, 0 edits): The patient was asleep but could be woken up easily.
    - SARI=65.82  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 14.4, 11 words, 1 edits): PHYSICAL EXAMINATION : GENERAL : The patient was asleep, but easily woken up.
    - SARI=91.36  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 6.3, 9 words, 1 edits): The patient was asleep, but could be woken easily.
    - SARI=61.22  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 64 - `725`

- **ORIGINAL**  (FKGL 10.9, 26 words): He is to follow up in approximately 10 days for recheck as well as prescription for intended AFOs, which he will need up to 6 months.
- **REFERENCE** (FKGL 11.5, 28 words): He is to come back in approximately 10 days for recheck as well as prescription for intended foot-drop braces, which he will need up to 6 months.
- **naive** (FKGL 4.2, 31 words, 0 edits): He will return in about 10 days for a recheck and to get a prescription for the AFOs he plans to use. He may need them for up to 6 months.
    - SARI=24.14  crit=0.00  NLIf=0.98  copyjrg=1.00
- **termonly** (FKGL 11.1, 28 words, 2 edits): He is to follow up in about 10 days for recheck as well as prescription for intended ankle-foot braces, which he will need up to 6 months.
    - SARI=56.24  crit=0.00  NLIf=0.63  copyjrg=0.00
- **grounded** (FKGL 12.1, 31 words, 2 edits): He is to follow up in about 10 days for recheck as well as prescription for intended braces that support ankle or foot, which he will need up to 6 months.
    - SARI=52.26  crit=0.00  NLIf=0.77  copyjrg=0.00

### Note 65 - `726`

- **ORIGINAL**  (FKGL 14.1, 8 words): Genitourinary : The external genitalia appeared to be normal.
- **REFERENCE** (FKGL 12.3, 8 words): The penis/vagina/genitals appeared to be normal.
- **naive** (FKGL 5.7, 7 words, 0 edits): The outside of the genitals looked normal.
    - SARI=28.29  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 11.9, 10 words, 0 edits): Urinary and sexual organs: The outside sexual parts looked normal.
    - SARI=25.91  crit=0.00  NLIf=0.67  copyjrg=0.00
- **grounded** (FKGL 6.9, 16 words, 0 edits): The parts used for peeing and sex stuff: The outside sex and reproduction parts looked normal.
    - SARI=25.91  crit=0.00  NLIf=0.15  copyjrg=0.00

### Note 66 - `727`

- **ORIGINAL**  (FKGL 12.2, 13 words): She is postop day 21 of an exploratory laparotomy with ovarian cancer staging.
- **REFERENCE** (FKGL 12.6, 17 words): She is 21 days after an open abdominal operation which explored how widespread the ovarian cancer was.
- **naive** (FKGL 14.3, 14 words, 0 edits): She is 21 days after surgery for an exploratory laparotomy with ovarian cancer staging.
    - SARI=51.87  crit=0.00  NLIf=0.99  copyjrg=0.75
- **termonly** (FKGL 10.4, 19 words, 3 edits): She is 21 days after surgery for a look-inside belly operation with cancer spread check of the ovaries.
    - SARI=48.37  crit=0.00  NLIf=0.87  copyjrg=0.00
- **grounded** (FKGL 9.9, 20 words, 3 edits): She is 21 days after surgery from a belly check surgery with checking how far the ovary cancer has spread.
    - SARI=48.93  crit=0.00  NLIf=0.64  copyjrg=0.00

### Note 67 - `732`

- **ORIGINAL**  (FKGL 8.5, 13 words): Prescription for prednisone as part of his chemotherapy has been given to him.
- **REFERENCE** (FKGL 7.6, 15 words): Prescription for steroid tablets as part of his cancer treatment has been given to him.
- **naive** (FKGL 9.3, 14 words, 0 edits): The patient has been given a prescription for prednisone as part of his chemotherapy.
    - SARI=30.89  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 9.9, 20 words, 1 edits): Prescription for a medicine that lowers the immune system as part of his cancer treatment has been given to him.
    - SARI=78.97  crit=0.00  NLIf=0.63  copyjrg=0.00
- **grounded** (FKGL 13.6, 32 words, 2 edits): The prescription for a medicine that lowers the body's immune response and inflammation as part of his drug treatment to stop the growth of cancer cells has been given to him.
    - SARI=68.25  crit=0.00  NLIf=0.24  copyjrg=0.00

### Note 68 - `738`

- **ORIGINAL**  (FKGL 9.1, 12 words): Photic stimulation was performed, but no clear-cut photic driving was seen.
- **REFERENCE** (FKGL 12.8, 17 words): Visual stimulation was performed, but no clear-cut changes in electrical activity of the brain was seen.
- **naive** (FKGL 6.9, 11 words, 0 edits): Photic stimulation was done, but no clear photic driving was seen.
    - SARI=21.78  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 3.4, 15 words, 2 edits): A light flash test was done, but no clear light-driven brain waves were seen.
    - SARI=31.00  crit=0.00  NLIf=0.74  copyjrg=0.00
- **grounded** (FKGL 1.9, 12 words, 2 edits): A light test was done, but no clear light response was seen.
    - SARI=32.04  crit=0.00  NLIf=0.92  copyjrg=0.00

### Note 69 - `739`

- **ORIGINAL**  (FKGL 15.6, 8 words): FAMILY HISTORY : Both parents died with myocardial infarctions.
- **REFERENCE** (FKGL 8.2, 8 words): Family history: Both parents died with heart attacks.
- **naive** (FKGL 8.2, 8 words, 0 edits): Family history: Both parents died from heart attacks.
    - SARI=61.01  crit=0.00  NLIf=0.92  copyjrg=0.00
- **termonly** (FKGL 8.2, 8 words, 1 edits): FAMILY HISTORY: Both parents died with heart attacks.
    - SARI=100.00  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 8.2, 8 words, 1 edits): Family history: Both parents died with heart attacks.
    - SARI=100.00  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 70 - `740`

- **ORIGINAL**  (FKGL 11.2, 11 words): Extremities : 2+ bilateral pitting edema to the level of the knees.
- **REFERENCE** (FKGL 10.1, 28 words): Hands and feet: There is swelling in both feet up to the level of the knees (when pressed, causes an indentation in the skin for a few seconds)
- **naive** (FKGL 7.4, 26 words, 0 edits): The patient's legs and arms show mild swelling that leaves small dents when pressed, and the swelling goes up to the knees on both sides.
    - SARI=36.16  crit=1.00  NLIf=0.02  copyjrg=0.00
- **termonly** (FKGL 5.3, 23 words, 0 edits): The arms and legs show a mild two-plus swelling that holds a dent and is on both sides up to the knees.
    - SARI=35.99  crit=0.00  NLIf=0.30  copyjrg=0.00
- **grounded** (FKGL 3.4, 14 words, 1 edits): Body parts: both sides show swelling that leaves a pit up to the knees.
    - SARI=35.23  crit=1.00  NLIf=0.98  copyjrg=0.00

### Note 71 - `741`

- **ORIGINAL**  (FKGL 14.3, 10 words): Following questions are mostly involved in a psychosocial donor evaluation.
- **REFERENCE** (FKGL 13.9, 15 words): Following questions are mostly involved in a donor evaluation of their psychological or social states.
- **naive** (FKGL 11.5, 10 words, 0 edits): The questions mostly look at the donor’s psychosocial evaluation.
    - SARI=13.31  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 14.7, 12 words, 1 edits): Following questions are mostly involved in a social and emotional donor evaluation.
    - SARI=68.52  crit=0.00  NLIf=0.78  copyjrg=0.00
- **grounded** (FKGL 12.3, 11 words, 1 edits): Following questions are mostly involved in a life effects donor evaluation.
    - SARI=66.67  crit=0.00  NLIf=0.03  copyjrg=0.00

### Note 72 - `742`

- **ORIGINAL**  (FKGL 24.1, 5 words): Mild nonmobile descending aortic atherosclerosis.
- **REFERENCE** (FKGL 11.1, 22 words): Mild non-moving hardening of the part of aorta (the largest artery of the body) that goes down the chest and abdomen.
- **naive** (FKGL 24.1, 5 words, 0 edits): Mild nonmobile descending aortic atherosclerosis.
    - SARI=2.78  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 6.5, 19 words, 0 edits): Mild plaque buildup in the lower part of the body's main artery, and the plaque does not move.
    - SARI=46.66  crit=0.00  NLIf=0.92  copyjrg=0.00
- **grounded** (FKGL 5.9, 18 words, 0 edits): Mild plaque buildup in the lower part of the main artery in the chest that does not move.
    - SARI=46.39  crit=0.00  NLIf=0.93  copyjrg=0.00

### Note 73 - `750`

- **ORIGINAL**  (FKGL 6.7, 8 words): The eustachian tube was obstructed with bone wax.
- **REFERENCE** (FKGL 3.1, 13 words): The passage between the nose and the ears was blocked with bone wax.
- **naive** (FKGL 3.8, 8 words, 0 edits): The eustachian tube was blocked with bone wax.
    - SARI=59.31  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL 8.0, 19 words, 3 edits): The tube that links the middle ear to the throat was blocked with a waxy material used in surgery.
    - SARI=33.64  crit=0.00  NLIf=0.27  copyjrg=0.00
- **grounded** (FKGL 10.0, 26 words, 2 edits): The tube that connects the middle ear to the back of the throat was blocked with a hard white body shape material made of animal fat.
    - SARI=33.09  crit=0.00  NLIf=0.15  copyjrg=0.00

### Note 74 - `752`

- **ORIGINAL**  (FKGL 6.3, 9 words): He was placed supine on the operating room table.
- **REFERENCE** (FKGL 7.2, 10 words): He was placed facing upwards on the operating room table.
- **naive** (FKGL 4.8, 11 words, 0 edits): He was placed on his back on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 5.8, 12 words, 1 edits): He was placed lying on his back on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 5.8, 12 words, 1 edits): He was placed lying on his back on the operating room table.
    - SARI=66.67  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 75 - `755`

- **ORIGINAL**  (FKGL 7.4, 7 words): A urinalysis was not performed this time.
- **REFERENCE** (FKGL 2.3, 8 words): A urine test was not performed this time.
- **naive** (FKGL 7.4, 7 words, 0 edits): A urinalysis was not performed this time.
    - SARI=26.16  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 1.3, 10 words, 1 edits): A test of the urine was not done this time.
    - SARI=33.73  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 1.6, 12 words, 1 edits): A test of the patient's pee was not done this time.
    - SARI=30.82  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 76 - `766`

- **ORIGINAL**  (FKGL 12.3, 21 words): Vision and hearing appeared to be adequate for testing, although she did indicate that she needed to update her eyeglass prescription.
- **REFERENCE** (FKGL 11.7, 21 words): Vision and hearing appeared to be okay for testing, although she did indicate that she needed to update her glasses prescription.
- **naive** (FKGL 9.8, 18 words, 0 edits): Vision and hearing seemed good enough for testing, but she said her eyeglass prescription needed to be updated.
    - SARI=18.20  crit=0.00  NLIf=0.99  copyjrg=0.67
- **termonly** (FKGL 9.1, 18 words, 3 edits): Vision and hearing seemed good enough for testing, although she said she needed to update her glasses order.
    - SARI=38.16  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 9.1, 17 words, 3 edits): Vision and hearing seemed enough for testing, although she said she needed to update her glasses order.
    - SARI=38.72  crit=0.00  NLIf=0.98  copyjrg=0.00

### Note 77 - `771`

- **ORIGINAL**  (FKGL 8.0, 24 words): I have talked to him several times about a colonoscopy, which he has refused, and so we have been doing stools for occult blood.
- **REFERENCE** (FKGL 17.5, 46 words): I have talked to him several times about a procedure to have a look inside the bowels (colonoscopy), which he has refused, and so we have been testing some stool samples in the lab to look for blood (which may be invisible to the naked eye).
- **naive** (FKGL 8.0, 24 words, 0 edits): I have talked to him several times about a colonoscopy, which he has refused, and so we have been doing stools for occult blood.
    - SARI=27.99  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 13.2, 36 words, 3 edits): I have talked to him several times about a look inside the large bowel with a thin tube, which he has refused, and so we have been doing tests of his bowel movements for hidden blood.
    - SARI=62.02  crit=0.00  NLIf=0.88  copyjrg=0.00
- **grounded** (FKGL 11.1, 30 words, 3 edits): I have talked to him several times about a test to look inside his large intestine, which he has refused, and so we have been checking poop for hidden blood.
    - SARI=62.50  crit=0.00  NLIf=0.97  copyjrg=0.00

### Note 78 - `783`

- **ORIGINAL**  (FKGL 8.4, 10 words): The knee was copiously irrigated and suction dried once again.
- **REFERENCE** (FKGL 7.6, 16 words): The knee was washed out thoroughly and dried with a suction (or mini-vacuum) once again
- **naive** (FKGL 4.4, 15 words, 0 edits): The knee was washed out with a lot of fluid and dried with suction again.
    - SARI=63.39  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 4.4, 15 words, 2 edits): The knee was washed with a lot of fluid and dried with suction once again.
    - SARI=66.80  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.4, 20 words, 2 edits): The knee was washed with a lot of fluid and dried with a machine that pulls in liquid once again.
    - SARI=62.88  crit=0.00  NLIf=0.77  copyjrg=0.00

### Note 79 - `784`

- **ORIGINAL**  (FKGL 10.9, 14 words): She is not having painful urination, any blood in the urine, frequency or hesitancy.
- **REFERENCE** (FKGL 11.1, 20 words): She is not having painful peeing, any blood in the pee, needing to pee very often or having difficulty peeing.
- **naive** (FKGL 10.9, 14 words, 0 edits): She is not having painful urination, any blood in the urine, frequency, or hesitancy.
    - SARI=21.25  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 9.9, 20 words, 2 edits): She is not having painful urination, any blood in the urine, needing to go often, or trouble starting to go.
    - SARI=63.78  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 9.3, 20 words, 2 edits): She is not having painful urination, any blood in the urine, how often she pees or trouble starting to pee.
    - SARI=62.63  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 80 - `789`

- **ORIGINAL**  (FKGL 14.8, 19 words): Cardiovascular : Chest pain in the retrosternal area, Occasional anginal pain and patient describes it as a sensation of tightness.
- **REFERENCE** (FKGL 14.6, 30 words): Heart and blood vessels: Chest pain just behind the breastbone, occasional chest pain when exercising or exerting themselves, which gets better with rest and patient describes it as feeling 'tightness'.
- **naive** (FKGL 4.2, 21 words, 0 edits): The patient has chest pain behind the breastbone. Sometimes the pain feels like angina, and the patient says it feels tight.
    - SARI=37.82  crit=0.00  NLIf=0.79  copyjrg=0.00
- **termonly** (FKGL 10.3, 23 words, 2 edits): Heart: Chest pain behind the breastbone, occasional chest pain from poor blood flow and the patient describes it as a sensation of tightness.
    - SARI=57.08  crit=0.00  NLIf=0.75  copyjrg=0.00
- **grounded** (FKGL 12.7, 33 words, 3 edits): The patient has heart and blood vessel symptoms: chest pain behind the breastbone, sometimes chest pain from poor blood flow to the heart and the patient describes it as a feeling of tightness.
    - SARI=58.14  crit=0.00  NLIf=0.90  copyjrg=0.00

### Note 81 - `790`

- **ORIGINAL**  (FKGL 4.8, 11 words): We excised a good bit of his synovium and synovial pouch.
- **REFERENCE** (FKGL 1.9, 12 words): We cut out a bit of the soft tissue of the joint.
- **naive** (FKGL 5.9, 11 words, 0 edits): We removed a large amount of his synovium and synovial pouch.
    - SARI=33.06  crit=0.00  NLIf=0.99  copyjrg=0.80
- **termonly** (FKGL 3.4, 14 words, 2 edits): We cut out a good bit of his joint lining and joint lining sac.
    - SARI=52.89  crit=0.00  NLIf=0.91  copyjrg=0.00
- **grounded** (FKGL 4.2, 14 words, 2 edits): We took out a good bit of his joint lining and joint lining pocket.
    - SARI=46.74  crit=0.00  NLIf=0.75  copyjrg=0.00

### Note 82 - `801`

- **ORIGINAL**  (FKGL 13.4, 11 words): An inflammatory process such as infection or ischemia must be considered.
- **REFERENCE** (FKGL 10.4, 13 words): An inflammatory process such as infection or reduced blood flow must be considered.
- **naive** (FKGL 13.4, 11 words, 0 edits): An inflammatory process such as infection or ischemia must be considered.
    - SARI=27.57  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 5.8, 13 words, 2 edits): A flare-up such as infection or poor blood flow must be considered.
    - SARI=48.03  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 6.7, 14 words, 2 edits): A flare-up such as infection or not enough blood flow must be considered.
    - SARI=47.08  crit=0.00  NLIf=0.90  copyjrg=0.00

### Note 83 - `804`

- **ORIGINAL**  (FKGL 2.9, 12 words): I have asked her to increase her prednisone when she goes home.
- **REFERENCE** (FKGL 2.9, 12 words): I have asked her to increase her steroid when she goes home.
- **naive** (FKGL 6.0, 15 words, 0 edits): The patient has been told to raise her prednisone dose after she leaves the hospital.
    - SARI=10.61  crit=0.00  NLIf=0.81  copyjrg=1.00
- **termonly** (FKGL 3.8, 12 words, 1 edits): I have asked her to increase her medicine when she goes home.
    - SARI=66.67  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 9.9, 21 words, 1 edits): I have asked her to increase her medicine that lowers the body's immune response and inflammation when she goes home.
    - SARI=66.67  crit=0.00  NLIf=0.23  copyjrg=0.00

### Note 84 - `844`

- **ORIGINAL**  (FKGL 10.2, 9 words): She may need other neuropathic pain medications as needed.
- **REFERENCE** (FKGL 6.3, 9 words): She may need other nerve pain medications as needed.
- **naive** (FKGL 4.8, 10 words, 0 edits): She may need other medicines for nerve pain when needed.
    - SARI=47.00  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 5.0, 9 words, 1 edits): She may need other nerve pain medicines as needed.
    - SARI=64.54  crit=0.00  NLIf=0.95  copyjrg=0.00
- **grounded** (FKGL 4.8, 10 words, 1 edits): She may need other medicines for nerve pain as needed.
    - SARI=52.10  crit=0.00  NLIf=0.96  copyjrg=0.00

### Note 85 - `852`

- **ORIGINAL**  (FKGL 12.4, 7 words): A prophylactic dose of antibiotics was given.
- **REFERENCE** (FKGL 10.7, 7 words): A prevention dose of antibiotics was given.
- **naive** (FKGL 10.7, 7 words, 0 edits): A preventive dose of antibiotics was given.
    - SARI=66.67  crit=0.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 7.2, 10 words, 1 edits): A dose of medicine to help prevent infection was given.
    - SARI=28.96  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 8.8, 12 words, 1 edits): A dose of medicine that kills bacteria to prevent sickness was given.
    - SARI=28.96  crit=0.00  NLIf=0.88  copyjrg=0.00

### Note 86 - `854`

- **ORIGINAL**  (FKGL 16.2, 6 words): Chronic hypokalemia secondary to chronic diarrhea.
- **REFERENCE** (FKGL 7.6, 9 words): Long term low potassium due to long term diarrhea.
- **naive** (FKGL 11.9, 12 words, 0 edits): The patient has long-term low potassium because of long-term diarrhea.
    - SARI=49.96  crit=0.00  NLIf=0.98  copyjrg=0.00
- **termonly** (FKGL 7.2, 12 words, 2 edits): The patient has long-term low potassium from long-term loose stools.
    - SARI=41.01  crit=0.00  NLIf=0.96  copyjrg=0.00
- **grounded** (FKGL 11.5, 17 words, 2 edits): The patient has a long-lasting low blood potassium level because of long-lasting loose, watery poop.
    - SARI=33.06  crit=0.00  NLIf=0.94  copyjrg=0.00

### Note 87 - `859`

- **ORIGINAL**  (FKGL 6.6, 4 words): No hepatosplenomegaly or tenderness.
- **REFERENCE** (FKGL 2.3, 9 words): No enlarged liver or spleen or pain when pushed.
- **naive** (FKGL 6.6, 4 words, 0 edits): No hepatosplenomegaly or tenderness.
    - SARI=5.56  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 2.3, 9 words, 2 edits): No enlarged liver or spleen or pain when touched.
    - SARI=69.99  crit=0.00  NLIf=0.48  copyjrg=0.00
- **grounded** (FKGL 2.3, 9 words, 2 edits): No enlarged liver or spleen or pain on touch.
    - SARI=64.98  crit=0.00  NLIf=0.62  copyjrg=0.00

### Note 88 - `881`

- **ORIGINAL**  (FKGL 9.1, 11 words): He did not experience his left anterior chest pain with exercise.
- **REFERENCE** (FKGL 5.9, 11 words): He did not experience his left front chest pain with exercise.
- **naive** (FKGL 2.5, 10 words, 0 edits): He did not get left front chest pain with exercise.
    - SARI=56.36  crit=1.00  NLIf=0.97  copyjrg=0.00
- **termonly** (FKGL 2.6, 11 words, 2 edits): He did not have his left front chest pain with exercise.
    - SARI=62.40  crit=1.00  NLIf=0.97  copyjrg=0.00
- **grounded** (FKGL 2.6, 11 words, 2 edits): He did not feel his left front chest pain with exercise.
    - SARI=62.40  crit=1.00  NLIf=0.97  copyjrg=0.00

### Note 89 - `891`

- **ORIGINAL**  (FKGL 7.6, 9 words): Also, would use it to control the atrial fibrillation.
- **REFERENCE** (FKGL 6.0, 10 words): Also, would use it to control the irregular heart beat
- **naive** (FKGL 7.2, 10 words, 0 edits): Also, it would be used to control the atrial fibrillation.
    - SARI=12.08  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 6.8, 12 words, 1 edits): Also, would use it to control the fast and irregular heart rhythm.
    - SARI=72.92  crit=0.00  NLIf=0.80  copyjrg=0.00
- **grounded** (FKGL 4.8, 10 words, 1 edits): Also, would use it to control the heart rhythm problem.
    - SARI=69.44  crit=0.00  NLIf=0.88  copyjrg=0.00

### Note 90 - `900`

- **ORIGINAL**  (FKGL 11.1, 8 words): Overall the patient is a seemingly good historian.
- **REFERENCE** (FKGL 11.9, 10 words): Overall the patient is seemingly good at remembering their history
- **naive** (FKGL 7.2, 10 words, 0 edits): The patient seems to give a clear and reliable history.
    - SARI=26.61  crit=0.00  NLIf=0.67  copyjrg=0.00
- **termonly** (FKGL 7.6, 13 words, 1 edits): Overall the patient is a person who appears to give clear health history.
    - SARI=50.92  crit=0.00  NLIf=0.21  copyjrg=0.00
- **grounded** (FKGL 11.5, 9 words, 2 edits): Overall the patient appears to be a reliable reporter.
    - SARI=36.53  crit=0.00  NLIf=0.06  copyjrg=0.00

### Note 91 - `933`

- **ORIGINAL**  (FKGL 3.7, 10 words): No active Crohn 's disease was found during the colonoscopy.
- **REFERENCE** (FKGL 5.9, 14 words): No active Crohn 's disease was found during the camera test through the gut.
- **naive** (FKGL 3.7, 10 words, 0 edits): No active Crohn's disease was found during the colonoscopy.
    - SARI=31.21  crit=0.00  NLIf=0.99  copyjrg=1.00
- **termonly** (FKGL 5.8, 15 words, 2 edits): No flare-up of Crohn’s disease was found during the look inside the colon.
    - SARI=41.10  crit=0.00  NLIf=0.98  copyjrg=0.00
- **grounded** (FKGL 8.7, 22 words, 2 edits): No signs of a current Crohn’s flare-up were seen during the exam of the large intestine by a flexible tube.
    - SARI=14.38  crit=0.00  NLIf=0.80  copyjrg=0.00

### Note 92 - `935`

- **ORIGINAL**  (FKGL 16.4, 28 words): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have mounting exhaustion and respiratory distress.
- **REFERENCE** (FKGL 15.5, 28 words): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have worsening exhaustion and breathing distress.
- **naive** (FKGL 11.1, 27 words, 0 edits): Shortly after the first check, the patient seemed to start complaining of chest pain and looked to the nurse like exhaustion and trouble breathing were getting worse.
    - SARI=23.01  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 15.0, 28 words, 2 edits): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have growing tiredness and trouble breathing.
    - SARI=63.09  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 16.4, 29 words, 2 edits): Shortly after the patient's initial assessment, the patient apparently began to complain of chest pain and appeared to the nurse to have growing tiredness and having difficulty breathing.
    - SARI=62.70  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 93 - `968`

- **ORIGINAL**  (FKGL 8.2, 8 words): She has been referred for a pacemaker implantation.
- **REFERENCE** (FKGL 7.6, 9 words): She has been referred for a pacemaker fitting surgery.
- **naive** (FKGL 4.0, 13 words, 0 edits): She has been sent to a doctor to get a pacemaker put in.
    - SARI=23.47  crit=0.00  NLIf=0.96  copyjrg=0.00
- **termonly** (FKGL 3.5, 17 words, 2 edits): She has been sent for a small device to be put in to help the heart beat.
    - SARI=23.47  crit=0.00  NLIf=0.89  copyjrg=0.00
- **grounded** (FKGL 5.8, 20 words, 2 edits): She has been sent for care to have a small device placed in her chest to help control her heartbeat.
    - SARI=21.67  crit=0.00  NLIf=0.92  copyjrg=0.00

### Note 94 - `116`

- **ORIGINAL**  (FKGL -0.7, 8 words): There was some hematoma at the cath site.
- **REFERENCE** (FKGL 5.8, 13 words): There was some swelling due to collection of blood at the catheter site.
- **naive** (FKGL 6.3, 17 words, 0 edits): There was some bruising and a collection of blood at the site where the catheter was placed.
    - SARI=69.00  crit=0.00  NLIf=0.45  copyjrg=0.00
- **termonly** (FKGL 5.2, 18 words, 2 edits): There was some bruising with a collection of blood at the place where the tube was put in.
    - SARI=63.08  crit=0.00  NLIf=0.57  copyjrg=0.00
- **grounded** (FKGL 0.9, 12 words, 2 edits): There was some bruise at the place where the tube went in.
    - SARI=54.80  crit=0.00  NLIf=0.40  copyjrg=0.00

### Note 95 - `592`

- **ORIGINAL**  (FKGL 6.3, 9 words): The necrotic tissue was lifted out of the abdomen.
- **REFERENCE** (FKGL 3.7, 9 words): The dead flesh was lifted out of the abdomen.
- **naive** (FKGL 3.7, 9 words, 0 edits): The dead tissue was lifted out of the belly.
    - SARI=53.39  crit=0.00  NLIf=0.99  copyjrg=0.33
- **termonly** (FKGL 5.0, 9 words, 1 edits): The dead tissue was lifted out of the abdomen.
    - SARI=72.13  crit=0.00  NLIf=0.99  copyjrg=0.33
- **grounded** (FKGL 5.0, 9 words, 1 edits): The dead tissue was lifted out of the abdomen.
    - SARI=72.13  crit=0.00  NLIf=0.99  copyjrg=0.33

### Note 96 - `249`

- **ORIGINAL**  (FKGL 6.7, 8 words): Pressure was held and the area was hemostatic.
- **REFERENCE** (FKGL 5.2, 8 words): Pressure was held and the area stopped bleeding.
- **naive** (FKGL 4.8, 10 words, 0 edits): Pressure was kept on the area and it stopped bleeding.
    - SARI=32.56  crit=0.00  NLIf=0.28  copyjrg=0.00
- **termonly** (FKGL 6.0, 10 words, 1 edits): Pressure was held and the area was no longer bleeding.
    - SARI=67.13  crit=0.00  NLIf=0.48  copyjrg=0.00
- **grounded** (FKGL 6.3, 9 words, 1 edits): Pressure was held and the area was stopping bleeding.
    - SARI=67.96  crit=0.00  NLIf=0.49  copyjrg=0.00

### Note 97 - `701`

- **ORIGINAL**  (FKGL 3.7, 9 words): The area was lavaged with some saline and cleared.
- **REFERENCE** (FKGL 3.7, 11 words): The area was washed out with some salt water and cleared.
- **naive** (FKGL 3.7, 9 words, 0 edits): The area was washed with some saline and cleared.
    - SARI=59.43  crit=0.00  NLIf=0.99  copyjrg=0.50
- **termonly** (FKGL 3.7, 10 words, 2 edits): The area was washed with some salt water and cleared.
    - SARI=81.54  crit=0.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 3.7, 10 words, 2 edits): The area was cleaned with some salt water and cleared.
    - SARI=75.42  crit=0.00  NLIf=0.99  copyjrg=0.00

### Note 98 - `826`

- **ORIGINAL**  (FKGL 8.2, 8 words): Pain and inability to ambulate brought him in.
- **REFERENCE** (FKGL 6.3, 9 words): Pain and inability to move around brought him in.
- **naive** (FKGL 5.2, 8 words, 0 edits): Pain and inability to walk brought him in.
    - SARI=66.67  crit=0.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 2.5, 10 words, 1 edits): Pain and not being able to walk brought him in.
    - SARI=38.11  crit=0.00  NLIf=0.99  copyjrg=0.00
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
- **naive** (FKGL 4.0, 7 words, 0 edits): Other systems were checked and were normal.
    - SARI=23.57  crit=1.00  NLIf=0.99  copyjrg=0.00
- **termonly** (FKGL 4.8, 10 words, 1 edits): Other systems were reviewed and were found to be normal.
    - SARI=100.00  crit=1.00  NLIf=0.99  copyjrg=0.00
- **grounded** (FKGL 7.8, 12 words, 1 edits): Other systems were reviewed and were found to be common and ordinary.
    - SARI=66.67  crit=1.00  NLIf=0.82  copyjrg=0.00
