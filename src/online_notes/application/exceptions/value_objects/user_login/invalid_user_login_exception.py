from .user_login_exception import UserLoginException


class InvalidUserLoginException(UserLoginException):
    def __init__(self, *args) -> None:
        super().__init__(*args)
