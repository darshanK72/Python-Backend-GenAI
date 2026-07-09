"""Chat completion routes."""

from __future__ import annotations

import json

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from openai import OpenAI

from app.config import Settings, get_settings
from app.dependencies import get_openai_client
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.openai_service import OpenAIService

router = APIRouter(prefix="/chat", tags=["chat"])


def get_service(
    client: OpenAI = Depends(get_openai_client),
    settings: Settings = Depends(get_settings),
) -> OpenAIService:
    return OpenAIService(client, settings)


@router.post("", response_model=ChatResponse)
def create_chat_completion(
    payload: ChatRequest,
    service: OpenAIService = Depends(get_service),
) -> ChatResponse:
    try:
        return service.chat(payload)
    except Exception as exc:
        status_code, detail = OpenAIService.map_openai_error(exc)
        raise HTTPException(status_code=status_code, detail=detail) from exc


@router.post("/stream")
def stream_chat_completion(
    payload: ChatRequest,
    service: OpenAIService = Depends(get_service),
) -> StreamingResponse:
    def event_generator():
        try:
            for token in service.stream_tokens(payload):
                yield f"data: {json.dumps({'token': token})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as exc:
            status_code, detail = OpenAIService.map_openai_error(exc)
            yield f"data: {json.dumps({'error': detail, 'status_code': status_code})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
