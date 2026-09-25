"""JSON and logging helpers."""

from __future__ import annotations

import json
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, s):
        for st in self.streams:
            st.write(s)
            st.flush()

    def flush(self):
        for st in self.streams:
            st.flush()

    def isatty(self):
        return False

    def __getattr__(self, name):
        streams = self.__dict__.get("streams")
        if streams:
            return getattr(streams[0], name)
        raise AttributeError(name)


@contextmanager
def tee_to(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fh = open(path, "w", encoding="utf-8")
    original = sys.stdout
    sys.stdout = Tee(original, fh)
    try:
        yield
    finally:
        sys.stdout = original
        fh.close()


def load_json(path: Path, default: Any = None) -> Any:
    p = Path(path)
    if not p.exists():
        return default
    text = p.read_text(encoding="utf-8-sig")
    if not text.strip():
        return default
    return json.loads(text)


def save_json(path: Path, obj: Any) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False, default=str),
                 encoding="utf-8")
    return p


def banner(text: str, ch: str = "=", width: int = 78) -> None:
    line = ch * width
    print(f"\n{line}\n  {text}\n{line}")


def rule(text: str = "", width: int = 78) -> None:
    if text:
        print(f"\n  -- {text} " + "-" * max(0, width - len(text) - 7))
    else:
        print("  " + "-" * width)
