"""Readability formulas (FKGL, FRE, SMOG, Coleman-Liau) and their change from the input."""

from __future__ import annotations

from typing import Any, Dict, Optional

import textstat

from .text import tokens


def readability(text: str) -> Dict[str, Optional[float]]:
    if not (text or "").strip():
        return {"fkgl": None, "fre": None, "smog": None,
                "coleman_liau": None, "n_words": 0}
    return {
        "fkgl": textstat.flesch_kincaid_grade(text),
        "fre": textstat.flesch_reading_ease(text),
        "smog": textstat.smog_index(text),
        "coleman_liau": textstat.coleman_liau_index(text),
        "n_words": len(tokens(text)),
    }


def readability_deltas(sys_m: Dict[str, Any], input_m: Dict[str, Any]
                       ) -> Dict[str, float]:
    out: Dict[str, float] = {}
    if sys_m.get("fkgl") is not None and input_m.get("fkgl") is not None:
        out["fkgl_drop"] = round(input_m["fkgl"] - sys_m["fkgl"], 2)
    if sys_m.get("fre") is not None and input_m.get("fre") is not None:
        out["fre_gain"] = round(sys_m["fre"] - input_m["fre"], 2)
    if sys_m.get("smog") is not None and input_m.get("smog") is not None:
        out["smog_drop"] = round(input_m["smog"] - sys_m["smog"], 2)
    if (sys_m.get("coleman_liau") is not None
            and input_m.get("coleman_liau") is not None):
        out["coleman_liau_drop"] = round(
            input_m["coleman_liau"] - sys_m["coleman_liau"], 2)
    return out


def length_ratio(sys_out: str, ref: str) -> Optional[float]:
    rw = len(tokens(ref))
    if not rw:
        return None
    return len(tokens(sys_out)) / rw
