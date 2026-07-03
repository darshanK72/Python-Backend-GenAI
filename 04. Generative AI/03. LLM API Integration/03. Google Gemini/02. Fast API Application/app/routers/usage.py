"""Token counting routes."""

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings
from app.dependencies import get_gemini_client
from app.schemas.chat import TokenCountRequest, TokenCountResponse
from app.services.gemini_service import GeminiService
from google import genai

router = APIRouter(prefix="/usage", tags=["usage"])


@router.post("/tokens/count", response_model=TokenCountResponse)
def count_tokens(
    payload: TokenCountRequest,
    client: genai.Client = Depends(get_gemini_client),
    settings: Settings = Depends(get_settings),
) -> TokenCountResponse:
    model = payload.model or settings.gemini_model
    service = GeminiService(client, settings)
    return TokenCountResponse(
        token_count=service.count_tokens(payload.text, model),
        model=model,
    )
