class CustomException(Exception):
    # Constructors
    def __init__(self, message=None, cause=None):
        super().__init__(message)
        self.cause = cause

    def __str__(self):
        if self.cause:
            return f"{super().__str__()}: {self.cause}"
        else:
            return super().__str__()
