# 08 — Pydantic models
# Run: uvicorn 08_pydantic:app --reload --port 8000
# POST /users  {"name": "Ada", "email": "ada@example.com", "age": 30}

# EmailStr needs: pip install "pydantic[email]"  (or use str below)
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Lesson 08 — Pydantic")


class User(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    email: str = Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    age: int = Field(ge=0, le=150)

    @field_validator("name")
    @classmethod
    def strip_name(cls, value: str) -> str:
        return value.strip()


@app.post("/users", status_code=201)
def create_user(user: User):
    return {"created": user.model_dump()}
