from abc import ABC, abstractmethod

from src.app.models.user_model import UserModel


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: UserModel) -> UserModel:
        pass

    @abstractmethod
    def find_all(self) -> list[UserModel]:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> UserModel | None:
        pass

    @abstractmethod
    def delete(self, user: UserModel) -> None:
        pass
