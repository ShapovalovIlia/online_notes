class EmailException(Exception):
    def __init__(self, address: str) -> None:
        super().__init__(address)
