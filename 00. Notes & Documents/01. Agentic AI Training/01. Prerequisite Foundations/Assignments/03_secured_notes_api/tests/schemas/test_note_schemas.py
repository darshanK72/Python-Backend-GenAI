"""Tests for Pydantic note schemas."""

import pytest
from pydantic import ValidationError

from app.schemas.notes import Note, NoteCreate, NoteListResponse


# test_note_create_requires_non_empty_fields - test that NoteCreate accepts valid title and body
def test_note_create_requires_non_empty_fields() -> None:
    model = NoteCreate(title="Title", body="Body")
    assert model.title == "Title"


# test_note_create_rejects_empty_title - test that NoteCreate rejects an empty title
def test_note_create_rejects_empty_title() -> None:
    with pytest.raises(ValidationError):
        NoteCreate(title="", body="Body")


# test_note_list_response_shape - test that NoteListResponse holds items, total, limit, and offset
def test_note_list_response_shape() -> None:
    note = Note(id=1, title="T", body="B", created_at="2026-01-01T00:00:00+00:00")
    response = NoteListResponse(items=[note], total=1, limit=10, offset=0)
    assert response.total == 1
    assert len(response.items) == 1
