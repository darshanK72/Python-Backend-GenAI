# App with liveness and readiness probes
# Run: uvicorn app:app --port 8000

import os

from fastapi import FastAPI

app = FastAPI(title="Health probes")
_db_ready = False


@app.on_event("startup")
def startup():
    global _db_ready
    # Simulate DB connection on startup
    _db_ready = True


@app.get("/health")
def liveness():
    """Load balancer: is the process alive?"""
    return {"status": "alive"}


@app.get("/ready")
def readiness():
    """Orchestrator: can we serve traffic?"""
    if not _db_ready:
        return {"status": "not_ready", "db": False}
    return {"status": "ready", "db": True, "stage": os.getenv("APP_STAGE", "dev")}
