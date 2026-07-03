"""FastAPI dependencies."""

from __future__ import annotations

from functools import lru_cache

from fastapi import Depends, HTTPException
from openai import OpenAI
from pinecone import Pinecone

from app.config import Settings, get_settings
from app.services.embedding_service import EmbeddingService
from app.services.pinecone_store import PineconeStore


@lru_cache
def _build_openai_client(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key)


def get_openai_client(settings: Settings = Depends(get_settings)) -> OpenAI:
    if not settings.openai_api_key:
        raise HTTPException(status_code=503, detail="OPENAI_API_KEY is not configured.")
    return _build_openai_client(settings.openai_api_key)


@lru_cache
def _build_pinecone_store(api_key: str, index_name: str, namespace: str) -> PineconeStore:
    pc = Pinecone(api_key=api_key)
    description = pc.describe_index(index_name)
    index = pc.Index(host=description.host)
    return PineconeStore(index=index, index_name=index_name, namespace=namespace)


def get_vector_store(settings: Settings = Depends(get_settings)) -> PineconeStore:
    if not settings.pinecone_api_key or not settings.pinecone_index_name:
        raise HTTPException(
            status_code=503,
            detail="PINECONE_API_KEY and PINECONE_INDEX_NAME must be configured.",
        )
    return _build_pinecone_store(
        settings.pinecone_api_key,
        settings.pinecone_index_name,
        settings.pinecone_namespace,
    )


def get_embedding_service(
    client: OpenAI = Depends(get_openai_client),
    settings: Settings = Depends(get_settings),
) -> EmbeddingService:
    return EmbeddingService(client, settings.openai_embedding_model)
