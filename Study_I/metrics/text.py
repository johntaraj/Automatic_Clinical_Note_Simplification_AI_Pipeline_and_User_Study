"""Shared tokenisation and text helpers."""

from __future__ import annotations

import re
from typing import Dict, List, Set, Tuple

_WORD_RE = re.compile(r"[A-Za-z0-9]+")
_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9-]*")

STOPWORDS: Set[str] = {
    "a", "an", "the", "of", "to", "in", "on", "by", "for", "with", "and",
    "or", "is", "was", "as", "from", "at", "that", "this", "these", "those",
    "be", "are", "were", "has", "have", "had", "his", "her", "their",
    "your", "you", "he", "she", "they", "it", "its", "i", "we", "us",
    "also", "when", "while", "than", "then", "so", "but",
    "patient", "patients", "medical", "clinical",
}


def tokens(s: str) -> List[str]:
    return _WORD_RE.findall((s or "").lower())


def content_words(text: str) -> Set[str]:
    return {t for t in (w.lower() for w in _TOKEN_RE.findall(text or ""))
            if len(t) >= 3 and t not in STOPWORDS}


def contains_term(text: str, term: str) -> bool:
    term = (term or "").strip()
    if not term:
        return False
    escaped = re.escape(term).replace(r"\ ", r"\s+")
    left = r"(?<!\w)" if term[0].isalnum() else ""
    right = r"(?!\w)" if term[-1].isalnum() else ""
    return re.search(left + escaped + right, text or "", re.IGNORECASE) is not None


def ngrams(toks: List[str], n: int) -> Dict[Tuple[str, ...], int]:
    out: Dict[Tuple[str, ...], int] = {}
    for i in range(len(toks) - n + 1):
        g = tuple(toks[i:i + n])
        out[g] = out.get(g, 0) + 1
    return out


def split_sentences(text: str) -> List[str]:
    text = (text or "").strip()
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if p.strip()]
