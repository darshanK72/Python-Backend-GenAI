# 06 — Query parameters
# Run: uvicorn 06_query_parameters:app --reload --port 8000
# Try: GET /search?q=python&limit=5&skip=0

from fastapi import FastAPI, Query

app = FastAPI(title="Lesson 06 — Query Parameters")


@app.get("/search")
def search(q: str, limit: int = 10, skip: int = 0):
    return {"query": q, "limit": limit, "skip": skip, "results": []}


@app.get("/items/")
def list_items(
    q: str | None = Query(default=None, max_length=50),
    tags: list[str] = Query(default=[]),
):
    return {"q": q, "tags": tags}


@app.get("/users/")
def list_users(active: bool = True, role: str = "user"):
    return {"active": active, "role": role}
