# 03 — Request body with Pydantic
# Run: uvicorn 03_request_body:app --reload --port 8000

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Lesson 03")


class StudentCreate(BaseModel):
    name: str
    marks: int = Field(ge=0, le=100)
    city: str = "Nashik"


@app.post("/students")
def create_student(student: StudentCreate):
    return {"created": student.model_dump()}
