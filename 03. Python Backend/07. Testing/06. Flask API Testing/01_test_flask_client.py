# 01 — Flask test client
# Run: pytest 01_test_flask_client.py -v

import pytest

from app import app, _store


@pytest.fixture(autouse=True)
def reset_store():
    _store.clear()
    yield


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_create_note(client):
    r = client.post("/notes", json={"title": "Flask test"})
    assert r.status_code == 201
    assert r.get_json()["title"] == "Flask test"
