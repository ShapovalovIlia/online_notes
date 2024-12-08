from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncConnection
import sqlalchemy

from online_notes.application import User, UserLogin, UserPassword, Email
from online_notes.infrastructure.db.metadata import user_table


class UserGatewayImpl:
    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    async def save(self, user: User) -> None:
        stmt = sqlalchemy.insert(user_table).values(
            id=user.id,
            login=user.login,
            password=user.password,
            name=user.name,
            surname=user.surname,
            email=user.email,
        )

        await self._connection.execute(stmt)

    async def by_id(self, id_: UUID) -> User | None:
        stmt = sqlalchemy.select(user_table).where(user_table.c.id == id_)
        result = await self._connection.execute(stmt)
        row = result.fetchone()

        if row is None:
            return None

        return User(
            id_=row["id"],  # type: ignore
            login=UserLogin(row["login"]),  # type: ignore
            password=UserPassword(row["password"]),  # type: ignore
            name=row["name"],  # type: ignore
            surname=row["surname"],  # type: ignore
            email=Email(row["email"]),  # type: ignore
        )

    async def update(self, user: User) -> None:
        stmt = (
            sqlalchemy.update(user_table)
            .where(user_table.c.id == user.id)
            .values(
                login=user.login.login,
                password=user.password.password,
                name=user.name,
                surname=user.surname,
                email=user.email.address,
            )
        )

        await self._connection.execute(stmt)
