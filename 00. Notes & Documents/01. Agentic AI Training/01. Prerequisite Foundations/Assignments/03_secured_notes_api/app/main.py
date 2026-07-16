"""FastAPI application entry point."""

from fastapi import FastAPI

from app.config import get_settings
from app.endpoints import notes

# settings - loaded application settings
settings = get_settings()

# app - FastAPI application instance with registered routers
app = FastAPI(
    title=settings.app_title,
    description=(
        "In-memory notes CRUD with API-key auth and pagination. "
        "MAS prerequisite foundation assignment 03."
    ),
    version="1.0.0",
    debug=settings.app_debug,
)

app.include_router(notes.router)
