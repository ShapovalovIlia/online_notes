import pytest

from online_notes.application import Tag, TagNameException


class TestTag:
    def test_whitespaces(self):
        with pytest.raises(TagNameException):
            Tag("hute a")

        with pytest.raises(TagNameException):
            Tag("hute'\n")

    def test_empty(self):
        with pytest.raises(TagNameException):
            Tag("")
