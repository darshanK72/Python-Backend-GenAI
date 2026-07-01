# 01 — Integration test across service + repository + DB
# Run: pytest 01_test_integration_stack.py -v

import sqlite3

from integration_stack import NoteAppService, NoteRepository


def test_create_increments_count():
    conn = sqlite3.connect(":memory:")
    repo = NoteRepository(conn)
    svc = NoteAppService(repo)

    svc.create_note("Integration note")
    assert svc.stats()["total"] == 1
    conn.close()


def test_validation_before_db_write():
    conn = sqlite3.connect(":memory:")
    repo = NoteRepository(conn)
    svc = NoteAppService(repo)

    try:
        svc.create_note("  ")
        assert False
    except ValueError:
        assert svc.stats()["total"] == 0
    conn.close()
