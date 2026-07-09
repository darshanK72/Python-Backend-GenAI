"""pgvector — FastAPI entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import PROJECT_ROOT, REPO_ROOT, get_settings
from app.database import init_database
from app.routers import documents, search, seed

settings = get_settings()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_database()
    yield


app = FastAPI(
    title=settings.app_title,
    description=(
        "Demonstrates document ingest and semantic search with PostgreSQL pgvector + OpenAI embeddings. "
        "Start Postgres via docker compose in 03. PgVector/."
    ),
    version="1.0.0",
    debug=settings.app_debug,
    lifespan=lifespan,
)

app.include_router(documents.router, prefix="/api/v1")
app.include_router(search.router, prefix="/api/v1")
app.include_router(seed.router, prefix="/api/v1")


@app.get("/health")
def health() -> dict:
    current = get_settings()
    return {
        "status": "ok",
        "store": "pgvector",
        "openai_configured": bool(current.openai_api_key),
        "database_url_configured": bool(current.database_url),
        "embedding_model": current.openai_embedding_model,
        "table": current.pgvector_table,
        "env_sources": {
            "repo_root": str(REPO_ROOT),
            "project_root": str(PROJECT_ROOT),
        },
    }
