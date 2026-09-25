"""Stage 2: hard-term extraction with an LLM (Novita) and a rule-based sanitiser."""

from __future__ import annotations

import json
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import textstat
from wordfreq import zipf_frequency

from config import Config
from core.io import rule

SYSTEM_PROMPT = """You are a clinical-text simplifier's extraction + \
classification stage. Given a clinical note, identify EVERY span a 6th-grade \
reader would likely find hard AND tell the downstream simplifier what to do \
with each.

Return ONLY valid JSON. No markdown fences, no commentary outside JSON.

Schema (one array of objects):
[
  {
    "term": "<exact surface text from the note — preserve case>",
    "kind": "abbreviation" | "word" | "phrase",
    "category": "general_hard_word" | "medical_descriptor" | "medical_essential" \
| "abbreviation_route_unit" | "abbreviation_essential",
    "action": "replace" | "elaborate" | "abbr_expand" | "abbr_expand_elaborate",
    "reason": "<=20 words: why this term is hard>"
  }
]

KIND definitions:
  abbreviation: any short form that needs expansion.
    Examples: COPD, IV, mg, mmHg, pt, sob, EKG, BMI, NPO, BID, CHF, AFib, AAA, CMO.
  word: a SINGLE English word too formal / too jargon for a 6th grader.
    Examples: exacerbation, commenced, ambulating, splenectomy, hospice, extensively.
  phrase: a multi-word term that acts as one concept.
    Examples: atrial fibrillation, bone marrow transplant, low blood pressure, \
acute exacerbation.

CATEGORY -> ACTION (must match):
  general_hard_word        -> replace
  medical_descriptor       -> replace
  medical_essential        -> elaborate
  abbreviation_route_unit  -> abbr_expand
  abbreviation_essential   -> abbr_expand_elaborate

CATEGORY definitions:
  general_hard_word: formal / rare English with an easier everyday equivalent.
        Examples: commenced, advised, elevate, persisted, prompted evaluation, \
necessitating, concomitant, utilize, prior to, ascertain, extensively, ambulating.
  medical_descriptor: medical word describing a STATE, change, symptom, or \
finding (NOT a named diagnosis / drug / procedure).
    Examples: acute, exacerbation, dyspnea, pyrexia, edema, tachycardia, \
purulent, hypotension, antihypertensive.
  medical_essential: a NAMED diagnosis, drug, procedure, body part, test, or \
organism the patient will see / hear again.
    Examples: pneumonia, COPD, hypertension, Augmentin, cholecystectomy, MRI, \
atrial fibrillation, lipase, troponin, lymphoma, splenectomy.
  abbreviation_route_unit: route, frequency, or unit abbreviations.
    Examples: IV, IM, PO, BID, PRN, mg, mmHg, mL, U/L, q6h.
  abbreviation_essential: essential medical abbreviations the patient should \
learn.
    Examples: COPD, MRI, CT, MI, CHF, ECG, EKG, HbA1c, CXR, BMP, STEMI, AAA, \
AFib, CMO, ICU, ED, SBP, DBP.

SKIP — do NOT include these:
- Function words: the, a, an, is, are, was, were, of, to, for, on, in, at, by, \
from, with, and, or.
- Pronouns: she, he, they, you, we, her, his, their, our.
- Basic body parts (heart, lung, blood, skin, arm, leg, head, hand, foot, neck, \
face) UNLESS they're part of a HARD phrase.
- Morphological variants any 6th grader knows by morphology: worsening, \
increased, decreased, improved, started, presenting, ordered, held, consulted, \
admitted, transferred, monitored.
- Generic time / quantity words: days, weeks, morning, tomorrow, year-old, age, \
history.
- MIMIC anonymization placeholders: any token that appears inside `[** ... **]` \
or remnants of it ("Known lastname", "Known firstname", "Hospital1", "Company \
191", "Location 123", numeric IDs attached to placeholders). Skip these \
entirely.
- Typos that aren't real words (e.g. "monitering" — typo of "monitoring"). The \
simplifier will copy them through.
- Plain numbers / dosages / units used as values (e.g. "210", "16-31"). The \
number itself isn't a hard term.

GROUPING rules (CRITICAL):
- Do not overlook formal non-medical verbs or verb phrases around the medical
    terms. Include spans such as "advised", "elevate", "persisted", and
    "prompted evaluation" when a 6th grader would use "told", "raise",
    "stayed", or "led doctors to check" instead.
- Treat 2-3 word units as ONE term when they act as a single concept: \
"acute exacerbation", "atrial fibrillation", "myocardial infarction", \
"bone marrow transplant", "type 2 diabetes mellitus", "spontaneous rupture of \
membranes".
- If a treatment phrase combines a route / descriptor + drug, output the \
WHOLE PHRASE as one term (kind="phrase", category="medical_essential"):
    "IV augmentin"         -> one term
    "nebulized albuterol"  -> one term
    "supplemental O2"      -> one term
  Do NOT additionally output "IV" or "nebulized" or "supplemental" on their own.
- Each surface span in the note appears AT MOST ONCE in your output.
"""

