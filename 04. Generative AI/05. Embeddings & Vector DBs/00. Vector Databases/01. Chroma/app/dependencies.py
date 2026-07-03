"""FastAPI dependencies."""

from __future__ import annotations

from functools import lru_cache

import chromadb
from fastapi import Depends, HTTPException
from openai import OpenAI

from app.config import Settings, get_settings
from app.services.chroma_store import ChromaStore
from app.services.embedding_service import EmbeddingService


@lru_cache
def _build_openai_client(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key)


def get_openai_client(settings: Settings = Depends(get_settings)) -> OpenAI:
    if not settings.openai_api_key:
        raise HTTPException(status_code=503, detail="OPENAI_API_KEY is not configured.")
    return _build_openai_client(settings.openai_api_key)


@lru_cache
def _build_chroma_collection(persist_path: str, collection_name: str):
    client = chromadb.PersistentClient(path=persist_path)
    return client.get_or_create_collection(name=collection_name)


def get_vector_store(settings: Settings = Depends(get_settings)) -> ChromaStore:
    collection = _build_chroma_collection(settings.chroma_persist_path, settings.chroma_collection)
    return ChromaStore(collection)


def get_embedding_service(
    client: OpenAI = Depends(get_openai_client),
    settings: Settings = Depends(get_settings),
) -> EmbeddingService:
    return EmbeddingService(client, settings.openai_embedding_model)
