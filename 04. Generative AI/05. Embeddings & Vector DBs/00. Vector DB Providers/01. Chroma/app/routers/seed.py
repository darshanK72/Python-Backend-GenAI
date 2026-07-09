"""Load curriculum sample chunks."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from app.data.sample_corpus import SAMPLE_DOCUMENTS
from app.dependencies import get_embedding_service, get_vector_store
from app.routers.documents import _upsert_many
from app.schemas.documents import DocumentCreate, SeedResponse
from app.services.chroma_store import ChromaStore
from app.services.embedding_service import EmbeddingService

router = APIRouter(prefix="/seed", tags=["seed"])


@router.post("", response_model=SeedResponse)
def seed_sample_corpus(
    store: ChromaStore = Depends(get_vector_store),
    embedder: EmbeddingService = Depends(get_embedding_service),
) -> SeedResponse:
    docs = [DocumentCreate(**item) for item in SAMPLE_DOCUMENTS]
    count = _upsert_many(docs, store, embedder)
    return SeedResponse(upserted=count, message="Loaded curriculum sample chunks")