USER_TEMPLATE = """Clinical note:
\"\"\"
{note}
\"\"\"

Return the JSON array now."""

VALID_ACTIONS = {
    "general_hard_word": "replace",
    "medical_descriptor": "replace",
    "medical_essential": "elaborate",
    "abbreviation_route_unit": "abbr_expand",
    "abbreviation_essential": "abbr_expand_elaborate",
}
VALID_KINDS = {"abbreviation", "word", "phrase"}


_LEGIT_ABBREV_RE = re.compile(
    r"^[A-Za-z]{1,6}$"
    r"|^[A-Za-z]{1,4}(?:[/.\-][A-Za-z]{0,4})+$"
    r"|^[A-Za-z]{1,3}\d+[A-Za-z]?$"
    r"|^[A-Za-z]{1,5}\d[A-Za-z]*$"
)

_MEDICAL_SUFFIXES = (
    "ectomy", "otomy", "ostomy", "scopy", "plasty", "tripsy",
    "itis", "osis", "emia", "uria", "algia", "pathy", "trophy",
    "rrhea", "rrhage", "rrhagia", "phobia", "pnea", "spasm",
    "logy", "logist", "graphy", "gram", "centesis", "lysis",
    "surgery", "transplant",
)

_MORPHOLOGICAL_SKIP = {
    "worsening", "worsened", "worsens", "increased", "increases", "increasing",
    "decreased", "decreases", "decreasing", "improved", "improving", "improves",
    "started", "starting", "starts", "presented", "presenting", "presents",
    "ordered", "ordering", "orders", "held", "holding", "holds",
    "consulted", "consulting", "consults", "admitted", "admitting", "admits",
    "transferred", "transferring", "transfers", "monitored", "monitoring",
    "monitors", "received", "receiving", "receives", "noted", "noting", "notes",
    "continued", "continues", "discharged", "discharging", "tolerating",
    "tolerated", "stable",
}

_GENERAL_HARD_WORDS_NOT_MEDICAL = {
    "extensively", "extensive", "concomitant", "concomitantly",
    "subsequently", "subsequent", "commenced", "utilize", "utilization",
    "ascertain", "comorbidity", "comorbidities", "comprises", "comprised",
    "ambulating", "ambulation",
}


def _detect_input_casing(term: str, note_text: str) -> str:
    if not term or not note_text:
        return term
    m = re.search(r"\b" + re.escape(term.lower()) + r"\b", note_text.lower())
    return note_text[m.start():m.end()] if m else term


def sanity_fix(rec: Dict[str, Any], note_text: str
               ) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    rec = dict(rec)
    term_raw = (rec.get("term") or "").strip()
    if not term_raw:
        return None, "empty term"

    term_lc = term_raw.lower()
    fixed = _detect_input_casing(term_raw, note_text)
    rec["term"] = fixed
    notes: List[str] = []
    if fixed != term_raw:
        notes.append(f"casing: {term_raw!r} -> {fixed!r}")

    if term_lc in _MORPHOLOGICAL_SKIP:
        return None, f"morphological variant {term_raw!r} — a 6th-grader knows it"

    if rec.get("kind") == "abbreviation":
        looks_abbr = bool(_LEGIT_ABBREV_RE.match(term_raw))
        has_suffix = any(term_lc.endswith(s) for s in _MEDICAL_SUFFIXES)
        long_lower = len(term_raw) > 6 and term_raw.isalpha() and not term_raw.isupper()
        if has_suffix or long_lower or not looks_abbr:
            rec["kind"] = "phrase" if " " in fixed else "word"
            if has_suffix:
                rec["category"], rec["action"] = "medical_essential", "elaborate"
                notes.append(f"abbr->medical_essential ({fixed!r} has a medical suffix)")
            else:
                rec["category"], rec["action"] = "general_hard_word", "replace"
                notes.append(f"abbr->general_hard_word ({fixed!r} is a full word)")

    if (rec.get("category") == "medical_essential"
            and term_lc in _GENERAL_HARD_WORDS_NOT_MEDICAL):
        rec["category"], rec["action"] = "general_hard_word", "replace"
        notes.append(f"medical_essential->general_hard_word ({fixed!r} is formal English)")

    return rec, ("; ".join(notes) if notes else None)


