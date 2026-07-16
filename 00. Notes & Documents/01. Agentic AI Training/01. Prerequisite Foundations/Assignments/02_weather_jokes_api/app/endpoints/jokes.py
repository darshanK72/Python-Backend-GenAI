"""Joke endpoints."""

from fastapi import APIRouter, Depends

from app.dependencies import get_joke_service
from app.schemas.responses import JokeResponse
from app.services.joke_service import JokeService

# router - API router for joke endpoints
router = APIRouter(prefix="/joke", tags=["jokes"])


# get_joke - return a random joke from JokeAPI
@router.get("", response_model=JokeResponse)
async def get_joke(service: JokeService = Depends(get_joke_service)) -> JokeResponse:
    """Return a random joke from JokeAPI."""
    return await service.get_joke()
