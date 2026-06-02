# 01 — Hello FastAPI
# Run: uvicorn 01_hello:app --reload --port 8000
# Open: http://127.0.0.1:8000/docs
# Install: pip install fastapi "uvicorn[standard]"

from fastapi import FastAPI

app = FastAPI(title="Lesson 01")


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
