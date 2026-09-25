"""Glossary loaders and lookups, abbreviation detection, phrase splitting and second-hop lookup."""

import csv
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from wordfreq import zipf_frequency
except ImportError:
    zipf_frequency = None

MAX_PER_SOURCE = 2
WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[-'][A-Za-z0-9]+)*")


def _raise_csv_field_limit():
    limit = sys.maxsize
    while True:
        try:
            csv.field_size_limit(limit)
            return
        except OverflowError:
            limit //= 10


_raise_csv_field_limit()


def is_abbreviation(text):
    s = text.strip()
    n = len(s)
    if n < 1 or n > 10:
        return False
    if " " in s:
        return False
    if any(c.isdigit() for c in s):
        return True
    if n >= 2 and s.isupper() and s.isalpha():
        return True
    if sum(1 for c in s if c.isupper()) >= 2:
        return True
    return False


def classify_term_kind(text, dorland=None):
    s = text.strip()
    if " " in s:
        return "phrase"
    if dorland:
        if s in dorland or s.lower() in dorland.get("_ci", {}):
            return "abbreviation"
    if is_abbreviation(s):
        return "abbreviation"
    return "word"


def load_readme(path):
    if not path.exists():
        print(f"[warn] readme_lay_vocab.jsonl missing at {path}")
        return {}, []
    by_key, rows = {}, []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            term = obj.get("term", "")
            if not term:
                continue
            key = term.lower().strip()
            obj["_key"] = key
            rows.append(obj)
            by_key.setdefault(key, []).append(obj)
    return by_key, rows


_NIH_SENTINELS = {
    "PDX": "tumor tissue that has been taken from a patient",
    "psychological": "how the mind works",
    "physician assistant": "licensed to do certain medical procedures",
    "National Center for Complementary and Integrative Health": "a federal agency",
    "pyroxamide": "histone deacetylase inhibitors",
    "cytotoxin": "can kill cells",
}


def _nih_integrity_failures(data):
    folded = {str(key).casefold(): str(value) for key, value in data.items()}
    failures = []
    for term, phrase in _NIH_SENTINELS.items():
        definition = folded.get(term.casefold(), "")
        if phrase.casefold() not in definition.casefold():
            failures.append(term)
    return failures


def load_nih(path):
    if not path.exists():
        print(f"[warn] nih.json missing at {path}")
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[warn] could not parse nih.json: {e}")
        return {}

    manifest_path = path.with_name("nih_manifest.json")
    if manifest_path.exists():
        try:
            import hashlib
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            expected = manifest.get("output_sha256")
            if not expected or actual != expected:
                raise RuntimeError(
                    "nih.json checksum does not match nih_manifest.json; "
                    "run `python tools/repair_nih.py --write` to rebuild it"
                )
        except RuntimeError:
            raise
        except Exception as e:
            raise RuntimeError(f"could not verify NIH manifest: {e}") from e

    failures = _nih_integrity_failures(data)
    if failures:
        raise RuntimeError(
            "nih.json failed term-definition integrity checks for "
            f"{failures}; run `python tools/repair_nih.py --write`"
        )

    out = {}
    for key, definition in data.items():
        if not isinstance(definition, str) or not definition.strip():
            continue
        entry = {"term": key, "definition": definition}
        folded = key.casefold().strip()
        existing = out.get(folded)
        if existing is None:
            out[folded] = entry
        elif isinstance(existing, list):
            existing.append(entry)
        else:
            out[folded] = [existing, entry]
    return out


def load_dorland(path):
    if not path.exists():
        print(f"[warn] dorland file missing at {path}")
        return {}
    out = {}
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            term = row.get("term", "")
            cand = row.get("candidate", "")
            if not term or not cand:
                continue
            out.setdefault(term, []).append(cand)
    out["_ci"] = {k.lower(): v for k, v in out.items() if k != "_ci"}
    return out


def load_dictionary(path):
    if not path.exists():
        print(f"[warn] dictonary.csv missing at {path}")
        return {}
    out = {}
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            w = (row.get("word") or "").strip().lower()
            if not w:
                continue
            out.setdefault(w, []).append({
                "word": row.get("word"),
                "pos": row.get("pos", ""),
                "definition": row.get("definition", ""),
            })
    return out


def readme_lookup(text, readme_by_key, readme_rows):
    key = text.lower().strip()
    n_words = len(WORD_RE.findall(text))
    out, seen = [], set()
    for entry in readme_by_key.get(key, []):
        if entry["entry_id"] not in seen:
            seen.add(entry["entry_id"])
            out.append(entry)
            if len(out) >= MAX_PER_SOURCE:
                return out
    if n_words >= 2:
        pattern = re.compile(r"\b" + re.escape(key) + r"\b")
        for entry in readme_rows:
            if entry["entry_id"] in seen:
                continue
            if pattern.search(entry["_key"]):
                seen.add(entry["entry_id"])
                out.append(entry)
                if len(out) >= MAX_PER_SOURCE:
                    break
    return out


def nih_lookup(text, nih):
    if not nih:
        return []
    surface = text.strip()
    hit = nih.get(surface.casefold())
    if not hit:
        return []
    if not isinstance(hit, list):
        return [hit]
    exact = [entry for entry in hit if entry.get("term") == surface]
    return exact[:1]


def dorland_lookup(text, dorland):
    if not dorland:
        return []
    if text in dorland:
        return dorland[text][:MAX_PER_SOURCE]
    return dorland.get("_ci", {}).get(text.lower(), [])[:MAX_PER_SOURCE]


def dictionary_lookup(text, dictionary):
    return dictionary.get(text.lower().strip(), [])[:MAX_PER_SOURCE]


def load_glossary_json(path):
    if not path.exists():
        print(f"[warn] glossary missing at {path}")
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[warn] could not parse {path.name}: {e}")
        return {}
    if not isinstance(data, list):
        print(f"[warn] {path.name} is not a JSON list — skipping")
        return {}
    out = {}
    for obj in data:
        if not isinstance(obj, dict):
            continue
        term = (obj.get("term") or "").strip()
        definition = (obj.get("definition") or "").strip()
        if not term or not definition:
            continue
        key = term.lower().strip()
        out.setdefault(key, []).append({"term": term, "definition": definition})
    return out


def glossary_lookup(text, by_key):
    if not by_key:
        return []
    return by_key.get(text.lower().strip(), [])[:MAX_PER_SOURCE]


def generate_partitions(words):
    n = len(words)
    if n <= 1:
        return []
    from itertools import combinations
    all_parts = []
    for n_pieces in range(2, n + 1):
        for cuts in combinations(range(1, n), n_pieces - 1):
            pieces, prev = [], 0
            for c in cuts:
                pieces.append(" ".join(words[prev:c]))
                prev = c
            pieces.append(" ".join(words[prev:]))
            all_parts.append(pieces)
    return all_parts


def find_best_partition(words, can_define_fn):
    for parts in generate_partitions(words):
        if all(can_define_fn(p) for p in parts):
            return parts, True
    return list(words), False


def find_partial_partition(words, can_define_fn):
    best, best_key = None, None
    for parts in generate_partitions(words):
        undef_words = sum(len(WORD_RE.findall(p)) for p in parts
                          if not can_define_fn(p))
        key = (undef_words, len(parts))
        if best_key is None or key < best_key:
            best, best_key = parts, key
        if undef_words == 0:
            break
    if best is None:
        return list(words), len(words)
    return best, best_key[0]


def split_hard_phrase(text, readme_by_key, readme_rows, nih, dorland):
    words = WORD_RE.findall(text)
    if len(words) <= 1:
        return [text], "single"

    if readme_lookup(text, readme_by_key, readme_rows) or nih_lookup(text, nih):
        return [text], "whole_defined"

    def can_define(piece):
        return bool(readme_lookup(piece, readme_by_key, readme_rows)
                    or nih_lookup(piece, nih))

    partition, all_defined = find_best_partition(words, can_define)
    return partition, "partition_full" if all_defined else "partition_fallback"


_IRREGULAR_PLURALS = {
    "effusions": "effusion", "opacities": "opacity", "metastases": "metastasis",
    "diagnoses": "diagnosis", "prostheses": "prosthesis", "analyses": "analysis",
    "atelectases": "atelectasis", "stenoses": "stenosis", "neuroses": "neurosis",
    "emboli": "embolus", "thrombi": "thrombus", "bacteria": "bacterium",
    "vertebrae": "vertebra", "bullae": "bulla", "fungi": "fungus",
    "carcinomata": "carcinoma", "adenomata": "adenoma",
}


def _depluralise(word: str) -> Optional[str]:
    w = word.lower()
    if len(w) < 4 or not w.isalpha():
        return None
    if w in _IRREGULAR_PLURALS:
        return _IRREGULAR_PLURALS[w]
    if w.endswith("ies") and len(w) > 4:
        return w[:-3] + "y"
    if w.endswith(("ses", "xes", "zes", "ches", "shes")):
        return w[:-2]
    if w.endswith("s") and not w.endswith(("ss", "us", "is", "as")):
        return w[:-1]
    return None


def surface_variants(text: str) -> List[str]:
    raw = (text or "").strip()
    if not raw:
        return []
    out: List[str] = []
    seen = set()

    def push(s: str):
        s = re.sub(r"\s+", " ", (s or "")).strip()
        if not s:
            return
        k = s.lower()
        if k in seen:
            return
        seen.add(k)
        out.append(s)

    push(raw)
    lower = raw.lower()
    push(lower)

    push(re.sub(r"['\u2019]s\b", "", lower))

    if "-" in lower:
        push(lower.replace("-", " "))
        push(lower.replace("-", ""))
    if "/" in lower:
        push(lower.replace("/", " "))
    if " " in lower:
        push(lower.replace(" ", "-"))

    push(lower.strip(".,;:()[]"))
    push(re.sub(r"^(the|a|an)\s+", "", lower))

    words = lower.split()
    if words:
        head = _depluralise(words[-1])
        if head:
            push(" ".join(words[:-1] + [head]))
        singular_all = [(_depluralise(w) or w) for w in words]
        if singular_all != words:
            push(" ".join(singular_all))

    return out


_HOP_RARE_ZIPF = 3.0
_HOP_MIN_LEN = 4
_HOP_MAX_POSTINGS = 400

_GLUE = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "that", "which", "when", "where", "who", "whose", "what", "how",
    "of", "to", "in", "on", "at", "for", "with", "from", "by", "as",
    "or", "and", "but", "if", "so", "than", "then", "into", "onto",
    "within", "without", "about", "over", "under", "between", "through",
    "it", "its", "this", "these", "those", "you", "your", "they", "their",
    "can", "may", "might", "will", "would", "should", "must", "does", "do",
    "used", "using", "means", "meaning", "makes", "make", "made", "causes",
    "cause", "happens", "happen", "occurs", "occur", "gets", "get",
    "something", "someone", "part", "type", "kind", "way", "not",
}


