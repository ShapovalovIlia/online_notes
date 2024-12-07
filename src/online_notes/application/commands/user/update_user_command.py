from dataclasses import dataclass
from uuid import UUID

from online_notes.application.value_objects import Email
from online_notes.application.maybe import Maybe


@dataclass(slots=True, frozen=True, kw_only=True)
class UpdateUserCommand:
    id_: UUID
    name: Maybe[str]
    surname: Maybe[str]
    email: Maybe[Email]
