# 18 — Dependencies (shared logic)
# Run: uvicorn 18_dependencies:app --reload --port 8000
# GET /protected  header  X-API-Key: secret-demo-key

from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI(title="Lesson 18 — Dependencies")


def verify_api_key(x_api_key: str = Header(default="")):
    if x_api_key != "secret-demo-key":
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key


ApiKey = Annotated[str, Depends(verify_api_key)]


@app.get("/protected")
def protected_route(key: ApiKey):
    return {"message": "Access granted", "key_used": key}


def pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.get("/items")
def list_items(page: dict = Depends(pagination)):
    return {"page": page, "items": []}
