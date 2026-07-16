"""Health / liveness endpoints."""

from fastapi import APIRouter

from app.schemas.responses import HealthResponse

# router - API router for health endpoints
router = APIRouter(tags=["health"])


# health_check - return a simple liveness response
@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Liveness check for load balancers and monitors."""
    return HealthResponse(status="ok")
