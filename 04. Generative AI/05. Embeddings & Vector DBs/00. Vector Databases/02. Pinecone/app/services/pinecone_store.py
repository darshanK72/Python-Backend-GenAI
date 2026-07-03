"""Pinecone vector store adapter."""

from __future__ import annotations

from typing import Any

from pinecone import Index

from app.schemas.documents import DocumentResponse, SearchHit


def _clean_metadata(metadata: dict[str, Any]) -> dict[str, str | int | float | bool]:
    clean: dict[str, str | int | float | bool] = {"text": ""}
    for key, value in metadata.items():
        if key == "text":
            continue
        if isinstance(value, (str, int, float, bool)):
            clean[key] = value
        else:
            clean[key] = str(value)
    return clean


class PineconeStore:
    def __init__(self, index: Index, index_name: str, namespace: str) -> None:
        self._index = index
        self._index_name = index_name
        self._namespace = namespace

    @property
    def collection_name(self) -> str:
        return f"{self._index_name}/{self._namespace}"

    def upsert(
        self,
        ids: list[str],
        texts: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict[str, Any]],
    ) -> int:
        vectors = []
        for doc_id, text, vector, meta in zip(ids, texts, embeddings, metadatas, strict=True):
            payload = _clean_metadata(meta)
            payload["text"] = text
            vectors.append({"id": doc_id, "values": vector, "metadata": payload})
        self._index.upsert(vectors=vectors, namespace=self._namespace)
        return len(ids)

    def get(self, doc_id: str) -> DocumentResponse | None:
        result = self._index.fetch(ids=[doc_id], namespace=self._namespace)
        item = result.vectors.get(doc_id)
        if item is None:
            return None
        metadata = dict(item.metadata or {})
        text = str(metadata.pop("text", ""))
        return DocumentResponse(id=doc_id, text=text, metadata=metadata)

    def delete(self, doc_id: str) -> bool:
        existing = self._index.fetch(ids=[doc_id], namespace=self._namespace)
        if doc_id not in existing.vectors:
            return False
        self._index.delete(ids=[doc_id], namespace=self._namespace)
        return True

    def count(self) -> int:
        stats = self._index.describe_index_stats()
        ns = stats.namespaces or {}
        if self._namespace in ns:
            return int(ns[self._namespace].vector_count)
        return int(stats.total_vector_count or 0)

    def search(
        self,
        query_embedding: list[float],
        top_k: int,
        metadata_filter: dict[str, Any] | None = None,
    ) -> list[SearchHit]:
        response = self._index.query(
            vector=query_embedding,
            top_k=top_k,
            namespace=self._namespace,
            filter=metadata_filter,
            include_metadata=True,
        )
        hits: list[SearchHit] = []
        for match in response.matches:
            metadata = dict(match.metadata or {})
            text = str(metadata.pop("text", ""))
            hits.append(
                SearchHit(
                    id=match.id,
                    text=text,
                    score=round(float(match.score or 0.0), 6),
                    metadata=metadata,
                )
            )
        return hits
