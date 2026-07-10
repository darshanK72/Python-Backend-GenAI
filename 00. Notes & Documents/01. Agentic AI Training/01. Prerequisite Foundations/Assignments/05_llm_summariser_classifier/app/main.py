"""FastAPI application entry point."""

from fastapi import FastAPI

from app.config import get_settings
from app.endpoints import health, llm

settings = get_settings()

app = FastAPI(
    title=settings.app_title,
    description=(
        "Secured FastAPI service wrapping structured LLM summarise and classify calls. "
        "MAS prerequisite foundation assignment 05."
    ),
    version="1.0.0",
    debug=settings.app_debug,
)

app.include_router(health.router)
app.include_router(llm.router)
