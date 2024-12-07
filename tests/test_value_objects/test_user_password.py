import pytest

from online_notes.application import InvalidUserPasswordException, UserPassword


class TestUserPassword:
    def test_invalid_len(self) -> None:
        with pytest.raises(InvalidUserPasswordException):
            UserPassword("1234567")

    def test_invalid_case(self) -> None:
        with pytest.raises(InvalidUserPasswordException):
            UserPassword("abcdefgh")

        with pytest.raises(InvalidUserPasswordException):
            UserPassword("ABCDEFGH")

    def test_without_special_symbol(self) -> None:
        with pytest.raises(InvalidUserPasswordException):
            UserPassword("ABCDEFfH")

    def test_correct_password(self) -> None:
        UserPassword("ABCDEFfH@2")
