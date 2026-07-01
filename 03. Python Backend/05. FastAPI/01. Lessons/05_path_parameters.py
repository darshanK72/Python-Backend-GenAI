# 05 — Path parameters
# Run: uvicorn 05_path_parameters:app --reload --port 8000
# Try: GET /users/42   GET /files/report.pdf

from enum import Enum

from fastapi import FastAPI, Path

app = FastAPI(title="Lesson 05 — Path Parameters")


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    return {"model": model_name, "layers": 42}


@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"path": file_path}


@app.get("/items/{item_id}")
def get_item(item_id: int = Path(ge=1, le=1000, description="Item ID")):
    return {"item_id": item_id}
