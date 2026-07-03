"""Claude Chat API — FastAPI entry point."""

from fastapi import FastAPI

from app.config import PROJECT_ROOT, REPO_ROOT, get_settings
from app.routers import chat, usage

settings = get_settings()

app = FastAPI(
    title=settings.app_title,
    description=(
        "Demonstrates Anthropic Claude Messages API via FastAPI. "
        "Loads API keys from the repo root .env, with optional project-local overrides."
    ),
    version="1.0.0",
    debug=settings.app_debug,
)

app.include_router(chat.router, prefix="/api/v1")
app.include_router(usage.router, prefix="/api/v1")


@app.get("/health")
def health() -> dict:
    current = get_settings()
    return {
        "status": "ok",
        "claude_configured": bool(current.anthropic_api_key),
        "model": current.claude_model,
        "env_sources": {
            "repo_root": str(REPO_ROOT),
            "project_root": str(PROJECT_ROOT),
        },
    }
