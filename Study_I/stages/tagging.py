"""Parses <replace orig="..."> edit tags and anchors them in the rewritten sentence."""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

TAG_RE = re.compile(
    r'<(?P<tag>replace|elaborate|abbr)\b(?P<attrs>[^>]*)>'
    r'(?P<body>.*?)</(?P=tag)>',
    re.IGNORECASE | re.DOTALL,
)
ORIG_RE = re.compile(r'orig\s*=\s*"([^"]*)"', re.IGNORECASE)

STOP_BODIES = {"a", "an", "the", "of", "in", "on", "to", "and", "or",
               "for", "is", "was", "be", "by", "at", "it"}


def surface_spans(text: str, surface: str) -> List[Tuple[int, int]]:
    s = (surface or "").strip()
    if not s or not text:
        return []
    pattern = re.escape(s).replace(r"\ ", r"\s+")
    left = r"(?<!\w)" if s[0].isalnum() else ""
    right = r"(?!\w)" if s[-1].isalnum() else ""
    try:
        rx = re.compile(left + pattern + right, re.IGNORECASE)
    except re.error:
        return []
    return [(m.start(), m.end()) for m in rx.finditer(text)]


def _norm(s: str) -> str:
    return re.sub(r"[\s\W_]+", "", (s or "").lower())


def extract_operations(tagged: str) -> Tuple[List[Dict[str, Any]], str]:
    ops: List[Dict[str, Any]] = []
    chunks: List[str] = []
    plain_pos = 0
    last = 0

    for m in TAG_RE.finditer(tagged):
        before = tagged[last:m.start()]
        chunks.append(before)
        plain_pos += len(before)

        body = m.group("body")
        orig_m = ORIG_RE.search(m.group("attrs") or "")
        tag = m.group("tag").lower()
        bs, be = m.span("body")

        ops.append({
            "type": {"abbr": "abbr_expand"}.get(tag, tag),
            "src_text": orig_m.group(1).strip() if orig_m else None,
            "tgt_text": body,
            "span_tagged": [bs, be],
            "span_plain": [plain_pos, plain_pos + len(body)],
        })
        chunks.append(body)
        plain_pos += len(body)
        last = m.end()

    chunks.append(tagged[last:])
    return ops, "".join(chunks)


def filter_operations(ops: List[Dict[str, Any]], original: str, prose: str,
                      hard_terms: Optional[List[str]] = None
                      ) -> Tuple[List[Dict[str, Any]], List[str]]:
    kept: List[Dict[str, Any]] = []
    audit: List[str] = []
    hard_norm = {re.sub(r"\s+", " ", t).strip().lower()
                 for t in (hard_terms or []) if t}

    for op in ops:
        src = (op.get("src_text") or "").strip()
        tgt = (op.get("tgt_text") or "").strip()

        if src and tgt and _norm(src) == _norm(tgt):
            audit.append(f"DROP noop      {src!r} -> {tgt!r}  (nothing changed)")
            continue
        if tgt.lower() in STOP_BODIES or len(tgt) < 2:
            audit.append(f"DROP filler    {src!r} -> {tgt!r}  (body is filler)")
            continue
        src_norm = re.sub(r"\s+", " ", src).strip().lower()
        if not src_norm or (hard_norm and src_norm not in hard_norm):
            audit.append(f"DROP non-term  {src!r} -> {tgt!r}  "
                         f"(orig is not exactly one extracted hard term)")
            continue
        if not surface_spans(original, src):
            audit.append(f"DROP no-orig   {src!r} -> {tgt!r}  (orig not in input)")
            continue
        if not surface_spans(prose, tgt):
            audit.append(f"DROP no-body   {src!r} -> {tgt!r}  (body not in prose)")
            continue
        kept.append(op)
    return kept, audit


def retag_prose(prose: str, ops: List[Dict[str, Any]]
                ) -> Tuple[List[Dict[str, Any]], str]:
    if not ops or not prose:
        return ops, prose

    occupied: List[Tuple[int, int]] = []
    placed: List[Tuple[int, int, Dict[str, Any]]] = []

    def overlaps(s: int, e: int) -> bool:
        return any(not (e <= a or s >= b) for a, b in occupied)

    for op in sorted(ops, key=lambda o: -len(o.get("tgt_text") or "")):
        body = (op.get("tgt_text") or "").strip()
        if not body:
            continue
        for s, e in surface_spans(prose, body):
            if not overlaps(s, e):
                occupied.append((s, e))
                placed.append((s, e, op))
                break

    placed.sort(key=lambda t: t[0])

    kept: List[Dict[str, Any]] = []
    pieces: List[str] = []
    cursor = 0
    for start, end, op in placed:
        if start < cursor:
            continue
        pieces.append(prose[cursor:start])
        kind = op.get("type", "replace")
        src = op.get("src_text") or ""
        body_actual = prose[start:end]
        tag = {"replace": "replace", "elaborate": "elaborate"}.get(kind, "abbr")
        open_tag, close_tag = f'<{tag} orig="{src}">', f"</{tag}>"
        tagged_start = sum(len(p) for p in pieces) + len(open_tag)
        pieces.append(f"{open_tag}{body_actual}{close_tag}")
        op = dict(op)
        op["span_plain"] = [start, end]
        op["span_tagged"] = [tagged_start, tagged_start + len(body_actual)]
        kept.append(op)
        cursor = end
    pieces.append(prose[cursor:])
    return kept, "".join(pieces)


def tag_input(sentence: str, hard_terms: List[str]) -> str:
    candidates: List[Tuple[int, int]] = []
    seen = set()
    for raw in hard_terms:
        term = (raw or "").strip()
        key = re.sub(r"\s+", " ", term).lower()
        if not term or key in seen:
            continue
        seen.add(key)
        candidates.extend(surface_spans(sentence, term))

    chosen: List[Tuple[int, int]] = []
    for s, e in sorted(candidates, key=lambda sp: (-(sp[1] - sp[0]), sp[0])):
        if any(not (e <= a or s >= b) for a, b in chosen):
            continue
        chosen.append((s, e))
    chosen.sort()

    out: List[str] = []
    cursor = 0
    for s, e in chosen:
        out.append(sentence[cursor:s])
        out.append(f"<hard>{sentence[s:e]}</hard>")
        cursor = e
    out.append(sentence[cursor:])
    return "".join(out)
