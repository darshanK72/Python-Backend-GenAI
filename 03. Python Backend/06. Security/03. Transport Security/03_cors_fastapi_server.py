# 03 — CORS with FastAPI (runnable demo)
# Run: uvicorn 03_cors_fastapi_server:app --port 8010
# Test: curl -H "Origin: http://localhost:3000" -v http://127.0.0.1:8010/health

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CORS demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok", "cors": "restricted origins only"}
