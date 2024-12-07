__all__ = [
    "UpdateUserProcessor",
    "ChangeUserLoginProcessor",
    "ChangeUserPasswordProcessor",
    "CreateUserProcessor",
    "CreateNoteProcessor",
    "UpdateNoteProcessor",
]


from online_notes.application.interactors.user import (
    UpdateUserProcessor,
    ChangeUserLoginProcessor,
    ChangeUserPasswordProcessor,
    CreateUserProcessor,
)
from online_notes.application.interactors.note import (
    CreateNoteProcessor,
    UpdateNoteProcessor,
)
