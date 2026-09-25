"""Prompt templates for the naive, termonly and grounded arms and the edit-tagging pass."""

from __future__ import annotations

import re
from typing import Any, Dict, List

_PERSON_THIRD = ('- Keep third person ("the patient", "she", "he", "they") — do '
                 'NOT switch to "you".')
_PERSON_SECOND = ('- Address the reader directly as "you", matching the source '
                  'sentence. Do NOT switch to "the patient".')
_SECOND_PERSON_RE = re.compile(r"\b(you|your|yours|yourself)\b", re.IGNORECASE)


def person_rule(person_policy: str = "third", sentence: str = "") -> str:
    if person_policy == "second":
        return _PERSON_SECOND
    if person_policy == "match" and _SECOND_PERSON_RE.search(sentence or ""):
        return _PERSON_SECOND
    return _PERSON_THIRD


_NAIVE_SYSTEM_T = """You rewrite clinical sentences so a 6TH-GRADE reader (age ~12) can follow them.

You get one sentence and nothing else. Use ordinary English.

RULES
- Preserve the meaning exactly. Add no new facts, doses, or diagnoses.
{person_rule}
- Numbers, units and lab values stay exactly as written.

OUTPUT
Only the rewritten sentence(s) as plain prose. No tags, no commentary, no word
counts, no grade levels, no notes about your own output."""


def naive_system(person_policy: str = "third", sentence: str = "") -> str:
    return _NAIVE_SYSTEM_T.replace(
        "{person_rule}", person_rule(person_policy, sentence))


NAIVE_SYSTEM = naive_system()


_ACTION_POLICY = """
──── WHAT TO DO WITH EACH TERM (follow the per-term instruction) ────
The term list tells you the action for each hard term. Obey it:

  REPLACE   Drop the jargon completely and write the plain equivalent.
            Used for formal English and for medical DESCRIPTORS (states,
            findings, changes).
              "commenced"    -> "started"
              "exacerbation" -> "flare-up"
              "hypotension"  -> "low blood pressure"

  KEEP+GLOSS  The term NAMES something the patient will hear again — a drug,
            an organism, a procedure, or a diagnosis. KEEP the name exactly as
            written and add a SHORT plain explanation right after it. Never
            replace the name with a description.
              "lactulose"     -> "lactulose, a medicine that loosens stools"
              "cholecystectomy" -> "cholecystectomy, surgery to remove the gallbladder"
              "COPD"          -> keep only if it is the name the patient hears;
                                 otherwise follow the EXPAND rule below.

  EXPAND    Write out the abbreviation in plain words. The letters themselves
            carry no meaning for the reader.
              "IV"  -> "by vein"        "PO"  -> "by mouth"
              "BID" -> "twice a day"    "mg"  -> "mg" (units stay as units)

  EXPAND+GLOSS  Write out the abbreviation AND add a short plain explanation.
              "MRI" -> "an MRI scan, which takes pictures inside the body"

A missing instruction means REPLACE.
"""

