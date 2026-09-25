"""LLM clients: text completions (Fireworks API format) and Together chat, both able to
return prompt log-probabilities for ContextCite, plus an optional local transformers backend.
"""

from __future__ import annotations

import functools
import json
import os
import random
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


def _strip_thinking(text: str) -> str:
    text = re.sub(r"<think\b[^>]*>.*?</think>", "", text, flags=re.DOTALL)
    if "<think" in text:
        text = re.split(r"<think\b[^>]*>", text)[0]
    if "</think>" in text:
        text = text.split("</think>")[-1]
    return text.strip()


_END_MARKERS = [
    "<｜end▁of▁sentence｜>", "<｜end▁of▁file｜>", "<｜begin▁of▁file",
    "<｜begin▁of▁sentence｜>", "<｜User｜>", "<｜Assistant｜>",
    "<|endoftext|>", "<|eot_id|>", "<|im_end|>", "<|end|>", "</s>",
    "\n### Instruction", "\n### Response", "\n# --- start of prompt",
    "\n# --- end of prompt",
    "\n---", "\n***", "\n**", "\nInput:", "\nOutput:", "\nSentence:",
    "\n#", "\nWait,", "\nWait ", "\nGlossary:", "\nNote:", "\nExample",
]

_INLINE_END_MARKERS = [
    "assistant to=", "commentary to=", "analysis to=",
    "<|start|>assistant", "<|channel|>",
]

_TOGETHER_TEXT_STOPS = [
    "\n### Instruction", "\n### Response",
    "\n# --- start of prompt", "\n# --- end of prompt",
]

_TRAILING_ROLE_RE = re.compile(
    r"(?<=[.!?])(user|assistant|system|model|human)\b", re.IGNORECASE)


def _clean_completion(text: str) -> str:
    text = _strip_thinking(text)
    cut = len(text)
    for m in _END_MARKERS + _INLINE_END_MARKERS:
        i = text.find(m)
        if i != -1:
            cut = min(cut, i)
    text = text[:cut]
    text = re.sub(r"<｜[^>]*?｜>", "", text)
    text = re.sub(r"<\|[^>]*?\|>", "", text)
    role = _TRAILING_ROLE_RE.search(text)
    if role:
        text = text[:role.start()]
    return text.strip()


