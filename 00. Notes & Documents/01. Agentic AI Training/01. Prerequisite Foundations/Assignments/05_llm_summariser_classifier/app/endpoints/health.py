"""Health / liveness endpoints."""

from fastapi import APIRouter

from app.schemas.responses import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Liveness check for load balancers and monitors."""
    return HealthResponse(status="ok")
