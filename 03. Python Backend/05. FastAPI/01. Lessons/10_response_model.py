# 10 — Response model (filter/shape output)
# Run: uvicorn 10_response_model:app --reload --port 8000
# GET /users/1  — password is stored but never returned

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Lesson 10 — Response Model")

_users = {
    1: {"id": 1, "username": "ada", "email": "ada@example.com", "password": "secret"},
}


class UserPublic(BaseModel):
    id: int
    username: str
    email: str


class UserCreate(BaseModel):
    username: str = Field(min_length=3)
    email: str
    password: str = Field(min_length=8)


@app.get("/users/{user_id}", response_model=UserPublic)
def get_user(user_id: int):
    return _users[user_id]


@app.post("/users", response_model=UserPublic, status_code=201)
def create_user(payload: UserCreate):
    user_id = len(_users) + 1
    record = {"id": user_id, **payload.model_dump()}
    _users[user_id] = record
    return record
