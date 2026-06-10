from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from src.controllers.customers_controller import CustomersController
from src.database.postgres import postgres_session
from src.repositories.db_customer_repository import DBCustomerRepository
from src.repositories.memory_customer_repository import MemoryCustomerRepository
from src.repositories.customer_repository import CustomerRepository

_memory_repo = MemoryCustomerRepository()


def get_memory_repository() -> CustomerRepository:
    return _memory_repo


def get_user_repository(db: PostgresSession) -> CustomerRepository:
    return DBCustomerRepository(postgres=db)


def get_customer_controller(
    repository: Annotated[CustomerRepository, Depends(get_user_repository)],
) -> CustomersController:
    return CustomersController(user_repository=repository)


PostgresSession = Annotated[Session, Depends(postgres_session)]
CustomerControllerDep = Annotated[CustomersController, Depends(get_customer_controller)]
