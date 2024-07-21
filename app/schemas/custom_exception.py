class CustomException(Exception):
    pass
class UserAlreadyExistsException(CustomException):
    pass

class PasswordNotStrongEnoughException(CustomException):
    pass