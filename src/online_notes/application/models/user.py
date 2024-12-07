from uuid import UUID

from online_notes.application.value_objects import UserLogin, UserPassword
from online_notes.application.value_objects import Email
from online_notes.application.maybe import Maybe

from online_notes.application.exceptions import (
    WrongPasswordException,
    ChangePasswordException,
    ChangeLoginException,
)


class User:
    def __init__(
        self,
        *,
        id_: UUID,
        login: UserLogin,
        password: UserPassword,
        name: str,
        surname: str | None,
        email: Email | None,
    ) -> None:
        self._id = id_
        self._login = login
        self._password = password
        self._name = name
        self._surname = surname
        self._email = email

    @classmethod
    def create(
        cls,
        *,
        id_: UUID,
        login: UserLogin,
        password: UserPassword,
        name: str,
        surname: str | None,
        email: Email | None,
    ) -> "User":
        return User(
            id_=id_,
            login=login,
            password=password,
            name=name,
            surname=surname,
            email=email,
        )

    def update_info(
        self, *, name: Maybe[str], surname: Maybe[str], email: Maybe[Email]
    ) -> None:
        if name.is_set:
            self._name = name.value

        if surname.is_set:
            self._surname = surname.value

        if email.is_set:
            self._email = email.value

    def change_login(
        self, *, password: UserPassword, new_login: UserLogin
    ) -> None:
        if password != self._password:
            raise WrongPasswordException("Password doesn't match current one")

        if new_login == self._login:
            raise ChangeLoginException(
                "New login and current login are the same"
            )

        self._login = new_login

    def change_password(
        self, *, old_password: UserPassword, new_password: UserPassword
    ) -> None:
        if old_password != self._password:
            raise WrongPasswordException("Password doesn't match current one")
        if new_password == self._password:
            raise ChangePasswordException(
                "New password and current password are the same"
            )

        self._password = new_password
