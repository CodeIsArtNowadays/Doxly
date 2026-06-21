from src.core.exceptions import ProjectBaseException


class PermissionDeniedException(ProjectBaseException):
    def __init__(self):
        super().__init__('Permission denied', 403)