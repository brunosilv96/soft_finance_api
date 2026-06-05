class InvalidPayloadError(Exception):
    def __init__(self, message: str = "Invalid payload error") -> None:
        self.message: str = message
        super().__init__(self.message)
