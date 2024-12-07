from .user_exception import UserException


class ChangeLoginException(UserException):
    def __init__(self, *args) -> None:
        super().__init__(*args)
