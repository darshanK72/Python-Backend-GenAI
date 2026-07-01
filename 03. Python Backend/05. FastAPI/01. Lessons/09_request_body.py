# 09 — Request body
# Run: uvicorn 09_request_body:app --reload --port 8000
# POST /students  {"name": "Riya", "marks": 88, "city": "Pune"}

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Lesson 09 — Request Body")


class StudentCreate(BaseModel):
    name: str
    marks: int = Field(ge=0, le=100)
    city: str = "Nashik"


class StudentUpdate(BaseModel):
    marks: int | None = Field(default=None, ge=0, le=100)
    city: str | None = None


@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    return {"created": student.model_dump()}


@app.patch("/students/{student_id}")
def update_student(student_id: int, payload: StudentUpdate):
    return {"student_id": student_id, "updated": payload.model_dump(exclude_none=True)}
