class AppStoreConnectException(Exception):
    pass


class AppStoreConnectValidationError(AppStoreConnectException):
    pass

class AppStoreConnectValueError(AppStoreConnectException):
    pass