from typing import Annotated

from fastapi import Depends

from src.controllers.customers_controller import CustomersController
from src.repositories.memory_customer_repository import MemoryCustomerRepository
from src.repositories.customer_repository import CustomerRepository

_memory_repo = MemoryCustomerRepository()


def get_user_repository() -> CustomerRepository:
    return _memory_repo


def get_customer_controller(
    repository: Annotated[CustomerRepository, Depends(get_user_repository)],
) -> CustomersController:
    return CustomersController(user_repository=repository)


CustomerControllerDep = Annotated[CustomersController, Depends(get_customer_controller)]
