"""In-memory notes store."""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import HTTPException

from app.schemas.notes import Note, NoteCreate, NoteListResponse


class NoteStore:
    """Thread-unsafe in-memory note repository for assignment demos."""

    def __init__(self) -> None:
        self._store: dict[int, dict] = {}
        self._next_id = 1

    def reset(self) -> None:
        """Clear all notes — used in tests."""
        self._store.clear()
        self._next_id = 1

    def create(self, payload: NoteCreate) -> Note:
        """Create a note with server-assigned id and timestamp."""
        note = Note(
            id=self._next_id,
            title=payload.title,
            body=payload.body,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        self._store[self._next_id] = note.model_dump()
        self._next_id += 1
        return note

    def list_notes(self, *, limit: int, offset: int) -> NoteListResponse:
        """Return a paginated slice of notes."""
        all_notes = [Note(**item) for item in sorted(self._store.values(), key=lambda n: n["id"])]
        page = all_notes[offset : offset + limit]
        return NoteListResponse(items=page, total=len(all_notes), limit=limit, offset=offset)

    def get(self, note_id: int) -> Note:
        """Return one note or raise 404."""
        if note_id not in self._store:
            raise HTTPException(status_code=404, detail="Note not found.")
        return Note(**self._store[note_id])

    def delete(self, note_id: int) -> None:
        """Delete a note or raise 404."""
        if note_id not in self._store:
            raise HTTPException(status_code=404, detail="Note not found.")
        del self._store[note_id]
