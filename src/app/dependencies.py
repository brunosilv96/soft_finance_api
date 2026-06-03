from typing import Annotated

from fastapi import Depends

from src.app.controllers.users_controller import UsersController
from src.app.repositories.memory_users_repository import MemoryUsersRepository
from src.app.repositories.user_repository import UserRepository

_memory_repo = MemoryUsersRepository()


def get_user_repository() -> UserRepository:
    return _memory_repo


def get_user_controller(
    repository: Annotated[UserRepository, Depends(get_user_repository)],
) -> UsersController:
    return UsersController(user_repository=repository)


UserControllerDep = Annotated[UsersController, Depends(get_user_controller)]
