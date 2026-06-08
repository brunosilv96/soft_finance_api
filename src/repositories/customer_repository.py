from abc import ABC, abstractmethod

from src.models.customer_model import CustomerModel


class CustomerRepository(ABC):
    @abstractmethod
    def save(self, user: CustomerModel) -> CustomerModel:
        pass

    @abstractmethod
    def find_all(self) -> list[CustomerModel]:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> CustomerModel | None:
        pass

    @abstractmethod
    def delete(self, user: CustomerModel) -> None:
        pass
