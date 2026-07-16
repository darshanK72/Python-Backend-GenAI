"""Pydantic request and response schemas."""

from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    """Request body for creating a note."""

    title: str = Field(min_length=1)
    body: str = Field(min_length=1)


class Note(BaseModel):
    """A stored note with server-assigned id and timestamp."""

    id: int
    title: str
    body: str
    created_at: str


class NoteListResponse(BaseModel):
    """Paginated list of notes."""

    items: list[Note]
    total: int
    limit: int
    offset: int
