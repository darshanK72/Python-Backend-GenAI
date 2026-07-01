# 01 — Test async endpoints with pytest-asyncio
# Run: pytest 01_test_async_endpoints.py -v
# Install: pip install pytest-asyncio

import pytest
from httpx import ASGITransport, AsyncClient

from async_app import app

pytestmark = pytest.mark.asyncio


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


async def test_async_get_missing(client):
    r = await client.get("/async-value/color")
    assert r.status_code == 200
    assert r.json()["value"] == "missing"


async def test_async_set_and_get(client):
    await client.post("/async-value/color", params={"value": "blue"})
    r = await client.get("/async-value/color")
    assert r.json()["value"] == "blue"
