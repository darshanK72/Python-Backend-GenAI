# 02 — Graceful shutdown with lifespan events
# Run: uvicorn 02_graceful_shutdown:app --port 8000
# Press Ctrl+C and watch shutdown logs

import signal
from contextlib import asynccontextmanager

from fastapi import FastAPI

_connections = 0


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[startup] App ready")
    yield
    print("[shutdown] Draining connections, closing resources...")


app = FastAPI(lifespan=lifespan)


@app.get("/work")
def work():
    global _connections
    _connections += 1
    return {"connections_served": _connections}
