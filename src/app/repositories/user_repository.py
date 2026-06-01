from abc import ABC, abstractmethod

from src.app.models.user_model import UserModel

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: UserModel) -> UserModel:
        pass

    @abstractmethod
    def findAll(self) -> list[UserModel]:
        pass