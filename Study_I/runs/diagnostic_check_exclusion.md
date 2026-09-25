# Diagnostic-Check Exclusion Reanalysis

This is a disclosed post-hoc change to the reported high-risk rate, not a new experiment.
No independent clinical validation of the fixed diagnostic acceptance list was documented. Removing its flags does not establish that the affected outputs are clinically correct, or validate the remaining checks.

The original saved run is unchanged. All original focused estimates, bootstrap intervals and p-values were reproduced before the revised calculation.

## Rates

| Model | Arm | Sentences | Original flagged | Revised flagged | Original rate | Revised rate |
|---|---|---:|---:|---:|---:|---:|
| qwen3p7-plus | naive | 100 | 13 | 13 | 0.130 | 0.130 |
| qwen3p7-plus | termonly | 100 | 10 | 10 | 0.100 | 0.100 |
| qwen3p7-plus | grounded | 100 | 10 | 10 | 0.100 | 0.100 |
| together-deepseek-pro | naive | 100 | 10 | 10 | 0.100 | 0.100 |
| together-deepseek-pro | termonly | 100 | 12 | 11 | 0.120 | 0.110 |
| together-deepseek-pro | grounded | 100 | 9 | 9 | 0.090 | 0.090 |
| together-muse-glimmer | naive | 100 | 10 | 10 | 0.100 | 0.100 |
| together-muse-glimmer | termonly | 100 | 6 | 6 | 0.060 | 0.060 |
| together-muse-glimmer | grounded | 100 | 9 | 9 | 0.090 | 0.090 |
| together-nemotron-ultra | naive | 100 | 12 | 12 | 0.120 | 0.120 |
| together-nemotron-ultra | termonly | 100 | 11 | 11 | 0.110 | 0.110 |
| together-nemotron-ultra | grounded | 100 | 10 | 10 | 0.100 | 0.100 |
| together-qwen3.5-9b | naive | 100 | 10 | 10 | 0.100 | 0.100 |
| together-qwen3.5-9b | termonly | 100 | 12 | 12 | 0.120 | 0.120 |
| together-qwen3.5-9b | grounded | 100 | 11 | 10 | 0.110 | 0.100 |
| together-ternary-bonsai-27b | naive | 100 | 10 | 10 | 0.100 | 0.100 |
| together-ternary-bonsai-27b | termonly | 100 | 9 | 9 | 0.090 | 0.090 |
| together-ternary-bonsai-27b | grounded | 100 | 7 | 7 | 0.070 | 0.070 |

## Statistical Impact

- termonly_vs_naive: 18 of 36 significant before, 18 of 36 after.
- grounded_vs_termonly: 0 of 34 significant before, 0 of 34 after.
- Significance decisions changed: 0.
- Family-wide correction is recomputed, so adjusted p-values can change even for an unchanged metric.
- The JSON report records every original and revised focused comparison, including untested all-tie pairs.

## Changed Output Flags

### together-deepseek-pro, termonly, Note 82

Original: An inflammatory process such as infection or ischemia must be considered.

Saved output: A problem like an infection or blocked blood flow must be considered.

Composite flag: 1 to 0. No other active critical flag was present.

### together-qwen3.5-9b, grounded, Note 8

Original: Description : Fever, otitis media, and possible sepsis.

Saved output: Fever, ear infection, and possible severe bloodstream infection.

Composite flag: 1 to 0. No other active critical flag was present.

## Reproduction

Run the following from `Study_I`. The output prefix is outside the saved run.

```bash
python analysis/exclude_diagnostic_check.py runs/run100_20260815_222318 --output-prefix runs/diagnostic_check_exclusion
```

Without --output-prefix the script only prints this report. It makes no API calls.
