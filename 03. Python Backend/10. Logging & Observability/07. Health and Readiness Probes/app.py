# App with liveness and readiness for observability
# Run: uvicorn app:app --port 8022

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Probe demo")
_dependencies_ok = True


@app.get("/health")
def liveness():
    return {"status": "alive"}


@app.get("/ready")
def readiness():
    if not _dependencies_ok:
        raise HTTPException(503, detail="dependencies not ready")
    return {"status": "ready"}


@app.get("/metrics-info")
def metrics_info():
    return {"hint": "expose /metrics with prometheus_client in lesson 08"}
