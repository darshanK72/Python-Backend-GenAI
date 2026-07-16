"""File-backed session history shared between graph and MCP server."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TypedDict

from app.config import SESSION_STORE_PATH


class SessionEntry(TypedDict):
    """One turn recorded in session history."""

    turn: int
    query: str
    worker: str
    summary: str


# _store_path - resolve the session store path (call-time, patch-friendly)
def _store_path(path: Path | None = None) -> Path:
    return path or SESSION_STORE_PATH


# _ensure_store_file - create the JSON store file if it does not exist
def _ensure_store_file(path: Path | None = None) -> Path:
    target = _store_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        target.write_text("{}", encoding="utf-8")
    return target


# load_store - read the full session store from disk
def load_store(path: Path | None = None) -> dict[str, list[SessionEntry]]:
    target = _ensure_store_file(path)
    payload = json.loads(target.read_text(encoding="utf-8"))
    return payload if isinstance(payload, dict) else {}


# save_store - write the full session store to disk
def save_store(
    store: dict[str, list[SessionEntry]],
    path: Path | None = None,
) -> None:
    target = _ensure_store_file(path)
    target.write_text(json.dumps(store, indent=2), encoding="utf-8")


# append_entry - append one turn for a thread_id
def append_entry(
    thread_id: str,
    entry: SessionEntry,
    path: Path | None = None,
) -> None:
    store = load_store(path)
    history = store.setdefault(thread_id, [])
    history.append(entry)
    save_store(store, path)


# get_history - return the turn list for one thread
def get_history(thread_id: str, path: Path | None = None) -> list[SessionEntry]:
    store = load_store(path)
    return list(store.get(thread_id, []))


# format_history - format a recap or an empty-session message
def format_history(thread_id: str, path: Path | None = None) -> str:
    history = get_history(thread_id, path)
    if not history:
        return "No prior queries in this session"
    lines = []
    for item in history:
        lines.append(
            f"Turn {item['turn']}: [{item['worker']}] {item['query']} -> {item['summary']}"
        )
    return "\n".join(lines)


# clear_store - reset the session store to an empty object
def clear_store(path: Path | None = None) -> None:
    save_store({}, path)
