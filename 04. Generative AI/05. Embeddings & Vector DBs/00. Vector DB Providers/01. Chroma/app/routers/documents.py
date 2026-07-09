"""Document CRUD routes."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_embedding_service, get_vector_store
from app.schemas.documents import (
    DocumentBatchCreate,
    DocumentCountResponse,
    DocumentCreate,
    DocumentResponse,
)
from app.services.chroma_store import ChromaStore
from app.services.embedding_service import EmbeddingService

router = APIRouter(prefix="/documents", tags=["documents"])


def _upsert_many(
    documents: list[DocumentCreate],
    store: ChromaStore,
    embedder: EmbeddingService,
) -> int:
    ids = [doc.id for doc in documents]
    texts = [doc.text for doc in documents]
    metadatas = [doc.metadata for doc in documents]
    embeddings = embedder.embed_texts(texts)
    return store.upsert(ids, texts, embeddings, metadatas)


@router.post("", response_model=DocumentResponse)
def upsert_document(
    payload: DocumentCreate,
    store: ChromaStore = Depends(get_vector_store),
    embedder: EmbeddingService = Depends(get_embedding_service),
) -> DocumentResponse:
    _upsert_many([payload], store, embedder)
    doc = store.get(payload.id)
    if doc is None:
        raise HTTPException(status_code=500, detail="Upsert succeeded but document not found")
    return doc


@router.post("/batch", response_model=DocumentCountResponse)
def upsert_documents_batch(
    payload: DocumentBatchCreate,
    store: ChromaStore = Depends(get_vector_store),
    embedder: EmbeddingService = Depends(get_embedding_service),
) -> DocumentCountResponse:
    count = _upsert_many(payload.documents, store, embedder)
    return DocumentCountResponse(count=count, collection=store.collection_name)


@router.get("/{doc_id}", response_model=DocumentResponse)
def get_document(
    doc_id: str,
    store: ChromaStore = Depends(get_vector_store),
) -> DocumentResponse:
    doc = store.get(doc_id)
    if doc is None:
        raise HTTPException(status_code=404, detail=f"Document '{doc_id}' not found")
    return doc


@router.delete("/{doc_id}")
def delete_document(
    doc_id: str,
    store: ChromaStore = Depends(get_vector_store),
) -> dict:
    if not store.delete(doc_id):
        raise HTTPException(status_code=404, detail=f"Document '{doc_id}' not found")
    return {"deleted": doc_id}


@router.get("", response_model=DocumentCountResponse)
def document_count(store: ChromaStore = Depends(get_vector_store)) -> DocumentCountResponse:
    return DocumentCountResponse(count=store.count(), collection=store.collection_name)
