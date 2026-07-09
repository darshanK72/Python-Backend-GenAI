"""pgvector store adapter."""

from __future__ import annotations

from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models import Document
from app.schemas.documents import DocumentResponse, SearchHit


def _apply_metadata_filter(stmt, metadata_filter: dict[str, Any]):
    for key, value in metadata_filter.items():
        if isinstance(value, dict) and "$eq" in value:
            value = value["$eq"]
        stmt = stmt.where(Document.doc_metadata[key].astext == str(value))
    return stmt


class PgVectorStore:
    def __init__(self, session: Session, table_label: str) -> None:
        self._session = session
        self._table_label = table_label

    @property
    def collection_name(self) -> str:
        return self._table_label

    def upsert(
        self,
        ids: list[str],
        texts: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict[str, Any]],
    ) -> int:
        for doc_id, text, vector, meta in zip(ids, texts, embeddings, metadatas, strict=True):
            row = self._session.get(Document, doc_id)
            if row is None:
                row = Document(id=doc_id, text=text, doc_metadata=meta, embedding=vector)
                self._session.add(row)
            else:
                row.text = text
                row.doc_metadata = meta
                row.embedding = vector
        self._session.commit()
        return len(ids)

    def get(self, doc_id: str) -> DocumentResponse | None:
        row = self._session.get(Document, doc_id)
        if row is None:
            return None
        return DocumentResponse(id=row.id, text=row.text, metadata=row.doc_metadata or {})

    def delete(self, doc_id: str) -> bool:
        row = self._session.get(Document, doc_id)
        if row is None:
            return False
        self._session.delete(row)
        self._session.commit()
        return True

    def count(self) -> int:
        return int(self._session.scalar(select(func.count()).select_from(Document)) or 0)

    def search(
        self,
        query_embedding: list[float],
        top_k: int,
        metadata_filter: dict[str, Any] | None = None,
    ) -> list[SearchHit]:
        distance = Document.embedding.cosine_distance(query_embedding).label("distance")
        stmt = select(Document, distance).order_by(distance).limit(top_k)
        if metadata_filter:
            stmt = _apply_metadata_filter(stmt, metadata_filter)
        rows = self._session.execute(stmt).all()
        hits: list[SearchHit] = []
        for row, dist in rows:
            hits.append(
                SearchHit(
                    id=row.id,
                    text=row.text,
                    score=round(1.0 - float(dist), 6),
                    metadata=row.doc_metadata or {},
                )
            )
        return hits
