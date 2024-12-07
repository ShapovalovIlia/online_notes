import re
from dataclasses import dataclass

from online_notes.application.exceptions import InvalidEmailAddressException


@dataclass(frozen=True)
class Email:
    address: str

    def __post_init__(self) -> None:
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(email_regex, self.address):
            raise InvalidEmailAddressException(
                f"Invalid email address: {self.address}"
            )
