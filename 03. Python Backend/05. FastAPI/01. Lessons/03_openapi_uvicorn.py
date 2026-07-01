# 03 — OpenAPI and Uvicorn
# Run: uvicorn 03_openapi_uvicorn:app --reload --port 8000
#
# OpenAPI:  http://127.0.0.1:8000/openapi.json
# Swagger:  http://127.0.0.1:8000/docs
# ReDoc:    http://127.0.0.1:8000/redoc
#
# Uvicorn is the ASGI server that runs FastAPI apps:
#   uvicorn <module>:app --reload --host 0.0.0.0 --port 8000
# --reload watches files during development (not for production).

from fastapi import FastAPI

app = FastAPI(
    title="Lesson 03 — OpenAPI",
    description="FastAPI generates an OpenAPI schema from your routes and types.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.get("/items/{item_id}", tags=["items"], summary="Get an item by ID")
def get_item(item_id: int):
    """Return a single item. Appears in Swagger with this docstring."""
    return {"item_id": item_id, "name": f"Item {item_id}"}
