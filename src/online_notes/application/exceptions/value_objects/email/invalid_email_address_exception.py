from .email_exception import EmailException


class InvalidEmailAddressException(EmailException):
    def __init__(self, address: str) -> None:
        super().__init__(address)