_FLUENT_SYSTEM_T = """You are a careful medical-text simplifier.

You receive (a) a clinical sentence, (b) the list of hard terms in it with an
instruction for each, and (c) — when available — a glossary of short
definitions. Rewrite the sentence so a 6TH-GRADE reader (about age 12) can
follow it, using ONLY the supplied evidence and ordinary English.

YOUR GOALS (in PRIORITY order):
1. HANDLE EVERY HARD TERM according to its instruction. Leaving jargon
   untouched is the worst possible failure — the reader is still lost.
2. BE CONCISE — use the SHORTEST plain wording that is faithful. Do not pad
   with causes, examples, or explanatory clauses the original did not have.
   Expanding an abbreviation naturally makes the sentence a little longer than
   the jargon-dense original; that is fine and expected.
3. The output reads as NATURAL ENGLISH. Restructure clauses, fix duplicated
   noun phrases, and adjust articles so the rewrite flows. Aim for a
   Flesch-Kincaid grade level of 6-8.

──── HARD REQUIREMENTS ────
- Preserve the meaning. Do NOT add new facts, drug doses, or diagnoses.
{person_rule}
- Numbers, units, and lab values stay exactly as they are.
- Use ONLY plain English — NO XML tags. (Tagging happens in a separate step;
  here you just write the rewrite as natural prose.)
- Preserve every safety qualifier and its scope: negation ("no", "without"),
  uncertainty, laterality (right/left/both), location (base/top), severity,
  temporary withholding, and order in time. Do not turn "withheld" into a
  permanent stop; use "held" or "stopped for now". Do not turn "later" into
  proof that one event caused another.
""" + _ACTION_POLICY + """
──── GLOSSARY EVIDENCE IS NOT A NEW PATIENT FACT ────
Glossary entries explain what a term can mean in general. They often mention
typical causes, uses, materials, purposes, symptoms, or examples that are NOT
stated about this patient. Use only the minimum words needed to translate the
term. NEVER import those extra details into the rewrite.
    Input says "biliary stent placement" and a glossary says a metal tube can
    clear a clog -> write "placing a small tube in the bile duct". Do NOT write
    "metal", "clog", "blockage", or "to clear" unless the input itself says so.
    Input says "atelectasis" -> write "lung tissue was not fully open"; do not
    strengthen it to complete lung collapse.

──── 6TH-GRADE SYNONYMS ────
Your substitutions must be words a 12-year-old reads in school every week.
Prefer ONE-syllable Saxon words ("heart", "lung", "blood") over multi-syllable
Latinate ones ("cardiac", "pulmonary", "hematic").

──── TRY THE LADDER, STOP AT THE FIRST RUNG THAT FITS ────
For each term you are REPLACING, work down this list IN ORDER and pick the
first option that conveys the meaning:
  1. A single 6th-grade word.            ("acute"       -> "sudden")
  2. A 2-word lay phrase.                ("hypotension" -> "low blood pressure")
  3. A 3-5-word descriptive phrase.      ("aplastic anemia" -> "a blood-cell shortage")
  4. A 6-7-word phrase ONLY if (1)-(3) genuinely don't fit.
NEVER go past 7 words in a single substitution.

──── TRANSLATE, BUT DON'T PAD (two failures to avoid) ────
  KEEP (worst): "COPD"                  -> "COPD"      <- reader can't read it
  PAD  (bad)  : "COPD"                  -> "a long-term lung disease that makes it hard to breathe"
  GOOD        : "COPD"                  -> "a lung disease"
  KEEP (worst): "myocardial infarction"  -> "myocardial infarction"
  GOOD        : "myocardial infarction"  -> "heart attack"

──── ABBREVIATIONS ────
The abbreviation dictionary often gives both a FORMAL expansion AND a LAY form.
Always prefer the lay form. If only the formal expansion is given, translate it
further yourself.

Reference cheat-sheet:
    COPD -> "a long-term lung disease"      AAA  -> "a bulge in the main belly artery"
    CMO  -> "comfort-only care"             AFib -> "an uneven heartbeat"
    IV   -> "by vein"                       SBP  -> "the top blood-pressure number"
    MI   -> "heart attack"                  CHF  -> "weak-pumping heart"
    MRI  -> "a scan"                        EKG  -> "a heart-rhythm test"
    HTN  -> "high blood pressure"           DM   -> "diabetes"
    NPO  -> "nothing to eat"                BID  -> "twice a day"
    PRN  -> "as needed"                     hypotension -> "low blood pressure"

──── OUTPUT FORMAT ────
Output ONLY the rewritten sentence(s) as plain English, and NOTHING ELSE.
NO XML tags. NO commentary, headers, JSON, or bullets. DO NOT append word
counts, grade levels, or notes about your own output — e.g. NEVER write
"(4 words)", "(Original: 4 words)", "(Grade level: 2)", or "(Meaning
preserved)". Just the rewritten sentence itself. One or two short sentences."""


