"""ResearchAgent A2A server (port 8001)."""

from __future__ import annotations

import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.config import RESEARCH_AGENT_PORT
from app.schemas.prompts import RESEARCH_SYSTEM, RESEARCH_USER
from app.services.agent_card import build_agent_card
from app.services.llm_service import LLMService
from app.services.task_store import get_task, save_task

logging.basicConfig(level=logging.INFO)
# logger - ResearchAgent request logger for visible A2A handshakes
logger = logging.getLogger("research_agent")

# app - ResearchAgent FastAPI application exposing A2A endpoints
app = FastAPI(title="ResearchAgent")


class TaskMessage(BaseModel):
    """A2A task message payload."""

    role: str
    content: str


class TaskRequest(BaseModel):
    """A2A /tasks/send request body."""

    id: str
    message: TaskMessage


# run_research - call OpenAI for structured research on a topic
def run_research(topic: str, *, service: LLMService | None = None) -> str:
    """Call OpenAI for structured research on a topic."""
    llm = service or LLMService()
    return llm.chat(
        [
            {"role": "system", "content": RESEARCH_SYSTEM},
            {"role": "user", "content": RESEARCH_USER.format(topic=topic)},
        ],
        temperature=0.3,
    ).strip()


# agent_card - GET /.well-known/agent.json AgentCard discovery endpoint
@app.get("/.well-known/agent.json")
def agent_card() -> dict:
    """Return the ResearchAgent AgentCard for A2A discovery."""
    return build_agent_card()


# tasks_send - POST /tasks/send research task delegation endpoint
@app.post("/tasks/send")
def tasks_send(request: TaskRequest) -> dict:
    """Accept an A2A research task, run OpenAI, and return a completed TaskResult."""
    topic = request.message.content
    logger.info("A2A task received: %s — topic: %s", request.id, topic)
    output = run_research(topic)
    result = {"id": request.id, "status": "completed", "output": output}
    save_task(result)
    return result


# tasks_get - GET /tasks/{task_id} async polling endpoint
@app.get("/tasks/{task_id}")
def tasks_get(task_id: str) -> dict:
    """Return a previously stored TaskResult for polling clients."""
    result = get_task(task_id)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Task not found: {task_id}")
    return result


# main - start the ResearchAgent uvicorn server on port 8001
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("research_agent:app", host="0.0.0.0", port=RESEARCH_AGENT_PORT, reload=False)
