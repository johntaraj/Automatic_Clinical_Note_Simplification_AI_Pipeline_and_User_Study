"""Retrieval coverage and source-alignment metrics."""

from __future__ import annotations

import re
import statistics
from typing import Any, Dict, List, Optional, Sequence

try:
    from wordfreq import zipf_frequency
except ImportError:
    zipf_frequency = None


def term_zipf(term: str) -> Optional[float]:
    if zipf_frequency is None:
        return None
    t = (term or "").strip().lower()
    if not t:
        return None
    words = [w for w in t.split() if w.isalpha()]
    if not words:
        return None
    vals = [zipf_frequency(w, "en") for w in words]
    vals = [v for v in vals if v is not None]
    return round(min(vals), 2) if vals else None


def zipf_stratum(z: Optional[float], edges: Sequence[float]) -> str:
    if z is None:
        return "unknown"
    names = ["very_rare", "rare", "uncommon", "common"]
    for i, e in enumerate(edges):
        if z < e:
            return names[min(i, len(names) - 1)]
    return names[-1]


def coverage_for_note(hard_items: List[Dict[str, Any]],
                      zipf_edges: Sequence[float] = (2.5, 3.5, 4.5)
                      ) -> Dict[str, Any]:
    split_parents = {
        (it.get("parent_term") or "").strip().lower()
        for it in hard_items or []
        if it.get("parent_term") and it.get("attributions")
    }
    split_parents.discard("")

    rows: List[Dict[str, Any]] = []
    for it in hard_items or []:
        term = (it.get("text") or it.get("term") or "").strip()
        if not term:
            continue
        attribs = it.get("attributions") or []
        sources = sorted({a.get("source", "?") for a in attribs})
        z = term_zipf(term)
        covered = bool(attribs)
        rows.append({
            "term": term,
            "kind": it.get("kind"),
            "category": it.get("category"),
            "action": it.get("action"),
            "n_defs": len(attribs),
            "covered": covered,
            "addressed": covered or term.lower() in split_parents,
            "n_hopped": sum(1 for a in attribs if a.get("via_expansion")),
            "sources": sources,
            "zipf": z,
            "stratum": zipf_stratum(z, zipf_edges),
            "lookup_variant": it.get("lookup_variant"),
            "origin": it.get("origin", "extracted"),
        })
    n = len(rows)
    covered = sum(1 for r in rows if r["covered"])
    ext = [r for r in rows if r["origin"] == "extracted"]
    n_ext = len(ext)
    cov_ext = sum(1 for r in ext if r["covered"])
    addressed = sum(1 for r in ext if r["addressed"])
    return {
        "n_terms": n_ext,
        "n_covered": cov_ext,
        "coverage": round(cov_ext / n_ext, 4) if n_ext else None,
        "n_addressed": addressed,
        "coverage_addressed": round(addressed / n_ext, 4) if n_ext else None,
        "n_hopped": sum(r["n_hopped"] for r in rows),
        "n_terms_incl_salvage": n,
        "n_covered_incl_salvage": covered,
        "coverage_incl_salvage": round(covered / n, 4) if n else None,
        "n_salvaged": n - n_ext,
        "mean_defs_per_term": round(
            statistics.fmean([r["n_defs"] for r in ext]), 2) if ext else None,
        "per_term": rows,
    }


def source_matches_term(term: str, source: Dict[str, Any]) -> bool:
    entry = str(source.get("term") or "").strip().lower()
    t = (term or "").strip().lower()
    if not entry or not t:
        return False
    if entry in t or t in entry:
        return True
    return bool(set(entry.split()) & set(t.split()))


def source_alignment_for_note(hard_items: List[Dict[str, Any]],
                              sources: List[Dict[str, Any]],
                              zipf_edges: Sequence[float] = (2.5, 3.5, 4.5)
                              ) -> Dict[str, Any]:
    n_src = len(sources or [])
    rows: List[Dict[str, Any]] = []
    for it in hard_items or []:
        term = (it.get("text") or it.get("term") or "").strip()
        if not term:
            continue
        related = [s for s in (sources or []) if source_matches_term(term, s)]
        z = term_zipf(term)
        rows.append({
            "term": term,
            "n_related": len(related),
            "n_noise": n_src - len(related),
            "has_own_source": bool(related),
            "related_sources": sorted({s.get("source") for s in related}),
            "zipf": z,
            "stratum": zipf_stratum(z, zipf_edges),
        })
    n = len(rows)
    orphans = [r for r in rows if not r["has_own_source"]]
    return {
        "n_terms": n,
        "n_sources_shown": n_src,
        "n_orphan_terms": len(orphans),
        "orphan_terms": [r["term"] for r in orphans],
        "orphan_term_rate": round(len(orphans) / n, 4) if n else None,
        "on_term_sources": round(
            statistics.fmean([r["n_related"] for r in rows]), 2) if rows else None,
        "on_term_source_share": round(
            statistics.fmean([r["n_related"] / n_src for r in rows]), 4)
        if rows and n_src else None,
        "per_term": rows,
    }


