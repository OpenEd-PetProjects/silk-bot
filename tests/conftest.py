import pytest
from fastapi.testclient import TestClient

from silk_bot.api.app import create_app
from silk_bot.settings import Settings


@pytest.fixture()
def settings(monkeypatch: pytest.MonkeyPatch) -> Settings:
    """Настройки из тестового окружения."""
    # TODO: проставить TELEGRAM_BOT_TOKEN и прочие переменные через monkeypatch.
    raise NotImplementedError


@pytest.fixture()
def client() -> TestClient:
    """HTTP-клиент для проверки API."""
    # TODO: собрать TestClient(create_app()).
    raise NotImplementedError
