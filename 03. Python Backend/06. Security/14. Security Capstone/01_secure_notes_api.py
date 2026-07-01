# 01 — Secure Notes API capstone (auth + validation + rate limit)
# Run: uvicorn 01_secure_notes_api:app --port 8012
# Test:
#   curl -H "X-API-Key: demo-key" http://127.0.0.1:8012/notes
#   curl -X POST -H "X-API-Key: demo-key" -H "Content-Type: application/json" \
#        -d "{\"title\":\"Learn security\"}" http://127.0.0.1:8012/notes

import os
import secrets
import time
from collections import defaultdict

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Secure Notes API", docs_url="/docs")
API_KEY = os.getenv("LESSON_API_KEY", "demo-key")
MAX_REQUESTS = 30
WINDOW = 60
_hits: dict[str, list[float]] = defaultdict(list)
_notes: list[dict] = []
_next_id = 1


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)


def rate_limit(client: str = "default") -> None:
    now = time.time()
    window_start = now - WINDOW
    recent = [t for t in _hits[client] if t >= window_start]
    if len(recent) >= MAX_REQUESTS:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    recent.append(now)
    _hits[client] = recent


def verify_api_key(x_api_key: str = Header(default="")) -> str:
    if not secrets.compare_digest(x_api_key, API_KEY):
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key


@app.get("/notes")
def list_notes(_: str = Depends(verify_api_key)):
    rate_limit()
    return {"notes": _notes}


@app.post("/notes", status_code=201)
def create_note(payload: NoteCreate, _: str = Depends(verify_api_key)):
    rate_limit()
    global _next_id
    note = {"id": _next_id, "title": payload.title}
    _notes.append(note)
    _next_id += 1
    return note
