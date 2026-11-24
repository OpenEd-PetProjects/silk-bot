from typing import Any

import httpx

from silk_bot.api.schemas import NoteCreate, NoteRead, ReminderCreate, ReminderRead


class ApiClient:
    """HTTP-клиент бота к FastAPI API."""

    def __init__(self, base_url: str, timeout: float = 5.0) -> None:
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self) -> "ApiClient":
        # TODO: создать httpx.AsyncClient.
        raise NotImplementedError

    async def __aexit__(self, *exc_info: object) -> None:
        # TODO: закрыть httpx.AsyncClient.
        raise NotImplementedError

    async def get_health(self) -> dict[str, Any]:
        """GET /health."""
        # TODO: выполнить запрос и вернуть разобранный JSON.
        raise NotImplementedError

    async def create_note(self, payload: NoteCreate) -> NoteRead:
        """POST /notes."""
        # TODO: выполнить запрос и вернуть NoteRead.
        raise NotImplementedError

    async def list_notes(self) -> list[NoteRead]:
        """GET /notes."""
        # TODO: выполнить запрос и вернуть список NoteRead.
        raise NotImplementedError

    async def create_reminder(self, payload: ReminderCreate) -> ReminderRead:
        """POST /reminders."""
        # TODO: выполнить запрос и вернуть ReminderRead.
        raise NotImplementedError

    async def list_reminders(self) -> list[ReminderRead]:
        """GET /reminders."""
        # TODO: выполнить запрос и вернуть список ReminderRead.
        raise NotImplementedError
