class UserPasswordException(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)
