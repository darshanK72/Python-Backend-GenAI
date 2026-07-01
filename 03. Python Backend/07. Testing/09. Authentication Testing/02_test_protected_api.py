# 02 — Test protected API routes (FastAPI)
# Run: pytest 02_test_protected_api.py -v

import pytest
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()
API_KEY = "demo-key"


def require_key(x_api_key: str = Header(default="")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401)
    return x_api_key


@app.get("/admin")
def admin(_: str = Depends(require_key)):
    return {"ok": True}


@pytest.fixture
def client():
    return TestClient(app)


def test_admin_with_key(client):
    r = client.get("/admin", headers={"X-API-Key": "demo-key"})
    assert r.status_code == 200


def test_admin_without_key(client):
    r = client.get("/admin")
    assert r.status_code == 401
