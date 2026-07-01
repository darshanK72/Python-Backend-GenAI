# 19 — CORS (Cross-Origin Resource Sharing)
# Run: uvicorn 19_cors:app --reload --port 8000
# Allows browser JS on another origin to call this API.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Lesson 19 — CORS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/data")
def read_data():
    return {"message": "This response includes CORS headers"}
