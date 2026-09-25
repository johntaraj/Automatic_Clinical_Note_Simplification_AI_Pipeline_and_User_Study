"""High-risk edit checks: negation, uncertainty, laterality, numbers and units, severity,
diagnoses and drug names.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Set

from .text import contains_term
NEGATION_CUES = [
    "no", "not", "none", "without", "denies", "denied", "negative for",
    "absence of", "absent", "never", "free of", "unremarkable",
    "cannot be excluded", "can not be excluded", "cannot be ruled out",
    "can not be ruled out", "ruled out", "rule out", "excluded",
    "no evidence of", "nor",
]

UNCERTAINTY_CUES = [
    "possible", "possibly", "probable", "probably", "likely", "unlikely",
    "suggestive of", "suspicious for", "compatible with", "consistent with",
    "cannot be excluded", "can not be excluded", "cannot be ruled out",
    "can not be ruled out", "may", "might", "could", "consideration",
    "question of", "questionable", "concern for", "concerning for",
    "versus", "differential", "presumed", "apparent", "equivocal",
    "indeterminate", "uncertain", "appears", "seems",
]

TEMPORALITY_CUES = [
    "history of", "status post", "s/p", "currently", "now", "previous",
    "prior", "past", "resolved", "recurrence", "recurrent", "new onset",
    "chronic", "acute", "former", "old", "since", "before", "after",
    "later", "subsequent", "subsequently", "initially", "ongoing",
    "persistent", "persisted", "afterward", "afterwards",
]

SEVERITY_CUES = [
    "mild", "mildly", "moderate", "moderately", "severe", "severely",
    "marked", "markedly", "obvious", "small", "large", "massive",
    "minimal", "minimally", "extensive", "significant", "significantly",
    "worsening", "worse", "improved", "improving", "slight", "slightly",
    "profound", "critical",
]

LATERALITY_CUES = [
    "left", "right", "bilateral", "bilaterally", "unilateral", "both",
    "upper", "lower", "medial", "lateral", "proximal", "distal",
    "anterior", "posterior", "superior", "inferior", "basal", "bibasal",
    "apical", "midline", "ipsilateral", "contralateral",
]

SEVERITY_TIERS: Dict[str, int] = {
    "severe": 3, "severely": 3, "critical": 3, "critically": 3,
    "profound": 3, "profoundly": 3, "massive": 3, "massively": 3,
    "fulminant": 3, "life-threatening": 3, "life threatening": 3,
    "malignant": 3, "grave": 3, "gravely": 3, "florid": 3, "advanced": 3,
    "serious": 3, "seriously": 3, "dangerous": 3, "dangerously": 3,
    "very bad": 3, "very serious": 3, "emergency": 3,
    "moderate": 2, "moderately": 2, "marked": 2, "markedly": 2,
    "significant": 2, "significantly": 2, "substantial": 2,
    "substantially": 2, "extensive": 2, "extensively": 2, "large": 2,
    "considerable": 2, "big": 2, "quite bad": 2, "fairly bad": 2,
    "mild": 1, "mildly": 1, "slight": 1, "slightly": 1, "minimal": 1,
    "minimally": 1, "small": 1, "minor": 1, "trace": 1, "subtle": 1,
    "a little": 1, "a bit": 1, "not serious": 1,
}

def _cond(*forms: str):
    return tuple(forms)


CONDITION_LAY_FORMS: Dict[str, tuple] = {
    "encephalopathy": _cond(
        "confusion", "confused", "coma", "comatose", "unconscious",
        "brain damage", "brain injury", "brain swelling", "brain problem",
        "brain problems", "brain trouble", "brain disease", "brain failure",
        "problems with the brain", "brain does not work", "brain not working",
        "mental status", "disoriented", "delirium", "delirious",
        "cannot think clearly", "trouble thinking clearly",
        "unable to think clearly", "thinking problems", "drowsy"),
    "asterixis": _cond(
        "flap", "flaps", "flapping", "flapping tremor", "loss of muscle tone",
        "hands drop", "wrists drop", "hands fall", "hands give way"),
    "infarction": _cond(
        "heart attack", "tissue death", "tissue died", "death of tissue",
        "dead tissue", "blocked blood flow", "blood flow was blocked"),
    "infarct": _cond(
        "heart attack", "tissue death", "tissue died", "death of tissue",
        "dead tissue", "blocked blood flow", "blood flow was blocked"),
    "hemorrhage": _cond("bleed", "bleeds", "bleeding", "blood loss",
                        "burst blood vessel", "broken blood vessel"),
    "haemorrhage": _cond("bleed", "bleeds", "bleeding", "blood loss",
                         "burst blood vessel", "broken blood vessel"),
    "embolism": _cond("blood clot", "clot", "clots", "blockage", "blocked",
                      "blocking", "plugged"),
    "embolus": _cond("blood clot", "clot", "clots", "blockage", "blocked",
                     "blocking", "plugged"),
    "thrombosis": _cond("blood clot", "clot", "clots", "blocked"),
    "thrombus": _cond("blood clot", "clot", "clots", "blocked"),
    "sepsis": _cond("blood infection", "infection in the blood",
                    "body-wide infection", "body wide infection",
                    "whole-body infection", "whole body infection",
                    "serious infection", "severe infection",
                    "life-threatening infection", "dangerous infection",
                    "infection that spread", "infection spread"),
    "septic": _cond("blood infection", "infection in the blood",
                    "body-wide infection", "body wide infection",
                    "whole-body infection", "whole body infection",
                    "serious infection", "severe infection",
                    "life-threatening infection", "dangerous infection",
                    "infection that spread", "infection spread"),
    "pneumothorax": _cond("collapsed lung", "lung collapsed", "lung collapse",
                          "air around the lung", "air outside the lung"),
    "aneurysm": _cond("bulge", "bulging", "ballooning", "balloon",
                      "weak spot", "swollen blood vessel", "widened"),
    "perforation": _cond("hole", "tear", "torn", "burst", "punctured",
                         "puncture", "opening"),
    "perforated": _cond("hole", "tear", "torn", "burst", "punctured",
                        "puncture", "opening"),
    "rupture": _cond("burst", "tear", "torn", "broke open", "split open",
                     "broke apart", "break", "broke"),
    "ruptured": _cond("burst", "tear", "torn", "broke open", "split open",
                      "broke apart", "break", "broke"),
    "transection": _cond("cut", "cuts", "cut through", "cut across",
                         "severed", "completely cut", "cut in two", "split",
                         "tear", "torn", "tore"),
    "ischemia": _cond("not enough blood", "poor blood flow",
                      "reduced blood flow", "low blood flow",
                      "blood supply", "starved of blood", "lack of blood"),
    "ischaemia": _cond("not enough blood", "poor blood flow",
                       "reduced blood flow", "low blood flow",
                       "blood supply", "starved of blood", "lack of blood"),
    "necrosis": _cond("tissue death", "dead tissue", "tissue died",
                      "dying tissue", "tissue is dying", "died", "dying"),
    "necrotic": _cond("tissue death", "dead tissue", "tissue died",
                      "dying tissue", "tissue is dying", "died", "dying"),
    "carcinoma": _cond("cancer", "cancerous", "tumor", "tumour", "growth"),
    "sarcoma": _cond("cancer", "cancerous", "tumor", "tumour", "growth"),
    "lymphoma": _cond("cancer", "cancerous", "tumor", "tumour", "growth"),
    "leukemia": _cond("cancer", "blood cancer", "cancer of the blood"),
    "leukaemia": _cond("cancer", "blood cancer", "cancer of the blood"),
    "melanoma": _cond("cancer", "skin cancer", "cancerous", "growth"),
    "malignant": _cond("cancer", "cancerous", "can spread", "spreads"),
    "malignancy": _cond("cancer", "cancerous", "can spread", "spreads"),
    "metastasis": _cond("spread", "spreading", "has spread", "moved to"),
    "metastases": _cond("spread", "spreading", "has spread", "moved to"),
    "metastatic": _cond("spread", "spreading", "has spread", "moved to"),
    "cirrhosis": _cond("scarring of the liver", "scarred liver",
                       "liver scarring", "scarring in the liver",
                       "liver damage", "damaged liver", "scar tissue",
                       "liver disease", "liver failure", "liver problem",
                       "liver problems", "liver is scarred", "scarred"),
    "peritonitis": _cond("infection", "inflammation", "inflamed", "swelling",
                         "swollen", "belly lining", "abdominal lining",
                         "lining of the belly", "lining of the abdomen",
                         "peritoneum", "belly cavity"),
    "meningitis": _cond("infection around the brain", "brain covering",
                        "swelling around the brain", "covering of the brain",
                        "brain and spinal cord", "lining of the brain"),
    "tamponade": _cond("pressure around the heart", "fluid around the heart",
                       "squeezing the heart", "squeezes the heart"),
    "abscess": _cond("pocket of pus", "pus", "infected pocket",
                     "pus-filled", "pus filled", "pocket of infection"),
    "seizure": _cond("seizure", "seizures", "fit", "fits", "convulsion",
                     "convulsions", "shaking spell"),
    "coma": _cond("coma", "unconscious", "unresponsive", "deep sleep",
                  "cannot be woken", "could not be woken"),
    "overdose": _cond("too much", "excess", "more than the safe amount"),
    "obstruction": _cond("blockage", "blocked", "clog", "clogged",
                         "blocking", "plugged", "stuck"),
}

HIGH_RISK_CONDITIONS = tuple(CONDITION_LAY_FORMS)

UNIT_CUES = [
    "mg", "mcg", "ug", "g", "kg", "ml", "l", "cc", "cm", "mm", "mmhg",
    "mmol", "meq", "iu", "units", "unit", "%", "bpm",
    "days", "day", "weeks", "week", "months", "month", "years", "year",
    "hours", "hour",
]

UNIT_ALIASES: Dict[str, str] = {
    "mg": "mg", "milligram": "mg", "milligrams": "mg", "milligramme": "mg",
    "mcg": "mcg", "ug": "mcg", "microgram": "mcg", "micrograms": "mcg",
    "g": "g", "gram": "g", "grams": "g",
    "kg": "kg", "kilogram": "kg", "kilograms": "kg", "kilo": "kg",
    "ml": "ml", "millilitre": "ml", "millilitres": "ml",
    "milliliter": "ml", "milliliters": "ml",
    "l": "l", "litre": "l", "litres": "l", "liter": "l", "liters": "l",
    "cc": "ml",
    "cm": "cm", "centimetre": "cm", "centimetres": "cm",
    "centimeter": "cm", "centimeters": "cm",
    "mm": "mm", "millimetre": "mm", "millimetres": "mm",
    "millimeter": "mm", "millimeters": "mm",
    "mmhg": "mmhg", "millimetres of mercury": "mmhg",
    "millimeters of mercury": "mmhg",
    "mmol": "mmol", "millimole": "mmol", "millimoles": "mmol",
    "meq": "meq", "milliequivalent": "meq", "milliequivalents": "meq",
    "iu": "iu", "international unit": "iu", "international units": "iu",
    "unit": "unit", "units": "unit",
    "%": "%", "percent": "%", "per cent": "%", "percentage": "%",
    "bpm": "bpm", "beats per minute": "bpm",
    "day": "day", "days": "day",
    "week": "week", "weeks": "week",
    "month": "month", "months": "month",
    "year": "year", "years": "year",
    "hour": "hour", "hours": "hour",
}


_LEFT_AS_VERB = re.compile(
    r"(?:\b(?:was|were|is|are|has|have|had|he|she|they|who|patient|then)\s+left\b)"
    r"|(?:\bleft\s+(?:the|his|her|their|its|hospital|ward|ama|against|home|early)\b)",
    re.IGNORECASE,
)

_NUMBER_WORDS = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
    "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
    "eighteen": "18", "nineteen": "19", "twenty": "20", "thirty": "30",
    "forty": "40", "fifty": "50", "sixty": "60", "seventy": "70",
    "eighty": "80", "ninety": "90", "hundred": "100",
    "once": "1", "twice": "2", "single": "1", "double": "2",
    "half": "0.5",
}
_NUM_RE = re.compile(r"\d+(?:\.\d+)?")


def _canon_num(tok: str) -> str:
    try:
        f = float(tok)
    except ValueError:
        return tok
    return str(int(f)) if f == int(f) else str(f)


def numbers_in(text: str) -> Set[str]:
    t = (text or "").lower()
    out = {_canon_num(m) for m in _NUM_RE.findall(t)}
    for word, digit in _NUMBER_WORDS.items():
        if re.search(r"(?<!\w)" + word + r"(?!\w)", t):
            out.add(_canon_num(digit))
    return out


def units_in(text: str) -> Set[str]:
    t = (text or "").lower()
    out: Set[str] = set()
    if "%" in t:
        out.add("%")
    for spelling in sorted(UNIT_ALIASES, key=len, reverse=True):
        if spelling == "%":
            continue
        if re.search(r"(?<!\w)" + re.escape(spelling) + r"(?!\w)", t):
            out.add(UNIT_ALIASES[spelling])
    return out


WHO_INN_STEMS = (
    "olol", "alol", "ilol",
    "pril", "prilat",
    "sartan",
    "statin",
    "dipine",
    "cillin", "penem", "cycline", "mycin",
    "micin", "floxacin", "oxacin", "sulfa",
    "azole", "prazole", "conazole",
    "tidine",
    "parin", "parinux",
    "xaban", "gatran",
    "triptan", "setron", "peridol",
    "azepam", "zolam", "barbital",
    "caine",
    "vir", "vudine", "navir",
    "mab", "zumab", "ximab", "umab",
    "nib", "tinib", "ciclib",
    "prost", "profen", "coxib",
    "terol", "tropium",
    "gliptin", "gliflozin", "glitazone",
    "semide", "thiazide",
    "codone", "morphone", "fentanil", "fentanyl",
)

CURATED_DRUGS = {
    "lactulose", "atropine", "insulin", "warfarin", "aspirin", "morphine",
    "digoxin", "amiodarone", "prednisone", "prednisolone", "dexamethasone",
    "hydrocortisone", "metformin", "levothyroxine", "furosemide", "acetaminophen",
    "paracetamol", "ibuprofen", "naloxone", "epinephrine", "adrenaline",
    "norepinephrine", "dopamine", "dobutamine", "vasopressin", "propofol",
    "midazolam", "ketamine", "haloperidol", "lithium", "phenytoin",
    "levetiracetam", "valproate", "carbamazepine", "gabapentin", "tramadol",
    "oxycodone", "clopidogrel", "ticagrelor", "apixaban", "rivaroxaban",
    "augmentin", "amoxicillin", "vancomycin", "ceftriaxone", "meropenem",
    "piperacillin", "tazobactam", "azithromycin", "doxycycline", "nitroglycerin",
    "albuterol", "salbutamol", "ipratropium", "montelukast", "omeprazole",
    "pantoprazole", "ondansetron", "heparin", "enoxaparin", "colchicine",
    "allopurinol", "spironolactone", "hydrochlorothiazide", "amlodipine",
    "lisinopril", "losartan", "metoprolol", "atenolol", "carvedilol",
    "atorvastatin", "simvastatin", "rosuvastatin", "tamsulosin", "sildenafil",
    "rifaximin", "octreotide", "midodrine", "albumin", "ceftazidime",
}

_NON_DRUG_EXCEPTIONS = {
    "protein", "vitamin", "oxygen", "saline", "glucose", "sodium", "calcium",
    "potassium", "magnesium", "alcohol", "nicotine", "caffeine", "cortisol",
    "creatinine", "bilirubin", "albumin",
    "urine", "serum", "plasma", "carbon", "iodine", "chlorine",
}

_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9\-]{3,}")


def drug_names_in(text: str) -> Set[str]:
    found: Set[str] = set()
    for tok in _TOKEN_RE.findall(text or ""):
        low = tok.lower()
        if low in _NON_DRUG_EXCEPTIONS:
            continue
        if low in CURATED_DRUGS:
            found.add(low)
            continue
        if len(low) >= 6 and any(low.endswith(s) for s in WHO_INN_STEMS):
            found.add(low)
    return found


def _cues_present(text: str, cues: List[str]) -> Set[str]:
    return {c for c in cues if contains_term(text, c)}


def _laterality_cues(text: str) -> Set[str]:
    found = _cues_present(text, LATERALITY_CUES)
    if "left" in found:
        occurrences = len(re.findall(r"(?<!\w)left(?!\w)", text or "", re.IGNORECASE))
        verb_hits = len(_LEFT_AS_VERB.findall(text or ""))
        if verb_hits >= occurrences:
            found.discard("left")
    return found


SLOT_LEXICONS = {
    "negation": NEGATION_CUES,
    "uncertainty": UNCERTAINTY_CUES,
    "temporality": TEMPORALITY_CUES,
    "severity": SEVERITY_CUES,
}


def severity_tier(text: str) -> Optional[int]:
    tiers = [t for cue, t in SEVERITY_TIERS.items() if contains_term(text, cue)]
    return max(tiers) if tiers else None


def conditions_in(text: str) -> Set[str]:
    return {c for c in CONDITION_LAY_FORMS if contains_term(text, c)}


def condition_preserved(condition: str, sys_out: str) -> bool:
    if contains_term(sys_out, condition):
        return True
    return any(contains_term(sys_out, form)
               for form in CONDITION_LAY_FORMS.get(condition, ()))


HIGH_RISK = ("negation", "uncertainty", "laterality", "number_unit", "drug",
             "diagnostic_identity", "severity_downgrade")


def clinical_safety(orig: str, sys_out: str,
                    drug_is_critical: bool = True) -> Optional[Dict[str, Any]]:
    if not (orig or "").strip() or not (sys_out or "").strip():
        return None

    out: Dict[str, Any] = {}
    flags: List[Dict[str, Any]] = []
    any_slot = False
    critical = False

    for slot, cues in SLOT_LEXICONS.items():
        in_cues = _cues_present(orig, cues)
        if not in_cues:
            out[f"{slot}_preservation"] = None
            continue
        any_slot = True
        out_cues = _cues_present(sys_out, cues)
        preserved = 1.0 if out_cues else 0.0
        out[f"{slot}_preservation"] = preserved
        if preserved == 0.0:
            if slot in HIGH_RISK:
                critical = True
            flags.append({"slot": slot, "severity":
                          "critical" if slot in HIGH_RISK else "warning",
                          "input_cues": sorted(in_cues), "output_cues": []})

    lat_in = _laterality_cues(orig)
    if lat_in:
        any_slot = True
        lat_out = _laterality_cues(sys_out)
        fam = {
            "bilaterally": "bilateral", "both": "bilateral",
            "bilateral": "bilateral",
            "bibasal": "basal", "basal": "basal", "lower": "basal",
            "inferior": "basal",
        }
        norm_in = {fam.get(c, c) for c in lat_in}
        norm_out = {fam.get(c, c) for c in lat_out}
        kept = norm_in & norm_out
        recall = len(kept) / len(norm_in)
        out["laterality_preservation"] = round(recall, 3)
        if recall < 1.0:
            critical = True
            flags.append({"slot": "laterality", "severity": "critical",
                          "input_cues": sorted(norm_in),
                          "output_cues": sorted(norm_out),
                          "lost": sorted(norm_in - norm_out)})
    else:
        out["laterality_preservation"] = None

    n_in = numbers_in(orig) | units_in(orig)
    if n_in:
        any_slot = True
        n_out = numbers_in(sys_out) | units_in(sys_out)
        recall = len(n_in & n_out) / len(n_in)
        out["number_unit_preservation"] = round(recall, 3)
        if recall < 1.0:
            critical = True
            flags.append({"slot": "number_unit", "severity": "critical",
                          "input_cues": sorted(n_in),
                          "output_cues": sorted(n_out),
                          "lost": sorted(n_in - n_out)})
    else:
        out["number_unit_preservation"] = None

    drugs_in = drug_names_in(orig)
    if drugs_in:
        any_slot = True
        kept = {d for d in drugs_in if contains_term(sys_out, d)}
        recall = len(kept) / len(drugs_in)
        out["drug_preservation"] = round(recall, 3)
        out["drugs_in_input"] = sorted(drugs_in)
        out["drugs_dropped"] = sorted(drugs_in - kept)
        if recall < 1.0:
            if drug_is_critical:
                critical = True
            flags.append({"slot": "drug",
                          "severity": "critical" if drug_is_critical else "policy",
                          "input_cues": sorted(drugs_in),
                          "output_cues": sorted(kept),
                          "lost": sorted(drugs_in - kept)})
    else:
        out["drug_preservation"] = None

    conds_in = conditions_in(orig)
    if conds_in:
        any_slot = True
        kept = {c for c in conds_in if condition_preserved(c, sys_out)}
        recall = len(kept) / len(conds_in)
        out["diagnostic_identity_preservation"] = round(recall, 3)
        out["conditions_in_input"] = sorted(conds_in)
        out["conditions_lost"] = sorted(conds_in - kept)
        if recall < 1.0:
            critical = True
            flags.append({"slot": "diagnostic_identity", "severity": "critical",
                          "input_cues": sorted(conds_in),
                          "output_cues": sorted(kept),
                          "lost": sorted(conds_in - kept)})
    else:
        out["diagnostic_identity_preservation"] = None

    tier_in = severity_tier(orig)
    if tier_in is not None:
        any_slot = True
        tier_out = severity_tier(sys_out) or 0
        downgraded = tier_out < tier_in
        out["severity_downgrade"] = 1.0 if downgraded else 0.0
        out["severity_tier_input"] = tier_in
        out["severity_tier_output"] = tier_out or None
        if tier_in == 3 and tier_out <= 1:
            critical = True
            flags.append({"slot": "severity_downgrade", "severity": "critical",
                          "input_cues": [f"tier {tier_in}"],
                          "output_cues": [f"tier {tier_out}"],
                          "lost": ["grave severity stated as mild or absent"]})
        elif downgraded:
            flags.append({"slot": "severity_downgrade", "severity": "warning",
                          "input_cues": [f"tier {tier_in}"],
                          "output_cues": [f"tier {tier_out}"], "lost": []})
    else:
        out["severity_downgrade"] = None

    out["critical_error"] = 1.0 if (any_slot and critical) else 0.0
    out["safety_flags"] = flags
    return out
