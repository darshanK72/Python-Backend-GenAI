# Mini FastAPI app for testing lessons

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Testing demo API")
_store: dict[int, dict] = {}
_next_id = 1
API_KEY = "test-key"


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)


def verify_key(x_api_key: str = Header(default="")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="unauthorized")
    return x_api_key


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/notes")
def list_notes(_: str = Depends(verify_key)):
    return list(_store.values())


@app.post("/notes", status_code=201)
def create_note(payload: NoteCreate, _: str = Depends(verify_key)):
    global _next_id
    note = {"id": _next_id, "title": payload.title}
    _store[_next_id] = note
    _next_id += 1
    return note
