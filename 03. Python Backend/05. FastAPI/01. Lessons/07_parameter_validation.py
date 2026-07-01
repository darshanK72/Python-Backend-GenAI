# 07 — Parameter validation
# Run: uvicorn 07_parameter_validation:app --reload --port 8000
# Invalid values return 422 with details (try /products/0 or /search?q=)

from fastapi import FastAPI, Path, Query

app = FastAPI(title="Lesson 07 — Parameter Validation")


@app.get("/products/{product_id}")
def get_product(
    product_id: int = Path(ge=1, description="Must be a positive integer"),
):
    return {"product_id": product_id}


@app.get("/search")
def validated_search(
    q: str = Query(min_length=1, max_length=100),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100, alias="pageSize"),
):
    return {"q": q, "page": page, "page_size": page_size}
