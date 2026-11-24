from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройки приложения, читаются из переменных окружения."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    telegram_bot_token: str = Field(..., description="TELEGRAM_BOT_TOKEN")
    api_base_url: str = Field(default="http://127.0.0.1:8000", description="API_BASE_URL")
    api_timeout: float = Field(default=5.0, gt=0, description="API_TIMEOUT")
    log_level: str = Field(default="INFO", description="LOG_LEVEL")
    environment: str = Field(default="local", description="ENVIRONMENT")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Единая точка доступа к настройкам (кэш на процесс)."""
    # TODO: собрать Settings из окружения.
    raise NotImplementedError
