from dataclasses import dataclass
from uuid import UUID

from online_notes.application.value_objects import UserPassword, UserLogin


@dataclass(slots=True, frozen=True, kw_only=True)
class ChangeUserLoginCommand:
    id_: UUID
    password: UserPassword
    new_login: UserLogin
