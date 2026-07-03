"""Token counting routes."""

import anthropic
from fastapi import APIRouter, Depends

from app.config import Settings, get_settings
from app.dependencies import get_anthropic_client
from app.schemas.chat import TokenCountRequest, TokenCountResponse
from app.services.claude_service import ClaudeService

router = APIRouter(prefix="/usage", tags=["usage"])


@router.post("/tokens/count", response_model=TokenCountResponse)
def count_tokens(
    payload: TokenCountRequest,
    client: anthropic.Anthropic = Depends(get_anthropic_client),
    settings: Settings = Depends(get_settings),
) -> TokenCountResponse:
    model = payload.model or settings.claude_model
    service = ClaudeService(client, settings)
    return TokenCountResponse(
        token_count=service.count_tokens(
            payload.text,
            model,
            system_prompt=payload.system_prompt,
        ),
        model=model,
    )
