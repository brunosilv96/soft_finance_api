class ZeroDivisionError(Exception):
    message: str = "Is not possible divide from zero"

    def __str__(self) -> str:
        return self.message
