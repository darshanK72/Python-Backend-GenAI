# 02 — Path and query parameters
# Run: uvicorn 02_path_query:app --reload --port 8000

from fastapi import FastAPI

app = FastAPI(title="Lesson 02")


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/search")
def search(q: str, limit: int = 10):
    return {"query": q, "limit": limit}
