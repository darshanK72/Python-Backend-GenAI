"""FastAPI dependencies."""

from __future__ import annotations

from functools import lru_cache

from fastapi import Depends, HTTPException
from google import genai

from app.config import Settings, get_settings


@lru_cache
def _build_client(api_key: str) -> genai.Client:
    return genai.Client(api_key=api_key)


def get_gemini_client(settings: Settings = Depends(get_settings)) -> genai.Client:
    if not settings.google_api_key:
        raise HTTPException(
            status_code=503,
            detail=(
                "GOOGLE_API_KEY is not configured. "
                "Add it to the repo root .env or this project's .env file."
            ),
        )
    return _build_client(settings.google_api_key)
