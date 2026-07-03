"""Request and response models for vector store API."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class DocumentCreate(BaseModel):
    id: str = Field(min_length=1, max_length=256, examples=["c1"])
    text: str = Field(min_length=1, examples=["Alembic applies SQLAlchemy schema migrations."])
    metadata: dict[str, Any] = Field(default_factory=dict)


class DocumentBatchCreate(BaseModel):
    documents: list[DocumentCreate] = Field(min_length=1)


class DocumentResponse(BaseModel):
    id: str
    text: str
    metadata: dict[str, Any]


class DocumentCountResponse(BaseModel):
    count: int
    collection: str


class SearchRequest(BaseModel):
    query: str = Field(min_length=1, examples=["How do I run database migrations?"])
    top_k: int = Field(default=5, ge=1, le=50)
    filter: dict[str, Any] | None = Field(
        default=None,
        description="Metadata filter (Chroma `where` syntax)",
    )


class SearchHit(BaseModel):
    id: str
    text: str
    score: float
    metadata: dict[str, Any]


class SearchResponse(BaseModel):
    query: str
    top_k: int
    hits: list[SearchHit]


class SeedResponse(BaseModel):
    upserted: int
    message: str
