# 02 — Override FastAPI dependencies in tests
# Run: pytest 02_dependency_overrides.py -v

import pytest
from fastapi.testclient import TestClient

from app import app, verify_key


def always_auth():
    return "test-override"


@pytest.fixture
def client():
    app.dependency_overrides[verify_key] = always_auth
    yield TestClient(app)
    app.dependency_overrides.clear()


def test_notes_without_header_when_overridden(client):
    r = client.get("/notes")
    assert r.status_code == 200
