import pytest

from online_notes.application import InvalidEmailAddressException, Email


class TestEmail:
    def test_invalid_email_address_exception(self) -> None:
        with pytest.raises(InvalidEmailAddressException):
            Email("asdf")
