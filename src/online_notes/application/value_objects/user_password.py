from dataclasses import dataclass
import re

from online_notes.application.exceptions import InvalidUserPasswordException


@dataclass(frozen=True)
class UserPassword:
    password: str

    def __post_init__(self):
        if len(self.password) < 8:
            raise InvalidUserPasswordException(
                "Password must be at least 8 characters long."
            )

        if not re.search(r"\d", self.password):
            raise InvalidUserPasswordException(
                "Password must contain at least one digit."
            )

        if not re.search(r"[A-Z]", self.password):
            raise InvalidUserPasswordException(
                "Password must contain at least one uppercase letter."
            )

        if not re.search(r"[a-z]", self.password):
            raise InvalidUserPasswordException(
                "Password must contain at least one lowercase letter."
            )

        if not re.search(r"[\W_]", self.password):
            raise InvalidUserPasswordException(
                "Password must contain at least one special character."
            )
