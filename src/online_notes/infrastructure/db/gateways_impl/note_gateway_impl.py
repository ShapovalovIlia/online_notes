from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncConnection
import sqlalchemy

from online_notes.application import Note, Tag
from online_notes.infrastructure.db.metadata import note_table


class NoteGatewayImpl:
    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    async def save(self, note: Note) -> None:
        stmt = sqlalchemy.insert(note_table).values(
            id=note.id,
            tag=note.tag.tag,
            content=note.content,
            created_at=note.created_at,
            updated_at=note.updated_at,
        )
        await self._connection.execute(stmt)

    async def by_id(
        self,
        *,
        id_: UUID,
    ) -> Note | None:
        stmt = sqlalchemy.select(note_table).where(note_table.c.id == id_)
        result = await self._connection.execute(stmt)
        row = result.fetchone()

        if row is None:
            return None

        return Note(
            id_=row["id"],  # type: ignore
            tag=Tag(row["tag"]),  # type: ignore
            content=row["content"],  # type: ignore
            created_at=row["created_at"],  # type: ignore
            updated_at=row["updated_at"],  # type: ignore
        )

    async def update(self, note: Note) -> None:
        stmt = (
            sqlalchemy.update(note_table)
            .where(note_table.c.id == note.id)
            .values(
                tag=note.tag.tag,
                content=note.content,
                created_at=note.created_at,
                updated_at=note.updated_at,
            )
        )

        await self._connection.execute(stmt)
