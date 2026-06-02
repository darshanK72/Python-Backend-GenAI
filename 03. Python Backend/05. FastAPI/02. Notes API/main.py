# Notes API — full example (in-memory)
# Run from this folder:
#   uvicorn main:app --reload --port 8000
# Docs: http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Notes API",
    description="Backend practice project for FastAPI",
    version="1.0.0",
)

_store: dict[int, dict] = {}
_next_id = 1


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    body: str = ""


class Note(NoteCreate):
    id: int


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/notes", response_model=list[Note])
def list_notes():
    return list(_store.values())


@app.post("/notes", response_model=Note, status_code=201)
def create_note(payload: NoteCreate):
    global _next_id
    note = Note(id=_next_id, **payload.model_dump())
    _store[_next_id] = note.model_dump()
    _next_id += 1
    return note


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    if note_id not in _store:
        raise HTTPException(404, "Note not found")
    return _store[note_id]


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    if note_id not in _store:
        raise HTTPException(404, "Note not found")
    del _store[note_id]
