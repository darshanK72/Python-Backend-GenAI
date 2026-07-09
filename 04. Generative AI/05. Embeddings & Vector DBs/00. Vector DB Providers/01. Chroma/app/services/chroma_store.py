"""Chroma vector store adapter."""

from __future__ import annotations

from typing import Any

from chromadb.api.models.Collection import Collection

from app.schemas.documents import DocumentResponse, SearchHit


def _stringify_metadata(metadata: dict[str, Any]) -> dict[str, str | int | float | bool]:
    clean: dict[str, str | int | float | bool] = {}
    for key, value in metadata.items():
        if isinstance(value, (str, int, float, bool)):
            clean[key] = value
        else:
            clean[key] = str(value)
    return clean


class ChromaStore:
    def __init__(self, collection: Collection) -> None:
        self._collection = collection

    @property
    def collection_name(self) -> str:
        return self._collection.name

    def upsert(
        self,
        ids: list[str],
        texts: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict[str, Any]],
    ) -> int:
        self._collection.upsert(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=[_stringify_metadata(m) for m in metadatas],
        )
        return len(ids)

    def get(self, doc_id: str) -> DocumentResponse | None:
        result = self._collection.get(ids=[doc_id], include=["documents", "metadatas"])
        if not result["ids"]:
            return None
        return DocumentResponse(
            id=result["ids"][0],
            text=result["documents"][0] or "",
            metadata=result["metadatas"][0] or {},
        )

    def delete(self, doc_id: str) -> bool:
        existing = self._collection.get(ids=[doc_id])
        if not existing["ids"]:
            return False
        self._collection.delete(ids=[doc_id])
        return True

    def count(self) -> int:
        return self._collection.count()

    def search(
        self,
        query_embedding: list[float],
        top_k: int,
        metadata_filter: dict[str, Any] | None = None,
    ) -> list[SearchHit]:
        kwargs: dict[str, Any] = {
            "query_embeddings": [query_embedding],
            "n_results": top_k,
            "include": ["documents", "metadatas", "distances"],
        }
        if metadata_filter:
            kwargs["where"] = metadata_filter
        result = self._collection.query(**kwargs)
        hits: list[SearchHit] = []
        for i, doc_id in enumerate(result["ids"][0]):
            distance = result["distances"][0][i]
            hits.append(
                SearchHit(
                    id=doc_id,
                    text=result["documents"][0][i] or "",
                    score=round(1.0 - distance, 6),
                    metadata=result["metadatas"][0][i] or {},
                )
            )
        return hits
