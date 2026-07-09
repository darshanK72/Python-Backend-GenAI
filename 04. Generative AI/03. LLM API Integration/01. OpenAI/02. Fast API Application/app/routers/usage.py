"""Token counting and usage helpers."""

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings
from app.schemas.chat import TokenCountRequest, TokenCountResponse
from app.utils.token_counter import count_text_tokens

router = APIRouter(prefix="/usage", tags=["usage"])


@router.post("/tokens/count", response_model=TokenCountResponse)
def count_tokens(
    payload: TokenCountRequest,
    settings: Settings = Depends(get_settings),
) -> TokenCountResponse:
    model = payload.model or settings.openai_model
    token_count, encoding = count_text_tokens(payload.text, model)
    return TokenCountResponse(
        token_count=token_count,
        model=model,
        encoding=encoding,
    )
