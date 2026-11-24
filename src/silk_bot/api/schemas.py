from datetime import datetime

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Ответ health-check маршрута."""

    status: str = Field(default="ok")
    version: str = Field(default="0.1.0")


class NoteCreate(BaseModel):
    """Тело запроса для создания заметки."""

    text: str = Field(min_length=1, max_length=2000)


class NoteRead(NoteCreate):
    """Заметка в ответе API."""

    id: int
    created_at: datetime


class ReminderCreate(BaseModel):
    """Тело запроса для создания напоминания."""

    text: str = Field(min_length=1, max_length=2000)
    due_at: datetime


class ReminderRead(ReminderCreate):
    """Напоминание в ответе API."""

    id: int
    done: bool = False
