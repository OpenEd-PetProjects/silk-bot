from fastapi import APIRouter

from silk_bot.api.schemas import NoteCreate, NoteRead

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteRead, status_code=201)
async def create_note(payload: NoteCreate) -> NoteRead:
    """Создать заметку."""
    # TODO: реализовать хранение заметки.
    raise NotImplementedError


@router.get("", response_model=list[NoteRead])
async def list_notes() -> list[NoteRead]:
    """Список заметок."""
    # TODO: вернуть сохранённые заметки.
    raise NotImplementedError