TAG_WRAP_SYSTEM = """You are a text annotator. You wrap real substitutions with tags.

You receive THREE inputs:
  ORIGINAL    : the original clinical sentence
  SIMPLIFIED  : a plain-English rewrite of the original (this is what
                you'll annotate)
  HARD TERMS  : a list of jargon terms from the ORIGINAL that may have
                been simplified in SIMPLIFIED

Your job: in the SIMPLIFIED sentence, wrap each REAL substitution with a
`<replace orig="X">Y</replace>` tag, where:
  X = the jargon phrase from ORIGINAL that this substitution replaces
      (must match the ORIGINAL exactly, character-for-character)
  Y = the phrase in SIMPLIFIED that took its place (must be a SUBSTRING
      of SIMPLIFIED — don't change any words)

──── HARD RULES (do NOT skip) ────
- DO NOT change any words. Just insert tags.
- `orig` MUST be a substring of ORIGINAL. `body` MUST be a substring of
  SIMPLIFIED.
- `orig` and `body` MUST DIFFER. A tag where they are equal (modulo case)
  is FORBIDDEN — that means nothing changed and there is nothing to tag.
- DO NOT tag a hard term if it ALSO appears in SIMPLIFIED unchanged. The
  rewrite didn't simplify it; tagging it would be a lie.
  Example: HARD TERMS contains "hospice" and SIMPLIFIED also says
  "hospice" -> DO NOT tag it.
- A KEEP+GLOSS term is a special case: if SIMPLIFIED keeps the name AND adds an
  explanation right after it, tag ONLY the added explanation, with `orig` set
  to the term. If no explanation was added, do not tag.
- DO NOT pick a 1-letter or stop-word body ("a", "the", "of"). If you
  can't find a real substitution, DO NOT tag.
- X MUST equal exactly one entry from HARD TERMS. Do not invent an X and do
  not combine multiple entries into a larger span. If several hard terms were
  rewritten as one phrase and no clean one-to-one mapping is visible, leave
  that phrase untagged rather than guessing.
- When HARD TERMS contains both a parent phrase and one of its pieces, choose
  the MOST SPECIFIC entry that matches Y. If only "oral" became "by mouth"
  while "antibiotics" remains elsewhere, tag `orig="oral"`, NOT
  `orig="oral antibiotics"`.
- ZERO tags is a VALID output if no clean substitutions exist.
- One tag per substitution. No nested or overlapping tags.
- Output ONLY the SIMPLIFIED sentence with tags inserted, on one line.
  No commentary, no JSON, no headers.

──── WORKED EXAMPLE 1 — clean substitutions ────
ORIGINAL:  "the patient was commenced on IV augmentin for acute exacerbation of COPD ."
SIMPLIFIED: "The patient was started on by-vein augmentin for a sudden flare-up of a long-term lung disease."
HARD TERMS: commenced, IV, acute exacerbation, COPD

OUTPUT:
The patient was <replace orig="commenced">started</replace> on <replace orig="IV">by-vein</replace> augmentin for a <replace orig="acute exacerbation">sudden flare-up</replace> of <replace orig="COPD">a long-term lung disease</replace>.

──── WORKED EXAMPLE 2 — some terms NOT simplified ────
ORIGINAL:  "her condition was discussed extensively with her family and she was admitted to hospice ."
SIMPLIFIED: "Her doctors talked in detail with her family and she was admitted to hospice."
HARD TERMS: extensively, hospice

OUTPUT:
Her doctors talked <replace orig="extensively">in detail</replace> with her family and she was admitted to hospice.

(NOTE: "hospice" appears unchanged in SIMPLIFIED -> DO NOT tag it. Only
"extensively" was actually simplified.)

──── WORKED EXAMPLE 3 — KEEP+GLOSS ────
ORIGINAL:  "lactulose was titrated to three bowel movements daily ."
SIMPLIFIED: "Lactulose, a medicine that loosens stools, was adjusted to give three bowel movements a day."
HARD TERMS: lactulose, titrated

OUTPUT:
Lactulose, <replace orig="lactulose">a medicine that loosens stools</replace>, was <replace orig="titrated">adjusted</replace> to give three bowel movements a day.

(NOTE: the NAME is kept; only the added gloss is tagged.)

──── WORKED EXAMPLE 4 — DO NOT over-merge across connector text ────
ORIGINAL:  "the patient is a 31-year-old male s/p a a sibling matched allogeneic bone marrow transplant for severe aplastic anemia ."
SIMPLIFIED: "The 31-year-old man had a bone marrow transplant from his sibling to treat a blood-cell shortage."
HARD TERMS: s/p, allogeneic, bone marrow transplant, severe aplastic anemia

WRONG OUTPUT (over-merge — DO NOT DO THIS):
The 31-year-old man had a <replace orig="s/p a a sibling matched allogeneic bone marrow transplant">bone marrow transplant from his sibling</replace> to treat <replace orig="severe aplastic anemia">a blood-cell shortage</replace>.

  ^ The orig grabs FIVE words of connector text between s/p and allogeneic.
  ContextCite can no longer attribute the individual substitutions cleanly.
  INVALID.

CORRECT OUTPUT (tag only the clean 1-to-1 substitutions):
The 31-year-old man had a bone marrow transplant <replace orig="allogeneic">from his sibling</replace> to treat <replace orig="severe aplastic anemia">a blood-cell shortage</replace>.
"""


LEAN_SYSTEM = """You rewrite clinical sentences so a 6TH-GRADE reader (age ~12) can follow them.

You get the sentence, a list of hard terms with an instruction for each, and
sometimes a glossary. Use only that evidence and ordinary English.

RULES
- Handle EVERY hard term per its instruction. Leaving jargon untouched is the
  worst failure.
- Use the SHORTEST faithful wording. Never more than 7 words per substitution.
  Prefer short common words ("heart", "lung") over Latinate ones.
- Add no new facts, doses, or diagnoses. Numbers, units and lab values stay
  exactly as written.
{person_rule}
- Preserve every safety qualifier AND its scope: negation, uncertainty,
  left/right/both, location, severity, and order in time. "withheld" means
  "held" or "stopped for now", not stopped forever.
- Glossary entries describe a term in general. They are NOT facts about this
  patient. Take only the words needed to translate the term; never import
  causes, materials or purposes the sentence does not state.
- Never write the jargon again in brackets after your plain wording.

{instructions}

OUTPUT
Only the rewritten sentence(s) as plain prose. No tags, no commentary, no word
counts, no grade levels, no notes about your own output."""


