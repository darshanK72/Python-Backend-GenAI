# API with Redis health check for compose lesson
# Run: uvicorn app.main:app --port 8000

import os

from fastapi import FastAPI

app = FastAPI(title="Compose lesson API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/redis-ping")
def redis_ping():
    try:
        import redis

        host = os.getenv("REDIS_HOST", "localhost")
        port = int(os.getenv("REDIS_PORT", "6379"))
        client = redis.Redis(host=host, port=port, decode_responses=True)
        client.ping()
        return {"redis": "ok"}
    except Exception as exc:
        return {"redis": "error", "detail": str(exc)}
