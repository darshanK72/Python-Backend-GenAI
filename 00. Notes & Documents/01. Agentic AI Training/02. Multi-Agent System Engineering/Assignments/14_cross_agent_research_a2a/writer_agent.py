"""WriterAgent FastAPI service (port 8002) and thin CLI entry."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from app.cli.commands import run_brief
from app.cli.runner import main
from app.graph.builder import build_graph

# app - WriterAgent FastAPI application
app = FastAPI(title="WriterAgent")

# graph - compiled discovery → delegation → writer StateGraph
graph = build_graph()


class BriefRequest(BaseModel):
    """HTTP request body for POST /brief."""

    topic: str


class BriefResponse(BaseModel):
    """HTTP response body for POST /brief."""

    topic: str
    task_id: str
    research_result: str
    article: str


# create_brief - HTTP endpoint that runs the writer LangGraph for a topic
@app.post("/brief", response_model=BriefResponse)
def create_brief(request: BriefRequest) -> BriefResponse:
    """Run discovery → delegation → writer and return the brief payload."""
    result = run_brief(request.topic, graph=graph)
    return BriefResponse(
        topic=result["topic"],
        task_id=result["task_id"],
        research_result=result["research_result"],
        article=result["article"],
    )


# main - run the WriterAgent CLI (or use uvicorn for the HTTP API)
if __name__ == "__main__":
    raise SystemExit(main())
