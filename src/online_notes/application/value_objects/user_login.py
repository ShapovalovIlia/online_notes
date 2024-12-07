import re
from dataclasses import dataclass

from online_notes.application.exceptions import InvalidUserLoginException


@dataclass(frozen=True)
class UserLogin:
    login: str

    def __post_init__(self):
        if not (3 <= len(self.login) <= 18):
            raise InvalidUserLoginException(
                "Login length must be between 3 and 18 characters."
            )

        if not re.match(r"^[a-zA-Z0-9._]+$", self.login):
            raise InvalidUserLoginException(
                "Login can only contain letters, numbers, dots, and underscores."
            )

        if self.login.startswith((".", "_")) or self.login.endswith(
            (".", "_")
        ):
            raise InvalidUserLoginException(
                "Login cannot start or end with '.' or '_'."
            )

        if ".." in self.login or "__" in self.login:
            raise InvalidUserLoginException(
                "Login cannot contain consecutive '.' or '_'."
            )
