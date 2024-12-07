from datetime import datetime

from online_notes.application.transaction_manager import TransactionManager
from online_notes.application.gateways import NoteGateway
from online_notes.application.commands import UpdateNoteCommand
from online_notes.application.exceptions import DatabaseException


class UpdateNoteProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        note_gateway: NoteGateway,
    ) -> None:
        self._transaction_manager = transaction_manager
        self._note_gateway = note_gateway

    async def process(self, command: UpdateNoteCommand) -> None:
        note = await self._note_gateway.by_id(id_=command.id_)

        if not note:
            raise DatabaseException("there is no note with such id")

        note.update(
            tag=command.tag, content=command.content, updated_at=datetime.now()
        )

        await self._note_gateway.save(note)
        await self._transaction_manager.commit()
