"""On-disk cache for LLM responses, keyed by request content."""

from __future__ import annotations

import hashlib
import json
import threading
from pathlib import Path
from typing import Any, Dict, Optional

SCHEMA = "v1"


class ResponseCache:
    def __init__(self, root: Optional[Path], enabled: bool = True):
        self.root = Path(root) if root else None
        self.enabled = bool(enabled and root)
        self._lock = threading.Lock()
        self.hits = 0
        self.misses = 0
        self.writes = 0
        if self.enabled:
            self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key: str) -> Path:
        return self.root / key[:2] / f"{key}.json"

    @staticmethod
    def make_key(kind: str, model: str, prompt: str, response: str = "") -> str:
        h = hashlib.sha256()
        for part in (SCHEMA, kind, model, prompt, response):
            h.update(part.encode("utf-8", "replace"))
            h.update(b"\x00")
        return h.hexdigest()

    def get(self, key: str) -> Optional[Any]:
        if not self.enabled:
            return None
        p = self._path(key)
        if not p.exists():
            with self._lock:
                self.misses += 1
            return None
        try:
            value = json.loads(p.read_text(encoding="utf-8"))["v"]
        except Exception:
            with self._lock:
                self.misses += 1
            return None
        with self._lock:
            self.hits += 1
        return value

    def put(self, key: str, value: Any) -> None:
        if not self.enabled:
            return
        p = self._path(key)
        try:
            p.parent.mkdir(parents=True, exist_ok=True)
            tmp = p.with_suffix(".tmp")
            tmp.write_text(json.dumps({"v": value}), encoding="utf-8")
            tmp.replace(p)
            with self._lock:
                self.writes += 1
        except Exception:
            pass

    def stats(self) -> Dict[str, Any]:
        total = self.hits + self.misses
        return {
            "enabled": self.enabled,
            "hits": self.hits,
            "misses": self.misses,
            "writes": self.writes,
            "hit_rate": round(self.hits / total, 4) if total else None,
            "dir": str(self.root) if self.root else None,
        }

    def reset_stats(self) -> None:
        with self._lock:
            self.hits = self.misses = self.writes = 0


_CACHE = ResponseCache(None, enabled=False)


def configure(root: Optional[Path], enabled: bool = True) -> ResponseCache:
    global _CACHE
    _CACHE = ResponseCache(root, enabled)
    return _CACHE


def get_cache() -> ResponseCache:
    return _CACHE
