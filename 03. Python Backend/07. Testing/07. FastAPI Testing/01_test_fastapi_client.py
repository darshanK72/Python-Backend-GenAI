# 01 — FastAPI TestClient
# Run: pytest 01_test_fastapi_client.py -v

import pytest
from fastapi.testclient import TestClient

from app import _store, app

HEADERS = {"X-API-Key": "test-key"}


@pytest.fixture(autouse=True)
def reset_store():
    _store.clear()
    yield


@pytest.fixture
def client():
    return TestClient(app)


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_create_note(client):
    r = client.post("/notes", json={"title": "FastAPI test"}, headers=HEADERS)
    assert r.status_code == 201
    assert r.json()["title"] == "FastAPI test"
