# 27 — Middleware
# Run: uvicorn 27_middleware:app --reload --port 8000
# Every response includes X-Process-Time and X-Request-ID headers.

import time
import uuid

from fastapi import FastAPI, Request

app = FastAPI(title="Lesson 27 — Middleware")


@app.middleware("http")
async def add_timing_header(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - start
    response.headers["X-Process-Time"] = f"{elapsed:.4f}s"
    response.headers["X-Request-ID"] = request_id
    return response


@app.get("/")
def home(request: Request):
    return {"request_id": request.state.request_id}
