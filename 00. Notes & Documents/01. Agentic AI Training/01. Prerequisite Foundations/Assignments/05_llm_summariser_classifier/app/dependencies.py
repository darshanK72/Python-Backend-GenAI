"""FastAPI dependency injection helpers."""

from __future__ import annotations

import secrets
from functools import lru_cache

from fastapi import Depends, Header, HTTPException

from app.config import Settings, get_settings
from app.services.llm_service import LLMService


# get_llm_service - return a cached LLMService instance
@lru_cache
def get_llm_service() -> LLMService:
    return LLMService()


# verify_api_key - validate the X-API-Key header against the configured key
def verify_api_key(
    x_api_key: str = Header(default=""),
    settings: Settings = Depends(get_settings),
) -> str:
    """Validate the X-API-Key header against the configured key."""
    if not x_api_key or not secrets.compare_digest(x_api_key, settings.llm_service_api_key):
        raise HTTPException(status_code=401, detail="Invalid or missing API key.")
    return x_api_key