def source_alignment_summary(per_note: List[Dict[str, Any]]) -> Dict[str, Any]:
    rows: List[Dict[str, Any]] = []
    for note in per_note:
        rows.extend((note.get("source_alignment") or {}).get("per_term") or [])
    if not rows:
        return {}

    def _bucket(rs: List[Dict[str, Any]]) -> Dict[str, Any]:
        n = len(rs)
        orph = sum(1 for r in rs if not r["has_own_source"])
        return {
            "n_terms": n,
            "n_orphan": orph,
            "orphan_term_rate": round(orph / n, 4) if n else None,
            "on_term_sources": round(
                statistics.fmean([r["n_related"] for r in rs]), 2),
        }

    strata = {name: _bucket([r for r in rows if r["stratum"] == name])
              for name in ("very_rare", "rare", "uncommon", "common", "unknown")
              if any(r["stratum"] == name for r in rows)}
    worst = sorted((r for r in rows if not r["has_own_source"]),
                   key=lambda r: (r["zipf"] if r["zipf"] is not None else 99))
    return {
        "overall": _bucket(rows),
        "split_adjusted": split_adjusted_orphan_summary(per_note),
        "by_zipf_stratum": strata,
        "rarest_orphan_terms": [
            {"term": r["term"], "zipf": r["zipf"], "stratum": r["stratum"]}
            for r in worst[:15]
        ],
    }


_UNIT_WORD_RE = re.compile(r"[a-z0-9]+")


def _split_remainders(parent: str, children: List[str]) -> List[str]:
    parent_words = _UNIT_WORD_RE.findall((parent or "").lower())
    used = [False] * len(parent_words)
    for child in sorted(children, key=lambda text: -len(_UNIT_WORD_RE.findall(text))):
        child_words = _UNIT_WORD_RE.findall((child or "").lower())
        if not child_words:
            continue
        for start in range(len(parent_words) - len(child_words) + 1):
            end = start + len(child_words)
            if not any(used[start:end]) and parent_words[start:end] == child_words:
                used[start:end] = [True] * len(child_words)
                break

    remainders: List[str] = []
    start: Optional[int] = None
    for index, matched in enumerate(used + [True]):
        if not matched and start is None:
            start = index
        elif matched and start is not None:
            remainders.append(" ".join(parent_words[start:index]))
            start = None
    return remainders


def split_adjusted_orphan_summary(per_note: List[Dict[str, Any]]) -> Dict[str, Any]:
    rows: List[Dict[str, Any]] = []
    for note in per_note:
        items = note.get("hard_items") or []
        sources = note.get("sources") or []
        children_by_parent: Dict[str, List[Dict[str, Any]]] = {}
        for item in items:
            parent = (item.get("parent_term") or "").strip().lower()
            if parent:
                children_by_parent.setdefault(parent, []).append(item)

        for item in items:
            if (item.get("origin") or "extracted") != "extracted":
                continue
            term = (item.get("text") or item.get("term") or "").strip()
            if not term:
                continue
            children = children_by_parent.get(term.lower(), [])
            if not children:
                rows.append({
                    "term": term,
                    "kind": "original",
                    "has_own_source": any(source_matches_term(term, source)
                                          for source in sources),
                })
                continue

            child_terms = []
            for child in children:
                child_term = (child.get("text") or child.get("term") or "").strip()
                if not child_term:
                    continue
                child_terms.append(child_term)
                rows.append({
                    "term": child_term,
                    "kind": "split",
                    "parent_term": term,
                    "has_own_source": any(
                        source_matches_term(child_term, source) for source in sources),
                })
            for remainder in _split_remainders(term, child_terms):
                rows.append({
                    "term": remainder,
                    "kind": "unresolved_remainder",
                    "parent_term": term,
                    "has_own_source": any(
                        source_matches_term(remainder, source) for source in sources),
                })

    n_units = len(rows)
    orphans = [row for row in rows if not row["has_own_source"]]
    return {
        "n_units": n_units,
        "n_orphan": len(orphans),
        "split_adjusted_orphan_rate": (
            round(len(orphans) / n_units, 4) if n_units else None
        ),
        "orphan_units": [row["term"] for row in orphans],
        "per_unit": rows,
    }


