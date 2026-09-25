"""Configuration: model registry, run settings, presets and API-key lookup."""

from __future__ import annotations

import os
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional

HERE = Path(__file__).resolve().parent


@dataclass(frozen=True)
class ModelSpec:
    slug: str
    model_id: str
    provider: str
    backend: str = "fireworks"
    contextcite: bool = True
    num_workers: int = 6
    reasoning_effort: str = "none"
    max_new_tokens: Optional[int] = None
    note: str = ""


MODEL_REGISTRY: Dict[str, ModelSpec] = {
    "together-qwen3.5-9b": ModelSpec(
        slug="together-qwen3.5-9b", model_id="Qwen/Qwen3.5-9B", provider="together",
        backend="fireworks", num_workers=4, reasoning_effort="",
    ),
    "together-muse-glimmer": ModelSpec(
        slug="together-muse-glimmer", model_id="meta-models/Muse-Glimmer-30B", provider="together",
        backend="fireworks", num_workers=4, reasoning_effort="",
    ),
    "qwen3p7-plus": ModelSpec(
        slug="qwen3p7-plus", model_id="accounts/fireworks/models/qwen3p7-plus", provider="fireworks",
    ),
    "together-nemotron-ultra": ModelSpec(
        slug="together-nemotron-ultra", model_id="nvidia/nemotron-3-ultra-550b-a55b", provider="together",
        backend="together_chat", num_workers=4, reasoning_effort="",
    ),
    "together-deepseek-pro": ModelSpec(
        slug="together-deepseek-pro", model_id="deepseek-ai/DeepSeek-V4-Pro", provider="together",
        backend="together_chat", num_workers=4, reasoning_effort="",
    ),
    "together-ternary-bonsai-27b": ModelSpec(
        slug="together-ternary-bonsai-27b", model_id="Prism-ML/Ternary-Bonsai-27B", provider="together",
        backend="fireworks", num_workers=4, reasoning_effort="", max_new_tokens=3072,
    ),
}

PROVIDER_BASE_URL = {
    "fireworks": "https://api.fireworks.ai/inference/v1",
    "together": "https://api.together.ai/v1",
}


