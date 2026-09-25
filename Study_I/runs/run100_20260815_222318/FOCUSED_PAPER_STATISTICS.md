# Focused paper-tier statistical analysis

This post hoc analysis includes only the six paper-tier metrics that
are directional, measured per sentence, and available in both arms.
It uses two-sided paired Wilcoxon tests and one Benjamini-Hochberg
correction across all valid model-metric tests within each contrast.
No generation or metric value was changed.

Metrics: `human_edit_recall`, `fkgl_drop`, `coleman_liau_drop`, `nli_faithfulness`, `nli_completeness`, `critical_error`.

## termonly versus naive

18 of 36 valid tests survive contrast-wide FDR correction.

| Model | Metric | n | Mean A | Mean B | A - B | 95% CI | Adjusted p | Result |
|---|---|---:|---:|---:|---:|---|---:|---|
| `qwen3p7-plus` | `human_edit_recall` | 99 | 0.976 | 0.718 | +0.259 | [+0.177, +0.344] | <0.0001 | improvement |
| `qwen3p7-plus` | `fkgl_drop` | 100 | 4.026 | 3.769 | +0.258 | [-0.382, +0.891] | 0.2869 | not significant |
| `qwen3p7-plus` | `coleman_liau_drop` | 100 | 4.563 | 4.556 | +0.008 | [-0.625, +0.623] | 0.9739 | not significant |
| `qwen3p7-plus` | `nli_faithfulness` | 100 | 0.826 | 0.833 | -0.007 | [-0.063, +0.050] | 0.0689 | not significant |
| `qwen3p7-plus` | `nli_completeness` | 100 | 0.790 | 0.820 | -0.030 | [-0.102, +0.041] | 0.1086 | not significant |
| `qwen3p7-plus` | `critical_error` | 100 | 0.100 | 0.130 | -0.030 | [-0.070, +0.000] | 0.7198 | not significant |
| `together-deepseek-pro` | `human_edit_recall` | 99 | 0.995 | 0.785 | +0.210 | [+0.141, +0.285] | <0.0001 | improvement |
| `together-deepseek-pro` | `fkgl_drop` | 100 | 3.694 | 3.732 | -0.038 | [-0.611, +0.531] | 0.7548 | not significant |
| `together-deepseek-pro` | `coleman_liau_drop` | 100 | 4.932 | 4.884 | +0.048 | [-0.535, +0.627] | 0.7198 | not significant |
| `together-deepseek-pro` | `nli_faithfulness` | 100 | 0.794 | 0.792 | +0.002 | [-0.051, +0.057] | 0.4650 | not significant |
| `together-deepseek-pro` | `nli_completeness` | 100 | 0.782 | 0.842 | -0.060 | [-0.124, +0.004] | 0.0554 | not significant |
| `together-deepseek-pro` | `critical_error` | 100 | 0.120 | 0.100 | +0.020 | [-0.020, +0.060] | 0.7895 | not significant |
| `together-muse-glimmer` | `human_edit_recall` | 99 | 0.995 | 0.568 | +0.427 | [+0.337, +0.520] | <0.0001 | improvement |
| `together-muse-glimmer` | `fkgl_drop` | 100 | 3.593 | 2.963 | +0.630 | [-0.193, +1.485] | 0.4650 | not significant |
| `together-muse-glimmer` | `coleman_liau_drop` | 100 | 5.161 | 3.559 | +1.602 | [+0.715, +2.569] | 0.0017 | improvement |
| `together-muse-glimmer` | `nli_faithfulness` | 100 | 0.793 | 0.901 | -0.108 | [-0.167, -0.051] | <0.0001 | deterioration |
| `together-muse-glimmer` | `nli_completeness` | 100 | 0.763 | 0.861 | -0.098 | [-0.168, -0.028] | 0.0001 | deterioration |
| `together-muse-glimmer` | `critical_error` | 100 | 0.060 | 0.100 | -0.040 | [-0.090, +0.000] | 0.6029 | not significant |
| `together-nemotron-ultra` | `human_edit_recall` | 99 | 0.983 | 0.668 | +0.315 | [+0.233, +0.401] | <0.0001 | improvement |
| `together-nemotron-ultra` | `fkgl_drop` | 100 | 3.908 | 3.365 | +0.544 | [-0.078, +1.148] | 0.0275 | improvement |
| `together-nemotron-ultra` | `coleman_liau_drop` | 100 | 4.975 | 4.513 | +0.462 | [-0.737, +1.433] | 0.0252 | improvement |
| `together-nemotron-ultra` | `nli_faithfulness` | 100 | 0.815 | 0.864 | -0.049 | [-0.113, +0.016] | 0.0103 | deterioration |
| `together-nemotron-ultra` | `nli_completeness` | 100 | 0.783 | 0.873 | -0.090 | [-0.156, -0.025] | 0.0006 | deterioration |
| `together-nemotron-ultra` | `critical_error` | 100 | 0.110 | 0.120 | -0.010 | [-0.050, +0.030] | 0.8812 | not significant |
| `together-qwen3.5-9b` | `human_edit_recall` | 99 | 0.955 | 0.706 | +0.250 | [+0.169, +0.335] | <0.0001 | improvement |
| `together-qwen3.5-9b` | `fkgl_drop` | 100 | 4.470 | 3.301 | +1.169 | [+0.645, +1.714] | <0.0001 | improvement |
| `together-qwen3.5-9b` | `coleman_liau_drop` | 100 | 5.049 | 4.380 | +0.669 | [+0.030, +1.312] | 0.0204 | improvement |
| `together-qwen3.5-9b` | `nli_faithfulness` | 100 | 0.804 | 0.844 | -0.040 | [-0.104, +0.026] | 0.0830 | not significant |
| `together-qwen3.5-9b` | `nli_completeness` | 100 | 0.760 | 0.895 | -0.135 | [-0.193, -0.081] | <0.0001 | deterioration |
| `together-qwen3.5-9b` | `critical_error` | 100 | 0.120 | 0.100 | +0.020 | [-0.020, +0.060] | 0.7895 | not significant |
| `together-ternary-bonsai-27b` | `human_edit_recall` | 99 | 0.987 | 0.787 | +0.199 | [+0.123, +0.280] | 0.0003 | improvement |
| `together-ternary-bonsai-27b` | `fkgl_drop` | 100 | 3.583 | 2.885 | +0.697 | [+0.247, +1.154] | 0.0093 | improvement |
| `together-ternary-bonsai-27b` | `coleman_liau_drop` | 100 | 4.455 | 4.297 | +0.158 | [-0.463, +0.745] | 0.5830 | not significant |
| `together-ternary-bonsai-27b` | `nli_faithfulness` | 100 | 0.816 | 0.796 | +0.020 | [-0.035, +0.077] | 0.8812 | not significant |
| `together-ternary-bonsai-27b` | `nli_completeness` | 100 | 0.747 | 0.903 | -0.155 | [-0.216, -0.097] | <0.0001 | deterioration |
| `together-ternary-bonsai-27b` | `critical_error` | 100 | 0.090 | 0.100 | -0.010 | [-0.050, +0.030] | 0.8812 | not significant |

