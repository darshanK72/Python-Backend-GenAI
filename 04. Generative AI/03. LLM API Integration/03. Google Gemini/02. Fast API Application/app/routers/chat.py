"""Gemini chat routes."""

from __future__ import annotations

import json

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from google import genai

from app.config import Settings, get_settings
from app.dependencies import get_gemini_client
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.gemini_service import GeminiService

router = APIRouter(prefix="/chat", tags=["chat"])


def get_service(
    client: genai.Client = Depends(get_gemini_client),
    settings: Settings = Depends(get_settings),
) -> GeminiService:
    return GeminiService(client, settings)


@router.post("", response_model=ChatResponse)
def create_chat_completion(
    payload: ChatRequest,
    service: GeminiService = Depends(get_service),
) -> ChatResponse:
    try:
        return service.chat(payload)
    except Exception as exc:
        status_code, detail = GeminiService.map_error(exc)
        raise HTTPException(status_code=status_code, detail=detail) from exc


@router.post("/stream")
def stream_chat_completion(
    payload: ChatRequest,
    service: GeminiService = Depends(get_service),
) -> StreamingResponse:
    def event_generator():
        try:
            for token in service.stream_tokens(payload):
                yield f"data: {json.dumps({'token': token})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as exc:
            status_code, detail = GeminiService.map_error(exc)
            yield f"data: {json.dumps({'error': detail, 'status_code': status_code})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
