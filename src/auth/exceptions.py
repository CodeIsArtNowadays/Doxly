from src.core.exceptions import ProjectBaseException


class UserException(ProjectBaseException):
    def __init__(self):
        super().__init__('Bad credentials', 401)
