class NotFoundError(Exception):
    def __init__(self, message: str = "Information not found") -> None:
        self.message: str = message
        super().__init__(self.message)
