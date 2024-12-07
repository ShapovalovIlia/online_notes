from online_notes.application.value_objects import Tag


class CreateNoteCommand:
    tag: Tag
    content: str
