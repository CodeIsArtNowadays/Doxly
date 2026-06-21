class ProjectBaseException(Exception):

    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__()

    def __str__(self):
        f'{self.message} - {self.status_code}'


class AuthRequireException(ProjectBaseException):
    def __init__(self):
        super().__init__('Authentication Require', 401)