def _truncate_to_last_sentence(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return ""
    cut = max(t.rfind(". "), t.rfind(".\n"), t.rfind("! "), t.rfind("? "))
    if t.endswith((".", "!", "?")):
        return t
    if cut > 0:
        return t[:cut + 1].strip()
    return ""


def _messages_to_prompt(messages: List[Dict[str, str]]) -> str:
    sys_parts, turn_parts = [], []
    for m in messages:
        role = (m.get("role") or "user").lower()
        content = m.get("content") or ""
        if role == "system":
            sys_parts.append(content)
        else:
            turn_parts.append(content)
    system = "\n\n".join(p for p in sys_parts if p).strip()
    body = "\n\n".join(p for p in turn_parts if p).strip()
    if system:
        return f"{system}\n\n{body}\n\n### Response:\n"
    return f"{body}\n\n### Response:\n"


class EchoUnsupported(Exception):
    pass


def _apply_reasoning(payload: Dict[str, Any], effort: str, base_url: str) -> None:
    if not effort:
        return
    if "api.together.ai" in (base_url or "").lower():
        payload["reasoning"] = ({"enabled": False} if effort == "none"
                                else {"enabled": True})
        if effort != "none":
            payload["reasoning_effort"] = effort
    else:
        payload["reasoning_effort"] = effort


class ProviderUnavailable(Exception):
    pass


_FATAL_STATUS = {401, 402, 403, 412}
_PROVIDER_DEAD: Dict[str, str] = {}


class _AdaptiveThrottle:
    def __init__(self, floor: float = 0.0, ceil: float = 8.0) -> None:
        self._lock = threading.Lock()
        self._interval = floor
        self._floor = floor
        self._ceil = ceil
        self._next = 0.0
        self.penalties = 0

    def wait(self) -> None:
        with self._lock:
            slot = max(time.monotonic(), self._next)
            self._next = slot + self._interval
        delay = slot - time.monotonic()
        if delay > 0:
            time.sleep(delay)

    def penalise(self, retry_after: Optional[float] = None) -> None:
        with self._lock:
            self.penalties += 1
            self._interval = min(self._ceil, max(0.5, self._interval * 2.0))
            hold = retry_after if retry_after else self._interval
            self._next = max(self._next, time.monotonic() + hold)

    def reward(self) -> None:
        if self._interval <= self._floor:
            return
        with self._lock:
            self._interval = max(self._floor, self._interval * 0.97)

    @property
    def interval(self) -> float:
        return self._interval


_THROTTLES: Dict[str, _AdaptiveThrottle] = {}
_THROTTLE_LOCK = threading.Lock()


def throttle_for(base_url: str) -> _AdaptiveThrottle:
    with _THROTTLE_LOCK:
        t = _THROTTLES.get(base_url)
        if t is None:
            t = _AdaptiveThrottle()
            _THROTTLES[base_url] = t
        return t


def _sleep_jittered(seconds: float) -> None:
    time.sleep(seconds * (0.5 + random.random()))


_FAIL_LOCK = threading.Lock()
_FAIL_COUNTS: Dict[str, int] = {}
_FAIL_PRINT_LIMIT = 3


def _note_scoring_failure(msg: str) -> None:
    kind = "429" if "429" in msg else msg[:40]
    with _FAIL_LOCK:
        n = _FAIL_COUNTS.get(kind, 0) + 1
        _FAIL_COUNTS[kind] = n
    if n <= _FAIL_PRINT_LIMIT:
        print(f"  [warn] echo scoring failed after retries ({msg[:90]}) "
              f"- using -1e4 for this ablation")
    elif n == _FAIL_PRINT_LIMIT + 1:
        print(f"  [warn] ...further '{kind}' scoring failures suppressed; "
              f"total reported at end of stage.")


def scoring_failure_counts() -> Dict[str, int]:
    with _FAIL_LOCK:
        return dict(_FAIL_COUNTS)


SCORE_FAILED = -1e4


def _degenerate_echo_tokens(tokens: List[Tuple[float, int, int]],
                            max_zero_rate: float = 0.10) -> bool:
    if not tokens:
        return True
    zero_count = sum(float(logprob) == 0.0 for logprob, _, _ in tokens)
    if zero_count == len(tokens):
        return True
    return len(tokens) >= 5 and zero_count / len(tokens) > max_zero_rate


def _sum_spans(tokens: List[Tuple[float, int, int]],
               spans: List[Tuple[int, int]]) -> List[float]:
    out: List[float] = []
    for start, end in spans:
        out.append(sum(lp for lp, ts, te in tokens if ts < end and te > start))
    return out


def _count_spans(tokens: List[Tuple[float, int, int]],
                 spans: List[Tuple[int, int]]) -> List[int]:
    return [sum(1 for _, ts, te in tokens if ts < end and te > start)
            for start, end in spans]


class _SpanScoringMixin:
    def log_prob_spans(self, prompt: str, response: str,
                       spans: List[Tuple[int, int]]) -> List[float]:
        return [self.log_prob_of_response(prompt + response[:s], response[s:e])
                for s, e in spans]

    def log_prob_spans_batch(self, prompts: List[str], response: str,
                             spans: List[Tuple[int, int]],
                             batch_size: int = 4) -> List[List[float]]:
        return [self.log_prob_spans(p, response, spans) for p in prompts]


@dataclass
class FireworksConfig:
    model_name: str = "accounts/fireworks/models/deepseek-v4-flash"
    fallback_models: List[str] = field(default_factory=lambda: [
        "accounts/fireworks/models/qwen3p7-plus",
    ])
    base_url: str = "https://api.fireworks.ai/inference/v1"
    api_key: str = ""
    key_file: str = "firework.txt"
    max_new_tokens: int = 512
    temperature: float = 0.0
    top_p: float = 1.0
    seed: int = 1234
    reasoning_effort: str = "none"
    num_workers: int = 8
    max_retries: int = 9
    timeout_s: float = 120.0
    require_echo: bool = True
    api_keys: List[str] = field(default_factory=list)
    quantization: str = "api"

    def resolve_keys(self) -> List[str]:
        out = [k.strip() for k in ([self.api_key] + list(self.api_keys))
               if k and k.strip()]
        if out:
            return list(dict.fromkeys(out))
        return [self.resolve_key()]

    def resolve_key(self) -> str:
        if self.api_key.strip():
            return self.api_key.strip()
        if self.api_keys and self.api_keys[0].strip():
            return self.api_keys[0].strip()
        env = os.environ.get("FIREWORKS_API_KEY", "").strip()
        if env:
            return env
        for base in (Path.cwd(), Path(__file__).resolve().parent):
            fp = base / self.key_file
            if fp.exists():
                k = fp.read_text(encoding="utf-8").strip().splitlines()
                if k and k[0].strip():
                    return k[0].strip()
        raise SystemExit(
            f"No Fireworks API key. Set FIREWORKS_API_KEY or put the key "
            f"(one line) in {self.key_file}."
        )


class _KeyRotationMixin:
    def _init_keys(self) -> None:
        self._keys = self.cfg.resolve_keys()
        self._key_idx = 0
        self._key_lock = threading.Lock()

    @property
    def _key(self) -> str:
        return self._keys[self._key_idx]

    @property
    def _dead_tag(self) -> str:
        return f"{self.cfg.base_url}#{self._key[-8:]}"

    def _rotate_key(self, reason: str) -> bool:
        with self._key_lock:
            spent = self._key
            if self._key_idx + 1 >= len(self._keys):
                return False
            self._key_idx += 1
            if self.session is not None:
                self.session.headers["Authorization"] = f"Bearer {self._key}"
            print(f"\n  [key] key ...{spent[-6:]} rejected ({reason[:70]}); "
                  f"rotating to key {self._key_idx + 1}/{len(self._keys)} "
                  f"...{self._key[-6:]}\n")
            return True


class FireworksLLM(_KeyRotationMixin):
    uses_text_completions = True

    def __init__(self, cfg: FireworksConfig):
        self.cfg = cfg
        self.session = None
        self.chosen_model: Optional[str] = None
        self._loaded = False
        self._init_keys()

    def load(self):
        if self._loaded:
            return
        try:
            import requests
        except ImportError as e:
            raise RuntimeError("Fireworks backend needs `requests` "
                               "(pip install requests).") from e
        key = self._key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        })
        if not self.cfg.require_echo:
            self.chosen_model = self.cfg.model_name
            self._loaded = True
            print(f"[llm] completions generation on {self.chosen_model} "
                  f"(echo probe skipped for this stage).")
            return
        print(f"[llm] Fireworks backend — probing echo on {self.cfg.model_name} …")
        candidates = [self.cfg.model_name] + list(self.cfg.fallback_models)
        last_err = None
        for model in candidates:
            try:
                if self._echo_ok(model):
                    self.chosen_model = model
                    self._loaded = True
                    print(f"[llm] echo works on {model} — using it.")
                    return
            except Exception as e:
                last_err = e
                print(f"[llm] {model}: {e}")
        raise RuntimeError(
            "Fireworks echo (prompt-token logprobs) unsupported on every "
            f"candidate model {candidates}. Full ContextCite needs echo. "
            f"Last error: {last_err}"
        )

    def _echo_ok(self, model: str) -> bool:
        prefix = ("Rewrite for a patient: The patient was commenced on oral "
                  "antibiotics for cellulitis.\nRewrite:")
        try:
            tokens = self._score_tokens(
                prefix, " The patient started antibiotics by mouth for a skin "
                        "infection.", model=model)
        except EchoUnsupported:
            return False
        return bool(tokens) and not _degenerate_echo_tokens(tokens)

    def _completions(self, prompt: str, max_tokens: int = 1, echo: bool = False,
                     logprobs: Optional[int] = None, temperature: float = 0.0,
                     top_p: float = 1.0, model: Optional[str] = None,
                     stop: Optional[List[str]] = None,
                     prompt_logprobs: Optional[int] = None) -> Dict[str, Any]:
        import requests
        if self.session is None:
            self._ensure_loaded()
        url = f"{self.cfg.base_url}/completions"
        payload: Dict[str, Any] = {
            "model": model or self.chosen_model or self.cfg.model_name,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "echo": echo,
        }
        if logprobs is not None:
            payload["logprobs"] = logprobs
        if prompt_logprobs is not None:
            payload["prompt_logprobs"] = prompt_logprobs
        if stop:
            if "api.together.ai" in self.cfg.base_url.lower():
                payload["stop"] = _TOGETHER_TEXT_STOPS
            else:
                payload["stop"] = stop
        _apply_reasoning(payload, self.cfg.reasoning_effort, self.cfg.base_url)

        backoff = 1.5
        last_err = None
        dead = _PROVIDER_DEAD.get(self._dead_tag)
        if dead:
            raise ProviderUnavailable(dead)
        pace = throttle_for(self.cfg.base_url)
        for attempt in range(self.cfg.max_retries):
            pace.wait()
            try:
                r = self.session.post(url, json=payload, timeout=self.cfg.timeout_s)
            except requests.RequestException as e:
                last_err = e
                _sleep_jittered(backoff)
                backoff *= 2
                continue
            if r.status_code in _FATAL_STATUS:
                reason = (f"HTTP {r.status_code} from {self.cfg.base_url}: "
                          f"{r.text[:300]}")
                if self._rotate_key(f"HTTP {r.status_code}"):
                    continue
                if self._dead_tag not in _PROVIDER_DEAD:
                    _PROVIDER_DEAD[self._dead_tag] = reason
                    print(f"\n[fatal] every key for {self.cfg.base_url} was "
                          f"rejected and will not recover:\n        {reason}\n")
                raise ProviderUnavailable(reason)
            if r.status_code in (429, 500, 502, 503, 504):
                ra = r.headers.get("retry-after")
                ra_s = float(ra) if ra and ra.replace(".", "", 1).isdigit() else None
                if r.status_code == 429:
                    pace.penalise(ra_s)
                if attempt == self.cfg.max_retries - 1:
                    raise RuntimeError(f"Persistent {r.status_code} after "
                                       f"{self.cfg.max_retries} retries: {r.text[:300]}")
                _sleep_jittered(ra_s if ra_s else backoff)
                backoff *= 2
                continue
            if r.status_code >= 400:
                raise RuntimeError(f"HTTP {r.status_code} from completions API: {r.text[:500]}")
            pace.reward()
            return r.json()
        raise RuntimeError(f"Request failed without a successful response: {last_err}")

    @staticmethod
    def _prompt_logprobs_as_legacy(data: Dict[str, Any],
                                   full_text: str = "") -> Dict[str, Any]:
        pl = (data.get("choices") or [{}])[0].get("prompt_logprobs")
        if not isinstance(pl, list) or not pl:
            return {}
        tokens: List[str] = []
        values: List[Optional[float]] = []
        for entry in pl:
            if not isinstance(entry, dict) or not entry:
                tokens.append("")
                values.append(None)
                continue
            first = next(iter(entry.values()))
            if not isinstance(first, dict):
                tokens.append("")
                values.append(None)
                continue
            tokens.append(str(first.get("decoded_token") or ""))
            lv = first.get("logprob")
            values.append(float(lv) if isinstance(lv, (int, float)) else None)
        if not any(v is not None for v in values):
            return {}
        if full_text and tokens and not tokens[0]:
            recon = "".join(tokens)
            if recon and recon != full_text and full_text.endswith(recon):
                tokens[0] = full_text[:len(full_text) - len(recon)]
        return {"tokens": tokens, "token_logprobs": values, "text_offset": None}

    def _score_tokens(self, prompt: str, response: str,
                      model: Optional[str] = None
                      ) -> List[Tuple[float, int, int]]:
        full = prompt + response
        try:
            data = self._completions(full, max_tokens=1, echo=True, logprobs=1,
                                     temperature=0.0, model=model)
            lp = data["choices"][0].get("logprobs") or {}
        except RuntimeError:
            lp = {}
        tlp = lp.get("token_logprobs")
        if not tlp:
            data = self._completions(full, max_tokens=1, echo=True,
                                     temperature=0.0, model=model,
                                     prompt_logprobs=0)
            lp = self._prompt_logprobs_as_legacy(data, full)
            tlp = lp.get("token_logprobs")
        if not tlp:
            raise EchoUnsupported("No token_logprobs or prompt_logprobs "
                                  "returned (echo unsupported on this "
                                  "model/endpoint).")
        if len(tlp) <= 2:
            raise EchoUnsupported(f"Only {len(tlp)} logprob(s) — echo did not "
                                  "include the prompt tokens.")
        start_char, end_char = len(prompt), len(full)
        out: List[Tuple[float, int, int]] = []
        offs = lp.get("text_offset")
        valid_offsets = offs is not None and any(
            isinstance(o, int) and o >= 0 for o in offs)
        if valid_offsets:
            toks = lp.get("tokens") or []
            for index, (l, off) in enumerate(zip(tlp, offs)):
                if not isinstance(off, int) or off < 0 or l is None:
                    continue
                next_offsets = [
                    candidate for candidate in offs[index + 1:]
                    if isinstance(candidate, int) and candidate > off
                ]
                token_end = next_offsets[0] if next_offsets else (
                    off + len(toks[index]) if index < len(toks) and toks[index] else off + 1
                )
                if off < end_char and token_end > start_char:
                    out.append((float(l), off - start_char, token_end - start_char))
        else:
            toks = lp.get("tokens") or []
            if not toks:
                raise EchoUnsupported("Echo returned token_logprobs but no "
                                      "usable `text_offset` or `tokens` — cannot "
                                      "align to the response region.")
            recon = "".join(t or "" for t in toks)
            base = recon.find(prompt)
            if base >= 0:
                r_start = base + start_char
            else:
                r_start = None
                suffix_lengths = [
                    length for length in (2048, 1024, 512, 256, 128, 64, 32)
                    if length <= len(prompt)
                ]
                for suffix_length in suffix_lengths:
                    suffix = prompt[-suffix_length:]
                    suffix_pos = recon.rfind(suffix)
                    candidate_start = suffix_pos + suffix_length
                    if (suffix_pos >= 0
                            and recon[candidate_start:
                                      candidate_start + len(response)] == response):
                        r_start = candidate_start
                        break
                if r_start is None:
                    raise EchoUnsupported(
                        "Echo token strings contain neither the exact prompt "
                        "nor an exact long prompt suffix followed by the "
                        "scored response; alignment is unsafe."
                    )
            r_end = r_start + len(response)
            off = 0
            for tok, l in zip(toks, tlp):
                token_end = off + len(tok or "")
                if l is not None and off < r_end and token_end > r_start:
                    out.append((float(l), off - r_start, token_end - r_start))
                off = token_end
        return out

    def _score(self, prompt: str, response: str, model: Optional[str] = None):
        toks = self._score_tokens(prompt, response, model)
        return sum(t[0] for t in toks), len(toks)

    def apply_chat_template(self, messages: List[Dict[str, str]]) -> str:
        return _messages_to_prompt(messages)

    def _complete_once(self, prompt: str, max_new: int, temp: float,
                       stop_strings: Optional[List[str]]) -> tuple[str, Optional[str]]:
        data = self._completions(prompt, max_tokens=max_new, echo=False,
                                 temperature=temp, top_p=self.cfg.top_p,
                                 stop=_END_MARKERS)
        choice = data["choices"][0]
        text = _clean_completion(choice.get("text", "") or "")
        if stop_strings:
            for s in stop_strings:
                idx = text.find(s)
                if idx != -1:
                    text = text[:idx]
        return text, choice.get("finish_reason")

    def complete(self, prompt: str, max_new_tokens: Optional[int] = None,
                 temperature: Optional[float] = None,
                 stop_strings: Optional[List[str]] = None,
                 attempt: int = 0) -> str:
        self._ensure_loaded()
        max_new = max_new_tokens or self.cfg.max_new_tokens
        temp = self.cfg.temperature if temperature is None else temperature
        from core.cache import get_cache
        cache = get_cache()
        model = self.chosen_model or self.cfg.model_name
        base = f"gen:{max_new}:{self.cfg.reasoning_effort}"
        kind = base if (attempt == 0 and temp == 0) else f"{base}:t{temp}:a{attempt}"
        key = cache.make_key(kind, model, prompt)
        if key:
            hit = cache.get(key)
            if isinstance(hit, str):
                return hit
        text, finish_reason = self._complete_once(prompt, max_new, temp, stop_strings)
        if finish_reason == "length":
            retry_max = min(max_new * 2, max(2048, self.cfg.max_new_tokens * 2))
            if retry_max > max_new:
                text, finish_reason = self._complete_once(
                    prompt, retry_max, temp, stop_strings
                )
            if finish_reason == "length":
                salvaged = _truncate_to_last_sentence(text)
                if salvaged.strip():
                    print(f"  [warn] completion hit max_tokens={retry_max}; "
                          f"salvaging the first {len(salvaged.split())} words")
                    return salvaged
                raise RuntimeError(
                    f"Completion remained truncated at max_tokens={retry_max} "
                    f"and produced no usable prefix."
                )
        if not text.strip():
            text, _ = self._complete_once(
                prompt, max_new, max(temp, 0.7), stop_strings
            )
        if key and text.strip():
            cache.put(key, text)
        return text

    def chat(self, messages: List[Dict[str, str]],
             max_new_tokens: Optional[int] = None,
             temperature: Optional[float] = None,
             stop_strings: Optional[List[str]] = None) -> str:
        return self.complete(self.apply_chat_template(messages),
                             max_new_tokens=max_new_tokens,
                             temperature=temperature, stop_strings=stop_strings)

    def _tokens_cached(self, prompt: str, response: str
                       ) -> Optional[List[Tuple[float, int, int]]]:
        from core.cache import get_cache
        cache = get_cache()
        model = self.chosen_model or self.cfg.model_name
        ckey = cache.make_key("echotok", model, prompt, response)
        hit = cache.get(ckey)
        if isinstance(hit, list) and hit:
            cached = [(float(a), int(b), int(c)) for a, b, c in hit]
            if _degenerate_echo_tokens(cached):
                return None
            return cached
        try:
            toks = self._score_tokens(prompt, response)
        except ProviderUnavailable:
            raise
        except RuntimeError as e:
            _note_scoring_failure(str(e))
            return None
        if not toks:
            return None
        if _degenerate_echo_tokens(toks):
            zeros = sum(t[0] == 0.0 for t in toks)
            _note_scoring_failure(f"degenerate echo: {zeros}/{len(toks)} "
                                  f"tokens have log p == 0")
            return None
        cache.put(ckey, [[lp, a, b] for lp, a, b in toks])
        return toks

    def log_prob_of_response(self, prompt: str, response: str) -> float:
        self._ensure_loaded()
        toks = self._tokens_cached(prompt, response)
        if toks is None:
            return SCORE_FAILED
        return sum(t[0] for t in toks)

    def log_prob_spans(self, prompt: str, response: str,
                       spans: List[Tuple[int, int]]) -> List[float]:
        self._ensure_loaded()
        toks = self._tokens_cached(prompt, response)
        if toks is None:
            return [SCORE_FAILED] * len(spans)
        return _sum_spans(toks, spans)

    def span_token_counts(self, prompt: str, response: str,
                          spans: List[Tuple[int, int]]) -> List[int]:
        self._ensure_loaded()
        toks = self._tokens_cached(prompt, response)
        return _count_spans(toks, spans) if toks else []

    def log_prob_spans_batch(self, prompts: List[str], response: str,
                             spans: List[Tuple[int, int]],
                             batch_size: int = 4) -> List[List[float]]:
        self._ensure_loaded()
        if not prompts:
            return []
        n_workers = max(1, min(self.cfg.num_workers, len(prompts)))
        results: List[Optional[List[float]]] = [None] * len(prompts)
        if n_workers == 1:
            for i, p in enumerate(prompts):
                results[i] = self.log_prob_spans(p, response, spans)
            return results

        def one(i_p):
            i, p = i_p
            return i, self.log_prob_spans(p, response, spans)

        with ThreadPoolExecutor(max_workers=n_workers) as ex:
            for i, val in ex.map(one, list(enumerate(prompts))):
                results[i] = val
        return results

    def log_prob_batch(self, prompts: List[str], response: str,
                       batch_size: int = 4) -> List[float]:
        self._ensure_loaded()
        if not prompts:
            return []
        n_workers = max(1, min(self.cfg.num_workers, len(prompts)))
        results: List[Optional[float]] = [None] * len(prompts)

        if n_workers == 1:
            for i, p in enumerate(prompts):
                results[i] = self.log_prob_of_response(p, response)
            return results

        def one(i_p):
            i, p = i_p
            return i, self.log_prob_of_response(p, response)

        with ThreadPoolExecutor(max_workers=n_workers) as ex:
            for i, val in ex.map(one, list(enumerate(prompts))):
                results[i] = val
        return results

    def _ensure_loaded(self):
        if not self._loaded:
            self.load()


