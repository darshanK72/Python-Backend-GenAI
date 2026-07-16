"""Fetch and chunk Wikipedia articles for indexing."""

from __future__ import annotations

import wikipediaapi
from langchain_core.documents import Document

from app.config import CHUNK_OVERLAP, CHUNK_SIZE, WIKIPEDIA_ARTICLES


# fetch_articles - download Wikipedia pages for the configured titles
def fetch_articles(titles: list[str] | None = None) -> list[Document]:
    wiki = wikipediaapi.Wikipedia(
        language="en",
        user_agent="MAS-Training/1.0",
    )
    article_titles = titles or WIKIPEDIA_ARTICLES
    documents: list[Document] = []
    for title in article_titles:
        page = wiki.page(title)
        if not page.exists():
            raise RuntimeError(f"Wikipedia article not found: {title}")
        documents.append(
            Document(
                page_content=page.text,
                metadata={"doc_title": title},
            )
        )
    return documents


# chunk_documents - split articles into overlapping character chunks
def chunk_documents(documents: list[Document]) -> list[Document]:
    chunks: list[Document] = []
    for document in documents:
        text = document.page_content
        title = document.metadata["doc_title"]
        start = 0
        index = 0
        while start < len(text):
            end = start + CHUNK_SIZE
            chunk_text = text[start:end].strip()
            if chunk_text:
                chunks.append(
                    Document(
                        page_content=chunk_text,
                        metadata={"doc_title": title, "chunk_index": index},
                    )
                )
                index += 1
            if end >= len(text):
                break
            start = end - CHUNK_OVERLAP
    return chunks
