import pytest

from online_notes.application import InvalidUserLoginException, UserLogin


class TestUserLogin:
    def test_length(self) -> None:
        with pytest.raises(InvalidUserLoginException):
            UserLogin("af")

        with pytest.raises(InvalidUserLoginException):
            UserLogin("abcdefghijklmonpqrs")

    def test_symbols(self) -> None:
        with pytest.raises(InvalidUserLoginException):
            UserLogin("saf@")

    def test_prefix_postfix(self) -> None:
        with pytest.raises(InvalidUserLoginException):
            UserLogin("_saf")

        with pytest.raises(InvalidUserLoginException):
            UserLogin("saf.")

    def test_sequence(self) -> None:
        with pytest.raises(InvalidUserLoginException):
            UserLogin("sa..f")
