# 22 — MongoDB (Motor async driver)
# Run: uvicorn 22_mongodb:app --reload --port 8000
# Requires MongoDB on mongodb://localhost:27017
# Install: pip install motor
#
# If MongoDB is not running, endpoints return 503 with a clear message.

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

try:
    from motor.motor_asyncio import AsyncIOMotorClient
except ImportError:
    AsyncIOMotorClient = None  # type: ignore[misc, assignment]

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "fastapi_lessons"
COLLECTION = "tasks"

client = None
db = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global client, db
    if AsyncIOMotorClient is None:
        yield
        return
    client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=2000)
    db = client[DB_NAME]
    try:
        await client.admin.command("ping")
    except Exception:
        db = None
    yield
    if client:
        client.close()


app = FastAPI(title="Lesson 22 — MongoDB", lifespan=lifespan)


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    done: bool = False


def _require_db():
    if db is None:
        raise HTTPException(
            503,
            "MongoDB unavailable. Install motor and start MongoDB on localhost:27017.",
        )
    return db


@app.get("/tasks")
async def list_tasks():
    database = _require_db()
    cursor = database[COLLECTION].find({}, {"_id": 0})
    return [doc async for doc in cursor]


@app.post("/tasks", status_code=201)
async def create_task(task: TaskCreate):
    database = _require_db()
    doc = task.model_dump()
    await database[COLLECTION].insert_one(doc)
    return doc
