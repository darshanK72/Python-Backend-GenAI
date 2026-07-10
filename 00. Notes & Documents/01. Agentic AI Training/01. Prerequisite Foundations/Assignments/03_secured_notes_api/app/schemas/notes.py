"""Pydantic request and response schemas."""

from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    title: str = Field(min_length=1)
    body: str = Field(min_length=1)


class Note(BaseModel):
    id: int
    title: str
    body: str
    created_at: str


class NoteListResponse(BaseModel):
    items: list[Note]
    total: int
    limit: int
    offset: int
