"""FAISS vector store helpers."""

from __future__ import annotations

from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from app.config import EMBEDDING_MODEL, FAISS_INDEX_DIR, Settings, get_settings


class VectorStore:
    """Thin wrapper around a FAISS store for build, load, and search."""

    # __init__ - wrap an existing FAISS store instance
    def __init__(self, store: FAISS) -> None:
        self._store = store

    # similarity_search - return the top-k documents for a query
    def similarity_search(self, query: str, k: int = 4) -> list[Document]:
        return self._store.similarity_search(query, k=k)

    # build_and_save - embed documents, build FAISS, and persist to disk
    @classmethod
    def build_and_save(
        cls,
        documents: list[Document],
        index_dir: Path | None = None,
        *,
        settings: Settings | None = None,
    ) -> "VectorStore":
        cfg = settings or get_settings()
        if not cfg.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY is not set in the environment.")
        embeddings = OpenAIEmbeddings(
            api_key=cfg.openai_api_key,
            model=EMBEDDING_MODEL,
        )
        store = FAISS.from_documents(documents, embeddings)
        target = index_dir or FAISS_INDEX_DIR
        target.mkdir(parents=True, exist_ok=True)
        store.save_local(str(target))
        return cls(store)

    # load_local - load a previously saved FAISS index from disk
    @classmethod
    def load_local(
        cls,
        index_dir: Path | None = None,
        *,
        settings: Settings | None = None,
    ) -> "VectorStore":
        cfg = settings or get_settings()
        if not cfg.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY is not set in the environment.")
        target = index_dir or FAISS_INDEX_DIR
        if not target.exists():
            raise FileNotFoundError(
                f"FAISS index not found at {target}. Run: python rebuild_index.py"
            )
        embeddings = OpenAIEmbeddings(
            api_key=cfg.openai_api_key,
            model=EMBEDDING_MODEL,
        )
        store = FAISS.load_local(
            str(target),
            embeddings,
            allow_dangerous_deserialization=True,
        )
        return cls(store)
