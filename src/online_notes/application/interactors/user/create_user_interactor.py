from uuid_extensions import uuid7

from online_notes.application.transaction_manager import TransactionManager
from online_notes.application.gateways import UserGateway
from online_notes.application.commands import CreateUserCommand
from online_notes.application.models import User


class CreateUserProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        user_gateway: UserGateway,
    ) -> None:
        self._transaction_manager = transaction_manager
        self._user_gateway = user_gateway

    async def process(self, command: CreateUserCommand) -> None:
        user = User.create(
            id_=uuid7(),
            login=command.login,
            password=command.password,
            name=command.name,
            surname=command.surname,
            email=command.email,
        )

        await self._user_gateway.save(user)
        await self._transaction_manager.commit()
