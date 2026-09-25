"""Core components: LLM clients, ContextCite, response cache and vocabulary helpers."""

import sys as _sys

for _s in (_sys.stdout, _sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
