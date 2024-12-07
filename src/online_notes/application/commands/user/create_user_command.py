from dataclasses import dataclass

from online_notes.application.value_objects import (
    Email,
    UserLogin,
    UserPassword,
)


@dataclass(slots=True, frozen=True, kw_only=True)
class CreateUserCommand:
    login: UserLogin
    password: UserPassword
    name: str
    surname: str | None
    email: Email | None
