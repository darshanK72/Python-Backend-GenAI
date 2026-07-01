# 02 — FastAPI /metrics endpoint
# Run: uvicorn 02_fastapi_metrics:app --port 8023
# Install: pip install prometheus-client

try:
    from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest
except ImportError:
    print("Install: pip install prometheus-client")
    raise SystemExit(1)

from fastapi import FastAPI, Response

app = FastAPI()
NOTES_CREATED = Counter("notes_created_total", "Notes created")


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/notes")
def create_note():
    NOTES_CREATED.inc()
    return {"created": True}
