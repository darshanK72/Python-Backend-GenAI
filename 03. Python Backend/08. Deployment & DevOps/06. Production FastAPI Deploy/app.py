# Production-ready FastAPI app
# Run: uvicorn app:app --host 127.0.0.1 --port 8000

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

DEBUG = os.getenv("DEBUG", "false").lower() == "true"
STAGE = os.getenv("APP_STAGE", "development")

app = FastAPI(
    title="Production FastAPI",
    docs_url="/docs" if DEBUG else None,
    redoc_url=None,
    openapi_url="/openapi.json" if DEBUG else None,
)

if not DEBUG:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=os.getenv("CORS_ORIGINS", "").split(","),
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )


@app.get("/health")
def health():
    return {"status": "ok", "stage": STAGE}
