"""Shared environment loader for LLM API Integration scripts."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


def find_repo_root(start: Path | None = None) -> Path:
    """Walk up from *start* until we find the repo root (requirements.txt)."""
    start = start or Path(__file__).resolve().parent
    for candidate in (start, *start.parents):
        if (candidate / "requirements.txt").is_file():
            return candidate
    raise RuntimeError("Could not find repo root (requirements.txt)")


def load_project_env(*, local_env: Path | None = None) -> Path:
    """
    Load environment variables from the repo-root .env, then an optional local .env.

    Local values override global ones. Returns the repo root path.
    """
    repo_root = find_repo_root()
    global_env = repo_root / ".env"
    if global_env.is_file():
        load_dotenv(global_env, override=False)

    if local_env and local_env.is_file():
        load_dotenv(local_env, override=True)

    return repo_root


def require_key(name: str) -> str | None:
    """Load env files and return *name* or print a helpful message."""
    load_project_env()
    value = os.getenv(name, "").strip()
    if value:
        return value
    print(f"Missing {name}. Add it to the repo root .env (see example.env).")
    return None
