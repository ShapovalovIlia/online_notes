from .user_password_exception import UserPasswordException


class InvalidUserPasswordException(UserPasswordException):
    def __init__(self, *args) -> None:
        super().__init__(*args)
