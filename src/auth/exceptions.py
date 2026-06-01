class UserException(Exception):
    def __init__(self):
        super().__init__('Bad credentials')