def definition_readability(per_note: List[Dict[str, Any]]) -> Dict[str, Any]:
    from .readability import readability

    texts, zipfs = [], []
    by_source: Dict[str, List[float]] = {}
    for note in per_note:
        for s in note.get("sources") or []:
            text = (s.get("text") or "").strip()
            if not text:
                continue
            grade = readability(text).get("fkgl")
            if grade is None:
                continue
            texts.append(float(grade))
            by_source.setdefault(str(s.get("source") or "?"), []).append(float(grade))
            z = term_zipf(text)
            if z is not None:
                zipfs.append(z)
    if not texts:
        return {}
    return {
        "n_definitions": len(texts),
        "definition_fkgl": round(statistics.fmean(texts), 2),
        "definition_fkgl_median": round(statistics.median(texts), 2),
        "definition_min_zipf": round(statistics.fmean(zipfs), 2) if zipfs else None,
        "definition_redundancy": definition_redundancy(per_note),
        "by_source": {k: round(statistics.fmean(v), 2)
                      for k, v in sorted(by_source.items(),
                                         key=lambda kv: -statistics.fmean(kv[1]))},
    }


_REDUNDANCY_STOP = frozenset(
    "a an the of or and to in for is are be as that this on at from it its by "
    "with which who whose not no any some other such used use your you".split())


def definition_redundancy(per_note: List[Dict[str, Any]]) -> Optional[float]:
    scores: List[float] = []
    for note in per_note:
        by_term: Dict[str, List[set]] = {}
        for s in note.get("sources") or []:
            term = (s.get("term") or "").strip().lower()
            words = {w for w in re.findall(r"[a-z']+", (s.get("text") or "").lower())
                     if len(w) > 2 and w not in _REDUNDANCY_STOP}
            if term and words:
                by_term.setdefault(term, []).append(words)
        for sets in by_term.values():
            for i in range(len(sets)):
                for j in range(i + 1, len(sets)):
                    union = sets[i] | sets[j]
                    if union:
                        scores.append(len(sets[i] & sets[j]) / len(union))
    return round(statistics.fmean(scores), 4) if scores else None


def coverage_summary(per_note: List[Dict[str, Any]],
                     zipf_edges: Sequence[float] = (2.5, 3.5, 4.5)
                     ) -> Dict[str, Any]:
    all_rows: List[Dict[str, Any]] = []
    for note in per_note:
        all_rows.extend((note.get("retrieval") or {}).get("per_term") or [])
    rows = [r for r in all_rows if r.get("origin", "extracted") == "extracted"]

    def _bucket(rs: List[Dict[str, Any]]) -> Dict[str, Any]:
        n = len(rs)
        cov = sum(1 for r in rs if r["covered"])
        addr = sum(1 for r in rs if r.get("addressed", r["covered"]))
        return {
            "n_terms": n,
            "n_covered": cov,
            "coverage": round(cov / n, 4) if n else None,
            "n_addressed": addr,
            "coverage_addressed": round(addr / n, 4) if n else None,
            "mean_defs": round(statistics.fmean([r["n_defs"] for r in rs]), 2) if rs else None,
        }

    strata: Dict[str, Any] = {}
    for name in ("very_rare", "rare", "uncommon", "common", "unknown"):
        subset = [r for r in rows if r["stratum"] == name]
        if subset:
            strata[name] = _bucket(subset)

    by_source: Dict[str, int] = {}
    for r in all_rows:
        for s in r["sources"]:
            by_source[s] = by_source.get(s, 0) + 1

    by_origin: Dict[str, Any] = {}
    for name in sorted({r.get("origin", "extracted") for r in all_rows}):
        by_origin[name] = _bucket(
            [r for r in all_rows if r.get("origin", "extracted") == name])

    variants: Dict[str, int] = {}
    for r in all_rows:
        v = r.get("lookup_variant")
        if v:
            variants[v] = variants.get(v, 0) + 1

    return {
        "overall": _bucket(rows),
        "overall_incl_salvage": _bucket(all_rows),
        "by_zipf_stratum": strata,
        "definitions_by_source": dict(sorted(by_source.items(), key=lambda kv: -kv[1])),
        "by_origin": by_origin,
        "hits_by_lookup_variant": dict(sorted(variants.items(), key=lambda kv: -kv[1])),
        "n_expansion_definitions": sum(r.get("n_hopped", 0) for r in all_rows),
        "unaddressed_terms": sorted(
            {r["term"] for r in rows if not r.get("addressed", r["covered"])}
        )[:60],
        "uncovered_terms": sorted(
            {r["term"] for r in rows if not r["covered"]}
        )[:60],
    }
