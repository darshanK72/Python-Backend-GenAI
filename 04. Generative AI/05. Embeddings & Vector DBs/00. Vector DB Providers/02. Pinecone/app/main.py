"""Pinecone vector store — FastAPI entry point."""

from fastapi import FastAPI

from app.config import PROJECT_ROOT, REPO_ROOT, get_settings
from app.routers import documents, search, seed

settings = get_settings()

app = FastAPI(
    title=settings.app_title,
    description=(
        "Demonstrates document ingest and semantic search with Pinecone + OpenAI embeddings. "
        "Requires a pre-created Pinecone index (dimension 1536, cosine)."
    ),
    version="1.0.0",
    debug=settings.app_debug,
)

app.include_router(documents.router, prefix="/api/v1")
app.include_router(search.router, prefix="/api/v1")
app.include_router(seed.router, prefix="/api/v1")


@app.get("/health")
def health() -> dict:
    current = get_settings()
    return {
        "status": "ok",
        "store": "pinecone",
        "openai_configured": bool(current.openai_api_key),
        "pinecone_configured": bool(current.pinecone_api_key and current.pinecone_index_name),
        "embedding_model": current.openai_embedding_model,
        "index": current.pinecone_index_name,
        "namespace": current.pinecone_namespace,
        "env_sources": {
            "repo_root": str(REPO_ROOT),
            "project_root": str(PROJECT_ROOT),
        },
    }
