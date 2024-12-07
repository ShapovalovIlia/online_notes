from uuid import uuid4
from datetime import datetime

from online_notes.application import Note, Tag, Maybe


def create_note() -> Note:
    return Note.create(
        id_=uuid4(),
        tag=Tag("huinya"),
        content=" s s s",
        created_at=datetime.now(),
    )


class TestNote:
    def test_update_note(self):
        note = create_note()

        new_note_tag = Maybe(Tag("baobab"))
        new_content: Maybe = Maybe.without_value()

        note.update(
            tag=new_note_tag, content=new_content, updated_at=datetime.now()
        )

        assert note._tag == new_note_tag.value
        assert note._content == " s s s"