class TogetherChatLLM(_KeyRotationMixin):
    def __init__(self, cfg: FireworksConfig):
        self.cfg = cfg
        self.session = None
        self.chosen_model = cfg.model_name
        self._loaded = False
        self._init_keys()

    def load(self):
        if self._loaded:
            return
        import requests
        key = self._key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        })
        self._loaded = True
        if self.cfg.require_echo:
            score = self.log_prob_of_response(
                self.apply_chat_template([
                    {"role": "system", "content": "Answer briefly."},
                    {"role": "user", "content": "Capital of France?"},
                ]),
                "Paris.",
            )
            if score <= -1e4:
                raise RuntimeError(
                    f"Together chat prompt logprobs unavailable for "
                    f"{self.chosen_model}."
                )
            print(f"[llm] chat echo works on {self.chosen_model} — using it.")
        else:
            print(f"[llm] chat generation on {self.chosen_model} "
                  f"(echo probe skipped for this stage).")

    def _request(self, messages: List[Dict[str, str]], max_tokens: int,
                 temperature: float, echo: bool = False,
                 logprobs: Optional[int] = None) -> Dict[str, Any]:
        import requests
        if self.session is None:
            self.load()
        payload: Dict[str, Any] = {
            "model": self.chosen_model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": self.cfg.top_p,
            "reasoning": {"enabled": False},
        }
        if echo:
            payload["echo"] = True
        if logprobs is not None:
            payload["logprobs"] = logprobs
        backoff = 2.0
        pace = throttle_for(self.cfg.base_url)
        dead = _PROVIDER_DEAD.get(self._dead_tag)
        if dead:
            raise ProviderUnavailable(dead)
        for attempt in range(self.cfg.max_retries):
            pace.wait()
            try:
                response = self.session.post(
                    f"{self.cfg.base_url}/chat/completions",
                    json=payload,
                    timeout=self.cfg.timeout_s,
                )
            except requests.RequestException as exc:
                if attempt == self.cfg.max_retries - 1:
                    raise RuntimeError(f"Together chat request failed: {exc}") from exc
                _sleep_jittered(backoff)
                backoff *= 2
                continue
            if response.status_code in _FATAL_STATUS:
                reason = (f"HTTP {response.status_code} from "
                          f"{self.cfg.base_url}: {response.text[:300]}")
                if self._rotate_key(f"HTTP {response.status_code}"):
                    continue
                if self._dead_tag not in _PROVIDER_DEAD:
                    _PROVIDER_DEAD[self._dead_tag] = reason
                    print(f"\n[fatal] every key for {self.cfg.base_url} was "
                          f"rejected and will not recover:\n        {reason}\n")
                raise ProviderUnavailable(reason)
            if response.status_code in (429, 500, 502, 503, 504):
                retry_after = response.headers.get("retry-after")
                ra_s = (float(retry_after)
                        if retry_after and retry_after.replace(".", "", 1).isdigit()
                        else None)
                if response.status_code == 429:
                    pace.penalise(ra_s)
                if attempt == self.cfg.max_retries - 1:
                    raise RuntimeError(
                        f"Persistent Together chat HTTP {response.status_code}: "
                        f"{response.text[:500]}"
                    )
                _sleep_jittered(ra_s if ra_s else backoff)
                backoff *= 2
                continue
            if response.status_code >= 400:
                raise RuntimeError(
                    f"Together chat HTTP {response.status_code}: "
                    f"{response.text[:500]}"
                )
            pace.reward()
            return response.json()
        raise RuntimeError("Together chat request failed without a response")

    @staticmethod
    def _decode_prompt_with_prefix(
        prompt: str,
    ) -> tuple[List[Dict[str, str]], str]:
        decoder = json.JSONDecoder()
        messages, end = decoder.raw_decode(prompt)
        if not isinstance(messages, list):
            raise ValueError("Together chat prompt is not a message list")
        normalized = [
            {"role": str(message["role"]),
             "content": str(message.get("content") or "")}
            for message in messages
        ]
        return normalized, prompt[end:]

    @classmethod
    def _decode_prompt(cls, prompt: str) -> List[Dict[str, str]]:
        messages, prefix = cls._decode_prompt_with_prefix(prompt)
        if prefix:
            raise ValueError(
                "Generated response prefix is only valid during scoring"
            )
        return messages

    def apply_chat_template(self, messages: List[Dict[str, str]]) -> str:
        normalized = [
            {"role": str(message.get("role") or "user"),
             "content": str(message.get("content") or "")}
            for message in messages
        ]
        return json.dumps(normalized, ensure_ascii=False, separators=(",", ":"))

    def complete(self, prompt: str, max_new_tokens: Optional[int] = None,
                 temperature: Optional[float] = None,
                 stop_strings: Optional[List[str]] = None,
                 attempt: int = 0) -> str:
        self._ensure_loaded()
        max_new = max_new_tokens or self.cfg.max_new_tokens
        temp = self.cfg.temperature if temperature is None else temperature
        from core.cache import get_cache
        cache = get_cache()
        model = self.chosen_model or self.cfg.model_name
        base = f"chatgen:{max_new}:{self.cfg.reasoning_effort}"
        kind = base if (attempt == 0 and temp == 0) else f"{base}:t{temp}:a{attempt}"
        key = cache.make_key(kind, model, prompt)
        if key:
            hit = cache.get(key)
            if isinstance(hit, str):
                return hit
        data = self._request(self._decode_prompt(prompt), max_new, temp)
        choice = data["choices"][0]
        finish_reason = choice.get("finish_reason")
        if finish_reason == "length":
            retry_max = min(max_new * 2, max(2048, self.cfg.max_new_tokens * 2))
            data = self._request(self._decode_prompt(prompt), retry_max, temp)
            choice = data["choices"][0]
            if choice.get("finish_reason") == "length":
                partial = _clean_completion(
                    ((choice.get("message") or {}).get("content") or ""))
                salvaged = _truncate_to_last_sentence(partial)
                if salvaged.strip():
                    print(f"  [warn] chat completion hit max_tokens={retry_max}; "
                          f"salvaging the first {len(salvaged.split())} words")
                    if key:
                        cache.put(key, salvaged)
                    return salvaged
                raise RuntimeError(
                    f"Together chat completion remained truncated at "
                    f"max_tokens={retry_max} and produced no usable prefix."
                )
        text = _clean_completion(
            ((choice.get("message") or {}).get("content") or "")
        )
        if stop_strings:
            for stop in stop_strings:
                index = text.find(stop)
                if index >= 0:
                    text = text[:index]
        text = text.strip()
        if key:
            cache.put(key, text)
        return text

    def chat(self, messages: List[Dict[str, str]],
             max_new_tokens: Optional[int] = None,
             temperature: Optional[float] = None,
             stop_strings: Optional[List[str]] = None) -> str:
        return self.complete(
            self.apply_chat_template(messages), max_new_tokens,
            temperature, stop_strings,
        )

    def _score_tokens(self, prompt: str, response: str
                      ) -> Optional[List[Tuple[float, int, int]]]:
        messages, response_prefix = self._decode_prompt_with_prefix(prompt)
        fixed_response = response_prefix + response
        messages.append({"role": "assistant", "content": fixed_response})
        try:
            data = self._request(
                messages, max_tokens=1, temperature=0.0,
                echo=True, logprobs=1,
            )
        except RuntimeError as exc:
            print(f"  [warn] chat echo scoring failed ({str(exc)[:100]})")
            return None
        out: List[Tuple[float, int, int]] = []
        for part in data.get("prompt") or []:
            logprobs = part.get("logprobs") or {}
            tokens = logprobs.get("tokens") or []
            values = logprobs.get("token_logprobs") or []
            reconstructed = "".join(str(token or "") for token in tokens)
            fixed_start = reconstructed.rfind(fixed_response)
            if fixed_start < 0:
                continue
            target_start = fixed_start + len(response_prefix)
            target_end = target_start + len(response)
            offset = 0
            for token, value in zip(tokens, values):
                token_end = offset + len(str(token or ""))
                if (value is not None and offset < target_end
                        and token_end > target_start):
                    out.append((float(value), offset - target_start,
                                token_end - target_start))
                offset = token_end
        return out or None

    def _tokens_cached(self, prompt: str, response: str
                       ) -> Optional[List[Tuple[float, int, int]]]:
        from core.cache import get_cache
        cache = get_cache()
        ckey = cache.make_key("chatechotok", self.chosen_model, prompt, response)
        hit = cache.get(ckey)
        if isinstance(hit, list) and hit:
            cached = [(float(a), int(b), int(c)) for a, b, c in hit]
            if _degenerate_echo_tokens(cached):
                return None
            return cached
        toks = self._score_tokens(prompt, response)
        if not toks:
            return None
        if _degenerate_echo_tokens(toks):
            zeros = sum(t[0] == 0.0 for t in toks)
            _note_scoring_failure(f"degenerate echo: {zeros}/{len(toks)} "
                                  f"tokens have log p == 0")
            return None
        cache.put(ckey, [[lp, a, b] for lp, a, b in toks])
        return toks

    def log_prob_of_response(self, prompt: str, response: str) -> float:
        self._ensure_loaded()
        toks = self._tokens_cached(prompt, response)
        if toks is None:
            return SCORE_FAILED
        return sum(t[0] for t in toks)

    def log_prob_spans(self, prompt: str, response: str,
                       spans: List[Tuple[int, int]]) -> List[float]:
        self._ensure_loaded()
        toks = self._tokens_cached(prompt, response)
        if toks is None:
            return [SCORE_FAILED] * len(spans)
        return _sum_spans(toks, spans)

    def span_token_counts(self, prompt: str, response: str,
                          spans: List[Tuple[int, int]]) -> List[int]:
        self._ensure_loaded()
        toks = self._tokens_cached(prompt, response)
        return _count_spans(toks, spans) if toks else []

    def log_prob_spans_batch(self, prompts: List[str], response: str,
                             spans: List[Tuple[int, int]],
                             batch_size: int = 1) -> List[List[float]]:
        self._ensure_loaded()
        if not prompts:
            return []
        n_workers = max(1, min(self.cfg.num_workers, len(prompts)))
        results: List[Optional[List[float]]] = [None] * len(prompts)
        if n_workers == 1:
            for i, p in enumerate(prompts):
                results[i] = self.log_prob_spans(p, response, spans)
            return results

        def one(i_p):
            i, p = i_p
            return i, self.log_prob_spans(p, response, spans)

        with ThreadPoolExecutor(max_workers=n_workers) as ex:
            for i, val in ex.map(one, list(enumerate(prompts))):
                results[i] = val
        return results

    def log_prob_batch(self, prompts: List[str], response: str,
                       batch_size: int = 1) -> List[float]:
        return [self.log_prob_of_response(prompt, response) for prompt in prompts]

    def _ensure_loaded(self):
        if not self._loaded:
            self.load()