## grounded versus termonly

0 of 34 valid tests survive contrast-wide FDR correction.

| Model | Metric | n | Mean A | Mean B | A - B | 95% CI | Adjusted p | Result |
|---|---|---:|---:|---:|---:|---|---:|---|
| `qwen3p7-plus` | `human_edit_recall` | 99 | 0.981 | 0.976 | +0.005 | [+0.000, +0.012] | 0.8163 | not significant |
| `qwen3p7-plus` | `fkgl_drop` | 100 | 3.730 | 4.026 | -0.296 | [-0.576, -0.048] | 0.2819 | not significant |
| `qwen3p7-plus` | `coleman_liau_drop` | 100 | 4.407 | 4.563 | -0.156 | [-0.470, +0.124] | 0.8163 | not significant |
| `qwen3p7-plus` | `nli_faithfulness` | 100 | 0.839 | 0.826 | +0.013 | [-0.012, +0.039] | 0.8163 | not significant |
| `qwen3p7-plus` | `nli_completeness` | 100 | 0.807 | 0.790 | +0.017 | [-0.004, +0.041] | 0.8163 | not significant |
| `together-deepseek-pro` | `human_edit_recall` | 99 | 0.997 | 0.995 | +0.002 | [+0.000, +0.005] | 0.8480 | not significant |
| `together-deepseek-pro` | `fkgl_drop` | 100 | 3.331 | 3.694 | -0.363 | [-0.667, -0.085] | 0.1803 | not significant |
| `together-deepseek-pro` | `coleman_liau_drop` | 100 | 5.156 | 4.932 | +0.224 | [-0.158, +0.598] | 0.8163 | not significant |
| `together-deepseek-pro` | `nli_faithfulness` | 100 | 0.768 | 0.794 | -0.025 | [-0.066, +0.014] | 0.8163 | not significant |
| `together-deepseek-pro` | `nli_completeness` | 100 | 0.769 | 0.782 | -0.013 | [-0.045, +0.019] | 0.8163 | not significant |
| `together-deepseek-pro` | `critical_error` | 100 | 0.090 | 0.120 | -0.030 | [-0.070, +0.000] | 0.8163 | not significant |
| `together-muse-glimmer` | `fkgl_drop` | 100 | 2.944 | 3.593 | -0.648 | [-1.189, -0.132] | 0.2407 | not significant |
| `together-muse-glimmer` | `coleman_liau_drop` | 100 | 4.929 | 5.161 | -0.232 | [-0.598, +0.139] | 0.3287 | not significant |
| `together-muse-glimmer` | `nli_faithfulness` | 100 | 0.737 | 0.793 | -0.056 | [-0.114, +0.002] | 0.3811 | not significant |
| `together-muse-glimmer` | `nli_completeness` | 100 | 0.736 | 0.763 | -0.028 | [-0.063, +0.006] | 0.2819 | not significant |
| `together-muse-glimmer` | `critical_error` | 100 | 0.090 | 0.060 | +0.030 | [+0.000, +0.070] | 0.8163 | not significant |
| `together-nemotron-ultra` | `human_edit_recall` | 99 | 0.971 | 0.983 | -0.012 | [-0.037, +0.003] | 0.8480 | not significant |
| `together-nemotron-ultra` | `fkgl_drop` | 100 | 3.392 | 3.908 | -0.516 | [-0.944, -0.105] | 0.2819 | not significant |
| `together-nemotron-ultra` | `coleman_liau_drop` | 100 | 4.860 | 4.975 | -0.115 | [-0.534, +0.277] | 0.8480 | not significant |
| `together-nemotron-ultra` | `nli_faithfulness` | 100 | 0.762 | 0.815 | -0.053 | [-0.096, -0.012] | 0.2236 | not significant |
| `together-nemotron-ultra` | `nli_completeness` | 100 | 0.739 | 0.783 | -0.044 | [-0.075, -0.017] | 0.3811 | not significant |
| `together-nemotron-ultra` | `critical_error` | 100 | 0.100 | 0.110 | -0.010 | [-0.030, +0.000] | 0.8480 | not significant |
| `together-qwen3.5-9b` | `human_edit_recall` | 99 | 0.987 | 0.955 | +0.031 | [+0.001, +0.071] | 0.8163 | not significant |
| `together-qwen3.5-9b` | `fkgl_drop` | 100 | 4.328 | 4.470 | -0.142 | [-0.516, +0.278] | 0.3756 | not significant |
| `together-qwen3.5-9b` | `coleman_liau_drop` | 100 | 4.915 | 5.049 | -0.134 | [-0.576, +0.471] | 0.2942 | not significant |
| `together-qwen3.5-9b` | `nli_faithfulness` | 100 | 0.789 | 0.804 | -0.015 | [-0.060, +0.031] | 0.1891 | not significant |
| `together-qwen3.5-9b` | `nli_completeness` | 100 | 0.738 | 0.760 | -0.022 | [-0.068, +0.026] | 0.4174 | not significant |
| `together-qwen3.5-9b` | `critical_error` | 100 | 0.110 | 0.120 | -0.010 | [-0.050, +0.020] | 0.8480 | not significant |
| `together-ternary-bonsai-27b` | `human_edit_recall` | 99 | 0.975 | 0.987 | -0.012 | [-0.034, +0.000] | 0.8163 | not significant |
| `together-ternary-bonsai-27b` | `fkgl_drop` | 100 | 3.145 | 3.583 | -0.437 | [-0.840, -0.018] | 0.1352 | not significant |
| `together-ternary-bonsai-27b` | `coleman_liau_drop` | 100 | 3.912 | 4.455 | -0.543 | [-1.098, +0.060] | 0.0878 | not significant |
| `together-ternary-bonsai-27b` | `nli_faithfulness` | 100 | 0.813 | 0.816 | -0.004 | [-0.048, +0.040] | 0.8163 | not significant |
| `together-ternary-bonsai-27b` | `nli_completeness` | 100 | 0.755 | 0.747 | +0.008 | [-0.028, +0.044] | 0.8163 | not significant |
| `together-ternary-bonsai-27b` | `critical_error` | 100 | 0.070 | 0.090 | -0.020 | [-0.050, +0.000] | 0.8163 | not significant |
