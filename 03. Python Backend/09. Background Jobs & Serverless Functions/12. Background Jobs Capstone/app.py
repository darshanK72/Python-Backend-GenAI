# Capstone API — enqueue welcome email on signup
# Run: uvicorn app:app --port 8020

import uuid

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Jobs Capstone API")
_jobs: dict[str, dict] = {}


class Signup(BaseModel):
    email: EmailStr


def enqueue_welcome_email(email: str) -> str:
    job_id = str(uuid.uuid4())
    _jobs[job_id] = {"email": email, "status": "queued"}
    # In production: queue.enqueue(send_email, email)
    _jobs[job_id]["status"] = "sent"
    return job_id


@app.post("/signup", status_code=202)
def signup(payload: Signup):
    job_id = enqueue_welcome_email(str(payload.email))
    return {"message": "signup accepted", "job_id": job_id}


@app.get("/jobs/{job_id}")
def job_status(job_id: str):
    return _jobs.get(job_id, {"error": "not found"})
