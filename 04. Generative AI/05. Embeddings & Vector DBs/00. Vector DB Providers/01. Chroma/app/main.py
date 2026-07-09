"""Chroma vector store — FastAPI entry point."""

from fastapi import FastAPI

from app.config import PROJECT_ROOT, REPO_ROOT, get_settings
from app.routers import documents, search, seed

settings = get_settings()

app = FastAPI(
    title=settings.app_title,
    description=(
        "Demonstrates document ingest and semantic search with Chroma + OpenAI embeddings. "
        "Aligned with 06. Embeddings & Vector DBs notebooks."
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
        "store": "chroma",
        "openai_configured": bool(current.openai_api_key),
        "embedding_model": current.openai_embedding_model,
        "collection": current.chroma_collection,
        "persist_path": current.chroma_persist_path,
        "env_sources": {
            "repo_root": str(REPO_ROOT),
            "project_root": str(PROJECT_ROOT),
        },
    }
