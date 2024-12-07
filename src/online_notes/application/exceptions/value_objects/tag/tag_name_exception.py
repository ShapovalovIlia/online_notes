from .tag_exception import TagException


class TagNameException(TagException):
    def __init__(self, *args) -> None:
        super().__init__(*args)
