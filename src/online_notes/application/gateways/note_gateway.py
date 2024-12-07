from typing import Protocol
from uuid import UUID

from online_notes.application.models import Note


class NoteGateway(Protocol):
    async def save(self, note: Note) -> None:
        raise NotImplementedError

    async def by_id(self, id_: UUID) -> Note | None:
        raise NotImplementedError

    async def update(self, note: Note) -> None:
        raise NotImplementedError
