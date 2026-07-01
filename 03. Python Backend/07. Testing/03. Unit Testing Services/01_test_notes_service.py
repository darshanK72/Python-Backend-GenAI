# 01 — Unit test a service layer (no HTTP)
# Run: pytest 01_test_notes_service.py -v

import pytest

from notes_service import NotesService


def test_create_and_list():
    svc = NotesService()
    note = svc.create("Buy milk")
    assert note["id"] == 1
    assert len(svc.list_all()) == 1


def test_empty_title_raises():
    svc = NotesService()
    with pytest.raises(ValueError, match="title required"):
        svc.create("   ")


def test_get_missing_returns_none():
    svc = NotesService()
    assert svc.get(99) is None
