# 03 — Test Pydantic validation errors (422)
# Run: pytest 03_test_validation_errors.py -v

import pytest
from fastapi.testclient import TestClient

from app import app

HEADERS = {"X-API-Key": "test-key"}


@pytest.fixture
def client():
    return TestClient(app)


def test_empty_title_rejected(client):
    r = client.post("/notes", json={"title": ""}, headers=HEADERS)
    assert r.status_code == 422


def test_unauthorized_without_key(client):
    r = client.get("/notes")
    assert r.status_code == 401
