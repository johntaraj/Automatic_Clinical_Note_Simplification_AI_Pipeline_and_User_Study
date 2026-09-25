"""Stage 4: generation for the three arms and edit tagging; Stage 5: ContextCite on the
grounded arm.
"""

from __future__ import annotations

import re
import time
from typing import Any, Callable, Dict, List, Optional

from config import Config, ModelSpec
from core.contextcite import contextcite_note, format_result
from core.io import rule
from core.llm import FireworksConfig, FireworksLLM, TogetherChatLLM
from core.validity import output_problems
from stages import prompts as P
from stages.tagging import (
    extract_operations, filter_operations, retag_prose, tag_input,
)

ARM_SPECS = {
    "naive":    {"terms": False, "glossary": False, "contextcite": False},
    "termonly": {"terms": True,  "glossary": False, "contextcite": False},
    "grounded": {"terms": True,  "glossary": True,  "contextcite": True},
}


def make_llm(cfg: Config, spec: ModelSpec, require_echo: bool):
    from config import PROVIDER_BASE_URL
    keys = cfg.api_keys(spec.provider)
    fw = FireworksConfig(
        model_name=spec.model_id,
        fallback_models=[],
        base_url=PROVIDER_BASE_URL[spec.provider],
        api_key=keys[0],
        api_keys=keys[1:],
        max_new_tokens=spec.max_new_tokens or cfg.max_new_tokens,
        temperature=cfg.temperature,
        seed=cfg.seed,
        reasoning_effort=spec.reasoning_effort,
        num_workers=spec.num_workers,
        require_echo=require_echo,
    )
    llm = TogetherChatLLM(fw) if spec.backend == "together_chat" else FireworksLLM(fw)
    llm.load()
    return llm


_NOVITA_CLIENT = None


def _novita_annotate(cfg: Config, original: str, prose: str,
                     hard_terms: List[str]) -> str:
    global _NOVITA_CLIENT
    from core.cache import get_cache
    cache = get_cache()
    system, user = P.TAG_WRAP_SYSTEM, P.build_tag_wrap_user(
        original, prose, hard_terms)
    key = cache.make_key("annotate", f"{cfg.tagger_model}@0.0",
                         system + "\x00" + user)
    hit = cache.get(key)
    if isinstance(hit, str) and hit.strip():
        return hit

    if _NOVITA_CLIENT is None:
        from openai import OpenAI
        _NOVITA_CLIENT = OpenAI(api_key=cfg.api_key("novita"),
                                base_url=cfg.novita_base_url, timeout=180)
    resp = _NOVITA_CLIENT.chat.completions.create(
        model=cfg.tagger_model,
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": user}],
        temperature=0.0,
        max_tokens=cfg.max_new_tokens,
        extra_body={"enable_thinking": False, "reasoning_effort": "none"},
    )
    text = resp.choices[0].message.content or ""
    if "</think>" in text:
        text = text.split("</think>")[-1]
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    text = re.sub(r"^```[a-zA-Z]*\s*|```\s*$", "", text.strip())
    text = text.strip()
    if not text:
        raise RuntimeError("Novita annotator returned empty content")
    cache.put(key, text)
    return text


def _tagged_line(text: str) -> str:
    lines = [ln.strip() for ln in (text or "").splitlines() if ln.strip()]
    for ln in lines:
        if "</replace>" in ln or "</elaborate>" in ln or "</abbr>" in ln:
            return ln
    return lines[0] if lines else ""


def _first_line(text: str) -> str:
    for line in (text or "").splitlines():
        if line.strip():
            return line.strip()
    return ""


