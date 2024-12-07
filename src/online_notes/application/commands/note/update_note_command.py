from uuid import UUID

from online_notes.application.value_objects import Tag
from online_notes.application.maybe import Maybe


class UpdateNoteCommand:
    id_: UUID
    tag: Maybe[Tag]
    content: Maybe[str]
