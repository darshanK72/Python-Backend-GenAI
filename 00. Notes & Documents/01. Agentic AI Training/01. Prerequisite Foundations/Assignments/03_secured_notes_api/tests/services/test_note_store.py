"""Unit tests for NoteStore."""

import pytest
from fastapi import HTTPException

from app.schemas.notes import NoteCreate
from app.services.note_store import NoteStore


# store - return a fresh NoteStore instance for each test
@pytest.fixture
def store() -> NoteStore:
    return NoteStore()


# test_create_assigns_incrementing_ids - test that create assigns incrementing ids and timestamps
def test_create_assigns_incrementing_ids(store: NoteStore) -> None:
    first = store.create(NoteCreate(title="A", body="a"))
    second = store.create(NoteCreate(title="B", body="b"))

    assert first.id == 1
    assert second.id == 2
    assert first.created_at
    assert second.created_at


# test_list_notes_returns_paginated_slice - test that list_notes returns the correct page slice
def test_list_notes_returns_paginated_slice(store: NoteStore) -> None:
    for index in range(5):
        store.create(NoteCreate(title=f"N{index}", body="body"))

    page = store.list_notes(limit=2, offset=1)

    assert page.total == 5
    assert page.limit == 2
    assert page.offset == 1
    assert len(page.items) == 2
    assert page.items[0].title == "N1"


# test_get_returns_note - test that get returns a stored note by id
def test_get_returns_note(store: NoteStore) -> None:
    created = store.create(NoteCreate(title="Find me", body="here"))
    fetched = store.get(created.id)
    assert fetched.title == "Find me"


# test_get_missing_raises_404 - test that get raises 404 for a missing note
def test_get_missing_raises_404(store: NoteStore) -> None:
    with pytest.raises(HTTPException) as exc_info:
        store.get(42)
    assert exc_info.value.status_code == 404


# test_delete_removes_note - test that delete removes a note from the store
def test_delete_removes_note(store: NoteStore) -> None:
    created = store.create(NoteCreate(title="Gone", body="soon"))
    store.delete(created.id)

    with pytest.raises(HTTPException) as exc_info:
        store.get(created.id)
    assert exc_info.value.status_code == 404


# test_delete_missing_raises_404 - test that delete raises 404 for a missing note
def test_delete_missing_raises_404(store: NoteStore) -> None:
    with pytest.raises(HTTPException) as exc_info:
        store.delete(99)
    assert exc_info.value.status_code == 404


# test_reset_clears_store - test that reset clears all stored notes
def test_reset_clears_store(store: NoteStore) -> None:
    store.create(NoteCreate(title="Temp", body="temp"))
    store.reset()

    page = store.list_notes(limit=10, offset=0)
    assert page.total == 0
