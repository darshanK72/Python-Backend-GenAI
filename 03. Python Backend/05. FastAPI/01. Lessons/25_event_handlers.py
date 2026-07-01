# 25 — Startup and shutdown event handlers
# Run: uvicorn 25_event_handlers:app --reload --port 8000
# Watch the terminal on start/stop for lifecycle messages.

from contextlib import asynccontextmanager

from fastapi import FastAPI

_cache: dict[str, str] = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    _cache["status"] = "ready"
    print("[startup] Cache initialized")
    yield
    # Shutdown
    _cache.clear()
    print("[shutdown] Cache cleared")


app = FastAPI(title="Lesson 25 — Event Handlers", lifespan=lifespan)


@app.get("/status")
def status():
    return {"cache": _cache}
