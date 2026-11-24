import pytest

from silk_bot.settings import Settings, get_settings


def test_settings_reads_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Настройки читаются из переменных окружения."""
    # TODO: проверить, что TELEGRAM_BOT_TOKEN и API_BASE_URL попадают в Settings.
    raise NotImplementedError


def test_get_settings_is_cached() -> None:
    """get_settings() возвращает один и тот же объект."""
    # TODO: проверить кэширование (lru_cache).
    raise NotImplementedError
