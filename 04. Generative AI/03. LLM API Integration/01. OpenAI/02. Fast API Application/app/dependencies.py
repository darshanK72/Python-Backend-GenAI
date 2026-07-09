"""FastAPI dependencies."""

from __future__ import annotations

from functools import lru_cache

from fastapi import Depends, HTTPException
from openai import OpenAI

from app.config import Settings, get_settings


@lru_cache
def _build_client(api_key: str, base_url: str) -> OpenAI:
    return OpenAI(api_key=api_key, base_url=base_url)


def get_openai_client(settings: Settings = Depends(get_settings)) -> OpenAI:
    if not settings.openai_api_key:
        raise HTTPException(
            status_code=503,
            detail=(
                "OPENAI_API_KEY is not configured. "
                "Add it to the repo root .env or this project's .env file."
            ),
        )
    return _build_client(settings.openai_api_key, settings.openai_base_url)