def rare_tokens(text: str, cut: float = _HOP_RARE_ZIPF) -> set:
    if zipf_frequency is None:
        return set()
    out = set()
    for w in WORD_RE.findall(text or ""):
        lw = w.lower()
        if len(lw) >= _HOP_MIN_LEN and zipf_frequency(lw, "en") < cut:
            out.add(lw)
    return out


def looks_like_expansion(term: str, definition: str) -> bool:
    toks = [w.lower() for w in WORD_RE.findall(definition or "")]
    if not toks or len(toks) > 6:
        return False
    letters = re.sub(r"[^a-z]", "", (term or "").lower())
    if letters and "".join(t[0] for t in toks) == letters:
        return True
    return not any(t in _GLUE for t in toks)


def build_hop_index(readme_rows, nih, extra=None) -> Dict[str, List[Any]]:
    index: Dict[str, List[Any]] = {}

    def add(key: str, rec):
        for tok in rare_tokens(key):
            bucket = index.setdefault(tok, [])
            if len(bucket) < _HOP_MAX_POSTINGS:
                bucket.append(rec)

    for entry in readme_rows or []:
        add(entry.get("term", ""), ("readme", entry))
    for _, value in (nih or {}).items():
        entries = value if isinstance(value, list) else [value]
        for entry in entries:
            add(entry.get("term", ""), ("nih", entry))
    for label, by_key in (extra or {}).items():
        for _, value in (by_key or {}).items():
            entries = value if isinstance(value, list) else [value]
            for entry in entries:
                add(entry.get("term", ""), (label, entry))
    return index


