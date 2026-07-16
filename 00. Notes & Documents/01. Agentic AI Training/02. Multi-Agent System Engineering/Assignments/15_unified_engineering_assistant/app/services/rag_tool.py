"""RAG search implementation for the MCP rag_search tool."""

from __future__ import annotations

from app.config import RAG_K
from app.services.vector_store import VectorStore


# rag_search - return top-k FAISS chunks formatted for the supervisor
def rag_search(query: str) -> str:
    store = VectorStore.load_local()
    docs = store.similarity_search(query, k=RAG_K)
    if not docs:
        return "No matching knowledge base results found."
    lines = []
    for index, doc in enumerate(docs, start=1):
        title = doc.metadata.get("doc_title", "Unknown")
        lines.append(f"Result {index} (Source: {title}): {doc.page_content}")
    return "\n".join(lines)
