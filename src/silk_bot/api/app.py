from fastapi import FastAPI

from silk_bot.api.routers import health, notes, reminders


def create_app() -> FastAPI:
    """Фабрика FastAPI-приложения."""
    app = FastAPI(title="silk-bot API", version="0.1.0")
    # TODO: подключить роутеры health, notes, reminders.
    # TODO: добавить обработку ошибок и логирование.
    return app
