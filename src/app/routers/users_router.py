from fastapi import APIRouter, Depends, status
from src.app.repositories.memory_users_repository import MemoryUsersRepository
from src.app.controllers.users_controller import UsersController
from src.app.schemas.users.user import (UserRequestSchema, UserResponseSchema)

router = APIRouter(
    prefix="/users",
    tags=["Usuários"]
)

_memory_users_repository = MemoryUsersRepository()

def define_user_controller() -> UsersController:
    return UsersController(user_repository = _memory_users_repository)

@router.post("/", response_model = UserResponseSchema, status_code = status.HTTP_201_CREATED)
async def create(
        payload: UserRequestSchema,
        controller: UsersController = Depends(define_user_controller)
    ) -> UserResponseSchema:
    return controller.create(payload)

@router.get("/", response_model = list[UserResponseSchema], status_code = status.HTTP_200_OK)
async def all(
    controller: UsersController = Depends(define_user_controller)
):
    return controller.loadAll()