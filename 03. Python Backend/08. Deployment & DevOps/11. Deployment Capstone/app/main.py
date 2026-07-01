# Deployment capstone — Notes API with health + readiness
# Run: uvicorn app.main:app --port 8000

import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Deployment Capstone API", version="1.0.0")
_store: dict[int, dict] = {}
_next_id = 1
_redis_ok = False


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)


@app.on_event("startup")
def check_redis():
    global _redis_ok
    try:
        import redis

        host = os.getenv("REDIS_HOST", "localhost")
        client = redis.Redis(host=host, port=6379, decode_responses=True)
        client.ping()
        _redis_ok = True
    except Exception:
        _redis_ok = False


@app.get("/health")
def health():
    return {"status": "alive"}


@app.get("/ready")
def ready():
    if not _redis_ok:
        raise HTTPException(503, "redis not ready")
    return {"status": "ready", "notes": len(_store)}


@app.get("/notes")
def list_notes():
    return list(_store.values())


@app.post("/notes", status_code=201)
def create_note(payload: NoteCreate):
    global _next_id
    note = {"id": _next_id, "title": payload.title}
    _store[_next_id] = note
    _next_id += 1
    return note
