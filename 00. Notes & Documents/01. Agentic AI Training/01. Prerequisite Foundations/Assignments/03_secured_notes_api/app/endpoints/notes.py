"""Notes CRUD endpoints."""

from fastapi import APIRouter, Depends, Query, Response

from app.dependencies import get_note_store, verify_api_key
from app.schemas.notes import Note, NoteCreate, NoteListResponse
from app.services.note_store import NoteStore

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=Note, status_code=201)
def create_note(
    payload: NoteCreate,
    _: str = Depends(verify_api_key),
    store: NoteStore = Depends(get_note_store),
) -> Note:
    """Create a note (requires API key)."""
    return store.create(payload)


@router.get("", response_model=NoteListResponse)
def list_notes(
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    store: NoteStore = Depends(get_note_store),
) -> NoteListResponse:
    """List notes with pagination."""
    return store.list_notes(limit=limit, offset=offset)


@router.get("/{note_id}", response_model=Note)
def get_note(note_id: int, store: NoteStore = Depends(get_note_store)) -> Note:
    """Retrieve a single note by id."""
    return store.get(note_id)


@router.delete("/{note_id}", status_code=204, response_class=Response)
def delete_note(
    note_id: int,
    _: str = Depends(verify_api_key),
    store: NoteStore = Depends(get_note_store),
) -> Response:
    """Delete a note (requires API key)."""
    store.delete(note_id)
    return Response(status_code=204)