def generate_arm(cfg: Config, llm, arm: str, note: Dict[str, Any],
                 verbose: bool = True, attribute: bool = True) -> Dict[str, Any]:
    spec = ARM_SPECS[arm]
    sentence = note.get("original_clean") or note["original"]
    all_items = note.get("hard_items", [])
    hard_items = all_items if spec["terms"] else []
    sources = note.get("sources", []) if spec["glossary"] else []
    prompt_items = [it for it in hard_items
                    if (it.get("origin") or "extracted") == "extracted"]
    hard_terms = []
    seen = set()
    for it in hard_items:
        t = (it.get("text") or "").strip()
        if t and t.lower() not in seen:
            seen.add(t.lower())
            hard_terms.append(t)

    system = (P.naive_system(cfg.person_policy, sentence) if arm == "naive"
              else P.simplifier_system(cfg.prompt_style, cfg.tag_policy,
                                       cfg.person_policy, sentence))

    def build_prompt(active_sources: List[Dict[str, Any]]) -> str:
        if arm == "naive":
            user = f"Sentence: {sentence}\n\nRewrite the sentence now."
        else:
            user = P.build_simplify_user(sentence, prompt_items, active_sources,
                                         cfg.tag_policy, spec["glossary"],
                                         cfg.keep_gloss_scope)
        rendered = llm.apply_chat_template([
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ])
        if cfg.think_prefill and getattr(llm, "uses_text_completions", False):
            rendered += cfg.think_prefill
        return rendered

    t0 = time.time()
    prompt = build_prompt(sources)
    gen_error = None
    raw = ""
    attempts_used = 0
    problems: List[str] = []
    temps = cfg.retry_temperatures or [cfg.temperature]
    for attempt in range(max(1, cfg.max_generation_attempts)):
        attempts_used = attempt + 1
        temp = temps[attempt] if attempt < len(temps) else temps[-1]
        try:
            raw = llm.complete(prompt, max_new_tokens=llm.cfg.max_new_tokens,
                               temperature=temp, attempt=attempt)
            gen_error = None
        except Exception as e:
            raw = ""
            gen_error = f"{type(e).__name__}: {e}"
        problems = output_problems(_first_line(raw))
        if not problems:
            break
        if verbose and attempt + 1 < max(1, cfg.max_generation_attempts):
            print(f"      {arm:<9} attempt {attempts_used} unusable "
                  f"({', '.join(problems)}) - retrying at temperature "
                  f"{temps[min(attempt + 1, len(temps) - 1)]}")
    prose = _first_line(raw)
    gen_s = round(time.time() - t0, 2)

    record: Dict[str, Any] = {
        "arm": arm,
        "output": prose,
        "raw": raw,
        "gen_seconds": gen_s,
        "n_sources_shown": len(sources),
        "operations": [],
        "tagged": prose,
        "annotation": {},
        "generation_attempts": attempts_used,
        "output_problems": problems,
    }
    if gen_error:
        record["generation_error"] = gen_error
    if verbose:
        if gen_error:
            print(f"      {arm:<9} ({gen_s:>5.1f}s) GENERATION FAILED: {gen_error}")
        else:
            suffix = (f"   [UNUSABLE after {attempts_used}: "
                      f"{', '.join(problems)}]" if problems else
                      (f"   [ok on attempt {attempts_used}]"
                       if attempts_used > 1 else ""))
            print(f"      {arm:<9} ({gen_s:>5.1f}s, {len(sources)} sources): "
                  f"{prose}{suffix}")

    if not prose or not hard_terms:
        return record

    backend = cfg.tagger_backend
    tagged_raw = ""
    try:
        if backend == "novita":
            tagged_raw = _novita_annotate(cfg, sentence, prose, hard_terms)
        else:
            raise RuntimeError("same-model tagger requested")
    except Exception as e:
        if backend == "novita" and verbose:
            print(f"        [annotate] Novita failed ({type(e).__name__}) - "
                  f"falling back to the simplifier model")
        backend = "same-fallback"
        try:
            tag_prompt = llm.apply_chat_template([
                {"role": "system", "content": P.TAG_WRAP_SYSTEM},
                {"role": "user", "content": P.build_tag_wrap_user(
                    sentence, prose, hard_terms)},
            ])
            tagged_raw = llm.complete(tag_prompt,
                                      max_new_tokens=llm.cfg.max_new_tokens,
                                      temperature=0.0)
        except Exception as e2:
            backend = "failed"
            tagged_raw = ""
            if verbose:
                print(f"        [annotate] fallback tagger also failed "
                      f"({type(e2).__name__}: {e2}) - 0 edits for this arm")

    ops, _ = extract_operations(_tagged_line(tagged_raw))
    ops, audit = filter_operations(ops, sentence, prose, hard_terms)
    ops, tagged = retag_prose(prose, ops)

    record["operations"] = ops
    record["tagged"] = tagged
    record["annotation"] = {
        "backend": backend,
        "n_ops": len(ops),
        "dropped": audit,
        "mapped_terms": [o.get("src_text") for o in ops],
        "raw": tagged_raw,
    }
    if verbose:
        print(f"        edits: {len(ops)}"
              + (f"   ({len(audit)} annotations rejected)" if audit else ""))
        for line in audit:
            print(f"          {line}")

    if spec["contextcite"] and cfg.cc_enabled and attribute and sources and ops:
        _attribute(cfg, llm, build_prompt, sources, prose, ops, verbose)
    elif spec["contextcite"] and cfg.cc_enabled and not attribute and verbose:
        print("        (attribution skipped for this note -- cc_max_notes)")

    return record


