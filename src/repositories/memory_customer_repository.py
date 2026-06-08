from src.repositories.customer_repository import CustomerRepository
from src.models.customer_model import CustomerModel


class MemoryCustomerRepository(CustomerRepository):
    def __init__(self) -> None:
        self.users: list[CustomerModel] = []

    def save(self, user: CustomerModel) -> CustomerModel:
        self.users.append(user)

        return user

    def find_all(self) -> list[CustomerModel]:
        return self.users

    def find_by_id(self, id: str) -> CustomerModel | None:
        find_user: CustomerModel | None = next(
            (user for user in self.users if user.id == id), None
        )

        return find_user

    def delete(self, user: CustomerModel) -> None:
        self.users.remove(user)
        return
