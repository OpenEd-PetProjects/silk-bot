from fastapi import APIRouter

from silk_bot.api.schemas import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Health-check маршрут: GET /health."""
    # TODO: вернуть HealthResponse(status="ok", version=...).
    raise NotImplementedError