@dataclass
class LLMConfig:
    model_name: str = "Qwen/Qwen3-8B"
    quantization: str = "none"
    torch_dtype: str = "bfloat16"
    device_map: str = "auto"
    trust_remote_code: bool = True
    max_new_tokens: int = 512
    temperature: float = 0.0
    top_p: float = 1.0
    seed: int = 1234
    enable_thinking: bool = False
    hf_cache_dir: Optional[str] = None
    hf_token: Optional[str] = None
    extra: Dict[str, Any] = field(default_factory=dict)


def _dtype(name: str):
    import torch
    return {"float16": torch.float16, "fp16": torch.float16,
            "bfloat16": torch.bfloat16, "bf16": torch.bfloat16,
            "float32": torch.float32, "fp32": torch.float32}.get(name, torch.bfloat16)


def _canonical_model_name(name: str) -> str:
    return (name or "").strip()


def _inference_mode(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        import torch
        with torch.inference_mode():
            return fn(*args, **kwargs)
    return wrapper


def _bnb_config(cfg: LLMConfig, allow_cpu_offload: bool = False):
    if cfg.quantization == "none":
        return None
    try:
        from transformers import BitsAndBytesConfig
    except ImportError as e:
        raise RuntimeError(
            "bitsandbytes/transformers BitsAndBytesConfig not available — "
            "install bitsandbytes or set quantization='none'."
        ) from e
    if cfg.quantization == "8bit":
        return BitsAndBytesConfig(
            load_in_8bit=True,
            llm_int8_enable_fp32_cpu_offload=allow_cpu_offload,
        )
    if cfg.quantization in ("4bit", "fp4"):
        quant_type = "nf4" if cfg.quantization == "4bit" else "fp4"
        return BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type=quant_type,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=_dtype(cfg.torch_dtype),
            llm_int8_enable_fp32_cpu_offload=allow_cpu_offload,
        )
    raise ValueError(f"unknown quantization: {cfg.quantization!r}")


