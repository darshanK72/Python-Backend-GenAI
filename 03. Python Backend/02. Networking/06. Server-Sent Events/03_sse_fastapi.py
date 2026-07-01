# 03 — SSE with FastAPI (optional comparison)
# Run: uvicorn 03_sse_fastapi:app --port 8788
# Then: python 02_sse_client.py  (change URL to http://127.0.0.1:8788/events)

import asyncio
import time

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI(title="SSE demo")


async def event_generator():
    for i in range(5):
        yield f"data: fastapi event {i}\n\n"
        await asyncio.sleep(1)


@app.get("/events")
def events():
    return StreamingResponse(event_generator(), media_type="text/event-stream")
