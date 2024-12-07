from online_notes.application import (
    User,
    UserLogin,
    UserPassword,
    Maybe,
    Email,
)


from uuid import uuid4


def create_user() -> User:
    return User.create(
        id_=uuid4(),
        login=UserLogin("eblan228"),
        password=UserPassword("superEblan2@"),
        name="Lexus",
        surname="Kreker",
        email=None,
    )


class TestUser:
    def test_update_info(self):
        user = create_user()

        new_name = Maybe.with_value("Perdix")
        new_surname = Maybe.with_value("Analbnik")
        new_email = Maybe.with_value(Email("ilia.shapovalov98@gmail.com"))

        user.update_info(name=new_name, surname=new_surname, email=new_email)
        assert user._name == new_name.value
        assert user._surname == new_surname.value
        assert user._email == new_email.value

    def test_change_login(self):
        user = create_user()
        new_login = UserLogin("eblanchik")
        user.change_login(
            password=UserPassword("superEblan2@"), new_login=new_login
        )
        assert user._login == new_login

    def test_change_password(self):
        user = create_user()

        new_password = UserPassword("superEblan2!")
        user.change_password(
            old_password=UserPassword("superEblan2@"),
            new_password=new_password,
        )
        assert user._password == new_password
