"""Stage 3: definition retrieval from the local knowledge base."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from config import Config
from core.io import rule
from core.vocab import (
    MAX_PER_SOURCE, WORD_RE, build_hop_index, classify_term_kind,
    dictionary_lookup, find_best_partition, find_partial_partition,
    glossary_lookup, hop_lookup, load_dictionary, load_glossary_json,
    load_dorland, load_nih, load_readme, looks_like_expansion, dorland_lookup,
    nih_lookup, readme_lookup, surface_variants,
)
from metrics.coverage import coverage_for_note, source_alignment_for_note

SOURCE_LABEL = {
    "readme_lay_vocab.jsonl": "readme",
    "nih.json": "nih",
    "iowa.json": "iowa",
    "michigan_plmd.json": "michigan",
    "justplainclear.json": "justplainclear",
    "wiktionary.json": "wiktionary",
    "dorland_medical_abbreviations.csv": "dorland",
    "dictonary.csv": "dictionary",
    "thesarus.json": "thesaurus",
}


def source_label(raw: str) -> str:
    return "umls" if raw.startswith("UMLS") else SOURCE_LABEL.get(raw, raw)


HOP_SOURCE_FILE = {v: k for k, v in SOURCE_LABEL.items()}


def _hop_split_expansion(expansion: str, hop_index) -> List[Any]:
    words = WORD_RE.findall(expansion or "")
    if len(words) < 2:
        return []
    cache: Dict[str, List[Any]] = {}

    def probe(piece: str) -> List[Any]:
        key = piece.lower()
        if key not in cache:
            cache[key] = list(hop_lookup(piece, hop_index))
        return cache[key]

    partition, ok = find_best_partition(words, lambda p: bool(probe(p)))
    if not ok:
        partition, _ = find_partial_partition(words, lambda p: bool(probe(p)))
    out: List[Any] = []
    for piece in partition:
        if piece.strip().lower() == (expansion or "").strip().lower():
            continue
        if _piece_worth_showing(piece):
            out.extend(probe(piece))
    return out[:MAX_PER_SOURCE]


def load_sources(cfg: Config) -> Dict[str, Any]:
    d = cfg.root / "data"
    print("  loading glossaries ...")
    readme_by_key, readme_rows = load_readme(d / "readme_exp_good.jsonl")
    sources = {
        "readme_by_key": readme_by_key,
        "readme_rows": readme_rows,
        "nih": load_nih(d / "nih.json"),
        "dorland": load_dorland(d / "dorland_medical_abbreviations.csv"),
        "dictionary": load_dictionary(d / "dictonary.csv"),
        "iowa": load_glossary_json(d / "Iowa.json"),
        "michigan": load_glossary_json(d / "michigan_plmd.json"),
        "justplainclear": load_glossary_json(d / "justplainclear_en_clean.json"),
        "wiktionary": load_glossary_json(d / "wiktionary.json"),
        "thesaurus": load_glossary_json(d / "thesarus.json"),
    }
    sources["hop_index"] = build_hop_index(
        readme_rows, sources["nih"],
        {"iowa": sources["iowa"], "michigan": sources["michigan"],
         "justplainclear": sources["justplainclear"]})
    sources["hop_split_expansion"] = bool(getattr(cfg, "hop_split_expansion", False))
    print(f"    readme {len(readme_by_key):>6} keys | nih {len(sources['nih']):>6} | "
          f"dorland {len(sources['dorland']):>6} | dictionary {len(sources['dictionary']):>6}")
    print(f"    iowa {len(sources['iowa']):>4} | michigan {len(sources['michigan']):>5} | "
          f"jpc {len(sources['justplainclear']):>5} | wiktionary {len(sources['wiktionary']):>6} | "
          f"thesaurus {len(sources['thesaurus']):>5}")
    print(f"    hop index {len(sources['hop_index']):>5} rare tokens")
    return sources


def _raw_lookup(text: str, kind: str, sources: Dict[str, Any]
                ) -> Dict[str, List[Any]]:
    hits = {
        "iowa": glossary_lookup(text, sources.get("iowa", {})),
        "michigan": glossary_lookup(text, sources.get("michigan", {})),
        "justplainclear": glossary_lookup(text, sources.get("justplainclear", {})),
        "wiktionary": glossary_lookup(text, sources.get("wiktionary", {})),
        "thesaurus": glossary_lookup(text, sources.get("thesaurus", {})),
        "readme": [], "nih": [], "dorland": [], "dictionary": [],
    }
    if kind == "abbreviation":
        hits["dorland"] = dorland_lookup(text, sources["dorland"])
        hits["readme"] = readme_lookup(text, sources["readme_by_key"],
                                       sources["readme_rows"])
        hits["nih"] = nih_lookup(text, sources["nih"])
    elif kind == "phrase":
        hits["readme"] = readme_lookup(text, sources["readme_by_key"],
                                       sources["readme_rows"])
        hits["nih"] = nih_lookup(text, sources["nih"])
    else:
        hits["readme"] = readme_lookup(text, sources["readme_by_key"],
                                       sources["readme_rows"])
        hits["nih"] = nih_lookup(text, sources["nih"])
        hits["dictionary"] = dictionary_lookup(text, sources["dictionary"])
    return hits


def _build_attributions(term: str, hits: Dict[str, List[Any]]
                        ) -> List[Dict[str, Any]]:
    attribs: List[Dict[str, Any]] = []
    seen: set = set()

    def add(source: str, entry_term: str, definition: str, extra=None):
        if not definition:
            return
        norm = definition.strip().lower()[:200]
        if norm in seen:
            return
        seen.add(norm)
        rec = {"source": source, "term": entry_term,
               "definition": definition.strip()}
        if extra:
            rec.update(extra)
        attribs.append(rec)

    for r in hits["readme"]:
        add("readme_lay_vocab.jsonl", r.get("term", ""), r.get("definition", ""),
            {"entry_id": r.get("entry_id", "")})
    for r in hits["nih"]:
        add("nih.json", r.get("term", ""), r.get("definition", ""))
    for r in hits["iowa"]:
        add("iowa.json", r.get("term", ""), r.get("definition", ""))
    for r in hits["michigan"]:
        add("michigan_plmd.json", r.get("term", ""), r.get("definition", ""))
    for r in hits["justplainclear"]:
        add("justplainclear.json", r.get("term", ""), r.get("definition", ""))
    for cand in hits["dorland"]:
        add("dorland_medical_abbreviations.csv", term, cand)
    for r in hits["wiktionary"]:
        add("wiktionary.json", r.get("term", ""), r.get("definition", ""))
    for dd in hits["dictionary"]:
        pos = f" ({dd.get('pos')})" if dd.get("pos") else ""
        add("dictonary.csv", (dd.get("word") or term) + pos, dd.get("definition", ""))
    for r in hits["thesaurus"]:
        add("thesarus.json", r.get("term", ""), r.get("definition", ""))
    return attribs


def _apply_dictionary_policy(attribs: List[Dict[str, Any]], policy: str
                             ) -> List[Dict[str, Any]]:
    if policy != "last_resort" or not attribs:
        return attribs
    better = [a for a in attribs if a.get("source") != "dictonary.csv"]
    return better or attribs


def _second_hop(term: str, attribs: List[Dict[str, Any]],
                sources: Dict[str, Any]) -> int:
    hop_index = sources.get("hop_index")
    if not hop_index or not attribs:
        return 0
    seen = {(a.get("definition") or "").strip().lower()[:200] for a in attribs}
    seen_terms = {(a.get("term") or "").strip().lower() for a in attribs}
    added = 0
    for a in list(attribs):
        definition = a.get("definition") or ""
        if not looks_like_expansion(term, definition):
            continue
        hits = list(hop_lookup(definition, hop_index))
        if not hits and sources.get("hop_split_expansion"):
            hits = _hop_split_expansion(definition, hop_index)
        for src, entry in hits:
            head = (entry.get("term") or "").strip()
            body = (entry.get("definition") or "").strip()
            norm = body.lower()[:200]
            if not body or norm in seen or head.lower() in seen_terms:
                continue
            if looks_like_expansion(head, body):
                continue
            seen.add(norm)
            rec = {
                "source": HOP_SOURCE_FILE.get(src, src),
                "term": head,
                "definition": body,
                "via_expansion": definition.strip(),
            }
            if src == "readme" and entry.get("entry_id"):
                rec["entry_id"] = entry["entry_id"]
            attribs.append(rec)
            added += 1
    return added


def lookup_term(term: str, kind: str, sources: Dict[str, Any],
                use_variants: bool = True,
                dictionary_policy: str = "always"
                ) -> Tuple[List[Dict[str, Any]], Optional[str]]:
    forms = surface_variants(term) if use_variants else [term]
    for i, form in enumerate(forms):
        hits = _raw_lookup(form, kind, sources)
        attribs = _apply_dictionary_policy(
            _build_attributions(term, hits), dictionary_policy)
        if attribs:
            _second_hop(term, attribs, sources)
            return attribs, ("exact" if i == 0 else form)
    return [], None


_SPLIT_MED_SUFFIXES = (
    "ectomy", "otomy", "ostomy", "scopy", "plasty", "tripsy",
    "itis", "osis", "emia", "uria", "algia", "pathy", "trophy",
    "rrhea", "rrhage", "rrhagia", "phobia", "pnea", "spasm",
    "logy", "logist", "graphy", "gram", "centesis", "lysis",
)
_ROUTE_UNIT_ABBREVS = {
    "g", "kg", "mg", "mcg", "ug", "ng", "ml", "dl", "mmol", "meq", "iu",
    "mmhg", "bpm", "iv", "im", "po", "pr", "sq", "sc", "sl",
    "bid", "tid", "qid", "qhs", "prn", "npo", "q4h", "q6h", "q8h", "q12h",
}
_ABBREV_SHAPE = re.compile(
    r"^[A-Za-z]{1,4}(?:[/.\-][A-Za-z]{0,4})+$"
    r"|^[A-Za-z]{1,3}\d+[A-Za-z]?$"
    r"|^[A-Za-z]{1,5}\d[A-Za-z]*$"
)


def _classify_piece(text: str, has_dorland: bool) -> Tuple[str, str, str]:
    t = text.strip()
    lc = t.lower()
    multi = " " in t
    if not multi and lc in _ROUTE_UNIT_ABBREVS:
        return "abbreviation", "abbreviation_route_unit", "abbr_expand"
    abbr_shape = (not multi) and (
        bool(_ABBREV_SHAPE.match(t))
        or (len(t) >= 2 and t.isalpha() and t.isupper())
        or sum(1 for c in t if c.isupper()) >= 2
        or lc in _ROUTE_UNIT_ABBREVS
    )
    if abbr_shape and has_dorland:
        return "abbreviation", "abbreviation_essential", "abbr_expand_elaborate"
    if abbr_shape:
        try:
            from wordfreq import zipf_frequency
            z = zipf_frequency(lc, "en")
        except ImportError:
            z = 0.0
        if z < 4.0:
            return "abbreviation", "abbreviation_essential", "abbr_expand_elaborate"
    if not multi and any(lc.endswith(s) for s in _SPLIT_MED_SUFFIXES):
        return "word", "medical_essential", "elaborate"
    if multi:
        return "phrase", "medical_essential", "elaborate"
    return "word", "medical_descriptor", "replace"


_COMMON_ZIPF = 4.5


def _piece_worth_showing(piece: str) -> bool:
    p = piece.strip()
    if " " in p:
        return True
    lc = p.lower()
    if any(lc.endswith(s) for s in _SPLIT_MED_SUFFIXES):
        return True
    if _ABBREV_SHAPE.match(p) or (len(p) >= 2 and p.isalpha() and p.isupper()):
        return True
    try:
        from wordfreq import zipf_frequency
        return zipf_frequency(lc, "en") < _COMMON_ZIPF
    except ImportError:
        return True


def split_uncovered(term: str, sources: Dict[str, Any], use_variants: bool,
                    dictionary_policy: str = "always"
                    ) -> List[Dict[str, Any]]:
    words = WORD_RE.findall(term)
    if len(words) < 2:
        return []

    cache: Dict[str, bool] = {}

    def can_define(piece: str) -> bool:
        key = piece.lower()
        if key not in cache:
            kind = classify_term_kind(piece, sources["dorland"])
            attribs, _ = lookup_term(piece, kind, sources, use_variants,
                                     dictionary_policy)
            cache[key] = bool(attribs)
        return cache[key]

    partition, ok = find_best_partition(words, can_define)
    origin = "split_from_uncovered"
    if not ok:
        partition, _ = find_partial_partition(words, can_define)
        partition = [p for p in partition
                     if can_define(p) and _piece_worth_showing(p)]
        origin = "partial_split_from_uncovered"
    if not partition:
        return []

    out: List[Dict[str, Any]] = []
    for piece in partition:
        if piece.strip().lower() == term.strip().lower():
            continue
        has_med = bool(dorland_lookup(piece, sources["dorland"])) if len(piece) <= 8 else False
        kind, category, action = _classify_piece(piece, has_med)
        attribs, variant = lookup_term(piece, kind, sources, use_variants,
                                       dictionary_policy)
        if not attribs:
            continue
        out.append({
            "text": piece, "kind": kind, "category": category, "action": action,
            "attributions": attribs, "lookup_variant": variant,
            "origin": origin, "parent_term": term,
            "features": {},
        })
    return out


def build_sources_for_note(hard_items: List[Dict[str, Any]], max_sources: int
                           ) -> List[Dict[str, Any]]:
    ctx = []
    for item in hard_items:
        attribs = [a for a in (item.get("attributions") or []) if a.get("definition")]
        if not attribs:
            continue
        ctx.append({
            "term": item.get("text", ""),
            "kind": item.get("kind", "word"),
            "category": item.get("category", ""),
            "action": item.get("action", "replace"),
            "attribs": attribs,
        })
    if not ctx:
        return []

    ctx.sort(key=lambda c: (len(c["attribs"]),
                            min(len(a["definition"]) for a in c["attribs"])))

    sources: List[Dict[str, Any]] = []
    seen: set = set()
    depth = max(len(c["attribs"]) for c in ctx)
    for k in range(depth):
        for c in ctx:
            if k >= len(c["attribs"]):
                continue
            a = c["attribs"][k]
            sid = f"{c['term']}::{a.get('source', '?')}::{k}"
            if sid in seen:
                continue
            seen.add(sid)
            entry_term = a.get("term", c["term"])
            sources.append({
                "id": sid,
                "term": c["term"],
                "term_in_source": entry_term,
                "text": f"{entry_term}: {a.get('definition', '')}",
                "passage": a.get("definition", ""),
                "source": source_label(a.get("source", "?")),
                "raw_source": a.get("source", ""),
                "kind": c["kind"],
                "category": c["category"],
                "action": c["action"],
            })
            if len(sources) >= max_sources:
                return sources
    return sources


def run(cfg: Config, notes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    sources = load_sources(cfg)

    for note in notes:
        rule(f"note {note['note_idx']}  ({note.get('id')})")
        enriched: List[Dict[str, Any]] = []
        for item in note.get("hard_items", []):
            term = item.get("text", "")
            kind = item.get("kind") or classify_term_kind(term, sources["dorland"])
            attribs, variant = lookup_term(term, kind, sources,
                                           cfg.retrieval_normalise,
                                           cfg.dictionary_policy)
            item = dict(item)
            item["attributions"] = attribs
            item["lookup_variant"] = variant
            enriched.append(item)

            if attribs:
                tag = "" if variant == "exact" else f"  via {variant!r}"
                print(f"    {term:<34} {len(attribs)} def(s)  "
                      f"[{', '.join(sorted({source_label(a['source']) for a in attribs}))}]{tag}")
            else:
                print(f"    {term:<34} --  NO DEFINITION")
                if cfg.retrieval_split_uncovered and " " in term:
                    pieces = split_uncovered(term, sources,
                                             cfg.retrieval_normalise,
                                             cfg.dictionary_policy)
                    for p in pieces:
                        print(f"        split -> {p['text']:<26} "
                              f"{len(p['attributions'])} def(s)")
                    enriched.extend(pieces)

        note["hard_items"] = enriched
        note["retrieval"] = coverage_for_note(enriched, cfg.zipf_strata)
        note["sources"] = build_sources_for_note(enriched, cfg.cc_max_sources)
        note["source_alignment"] = source_alignment_for_note(
            enriched, note["sources"], tuple(cfg.zipf_strata))
        orph = note["source_alignment"]["orphan_terms"]
        cov = note["retrieval"]["coverage"]
        print(f"    coverage {cov if cov is not None else 'n/a'}   "
              f"glossary budget: {len(note['sources'])}/{cfg.cc_max_sources} entries")
        if orph:
            print(f"    [orphan] {len(orph)} term(s) have NO entry about them "
                  f"in the prompt: {', '.join(repr(t) for t in orph[:6])}")

    return notes
