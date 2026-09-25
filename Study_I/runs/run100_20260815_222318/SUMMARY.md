# Cross-model summary - `run100`

Models: together-ternary-bonsai-27b, qwen3p7-plus, together-deepseek-pro, together-muse-glimmer, together-nemotron-ultra, together-qwen3.5-9b

PAPER-tier metrics only. See each model's `report.md` for the appendix tier and the caveats.

## FKGL drop vs input   (higher is better, target > +4 grades)

*how many US grade levels easier than the original clinical text*

| model | naive | termonly | grounded |
|---|---:|---:|---:|
| together-ternary-bonsai-27b | 2.88 | 3.58 | 3.15 |
| qwen3p7-plus | 3.77 | 4.03 | 3.73 |
| together-deepseek-pro | 3.73 | 3.69 | 3.33 |
| together-muse-glimmer | 2.96 | 3.59 | 2.94 |
| together-nemotron-ultra | 3.36 | 3.91 | 3.39 |
| together-qwen3.5-9b | 3.30 | 4.47 | 4.33 |

## Coleman-Liau drop   (higher is better, target > +4)

*same as FKGL drop but CHARACTER-based, so it is immune to syllable-counter error on medical morphology*

| model | naive | termonly | grounded |
|---|---:|---:|---:|
| together-ternary-bonsai-27b | 4.30 | 4.46 | 3.91 |
| qwen3p7-plus | 4.56 | 4.56 | 4.41 |
| together-deepseek-pro | 4.88 | 4.93 | 5.16 |
| together-muse-glimmer | 3.56 | 5.16 | 4.93 |
| together-nemotron-ultra | 4.51 | 4.97 | 4.86 |
| together-qwen3.5-9b | 4.38 | 5.05 | 4.92 |

## length ratio vs reference   (descriptive, target 0.9-1.3)

*output words / reference words - catches padding and truncation*

| model | naive | termonly | grounded |
|---|---:|---:|---:|
| together-ternary-bonsai-27b | 1.20 | 0.97 | 1.03 |
| qwen3p7-plus | 1.06 | 0.95 | 0.96 |
| together-deepseek-pro | 1.13 | 1.09 | 1.13 |
| together-muse-glimmer | 0.97 | 1.10 | 1.20 |
| together-nemotron-ultra | 1.99 | 1.05 | 1.14 |
| together-qwen3.5-9b | 1.05 | 0.94 | 0.98 |

## NLI faithfulness   (higher is better, target > 0.70)

*input entails output - catches HALLUCINATION (added content)*

| model | naive | termonly | grounded |
|---|---:|---:|---:|
| together-ternary-bonsai-27b | 0.796 | 0.816 | 0.813 |
| qwen3p7-plus | 0.833 | 0.826 | 0.839 |
| together-deepseek-pro | 0.792 | 0.794 | 0.768 |
| together-muse-glimmer | 0.901 | 0.793 | 0.737 |
| together-nemotron-ultra | 0.864 | 0.815 | 0.762 |
| together-qwen3.5-9b | 0.844 | 0.804 | 0.789 |

## NLI completeness   (higher is better, target > 0.60)

*output entails input - catches OMISSION (dropped content)*

| model | naive | termonly | grounded |
|---|---:|---:|---:|
| together-ternary-bonsai-27b | 0.903 | 0.748 | 0.755 |
| qwen3p7-plus | 0.820 | 0.790 | 0.807 |
| together-deepseek-pro | 0.842 | 0.782 | 0.769 |
| together-muse-glimmer | 0.861 | 0.763 | 0.736 |
| together-nemotron-ultra | 0.873 | 0.783 | 0.739 |
| together-qwen3.5-9b | 0.895 | 0.760 | 0.738 |

## critical-error rate   (LOWER is better, target 0.00 - any value > 0 needs review)

*fraction of outputs that lost a high-risk slot: negation, uncertainty, laterality, a number/unit, or a drug name*

| model | naive | termonly | grounded |
|---|---:|---:|---:|
| together-ternary-bonsai-27b | 0.100 | 0.090 | 0.070 |
| qwen3p7-plus | 0.130 | 0.100 | 0.100 |
| together-deepseek-pro | 0.100 | 0.120 | 0.090 |
| together-muse-glimmer | 0.100 | 0.060 | 0.090 |
| together-nemotron-ultra | 0.120 | 0.110 | 0.100 |
| together-qwen3.5-9b | 0.100 | 0.120 | 0.110 |

## generation success rate   (higher is better, target 1.00)

*fraction of notes where this arm produced any output at all*

| model | naive | termonly | grounded |
|---|---:|---:|---:|
| together-ternary-bonsai-27b | 1.000 | 1.000 | 1.000 |
| qwen3p7-plus | 1.000 | 1.000 | 1.000 |
| together-deepseek-pro | 1.000 | 1.000 | 1.000 |
| together-muse-glimmer | 1.000 | 1.000 | 1.000 |
| together-nemotron-ultra | 1.000 | 1.000 | 1.000 |
| together-qwen3.5-9b | 1.000 | 1.000 | 1.000 |

## usable-output rate   (higher is better, target 1.00)

*of the outputs that exist, the fraction that are a rewrite rather than protocol text the model emitted about the task*

| model | naive | termonly | grounded |
|---|---:|---:|---:|
| together-ternary-bonsai-27b | 1.000 | 1.000 | 1.000 |
| qwen3p7-plus | 1.000 | 1.000 | 1.000 |
| together-deepseek-pro | 1.000 | 1.000 | 1.000 |
| together-muse-glimmer | 1.000 | 1.000 | 1.000 |
| together-nemotron-ultra | 1.000 | 1.000 | 1.000 |
| together-qwen3.5-9b | 1.000 | 1.000 | 1.000 |

## human edit recall   (higher is better, target > 0.85)

*of the jargon the human replaced, how much did we replace*

| model | naive | termonly | grounded |
|---|---:|---:|---:|
| together-ternary-bonsai-27b | 0.787 | 0.987 | 0.975 |
| qwen3p7-plus | 0.718 | 0.976 | 0.981 |
| together-deepseek-pro | 0.784 | 0.995 | 0.997 |
| together-muse-glimmer | 0.568 | 0.995 | 0.995 |
| together-nemotron-ultra | 0.668 | 0.983 | 0.971 |
| together-qwen3.5-9b | 0.706 | 0.955 | 0.987 |

## Attribution

| model | edits | ranked | flat | failed | helped | neutral | hurt | attributable | LDS held | LDS in | gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| together-ternary-bonsai-27b | 199 | 198 | 1 | 0 | 96 | 75 | 28 | 0.6771 | 0.7973 | 0.8772 | 0.0799 |
| qwen3p7-plus | 177 | 177 | 0 | 0 | 56 | 121 | 0 | 0.6071 | 0.6926 | 0.8415 | 0.1489 |
| together-deepseek-pro | 178 | 168 | 0 | 10 | 75 | 88 | 5 | 0.6533 | 0.669 | 0.8191 | 0.1501 |
| together-muse-glimmer | 199 | 199 | 0 | 0 | 109 | 83 | 7 | 0.6972 | 0.7714 | 0.8584 | 0.087 |
| together-nemotron-ultra | 167 | 167 | 0 | 0 | 63 | 101 | 3 | 0.6825 | 0.7262 | 0.8329 | 0.1067 |
| together-qwen3.5-9b | 173 | 173 | 0 | 0 | 76 | 95 | 2 | 0.6447 | 0.7716 | 0.8736 | 0.102 |
