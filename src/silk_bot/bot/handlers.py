from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from silk_bot.bot.client import ApiClient

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    """Приветствие и краткая справка."""
    # TODO: отправить текст со списком доступных команд.
    raise NotImplementedError


@router.message(Command("health"))
async def cmd_health(message: Message, api: ApiClient) -> None:
    """Проверка доступности API."""
    # TODO: вызвать api.get_health() и показать результат.
    raise NotImplementedError


@router.message(Command("note"))
async def cmd_note(message: Message, command: CommandObject, api: ApiClient) -> None:
    """Создание заметки через API."""
    # TODO: собрать NoteCreate из аргументов команды, вызвать api.create_note().
    raise NotImplementedError


@router.message(Command("remind"))
async def cmd_remind(message: Message, command: CommandObject, api: ApiClient) -> None:
    """Создание напоминания через API."""
    # TODO: разобрать аргументы (текст + время), вызвать api.create_reminder().
    raise NotImplementedError
