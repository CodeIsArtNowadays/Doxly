from src.core.exceptions import ProjectBaseException


class UserException(ProjectBaseException):
    def __init__(self, message='Bad credentials'):
        super().__init__(message, 401)