class LocalLLM(_SpanScoringMixin):
    def __init__(self, cfg: LLMConfig):
        self.cfg = cfg
        self.model = None
        self.tokenizer = None
        self._loaded = False

    def load(self):
        if self._loaded:
            return
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        self.cfg.model_name = _canonical_model_name(self.cfg.model_name)
        is_local = os.path.isdir(self.cfg.model_name)
        kwargs: Dict[str, Any] = {
            "trust_remote_code": self.cfg.trust_remote_code,
            "device_map": self.cfg.device_map,
        }
        if is_local:
            kwargs["local_files_only"] = True
        if self.cfg.hf_cache_dir and not is_local:
            kwargs["cache_dir"] = self.cfg.hf_cache_dir
        if self.cfg.hf_token and not is_local:
            kwargs["token"] = self.cfg.hf_token

        allow_cpu_offload = os.environ.get("ALLOW_CPU_OFFLOAD", "auto").lower()
        is_quantized = self.cfg.quantization in ("4bit", "8bit", "fp4")
        if allow_cpu_offload == "auto":
            allow_cpu_offload = is_quantized
        else:
            allow_cpu_offload = allow_cpu_offload in ("1", "true", "yes", "on")

        if torch.cuda.is_available() and torch.cuda.device_count() > 1:
            n = torch.cuda.device_count()
            total_gib = int(torch.cuda.get_device_properties(0).total_memory / 1024**3)
            headroom_gib = 2 if is_quantized else 3
            per_gpu_gb = max(4, total_gib - headroom_gib)
            kwargs["max_memory"] = {i: f"{per_gpu_gb}GiB" for i in range(n)}
            if (not is_quantized) or allow_cpu_offload:
                kwargs["max_memory"]["cpu"] = "30GiB"
            print(f"[llm] {n} GPUs visible, capping each at {per_gpu_gb} GiB")

        bnb = _bnb_config(self.cfg, allow_cpu_offload=allow_cpu_offload)
        if bnb is not None:
            kwargs["quantization_config"] = bnb
        else:
            kwargs["torch_dtype"] = _dtype(self.cfg.torch_dtype)

        print(f"[llm] loading {self.cfg.model_name} "
              f"(quant={self.cfg.quantization}, dtype={self.cfg.torch_dtype}) …")
        t0 = time.time()
        tok_kwargs: Dict[str, Any] = {"trust_remote_code": self.cfg.trust_remote_code}
        if is_local:
            tok_kwargs["local_files_only"] = True
        else:
            if self.cfg.hf_cache_dir:
                tok_kwargs["cache_dir"] = self.cfg.hf_cache_dir
            if self.cfg.hf_token:
                tok_kwargs["token"] = self.cfg.hf_token
        self.tokenizer = AutoTokenizer.from_pretrained(self.cfg.model_name, **tok_kwargs)
        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.model = AutoModelForCausalLM.from_pretrained(self.cfg.model_name, **kwargs)
        self.model.eval()
        try:
            self.model.config.pad_token_id = self.tokenizer.pad_token_id
        except Exception:
            pass
        torch.manual_seed(self.cfg.seed)
        self._loaded = True
        print(f"[llm] loaded in {time.time() - t0:.1f}s — "
              f"device map: {getattr(self.model, 'hf_device_map', 'single device')}")

    def apply_chat_template(self, messages: List[Dict[str, str]]) -> str:
        self._ensure_loaded()
        kwargs = {"tokenize": False, "add_generation_prompt": True}
        try:
            return self.tokenizer.apply_chat_template(
                messages, **kwargs, enable_thinking=self.cfg.enable_thinking)
        except TypeError:
            return self.tokenizer.apply_chat_template(messages, **kwargs)

    @_inference_mode
    def chat(self, messages: List[Dict[str, str]],
             max_new_tokens: Optional[int] = None,
             temperature: Optional[float] = None,
             stop_strings: Optional[List[str]] = None) -> str:
        self._ensure_loaded()
        prompt = self.apply_chat_template(messages)
        return self.complete(prompt, max_new_tokens=max_new_tokens,
                             temperature=temperature, stop_strings=stop_strings)

    @_inference_mode
    def complete(self, prompt: str, max_new_tokens: Optional[int] = None,
                 temperature: Optional[float] = None,
                 stop_strings: Optional[List[str]] = None) -> str:
        self._ensure_loaded()
        max_new = max_new_tokens or self.cfg.max_new_tokens
        temp = self.cfg.temperature if temperature is None else temperature
        inp = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        gen_kwargs: Dict[str, Any] = {
            "max_new_tokens": max_new,
            "do_sample": temp > 0,
            "temperature": max(temp, 1e-5),
            "top_p": self.cfg.top_p,
            "pad_token_id": self.tokenizer.pad_token_id,
        }
        if stop_strings:
            gen_kwargs["stop_strings"] = stop_strings
            gen_kwargs["tokenizer"] = self.tokenizer
        out = self.model.generate(**inp, **gen_kwargs)
        new_tokens = out[0, inp.input_ids.shape[1]:]
        return self.tokenizer.decode(new_tokens, skip_special_tokens=True)

    @_inference_mode
    def log_prob_of_response(self, prompt: str, response: str) -> float:
        import torch.nn.functional as F
        self._ensure_loaded()
        tok = self.tokenizer
        device = self.model.device
        prompt_ids = tok(prompt, return_tensors="pt").input_ids.to(device)
        full_ids = tok(prompt + response, return_tensors="pt").input_ids.to(device)
        p_len = prompt_ids.shape[1]
        if full_ids.shape[1] <= p_len:
            return -1e4
        out = self.model(full_ids)
        logits = out.logits[0, p_len - 1: full_ids.shape[1] - 1, :]
        targets = full_ids[0, p_len: full_ids.shape[1]]
        log_probs = F.log_softmax(logits.float(), dim=-1)
        gathered = log_probs.gather(1, targets.unsqueeze(1)).squeeze(1)
        return float(gathered.sum().item())

    @_inference_mode
    def log_prob_batch(self, prompts: List[str], response: str,
                       batch_size: int = 4) -> List[float]:
        import torch
        import torch.nn.functional as F
        self._ensure_loaded()
        tok = self.tokenizer
        device = self.model.device
        original_padding_side = tok.padding_side
        tok.padding_side = "left"
        try:
            out_scores: List[float] = []
            for i in range(0, len(prompts), batch_size):
                batch_prompts = prompts[i: i + batch_size]
                full_texts = [p + response for p in batch_prompts]
                prompt_lens = [len(tok(p, add_special_tokens=False).input_ids)
                               for p in batch_prompts]
                full_lens = [len(tok(f, add_special_tokens=False).input_ids)
                             for f in full_texts]
                r_lens = [max(0, fl - pl) for fl, pl in zip(full_lens, prompt_lens)]
                enc = tok(full_texts, return_tensors="pt", padding=True).to(device)
                out = self.model(**enc)
                T = enc.input_ids.shape[1]
                logits_view = out.logits
                for b, r in enumerate(r_lens):
                    if r == 0:
                        out_scores.append(-1e4)
                        continue
                    target = enc.input_ids[b, T - r: T]
                    pred = logits_view[b, T - r - 1: T - 1, :].float()
                    log_probs = F.log_softmax(pred, dim=-1)
                    gathered = log_probs.gather(1, target.unsqueeze(1)).squeeze(1)
                    out_scores.append(float(gathered.sum().item()))
                    del pred, log_probs, gathered
                del enc, out, logits_view
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            return out_scores
        finally:
            tok.padding_side = original_padding_side

    def _ensure_loaded(self):
        if not self._loaded:
            self.load()


