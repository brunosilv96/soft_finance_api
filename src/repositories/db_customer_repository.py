from src.dependencies import PostgresSession
from src.models.customer_model import CustomerModel
from src.repositories.customer_repository import CustomerRepository


class DBCustomerRepository(CustomerRepository):
    def __init__(self, postgres: PostgresSession) -> None:
        self.repository = postgres

    def save(self, user: CustomerModel) -> CustomerModel:
        return user

    def find_all(self) -> list[CustomerModel]:
        return []

    def find_by_id(self, id: str) -> CustomerModel | None:
        pass

    def delete(self, user: CustomerModel) -> None:
        pass
