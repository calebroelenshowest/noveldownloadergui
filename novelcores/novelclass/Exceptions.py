class IncorrectURL(Exception):

    def __init__(self, message):
        super().__init__(message)


class UnknowSourceError(Exception):

    def __init__(self, message):
        super().__init__(message)