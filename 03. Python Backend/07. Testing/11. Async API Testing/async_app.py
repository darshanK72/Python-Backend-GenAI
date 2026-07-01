# Async FastAPI app for testing

import asyncio

from fastapi import FastAPI

app = FastAPI()
_cache: dict[str, str] = {}


async def slow_lookup(key: str) -> str:
    await asyncio.sleep(0.01)
    return _cache.get(key, "missing")


@app.get("/async-value/{key}")
async def async_value(key: str):
    value = await slow_lookup(key)
    return {"key": key, "value": value}


@app.post("/async-value/{key}")
async def set_value(key: str, value: str):
    _cache[key] = value
    return {"saved": True}
