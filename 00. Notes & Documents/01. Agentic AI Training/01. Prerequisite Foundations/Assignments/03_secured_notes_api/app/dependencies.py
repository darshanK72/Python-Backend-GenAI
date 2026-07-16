"""FastAPI dependency injection helpers."""

from __future__ import annotations

import secrets

from fastapi import Depends, Header, HTTPException

from app.config import Settings, get_settings
from app.services.note_store import NoteStore

# _note_store - shared in-memory note store for the application
_note_store = NoteStore()


# get_note_store - return the shared NoteStore instance
def get_note_store() -> NoteStore:
    return _note_store


# verify_api_key - validate the X-API-Key header against the configured key
def verify_api_key(
    x_api_key: str = Header(default=""),
    settings: Settings = Depends(get_settings),
) -> str:
    """Validate the X-API-Key header against the configured key."""
    if not x_api_key or not secrets.compare_digest(x_api_key, settings.notes_api_key):
        raise HTTPException(status_code=401, detail="Invalid or missing API key.")
    return x_api_key