def _backend() -> str:
    return os.environ.get("LLM_BACKEND", "fireworks").strip().lower()


_GLOBAL_LLM = None


def get_llm(cfg=None):
    global _GLOBAL_LLM
    if _GLOBAL_LLM is not None:
        return _GLOBAL_LLM
    if cfg is None:
        cfg = config_from_env()
    if isinstance(cfg, FireworksConfig) and _backend() == "together_chat":
        _GLOBAL_LLM = TogetherChatLLM(cfg)
    elif isinstance(cfg, FireworksConfig):
        _GLOBAL_LLM = FireworksLLM(cfg)
    else:
        _GLOBAL_LLM = LocalLLM(cfg)
    _GLOBAL_LLM.load()
    return _GLOBAL_LLM


def reset_llm():
    global _GLOBAL_LLM
    if _GLOBAL_LLM is not None and isinstance(_GLOBAL_LLM, LocalLLM):
        try:
            import torch
            del _GLOBAL_LLM.model
            del _GLOBAL_LLM.tokenizer
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except Exception:
            pass
    _GLOBAL_LLM = None


def _fireworks_config_from_env() -> FireworksConfig:
    fb_env = os.environ.get("FIREWORKS_FALLBACKS", "").strip()
    fallbacks = (
        [m.strip() for m in fb_env.split(",") if m.strip()]
        if "FIREWORKS_FALLBACKS" in os.environ
        else FireworksConfig().fallback_models
    )
    return FireworksConfig(
        model_name=os.environ.get(
            "FIREWORKS_MODEL", "accounts/fireworks/models/deepseek-v4-flash"),
        fallback_models=fallbacks,
        base_url=os.environ.get(
            "FIREWORKS_BASE_URL", "https://api.fireworks.ai/inference/v1"),
        api_key=os.environ.get("FIREWORKS_API_KEY", "").strip(),
        key_file=os.environ.get("FIREWORKS_KEY_FILE", "firework.txt"),
        max_new_tokens=int(os.environ.get("MAX_NEW_TOKENS", "512")),
        temperature=float(os.environ.get("TEMPERATURE", "0.0")),
        seed=int(os.environ.get("SEED", "1234")),
        reasoning_effort=os.environ.get("FIREWORKS_REASONING_EFFORT", "none"),
        num_workers=int(os.environ.get("FIREWORKS_NUM_WORKERS", "8")),
        max_retries=int(os.environ.get("FIREWORKS_MAX_RETRIES", "6")),
        timeout_s=float(os.environ.get("FIREWORKS_TIMEOUT", "120")),
    )


def _local_config_from_env() -> LLMConfig:
    return LLMConfig(
        model_name=_canonical_model_name(os.environ.get("MODEL_NAME", "Qwen/Qwen3-8B")),
        quantization=os.environ.get("QUANTIZATION", "none"),
        torch_dtype=os.environ.get("TORCH_DTYPE", "bfloat16"),
        max_new_tokens=int(os.environ.get("MAX_NEW_TOKENS", "512")),
        temperature=float(os.environ.get("TEMPERATURE", "0.0")),
        seed=int(os.environ.get("SEED", "1234")),
        enable_thinking=os.environ.get("ENABLE_THINKING", "0") in ("1", "true", "True"),
        hf_cache_dir=os.environ.get("HF_CACHE_DIR") or None,
        hf_token=(os.environ.get("HF_TOKEN", "").strip()
                  or os.environ.get("HUGGING_FACE_HUB_TOKEN", "").strip() or None),
    )


def config_from_env():
    if _backend() == "local":
        return _local_config_from_env()
    return _fireworks_config_from_env()
