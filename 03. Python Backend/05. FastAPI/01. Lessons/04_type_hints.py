# 04 — Type hints (how FastAPI uses them)
# Run: uvicorn 04_type_hints:app --reload --port 8000
#
# FastAPI reads function parameter types to:
#   - parse path/query/body values
#   - validate and convert types
#   - document the API in OpenAPI

from fastapi import FastAPI

app = FastAPI(title="Lesson 04 — Type Hints")


@app.get("/sum")
def add_numbers(a: int, b: int) -> dict[str, int]:
    return {"result": a + b}


@app.get("/greet/{name}")
def greet(name: str, formal: bool = False) -> dict[str, str]:
    prefix = "Good day" if formal else "Hi"
    return {"message": f"{prefix}, {name}!"}
