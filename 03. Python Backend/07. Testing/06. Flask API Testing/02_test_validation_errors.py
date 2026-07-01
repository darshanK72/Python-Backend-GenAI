# 02 — Test validation and error responses (Flask)
# Run: pytest 02_test_validation_errors.py -v

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


def test_missing_title_returns_400(client):
    r = client.post("/notes", json={"title": "  "})
    assert r.status_code == 400
    assert "error" in r.get_json()


def test_list_empty(client):
    r = client.get("/notes")
    assert r.status_code == 200
    assert r.get_json() == []
