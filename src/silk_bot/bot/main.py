import asyncio
import logging

from aiogram import Bot, Dispatcher

from silk_bot.bot.client import ApiClient
from silk_bot.bot.handlers import router
from silk_bot.settings import get_settings

logger = logging.getLogger(__name__)


async def run() -> None:
    """Основной цикл бота (long polling)."""
    settings = get_settings()
    # TODO: создать Bot(settings.telegram_bot_token), Dispatcher, подключить router.
    # TODO: запустить polling и корректно закрыть сессию.
    raise NotImplementedError


def main() -> None:
    """Точка входа: python -m silk_bot.bot.main."""
    # TODO: настроить logging и вызвать asyncio.run(run()).
    raise NotImplementedError


if __name__ == "__main__":
    main()
