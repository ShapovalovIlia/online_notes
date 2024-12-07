from dataclasses import dataclass
from uuid import UUID

from online_notes.application.value_objects import UserPassword


@dataclass(slots=True, frozen=True, kw_only=True)
class ChangeUserPasswordCommand:
    id_: UUID
    old_password: UserPassword
    new_password: UserPassword