def _attribute(cfg: Config, llm, build_prompt: Callable, sources: List[Dict[str, Any]],
               prose: str, ops: List[Dict[str, Any]], verbose: bool) -> None:
    spans = [tuple(op["span_plain"]) for op in ops]
    if verbose:
        for op in ops:
            print(f"        * contextcite  {op.get('src_text')!r} -> "
                  f"{op.get('tgt_text')!r}")
    results = contextcite_note(
        llm=llm,
        sources=sources,
        build_prompt=build_prompt,
        response=prose,
        spans=spans,
        num_ablations=cfg.cc_num_ablations,
        heldout_ablations=cfg.cc_heldout_ablations,
        lambd=cfg.cc_lambda,
        seed=cfg.cc_seed,
        top_k=cfg.cc_topk,
        score_topk_masks=cfg.cc_score_topk_masks,
        leave_one_out=cfg.cc_leave_one_out,
    )
    for op, result in zip(ops, results):
        op["contextcite"] = result.as_dict()
        op["top_sources"] = result.ranked_sources(k=5)
        if verbose:
            print(format_result(result))


def run(cfg: Config, notes: List[Dict[str, Any]], model_key: str,
        checkpoint: Optional[Callable[[List[Dict[str, Any]]], None]] = None
        ) -> List[Dict[str, Any]]:
    spec = cfg.model_spec(model_key)
    cc_wanted = cfg.cc_enabled and "grounded" in cfg.arms
    need_echo = cc_wanted and spec.contextcite
    if cc_wanted and not spec.contextcite:
        print(f"  [info] ContextCite disabled for {spec.slug}: {spec.note}")

    llm = make_llm(cfg, spec, require_echo=need_echo)
    active_cc = need_echo
    if active_cc and cfg.cc_max_notes:
        print(f"  [info] ContextCite limited to the first {cfg.cc_max_notes} "
              f"notes (cc_max_notes); all notes still get generation and every "
              f"non-attribution metric.")

    done = sum(1 for n in notes if n.get("arms"))
    if done:
        print(f"  [resume] {done}/{len(notes)} notes already generated; "
              f"continuing from note {done + 1}.")

    for note in notes:
        if note.get("arms"):
            continue
        rule(f"note {note['note_idx']}  ({note.get('id')})")
        sentence = note.get("original_clean") or note["original"]
        print(f"      input    : {sentence}")
        print(f"      reference: {note.get('reference', '')}")
        terms = [it.get("text", "") for it in note.get("hard_items", [])]
        print(f"      tagged   : {tag_input(sentence, terms)}")

        attribute = active_cc and (
            not cfg.cc_max_notes or note["note_idx"] <= cfg.cc_max_notes)

        arms: Dict[str, Any] = {}
        for arm in cfg.arms:
            if arm not in ARM_SPECS:
                raise SystemExit(f"[generate] unknown arm {arm!r}")
            cfg_for_arm = cfg if active_cc else _cfg_without_cc(cfg)
            arms[arm] = generate_arm(cfg_for_arm, llm, arm, note,
                                     attribute=attribute)
        note["arms"] = arms
        if checkpoint:
            checkpoint(notes)

    return notes


def _cfg_without_cc(cfg: Config) -> Config:
    import copy
    c = copy.copy(cfg)
    c.cc_enabled = False
    return c
