from online_notes.application.transaction_manager import TransactionManager
from online_notes.application.gateways import UserGateway
from online_notes.application.commands import ChangeUserLoginCommand
from online_notes.application.exceptions import DatabaseException


class ChangeUserLoginProcessor:
    def __init__(
        self,
        transaction_manager: TransactionManager,
        user_gateway: UserGateway,
    ) -> None:
        self._transaction_manager = transaction_manager
        self._user_gateway = user_gateway

    async def process(self, command: ChangeUserLoginCommand) -> None:
        user = await self._user_gateway.by_id(command.id_)
        if not user:
            raise DatabaseException("couldn't find user with such id")

        user.change_login(
            password=command.password,
            new_login=command.new_login,
        )

        await self._user_gateway.save(user)
        await self._transaction_manager.commit()
