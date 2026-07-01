# Capstone — Notes API to test end-to-end

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Testing Capstone API")
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
    note = {"id": _next_id, "title": payload.title, "body": payload.body}
    _store[_next_id] = note
    _next_id += 1
    return note


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    note = _store.get(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="not found")
    return note


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    if note_id not in _store:
        raise HTTPException(status_code=404, detail="not found")
    del _store[note_id]
