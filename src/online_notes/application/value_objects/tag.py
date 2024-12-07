import re
from dataclasses import dataclass

from online_notes.application.exceptions import TagNameException


@dataclass(frozen=True)
class Tag:
    tag: str

    def __post_init__(self) -> None:
        if len(self.tag) == 0:
            raise TagNameException("tag length should be > 0")

        if re.search(r"\s", self.tag):
            raise TagNameException("tag can't contains whitespace symbols")
