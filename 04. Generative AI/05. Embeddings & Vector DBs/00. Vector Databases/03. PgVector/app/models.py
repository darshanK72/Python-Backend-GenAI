"""ORM models."""

from __future__ import annotations

from sqlalchemy import JSON, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pgvector.sqlalchemy import Vector


class Base(DeclarativeBase):
    pass


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(String(256), primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    doc_metadata: Mapped[dict] = mapped_column("metadata", JSON, default=dict)
    embedding: Mapped[list[float]] = mapped_column(Vector(1536))
