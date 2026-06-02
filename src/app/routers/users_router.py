from fastapi import APIRouter, Depends, status
from src.app.repositories.memory_users_repository import MemoryUsersRepository
from src.app.controllers.users_controller import UsersController
from src.app.schemas.users.user import (
    UserRequestSchema,
    UserResponseSchema,
    UserUpdateRequestSchema,
)

router = APIRouter(prefix="/users", tags=["Usuários"])

_memory_users_repository = MemoryUsersRepository()


def define_user_controller() -> UsersController:
    return UsersController(user_repository=_memory_users_repository)


@router.post(
    "/",
    name="Criar Usuário",
    description="Faz o registro de um novo usuário no sistema",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
async def create(
    payload: UserRequestSchema,
    controller: UsersController = Depends(define_user_controller),
) -> UserResponseSchema:
    return controller.create(payload)


@router.get(
    "/",
    name="Listar Usuários",
    description="Traz a lista completa de todos os usuários cadastrados no sistema",
    response_model=list[UserResponseSchema],
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def all(controller: UsersController = Depends(define_user_controller)):
    return controller.load_all()


@router.get(
    "/{id}",
    name="Buscar usuário por ID",
    description="Através do ID informado, faz a busca do usuário correspondente",
    response_model=UserResponseSchema,
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def find_by_id(
    id: str, controller: UsersController = Depends(define_user_controller)
):
    return controller.find_by_id(id=id)


@router.delete(
    "/{id}",
    name="Deletar Usuário",
    description="Excluí o usuário com o ID corresponde informado",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def find_by_id(
    id: str, controller: UsersController = Depends(define_user_controller)
):
    return controller.delete(id=id)


@router.patch(
    "/{id}",
    name="Atualizar Usuário",
    description="Faz a atualização parcial ou completa das informações do usuário",
    response_model=UserResponseSchema,
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def find_by_id(
    id: str,
    payload: UserUpdateRequestSchema,
    controller: UsersController = Depends(define_user_controller),
):
    return controller.update(id=id, payload=payload)
