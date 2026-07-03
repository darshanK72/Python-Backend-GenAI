"""Semantic search routes."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from app.dependencies import get_embedding_service, get_vector_store
from app.schemas.documents import SearchRequest, SearchResponse
from app.services.embedding_service import EmbeddingService
from app.services.pgvector_store import PgVectorStore

router = APIRouter(prefix="/search", tags=["search"])


@router.post("", response_model=SearchResponse)
def search_documents(
    payload: SearchRequest,
    store: PgVectorStore = Depends(get_vector_store),
    embedder: EmbeddingService = Depends(get_embedding_service),
) -> SearchResponse:
    query_vector = embedder.embed_query(payload.query)
    hits = store.search(query_vector, payload.top_k, payload.filter)
    return SearchResponse(query=payload.query, top_k=payload.top_k, hits=hits)
