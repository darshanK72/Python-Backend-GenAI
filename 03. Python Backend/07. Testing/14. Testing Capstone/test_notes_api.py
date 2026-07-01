# Capstone test suite — health, CRUD, validation, 404
# Run: pytest test_notes_api.py -v

import pytest
from fastapi.testclient import TestClient

from app import _store, app


@pytest.fixture(autouse=True)
def reset_store():
    _store.clear()
    yield


@pytest.fixture
def client():
    return TestClient(app)


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_create_and_get(client):
    created = client.post("/notes", json={"title": "Capstone", "body": "demo"}).json()
    fetched = client.get(f"/notes/{created['id']}").json()
    assert fetched["title"] == "Capstone"


def test_list_notes(client):
    client.post("/notes", json={"title": "One"})
    client.post("/notes", json={"title": "Two"})
    assert len(client.get("/notes").json()) == 2


def test_delete_note(client):
    note_id = client.post("/notes", json={"title": "Delete me"}).json()["id"]
    r = client.delete(f"/notes/{note_id}")
    assert r.status_code == 204
    assert client.get(f"/notes/{note_id}").status_code == 404


def test_validation_error(client):
    assert client.post("/notes", json={"title": ""}).status_code == 422


def test_not_found(client):
    assert client.get("/notes/999").status_code == 404
