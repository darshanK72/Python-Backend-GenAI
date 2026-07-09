"""FastAPI dependencies."""

from __future__ import annotations

from functools import lru_cache

from fastapi import Depends, HTTPException
from openai import OpenAI
from sqlalchemy.orm import Session

from app.config import Settings, get_settings
from app.database import get_db
from app.services.embedding_service import EmbeddingService
from app.services.pgvector_store import PgVectorStore


@lru_cache
def _build_openai_client(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key)


def get_openai_client(settings: Settings = Depends(get_settings)) -> OpenAI:
    if not settings.openai_api_key:
        raise HTTPException(status_code=503, detail="OPENAI_API_KEY is not configured.")
    return _build_openai_client(settings.openai_api_key)


def get_vector_store(
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
) -> PgVectorStore:
    return PgVectorStore(db, settings.pgvector_table)


def get_embedding_service(
    client: OpenAI = Depends(get_openai_client),
    settings: Settings = Depends(get_settings),
) -> EmbeddingService:
    return EmbeddingService(client, settings.openai_embedding_model)
