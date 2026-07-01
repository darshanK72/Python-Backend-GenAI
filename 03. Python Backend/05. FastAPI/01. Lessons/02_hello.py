# 02 — Hello World
# Run: uvicorn 02_hello:app --reload --port 8000
# Open: http://127.0.0.1:8000/docs
# Install: pip install fastapi "uvicorn[standard]"

from fastapi import FastAPI

app = FastAPI(title="Lesson 02 — Hello World")


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
