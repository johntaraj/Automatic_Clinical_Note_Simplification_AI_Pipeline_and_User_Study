"""Human-edit recall and replacement-level comparison with the clinician reference."""

from __future__ import annotations

import difflib
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .text import content_words, contains_term, tokens


def _find_sublist(hay: Sequence[str], needle: Sequence[str]
                  ) -> Optional[Tuple[int, int]]:
    if not needle or len(needle) > len(hay):
        return None
    first = needle[0]
    width = len(needle)
    for i in range(len(hay) - width + 1):
        if hay[i] == first and list(hay[i:i + width]) == list(needle):
            return i, i + width
    return None


def _aligned_span(orig_toks: Sequence[str], other_toks: Sequence[str],
                  lo: int, hi: int,
                  blocked: Sequence[Tuple[int, int]] = ()
                  ) -> Optional[List[str]]:
    sm = difflib.SequenceMatcher(a=list(orig_toks), b=list(other_toks),
                                 autojunk=False)
    out: List[str] = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if i2 <= lo or i1 >= hi:
            continue
        if tag == "equal":
            s, e = max(i1, lo), min(i2, hi)
            out.extend(other_toks[j1 + (s - i1):j1 + (e - i1)])
            continue
        if any(b_lo < i2 and i1 < b_hi for b_lo, b_hi in blocked):
            return None
        out.extend(other_toks[j1:j2])
    return out


def _token_f1(a: Sequence[str], b: Sequence[str]) -> Optional[float]:
    sa = content_words(" ".join(a))
    sb = content_words(" ".join(b))
    if not sa or not sb:
        return None
    hit = len(sa & sb)
    if not hit:
        return 0.0
    p, r = hit / len(sa), hit / len(sb)
    return 2 * p * r / (p + r)


def replacement_quality(orig: str, ref: str, sys_out: str,
                        terms: Sequence[str]) -> Dict[str, Any]:
    o = tokens(orig)
    r = tokens(ref)
    s = tokens(sys_out)
    rows: List[Dict[str, Any]] = []
    scores: List[float] = []
    edited: List[float] = []
    ambiguous = 0

    located: List[Tuple[str, Tuple[int, int]]] = []
    seen = set()
    for term in terms:
        term = (term or "").strip()
        key = term.lower()
        if not term or key in seen:
            continue
        seen.add(key)
        at = _find_sublist(o, tokens(term))
        if at is not None:
            located.append((term, at))

    located.sort(key=lambda kv: (kv[1][0] - kv[1][1], kv[1][0]))
    kept: List[Tuple[str, Tuple[int, int]]] = []
    for term, (lo, hi) in located:
        if any(k_lo <= lo and hi <= k_hi for _, (k_lo, k_hi) in kept):
            continue
        kept.append((term, (lo, hi)))

    for term, (lo, hi) in kept:
        others = [span for other, span in kept if other != term]
        gold = _aligned_span(o, r, lo, hi, others)
        got = _aligned_span(o, s, lo, hi, others)
        if gold is None or got is None:
            ambiguous += 1
            rows.append({"term": term, "ambiguous": True, "f1": None})
            continue
        f1 = _token_f1(got, gold)
        human_edited = [w.lower() for w in gold] != [w.lower()
                                                     for w in tokens(term)]
        rows.append({
            "term": term,
            "gold_replacement": " ".join(gold),
            "sys_replacement": " ".join(got),
            "human_edited": human_edited,
            "f1": None if f1 is None else round(f1, 3),
        })
        if f1 is not None:
            scores.append(f1)
            if human_edited:
                edited.append(f1)

    return {
        "replacement_quality": (round(sum(scores) / len(scores), 3)
                                if scores else None),
        "replacement_quality_edited": (round(sum(edited) / len(edited), 3)
                                       if edited else None),
        "replacement_hit_rate": (round(sum(1 for x in scores if x > 0)
                                       / len(scores), 3) if scores else None),
        "n_replacement_aligned": len(scores),
        "n_replacement_edited": len(edited),
        "n_replacement_ambiguous": ambiguous,
        "per_replacement": rows,
    }


