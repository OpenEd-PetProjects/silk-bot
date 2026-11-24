from fastapi.testclient import TestClient


def test_health_returns_ok(client: TestClient) -> None:
    """Health-check маршрут доступен и отвечает статусом ok."""
    # TODO: вызвать GET /health, проверить код 200 и тело ответа.
    raise NotImplementedError
