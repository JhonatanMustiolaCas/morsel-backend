class BadDirection(Exception):
    def __init__(self, message) -> None:
        self.message = message

    def __str__(self) -> str:
        return repr(self.message)


class InvalidCharMap(Exception):
    def __init__(self, message) -> None:
        self.message = message

    def __str__(self) -> str:
        return repr(self.message)


class InvalidSourceFormat(Exception):
    def __init__(self, message) -> None:
        self.message = message

    def __str__(self) -> str:
        return repr(self.message)
