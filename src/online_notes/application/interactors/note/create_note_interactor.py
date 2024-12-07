from uuid_extensions import uuid7
from datetime import datetime

from online_notes.application.transaction_manager import TransactionManager
from online_notes.application.gateways import NoteGateway
from online_notes.application.commands import CreateNoteCommand
from online_notes.application.models import Note


class CreateNoteProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        note_gateway: NoteGateway,
    ) -> None:
        self._transaction_manager = transaction_manager
        self._note_gateway = note_gateway

    async def process(self, command: CreateNoteCommand) -> None:
        note = Note.create(
            id_=uuid7(),
            tag=command.tag,
            content=command.content,
            created_at=datetime.now(),
        )

        await self._note_gateway.save(note)
        await self._transaction_manager.commit()