def _hop_headword_matches(expansion: str, headword: str) -> bool:
    from difflib import SequenceMatcher

    want = {word.lower() for word in WORD_RE.findall(expansion or "")
            if len(word) >= _HOP_MIN_LEN and word.lower() not in _GLUE}
    candidates = {word.lower() for word in WORD_RE.findall(headword or "")
                  if len(word) >= _HOP_MIN_LEN}
    if not want or not candidates:
        return False
    for token in want:
        if token in candidates:
            continue
        if not any(
            min(len(token), len(candidate)) >= 7
            and SequenceMatcher(None, token, candidate).ratio() >= 0.70
            for candidate in candidates
        ):
            return False
    return True


def hop_lookup(expansion: str, hop_index, limit: int = MAX_PER_SOURCE
               ) -> List[Any]:
    want = rare_tokens(expansion)
    if not want or not hop_index:
        return []
    hits, seen = [], set()
    for tok in sorted(want):
        for src, entry in hop_index.get(tok, []):
            if not _hop_headword_matches(expansion, entry.get("term", "")):
                continue
            key = (src, (entry.get("term") or "").lower())
            if key in seen:
                continue
            seen.add(key)
            hits.append((src, entry))
    if not hits:
        return []

    def plainness(item):
        _, entry = item
        toks = [w.lower() for w in WORD_RE.findall(entry.get("definition", ""))]
        if zipf_frequency is None or not toks:
            return 0.0
        return min(zipf_frequency(t, "en") for t in toks)

    hits.sort(key=plainness, reverse=True)
    return hits[:limit]