@dataclass
class Config:
    run_label: str = "run"
    num_notes: int = 5
    dataset: str = "laymaker"
    models: List[str] = field(default_factory=lambda: ["together-qwen3.5-9b"])

    arms: List[str] = field(default_factory=lambda: ["naive", "termonly", "grounded"])

    tag_policy: str = "replace"
    keep_gloss_scope: str = "names"
    prompt_style: str = "lean"

    cc_enabled: bool = True
    cc_max_sources: int = 16
    cc_num_ablations: int = 32
    cc_heldout_ablations: int = 32
    cc_lambda: float = 0.01
    cc_max_notes: Optional[int] = None
    cc_score_topk_masks: bool = True
    cc_topk: List[int] = field(default_factory=lambda: [1, 3])
    cc_seed: int = 1234
    cc_leave_one_out: bool = False

    cc_effect_threshold: float = 0.693
    cc_effect_threshold_sweep: List[float] = field(
        default_factory=lambda: [0.05, 0.10, 0.25, 0.693, 1.0])
    cc_attributable_lds: float = 0.40
    cc_attributable_margin: float = 0.10

    retrieval_normalise: bool = True
    retrieval_split_uncovered: bool = True
    retrieval_max_per_source: int = 2
    dictionary_policy: str = "last_resort"
    hop_split_expansion: bool = False
    use_umls: bool = False

    max_new_tokens: int = 512
    rationale_max_tokens: int = 3072
    think_prefill: str = ""
    temperature: float = 0.0
    max_generation_attempts: int = 3
    retry_temperatures: List[float] = field(
        default_factory=lambda: [0.0, 0.3, 0.7])
    person_policy: str = "match"
    seed: int = 1234
    two_pass: bool = True
    tagger_backend: str = "novita"
    tagger_model: str = "deepseek/deepseek-v4-flash-0731"

    extract_models: List[str] = field(
        default_factory=lambda: ["deepseek/deepseek-v4-flash-0731"])
    extract_temperature: float = 0.0
    extract_max_tokens: int = 4096
    novita_base_url: str = "https://api.novita.ai/openai"
    measure_extraction_stability: bool = False

    enable_torch_evals: bool = True
    bertscore_model: str = str(HERE / "roberta-large")
    bertscore_layers: int = 17
    bertscore_rescale: bool = True
    nli_model: str = str(HERE / "roberta-large-mnli")
    fdr_alpha: float = 0.05
    zipf_strata: List[float] = field(default_factory=lambda: [2.5, 3.5, 4.5])

    run_rationales: bool = True
    run_hallucination_audit: bool = True
    run_judge: bool = False
    judge_models: List[str] = field(default_factory=lambda: [
        "deepseek/deepseek-v4-pro", "zai-org/glm-5", "minimax/minimax-m3",
    ])

    use_cache: bool = True
    cache_dir: Path = HERE / "runs" / "_cache"

    force_rerun: bool = False
    fresh_shared: bool = False
    keep_retrieval: bool = False

    root: Path = HERE
    out_root: Path = HERE / "runs"

    def model_spec(self, name: str) -> ModelSpec:
        if name not in MODEL_REGISTRY:
            raise SystemExit(
                f"[config] unknown model {name!r}. Known: {sorted(MODEL_REGISTRY)}"
            )
        return MODEL_REGISTRY[name]

    def out_dir(self, model: str) -> Path:
        return self.out_root / self.run_label / model

    def shared_dir(self) -> Path:
        extract = (self.extract_models[0] if self.extract_models else "none")
        slug = extract.replace("/", "-")
        return (self.out_root / "_shared"
                / f"{self.dataset}_{self.num_notes}_{slug}")

    _KEY_GLOBS = {
        "fireworks": ["firework.txt", "firework[0-9].txt", "fireworks*.txt"],
        "together": ["togetherAI_KEY", "togetherAI_KEY[0-9]", "together*.txt"],
        "novita": ["novita.txt", "novita_api", "novita[0-9].txt"],
    }
    _KEY_ENV = {
        "fireworks": "FIREWORKS_API_KEY",
        "together": "TOGETHER_API_KEY",
        "novita": "NOVITA_API_KEY",
    }

    def api_keys(self, provider: str) -> List[str]:
        out: List[str] = []
        env = os.environ.get(self._KEY_ENV[provider], "").strip()
        if env:
            out.append(env)
        for base in (self.root / "keys", self.root):
            if not base.is_dir():
                continue
            paths: List[Path] = []
            for pattern in self._KEY_GLOBS[provider]:
                paths.extend(sorted(base.glob(pattern)))
            for p in paths:
                if not p.is_file():
                    continue
                try:
                    lines = p.read_text(encoding="utf-8").strip().splitlines()
                except OSError:
                    continue
                if lines and lines[0].strip():
                    out.append(lines[0].strip())
        deduped = list(dict.fromkeys(out))
        if not deduped:
            raise SystemExit(
                f"[config] no {provider} key - set ${self._KEY_ENV[provider]} "
                f"or create {self.root / 'keys' / self._KEY_GLOBS[provider][0]}"
            )
        return deduped

    def api_key(self, provider: str) -> str:
        return self.api_keys(provider)[0]

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["root"] = str(self.root)
        d["out_root"] = str(self.out_root)
        d["cache_dir"] = str(self.cache_dir)
        return d


def preset_audit5(models: Optional[List[str]] = None) -> Config:
    return Config(
        run_label="_smoke/audit5",
        dataset="fixture5",
        num_notes=5,
        models=models or ["together-qwen3.5-9b"],
        run_rationales=True,
        run_hallucination_audit=True,
        run_judge=False,
    )


def preset_full100(models: Optional[List[str]] = None) -> Config:
    return Config(
        run_label="run100",
        dataset="laymaker",
        num_notes=100,
        models=models or [
            "together-qwen3.5-9b",
            "together-muse-glimmer",
            "qwen3p7-plus",
            "together-nemotron-ultra",
            "together-deepseek-pro",
            "together-ternary-bonsai-27b",
        ],
        run_rationales=True,
        run_judge=False,
    )
