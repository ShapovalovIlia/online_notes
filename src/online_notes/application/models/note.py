from uuid import UUID
from datetime import datetime

from online_notes.application.maybe import Maybe
from online_notes.application.value_objects import Tag


class Note:
    def __init__(
        self,
        id_: UUID,
        tag: Tag,
        content: str,
        created_at: datetime,
        updated_at: datetime | None,
    ):
        self._id = id_
        self._tag = tag
        self._content = content
        self._created_at = created_at
        self._updated_at = updated_at

    @classmethod
    def create(
        cls,
        id_: UUID,
        tag: Tag,
        content: str,
        created_at: datetime,
    ) -> "Note":
        return Note(
            id_=id_,
            tag=tag,
            content=content,
            created_at=created_at,
            updated_at=None,
        )

    def update(
        self, tag: Maybe[Tag], content: Maybe[str], updated_at: datetime
    ):
        if tag.is_set:
            self._tag = tag.value

        if content.is_set:
            self._content = content.value

        self._updated_at = updated_at

    @property
    def id(self):
        return self._id

    @property
    def tag(self):
        return self._tag

    @property
    def content(self):
        return self._content

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at
