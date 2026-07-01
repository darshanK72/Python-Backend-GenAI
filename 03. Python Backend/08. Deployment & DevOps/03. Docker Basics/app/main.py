# Minimal API for Docker lessons
# Run locally: uvicorn main:app --host 0.0.0.0 --port 8000

from fastapi import FastAPI

app = FastAPI(title="Docker lesson API")


@app.get("/health")
def health():
    return {"status": "ok", "runtime": "docker-lesson"}
