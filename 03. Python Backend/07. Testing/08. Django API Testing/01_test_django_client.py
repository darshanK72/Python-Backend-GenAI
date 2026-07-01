# 01 — Django test client
# Run: pytest 01_test_django_client.py -v

import pytest
from django.test import Client

from django_app import configure


@pytest.fixture(scope="module", autouse=True)
def django_setup():
    configure()


@pytest.fixture
def client():
    return Client()


def test_health(client):
    r = client.get("/health/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_notes_list(client):
    r = client.get("/notes/")
    assert r.status_code == 200
    assert "notes" in r.json()
