"""FAISS vector store helpers."""

from __future__ import annotations

from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from app.config import FAISS_INDEX_DIR, Settings, get_settings


class VectorStore:
    """Thin wrapper around a local FAISS index."""

    # __init__ - wrap a loaded FAISS store
    def __init__(self, store: FAISS) -> None:
        self._store = store

    # similarity_search - return the top-k neighbour documents
    def similarity_search(self, query: str, k: int = 3) -> list[Document]:
        return self._store.similarity_search(query, k=k)

    # build_and_save - embed documents and persist the FAISS index
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
            model="text-embedding-3-small",
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
            model="text-embedding-3-small",
        )
        store = FAISS.load_local(
            str(target),
            embeddings,
            allow_dangerous_deserialization=True,
        )
        return cls(store)
