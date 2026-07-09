"""Claude chat routes."""

from __future__ import annotations

import json

import anthropic
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse

from app.config import Settings, get_settings
from app.dependencies import get_anthropic_client
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.claude_service import ClaudeService

router = APIRouter(prefix="/chat", tags=["chat"])


def get_service(
    client: anthropic.Anthropic = Depends(get_anthropic_client),
    settings: Settings = Depends(get_settings),
) -> ClaudeService:
    return ClaudeService(client, settings)


@router.post("", response_model=ChatResponse)
def create_chat_completion(
    payload: ChatRequest,
    service: ClaudeService = Depends(get_service),
) -> ChatResponse:
    try:
        return service.chat(payload)
    except Exception as exc:
        status_code, detail = ClaudeService.map_error(exc)
        raise HTTPException(status_code=status_code, detail=detail) from exc


@router.post("/stream")
def stream_chat_completion(
    payload: ChatRequest,
    service: ClaudeService = Depends(get_service),
) -> StreamingResponse:
    def event_generator():
        try:
            for token in service.stream_tokens(payload):
                yield f"data: {json.dumps({'token': token})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as exc:
            status_code, detail = ClaudeService.map_error(exc)
            yield f"data: {json.dumps({'error': detail, 'status_code': status_code})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
