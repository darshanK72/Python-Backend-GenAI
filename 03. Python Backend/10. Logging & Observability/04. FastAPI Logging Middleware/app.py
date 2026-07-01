# FastAPI app with logging middleware
# Run: uvicorn app:app --port 8021

import logging
import time
import uuid

from fastapi import FastAPI, Request

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("http")

app = FastAPI(title="Logging middleware demo")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    rid = request.headers.get("X-Request-ID", str(uuid.uuid4())[:8])
    start = time.perf_counter()
    log.info("start rid=%s %s %s", rid, request.method, request.url.path)
    response = await call_next(request)
    ms = int((time.perf_counter() - start) * 1000)
    log.info("end rid=%s status=%s duration_ms=%s", rid, response.status_code, ms)
    response.headers["X-Request-ID"] = rid
    return response


@app.get("/notes")
def notes():
    return [{"id": 1, "title": "Logged request"}]
