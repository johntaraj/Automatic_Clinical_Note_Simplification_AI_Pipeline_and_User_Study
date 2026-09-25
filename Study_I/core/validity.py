"""Detects outputs that are protocol text or prompt echoes rather than a rewrite."""

from __future__ import annotations

import re
from typing import List, Tuple

PATTERNS: List[Tuple[str, "re.Pattern[str]"]] = [
    ("response-header", re.compile(r"^\s*#{0,3}\s*response\s*:?\s*$", re.I)),
    ("response-inline", re.compile(r"#{2,3}\s*response\s*:", re.I)),
    ("instruction-echo", re.compile(r"#{2,3}\s*(instruction|input|task)\s*:", re.I)),
    ("channel-header", re.compile(r"\b(assistant|analysis|commentary)\s+to\s*=", re.I)),
    ("gloss-arrow", re.compile(r"^\s*\S[^\n]{0,120}\s->\s")),
    ("rewrite-imperative", re.compile(r"^\s*(rewrite|simplify)\s+(this|the)\b", re.I)),
    ("label-prefix", re.compile(
        r"^\s*(rewrite|rewritten|simplified|output|answer|response)\s*:", re.I)),
    ("repeated-label", re.compile(r"(\b\w+\s*:\s*)\1{2,}", re.I)),
    ("hard-tags-left", re.compile(r"</?hard>", re.I)),
    ("prompt-echo", re.compile(
        r"6th[- ]grade"
        r"|you rewrite clinical"
        r"|careful medical-text simplifier"
        r"|preserve the meaning exactly"
        r"|preserve meaning exactly"
        r"|do not add new facts"
        r"|output only the (rewritten|simplified)"
        r"|and nothing else"
        r"|stay exactly as they are", re.I)),
]


def output_problems(text: str) -> List[str]:
    t = (text or "").strip()
    if not t:
        return ["empty"]
    return [name for name, pat in PATTERNS if pat.search(t)]


def is_usable(text: str) -> bool:
    return not output_problems(text)