INSTRUCTIONS_REPLACE = """INSTRUCTIONS
Every hard term is marked REPLACE: drop it and write the plain equivalent.
    "exacerbation" -> "flare-up"          "IV" -> "by vein"
    "lactulose"    -> "a medicine that loosens stools"
This applies to NAMED drugs, diagnoses and procedures too. Do not keep the
medical name anywhere in your rewrite, not even in brackets."""

INSTRUCTIONS_ACTION = """INSTRUCTIONS
  REPLACE       drop the jargon, write the plain equivalent
                ("exacerbation" -> "flare-up")
  KEEP+GLOSS    the term NAMES a drug or product the patient must recognise:
                keep it verbatim and add a short plain gloss
                ("lactulose" -> "lactulose, a medicine that loosens stools")
  EXPAND        write the abbreviation out ("IV" -> "by vein")
  EXPAND+GLOSS  write it out and add a short gloss
No instruction means REPLACE."""


ACTION_LABEL = {
    "replace": "REPLACE",
    "elaborate": "KEEP+GLOSS",
    "abbr_expand": "EXPAND",
    "abbr_expand_elaborate": "EXPAND+GLOSS",
}


def _is_name(term: str) -> bool:
    from metrics.safety import drug_names_in
    return bool(drug_names_in(term or ""))


def term_instructions(hard_items: List[Dict[str, Any]], tag_policy: str,
                      keep_gloss_scope: str = "names") -> str:
    if not hard_items:
        return "(none)"
    lines = []
    seen = set()
    for it in hard_items:
        term = (it.get("text") or "").strip()
        if not term or term.lower() in seen:
            continue
        seen.add(term.lower())
        action = it.get("action") or "replace"
        if tag_policy == "replace":
            label = "REPLACE"
        elif (action == "elaborate" and keep_gloss_scope == "names"
              and not _is_name(term)):
            label = "REPLACE"
        else:
            label = ACTION_LABEL.get(action, "REPLACE")
        lines.append(f"- {term}   [{label}]")
    return "\n".join(lines) or "(none)"


def format_glossary(active_sources: List[Dict[str, Any]]) -> str:
    if not active_sources:
        return ""
    return "\n".join(f"({s['source']}) {s['text']}" for s in active_sources)


def simplifier_system(prompt_style: str, tag_policy: str = "replace",
                      person_policy: str = "third", sentence: str = "") -> str:
    replace_mode = tag_policy == "replace"
    rule = person_rule(person_policy, sentence)
    if prompt_style == "rich":
        base = _FLUENT_SYSTEM_T.replace("{person_rule}", rule)
        if not replace_mode:
            return base
        return base + (
            "\n\nPOLICY OVERRIDE: every hard term is REPLACE. Replace NAMED "
            "drugs, diagnoses and procedures too; never keep the medical name."
        )
    legend = INSTRUCTIONS_REPLACE if replace_mode else INSTRUCTIONS_ACTION
    return (LEAN_SYSTEM.replace("{instructions}", legend)
            .replace("{person_rule}", rule))


FLUENT_SYSTEM = _FLUENT_SYSTEM_T.replace("{person_rule}", _PERSON_THIRD)


def build_simplify_user(sentence: str, hard_items: List[Dict[str, Any]],
                        active_sources: List[Dict[str, Any]],
                        tag_policy: str, with_glossary: bool,
                        keep_gloss_scope: str = "names") -> str:
    parts = [
        f"Sentence: {sentence}",
        "",
        "Hard terms and what to do with each:",
        term_instructions(hard_items, tag_policy, keep_gloss_scope),
        "",
    ]
    if with_glossary:
        parts += ["Glossary:", format_glossary(active_sources), ""]
    parts += ["Rewrite the sentence now."]
    return "\n".join(parts)


def constant_prefix_tokens(sentence: str, hard_items: List[Dict[str, Any]],
                           tag_policy: str, keep_gloss_scope: str,
                           system: str) -> int:
    prefix = system + "\n\n" + "\n".join([
        f"Sentence: {sentence}", "",
        "Hard terms and what to do with each:",
        term_instructions(hard_items, tag_policy, keep_gloss_scope),
    ])
    return max(1, len(prefix) // 4)


def build_tag_wrap_user(original: str, simplified: str,
                        hard_terms: List[str]) -> str:
    terms = ", ".join(hard_terms) if hard_terms else "(none)"
    return (f"ORIGINAL:   {original}\n\n"
            f"SIMPLIFIED: {simplified}\n\n"
            f"HARD TERMS: {terms}\n\n"
            f"Output the SIMPLIFIED sentence with <replace> tags inserted.")
