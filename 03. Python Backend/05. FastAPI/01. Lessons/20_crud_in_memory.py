# 20 — CRUD operations (in-memory store)
# Run: uvicorn 20_crud_in_memory:app --reload --port 8000
# Try all endpoints at /docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Lesson 20 — CRUD")

notes: dict[int, dict] = {}
_next_id = 1


class NoteIn(BaseModel):
    title: str
    body: str


class Note(NoteIn):
    id: int


@app.get("/notes")
def list_notes():
    return list(notes.values())


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Not found")
    return notes[note_id]


@app.post("/notes", status_code=201)
def create_note(payload: NoteIn):
    global _next_id
    note = Note(id=_next_id, **payload.model_dump())
    notes[_next_id] = note.model_dump()
    _next_id += 1
    return note


@app.put("/notes/{note_id}")
def update_note(note_id: int, payload: NoteIn):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Not found")
    notes[note_id] = Note(id=note_id, **payload.model_dump()).model_dump()
    return notes[note_id]


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Not found")
    del notes[note_id]