def validate(rec: Dict[str, Any]) -> List[str]:
    errs = []
    if not isinstance(rec, dict):
        return ["record is not an object"]
    for k in ("term", "kind", "category", "action"):
        if k not in rec:
            errs.append(f"missing field {k!r}")
    if rec.get("kind") and rec["kind"] not in VALID_KINDS:
        errs.append(f"invalid kind {rec['kind']!r}")
    cat, act = rec.get("category", ""), rec.get("action", "")
    if cat and cat not in VALID_ACTIONS:
        errs.append(f"invalid category {cat!r}")
    elif cat and act != VALID_ACTIONS[cat]:
        errs.append(f"action {act!r} does not match category {cat!r}")
    return errs


def dedupe(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    by_term: Dict[str, Dict[str, Any]] = {}
    for it in items:
        t = (it.get("term") or "").strip().lower()
        if t and t not in by_term:
            by_term[t] = it
    kept: List[str] = []
    for t in sorted(by_term, key=len, reverse=True):
        tw = re.findall(r"\w[\w'-]*", t)
        inside = False
        for k in kept:
            kw = re.findall(r"\w[\w'-]*", k.lower())
            if len(tw) < len(kw):
                for i in range(len(kw) - len(tw) + 1):
                    if kw[i:i + len(tw)] == tw:
                        inside = True
                        break
            if inside:
                break
        if not inside:
            kept.append(by_term[t]["term"])
    return [by_term[k.lower()] for k in kept]


_ABBREV_LIKE = re.compile(
    r"^[A-Za-z]{1,4}(?:[/.\-][A-Za-z]{0,4})+$"
    r"|^[A-Za-z]{1,3}\d+[A-Za-z]?$"
    r"|^[A-Z]{2,}$"
)


def lex_features(text: str, aoa: Dict[str, Any]) -> Dict[str, Any]:
    t = (text or "").strip()
    if not t:
        return {"zipf": None, "aoa": None, "syllables": 0, "n_words": 0,
                "is_abbreviation": False}
    is_abbr = bool(_ABBREV_LIKE.match(t))
    tokens = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9'-]*", t) if w]
    if is_abbr:
        phrase_zipf, tok_z = None, []
    else:
        phrase_zipf = round(zipf_frequency(t.lower(), "en"), 2)
        tok_z = [zipf_frequency(w.lower(), "en") for w in tokens
                 if not _ABBREV_LIKE.match(w)]
    aoa_vals = [aoa.get(w.lower(), {}).get("aoa") for w in tokens]
    aoa_vals = [a for a in aoa_vals if a is not None]
    return {
        "zipf": phrase_zipf,
        "min_token_zipf": round(min(tok_z), 2) if tok_z else None,
        "aoa": round(max(aoa_vals), 2) if aoa_vals else None,
        "syllables": textstat.syllable_count(t),
        "n_words": len(tokens),
        "is_abbreviation": is_abbr,
    }


def load_aoa(path: Path) -> Dict[str, Any]:
    if not path.exists():
        print(f"  [warn] AoA file not found at {path} - AoA features disabled.")
        return {}
    import pandas as pd
    df = pd.read_csv(path)
    cols = {c.lower(): c for c in df.columns}
    word_col = cols.get("word") or cols.get("lemma") or df.columns[0]
    aoa_col = (cols.get("aoa_kup") or cols.get("aoa_kup_lem")
               or next((cols[c] for c in cols if "rating" in c and "mean" in c), None)
               or cols.get("aoa"))
    if aoa_col is None:
        print(f"  [warn] no AoA column in {list(df.columns)} - disabled.")
        return {}
    df = df[[word_col, aoa_col]].dropna()
    out: Dict[str, Any] = {}
    for w, a in zip(df[word_col], df[aoa_col]):
        k = str(w).lower()
        if k not in out:
            out[k] = {"aoa": float(a)}
    return out


_MIMIC_BRACKET_RE = re.compile(r"\[\s*\*+\s*([^*\[\]]*?)\s*\*+\s*\]", re.IGNORECASE)
_MIMIC_REMNANTS = [
    (re.compile(r"\b(?:known\s+)?(?:last|first|middle)\s*name\s*\d*\b", re.I), "the patient"),
    (re.compile(r"\bnamepattern\s*\d*\b", re.I), "the patient"),
    (re.compile(r"\bhospital\s*\d+\b", re.I), "the hospital"),
    (re.compile(r"\b(?:location|company|address|ward|country)\s*\d+\b", re.I), "this place"),
    (re.compile(r"\b(?:doctor|provider|md)\s*(?:first|last)?\s*name\s*\d*\b", re.I), "the doctor"),
    (re.compile(r"\b(?:doctor|provider)\s*\d+\b", re.I), "the doctor"),
    (re.compile(r"\b(?:telephone|phone|fax|pager)\s*\d+\b", re.I), ""),
    (re.compile(r"\b(?:numeric\s+identifier|medical\s+record\s+number|mrn)\s*\d+\b", re.I), ""),
]


def _bracket_sub(m: "re.Match[str]") -> str:
    c = (m.group(1) or "").strip().lower()
    if "doctor" in c or "md number" in c or "provider" in c:
        return "the doctor"
    if any(k in c for k in ("lastname", "firstname", "middlename", "last name",
                            "first name", "middle name", "name pattern",
                            "namepattern", "initial")):
        return "the patient"
    if "hospital" in c or "company" in c:
        return "the hospital"
    if any(k in c for k in ("location", "address", "country", "state", "city", "ward")):
        return "this place"
    return ""


def strip_mimic(text: str) -> str:
    text = _MIMIC_BRACKET_RE.sub(_bracket_sub, text)
    for pat, rep in _MIMIC_REMNANTS:
        text = pat.sub(rep, text)
    text = re.sub(r"\b(?:a|an|the)\s+(the\s+)", r"\1", text, flags=re.I)
    return re.sub(r"\s+", " ", text).strip()


def _strip_fences(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\s*", "", t)
        t = re.sub(r"```\s*$", "", t).strip()
    return t


def _parse_json(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    m = re.search(r"\[\s*(?:{.*?}\s*,?\s*)*\]", text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass
    return None


def _call(client, note: str, model: str, temperature: float,
          max_tokens: int, cache_tag: str = "extract"
          ) -> Tuple[Optional[list], str]:
    from core import cache as cache_mod
    cache = cache_mod.get_cache()
    prompt = SYSTEM_PROMPT + "\x00" + USER_TEMPLATE.format(note=note)
    key = cache.make_key(cache_tag, f"{model}@{temperature}", prompt)
    hit = cache.get(key)
    if hit is not None:
        raw = hit.get("raw", "")
        return _parse_json(_strip_fences(raw)), raw

    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": SYSTEM_PROMPT},
                  {"role": "user", "content": USER_TEMPLATE.format(note=note)}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    raw = resp.choices[0].message.content or ""
    parsed = _parse_json(_strip_fences(raw))
    if parsed is None and not _strip_fences(raw).rstrip().endswith("]"):
        bigger = min(max_tokens * 2, 16384)
        if bigger > max_tokens:
            print(f"      [truncated at {max_tokens} tokens] retrying with {bigger}")
            return _call(client, note, model, temperature, bigger, cache_tag)
    if parsed is not None:
        cache.put(key, {"raw": raw})
    return parsed, raw


def _records_to_items(parsed: Any, text: str, aoa: Dict[str, Any]):
    errors: List[str] = []
    items: List[Dict[str, Any]] = []
    audit: List[str] = []
    if not isinstance(parsed, list):
        errors.append("model did not return a JSON array")
        return items, audit, errors

    kept = []
    for rec in dedupe(parsed):
        fixed, msg = sanity_fix(rec, text)
        if fixed is None:
            audit.append(f"DROP {rec.get('term','?')!r}: {msg}")
            continue
        if msg:
            audit.append(f"FIX  {fixed.get('term','?')!r}: {msg}")
        kept.append(fixed)
    for j, rec in enumerate(kept):
        errs = validate(rec)
        if errs:
            errors.append(f"item {j}: {', '.join(errs)}")
            continue
        items.append({
            "text": rec["term"],
            "kind": rec["kind"],
            "category": rec["category"],
            "action": rec["action"],
            "reason": rec.get("reason", ""),
            "features": lex_features(rec["term"], aoa),
            "origin": "extracted",
        })
    return items, audit, errors


def term_jaccard(a: List[Dict[str, Any]], b: List[Dict[str, Any]]
                 ) -> Optional[float]:
    sa = {(it.get("text") or "").strip().lower() for it in a if it.get("text")}
    sb = {(it.get("text") or "").strip().lower() for it in b if it.get("text")}
    if not sa and not sb:
        return None
    return round(len(sa & sb) / len(sa | sb), 4)


def add_stability(cfg: Config, notes: List[Dict[str, Any]]
                  ) -> List[Dict[str, Any]]:
    from openai import OpenAI

    client = OpenAI(api_key=cfg.api_key("novita"),
                    base_url=cfg.novita_base_url, timeout=180)
    aoa = load_aoa(cfg.root / "data" / "en.aoa.csv")
    model = cfg.extract_models[0]
    for note in notes:
        if note.get("extraction_stability") is not None:
            continue
        items = note.get("hard_items") or []
        text = note.get("original_clean") or strip_mimic(note["original"])
        parsed, _ = _call(client, text, model, cfg.extract_temperature,
                          cfg.extract_max_tokens, cache_tag="extract-replicate")
        rep_items, _, _ = _records_to_items(parsed, text, aoa)
        jac = term_jaccard([i for i in items
                            if (i.get("origin") or "extracted") == "extracted"],
                           rep_items)
        note["extraction_stability"] = jac
        note.setdefault("extraction", {})["replicate_terms"] = [
            i["text"] for i in rep_items]
        print(f"    note {note.get('note_idx')}  stability Jaccard {jac}")
    vals = [n["extraction_stability"] for n in notes
            if isinstance(n.get("extraction_stability"), (int, float))]
    if vals:
        print(f"  mean extraction stability: {sum(vals) / len(vals):.4f} "
              f"over {len(vals)} notes")
    return notes


def run(cfg: Config, notes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    from openai import OpenAI

    client = OpenAI(api_key=cfg.api_key("novita"),
                    base_url=cfg.novita_base_url, timeout=180)
    aoa = load_aoa(cfg.root / "data" / "en.aoa.csv")
    print(f"  AoA table            : {len(aoa)} entries")
    print(f"  extraction model     : {cfg.extract_models[0]}")

    model = cfg.extract_models[0]
    for note in notes:
        text = strip_mimic(note["original"])
        note["original_clean"] = text
        rule(f"note {note['note_idx']}  ({note.get('id')})")
        print(f"    {text}")

        t0 = time.time()
        parsed, raw = _call(client, text, model, cfg.extract_temperature,
                            cfg.extract_max_tokens)
        elapsed = round(time.time() - t0, 2)

        errors: List[str] = []
        items: List[Dict[str, Any]] = []
        audit: List[str] = []
        items, audit, errors = _records_to_items(parsed, text, aoa)

        note["hard_items"] = items
        note["extraction"] = {
            "model": model, "elapsed_s": elapsed,
            "n_items": len(items), "sanitiser_audit": audit,
            "errors": errors, "raw": raw,
        }

        if getattr(cfg, "measure_extraction_stability", False):
            rep_parsed, _ = _call(client, text, model, cfg.extract_temperature,
                                  cfg.extract_max_tokens,
                                  cache_tag="extract-replicate")
            rep_items, _, _ = _records_to_items(rep_parsed, text, aoa)
            jac = term_jaccard(items, rep_items)
            note["extraction_stability"] = jac
            note["extraction"]["replicate_terms"] = [i["text"] for i in rep_items]
            if jac is not None:
                print(f"    stability (2nd extraction): Jaccard {jac}")

        if items:
            print(f"    {'term':<32}{'kind':<13}{'category':<24}"
                  f"{'action':<24}{'zipf':>6}{'aoa':>6}")
            for it in items:
                f = it["features"]
                z = f"{f['zipf']:.2f}" if f["zipf"] is not None else "-"
                a = f"{f['aoa']:.1f}" if f["aoa"] is not None else "-"
                print(f"    {it['text'][:31]:<32}{it['kind']:<13}"
                      f"{it['category']:<24}{it['action']:<24}{z:>6}{a:>6}")
        else:
            print("    (no hard terms accepted)")
        for line in audit:
            print(f"      sanitiser: {line}")
        for e in errors:
            print(f"      [schema] {e}")

    return notes
