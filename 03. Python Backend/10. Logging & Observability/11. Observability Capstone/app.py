# Observability capstone — logs + health + metrics
# Run: uvicorn app:app --port 8024

import logging
import time
import uuid

from fastapi import FastAPI, Request, Response

try:
    from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
except ImportError:
    Counter = Histogram = generate_latest = CONTENT_TYPE_LATEST = None

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("capstone")

app = FastAPI(title="Observability Capstone")

if Counter and Histogram:
    REQUESTS = Counter("capstone_requests_total", "Requests", ["path", "method"])
    DURATION = Histogram("capstone_request_seconds", "Duration")


@app.middleware("http")
async def observe(request: Request, call_next):
    rid = request.headers.get("X-Request-ID", str(uuid.uuid4())[:8])
    start = time.perf_counter()
    response = await call_next(request)
    sec = time.perf_counter() - start
    log.info(
        "rid=%s method=%s path=%s status=%s duration_ms=%s",
        rid,
        request.method,
        request.url.path,
        response.status_code,
        int(sec * 1000),
    )
    if Counter and Histogram:
        REQUESTS.labels(path=request.url.path, method=request.method).inc()
        DURATION.observe(sec)
    response.headers["X-Request-ID"] = rid
    return response


@app.get("/health")
def health():
    return {"status": "alive"}


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.get("/metrics")
def metrics():
    if not generate_latest:
        return Response("prometheus_client not installed", status_code=501)
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
