# FastAPI with Prometheus /metrics
# Run: uvicorn app:app --port 8023
# Metrics: http://127.0.0.1:8023/metrics

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

app = FastAPI(title="Metrics demo")
REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["method", "path"])


@app.middleware("http")
async def count_requests(request, call_next):
    response = await call_next(request)
    REQUESTS.labels(request.method, request.url.path).inc()
    return response


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