def _supported_vocabulary(term: str, defs: List[Dict[str, Any]],
                          ref: str, orig: str):
    tw = set(w.lower() for w in term.split())
    def_words: set = set()
    for d in defs or []:
        dt = d.get("definition") or d.get("text") or d.get("passage") or ""
        def_words |= (content_words(dt) - tw)
    ref_added = content_words(ref) - content_words(orig)
    return def_words, ref_added


def edit_replacement(orig: str, ref: str, sys_out: str,
                     hard_terms: List[Dict[str, Any]]
                     ) -> Optional[Dict[str, Any]]:
    if not (ref or "").strip() or not hard_terms:
        return None

    orig_cw = content_words(orig)
    ref_cw = content_words(ref)
    sys_cw = content_words(sys_out)

    gold = recalled = copied = 0
    sys_changes = supported = borrowed = 0
    per_term: List[Dict[str, Any]] = []
    seen = set()

    for it in hard_terms:
        term = (it.get("text") or it.get("term") or "").strip()
        key = term.lower()
        if not term or key in seen:
            continue
        seen.add(key)
        defs = it.get("attributions") or it.get("definitions") or []

        gold_simpl = not contains_term(ref, term)
        sys_simpl = not contains_term(sys_out, term)
        is_supported = None
        is_borrowed = None

        if gold_simpl:
            gold += 1
            if sys_simpl:
                recalled += 1
            else:
                copied += 1

        if sys_simpl:
            sys_changes += 1
            def_words, ref_added = _supported_vocabulary(term, defs, ref, orig)
            is_supported = bool(ref_added & sys_cw)
            is_borrowed = bool(def_words & sys_cw)
            if is_supported:
                supported += 1
            if is_borrowed:
                borrowed += 1

        per_term.append({
            "term": term,
            "gold_simplified": gold_simpl,
            "sys_simplified": sys_simpl,
            "supported": is_supported,
            "borrowed_from_definition": is_borrowed,
        })

    recall = recalled / gold if gold else None
    precision = supported / sys_changes if sys_changes else None
    f1 = None
    if recall is not None and precision is not None and (recall + precision) > 0:
        f1 = 2 * recall * precision / (recall + precision)
    elif recall == 0.0:
        f1 = 0.0

    hard_set = {(it.get("text") or it.get("term") or "").strip().lower()
                for it in hard_terms}
    removed_by_sys = orig_cw - sys_cw
    removed_by_ref = orig_cw - ref_cw
    extra = {w for w in removed_by_sys
             if w not in removed_by_ref
             and not any(w in h for h in hard_set if h)}
    aggressiveness = len(extra) / (len(removed_by_sys) or 1)

    quality = replacement_quality(
        orig, ref, sys_out,
        [(it.get("text") or it.get("term") or "") for it in hard_terms])

    return {
        "human_edit_recall": round(recall, 3) if recall is not None else None,
        "replacement_precision": round(precision, 3) if precision is not None else None,
        "replacement_f1": round(f1, 3) if f1 is not None else None,
        "replacement_quality": quality["replacement_quality"],
        "replacement_quality_edited": quality["replacement_quality_edited"],
        "replacement_hit_rate": quality["replacement_hit_rate"],
        "n_replacement_aligned": quality["n_replacement_aligned"],
        "n_replacement_edited": quality["n_replacement_edited"],
        "n_replacement_ambiguous": quality["n_replacement_ambiguous"],
        "definition_borrow_rate": (round(borrowed / sys_changes, 3)
                                   if sys_changes else None),
        "copy_jargon_rate": round(copied / gold, 3) if gold else None,
        "rewrite_aggressiveness": round(aggressiveness, 3),
        "n_gold_edits": gold,
        "n_sys_edits": sys_changes,
        "n_borrowed": borrowed,
        "per_term": per_term,
        "per_replacement": quality["per_replacement"],
    }
