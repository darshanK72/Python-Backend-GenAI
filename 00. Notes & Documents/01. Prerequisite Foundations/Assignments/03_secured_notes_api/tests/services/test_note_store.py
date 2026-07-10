"""Unit tests for NoteStore."""

import pytest
from fastapi import HTTPException

from app.schemas.notes import NoteCreate
from app.services.note_store import NoteStore


@pytest.fixture
def store() -> NoteStore:
    return NoteStore()


def test_create_assigns_incrementing_ids(store: NoteStore) -> None:
    first = store.create(NoteCreate(title="A", body="a"))
    second = store.create(NoteCreate(title="B", body="b"))

    assert first.id == 1
    assert second.id == 2
    assert first.created_at
    assert second.created_at


def test_list_notes_returns_paginated_slice(store: NoteStore) -> None:
    for index in range(5):
        store.create(NoteCreate(title=f"N{index}", body="body"))

    page = store.list_notes(limit=2, offset=1)

    assert page.total == 5
    assert page.limit == 2
    assert page.offset == 1
    assert len(page.items) == 2
    assert page.items[0].title == "N1"


def test_get_returns_note(store: NoteStore) -> None:
    created = store.create(NoteCreate(title="Find me", body="here"))
    fetched = store.get(created.id)
    assert fetched.title == "Find me"


def test_get_missing_raises_404(store: NoteStore) -> None:
    with pytest.raises(HTTPException) as exc_info:
        store.get(42)
    assert exc_info.value.status_code == 404


def test_delete_removes_note(store: NoteStore) -> None:
    created = store.create(NoteCreate(title="Gone", body="soon"))
    store.delete(created.id)

    with pytest.raises(HTTPException) as exc_info:
        store.get(created.id)
    assert exc_info.value.status_code == 404


def test_delete_missing_raises_404(store: NoteStore) -> None:
    with pytest.raises(HTTPException) as exc_info:
        store.delete(99)
    assert exc_info.value.status_code == 404


def test_reset_clears_store(store: NoteStore) -> None:
    store.create(NoteCreate(title="Temp", body="temp"))
    store.reset()

    page = store.list_notes(limit=10, offset=0)
    assert page.total == 0
