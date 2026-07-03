"""FastAPI dependencies."""

from __future__ import annotations

from functools import lru_cache

import anthropic
from fastapi import Depends, HTTPException

from app.config import Settings, get_settings


@lru_cache
def _build_client(api_key: str) -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=api_key)


def get_anthropic_client(
    settings: Settings = Depends(get_settings),
) -> anthropic.Anthropic:
    if not settings.anthropic_api_key:
        raise HTTPException(
            status_code=503,
            detail=(
                "ANTHROPIC_API_KEY is not configured. "
                "Add it to the repo root .env or this project's .env file."
            ),
        )
    return _build_client(settings.anthropic_api_key)
