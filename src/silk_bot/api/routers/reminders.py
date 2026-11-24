from fastapi import APIRouter

from silk_bot.api.schemas import ReminderCreate, ReminderRead

router = APIRouter(prefix="/reminders", tags=["reminders"])


@router.post("", response_model=ReminderRead, status_code=201)
async def create_reminder(payload: ReminderCreate) -> ReminderRead:
    """Создать напоминание."""
    # TODO: реализовать хранение напоминания.
    raise NotImplementedError


@router.get("", response_model=list[ReminderRead])
async def list_reminders() -> list[ReminderRead]:
    """Список напоминаний."""
    # TODO: вернуть сохранённые напоминания.
    raise NotImplementedError
