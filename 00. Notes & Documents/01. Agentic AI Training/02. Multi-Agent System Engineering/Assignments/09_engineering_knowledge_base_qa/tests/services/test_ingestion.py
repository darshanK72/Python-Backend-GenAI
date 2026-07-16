"""Tests for document chunking."""

from langchain_core.documents import Document

from app.config import CHUNK_OVERLAP, CHUNK_SIZE
from app.services.ingestion import chunk_documents


# test_chunk_documents_overlap - test overlapping character chunks preserve metadata
def test_chunk_documents_overlap() -> None:
    text = "a" * (CHUNK_SIZE + 100)
    docs = chunk_documents([Document(page_content=text, metadata={"doc_title": "Test"})])
    assert len(docs) >= 2
    assert docs[0].metadata["chunk_index"] == 0
    assert docs[1].metadata["chunk_index"] == 1
    assert len(docs[0].page_content) <= CHUNK_SIZE
    assert CHUNK_OVERLAP > 0
