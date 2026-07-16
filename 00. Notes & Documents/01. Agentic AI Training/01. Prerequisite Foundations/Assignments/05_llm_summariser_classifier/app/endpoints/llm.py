"""LLM-backed summarise and classify endpoints."""

from fastapi import APIRouter, Depends

from app.dependencies import get_llm_service, verify_api_key
from app.schemas.llm import ClassifyResult, SummariseResult
from app.schemas.requests import TextRequest
from app.services.llm_service import LLMService

# router - API router for LLM endpoints
router = APIRouter(tags=["llm"])


# summarise - summarise free text into a short summary and word count
@router.post("/summarise", response_model=SummariseResult)
def summarise(
    payload: TextRequest,
    _: str = Depends(verify_api_key),
    llm_service: LLMService = Depends(get_llm_service),
) -> SummariseResult:
    """Summarise free text into a short summary and word count."""
    return llm_service.summarise_text(payload.text)


# classify - classify free text into bug, feature, question, or feedback
@router.post("/classify", response_model=ClassifyResult)
def classify(
    payload: TextRequest,
    _: str = Depends(verify_api_key),
    llm_service: LLMService = Depends(get_llm_service),
) -> ClassifyResult:
    """Classify free text into bug, feature, question, or feedback."""
    return llm_service.classify_text(payload.text)
