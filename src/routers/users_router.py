from fastapi import APIRouter, status
from src.dependencies import UserControllerDep
from src.models.user_model import UserModel
from src.schemas.user_schema import (
    UserRequestSchema,
    UserResponseSchema,
    UserUpdateRequestSchema,
)

router = APIRouter(prefix="/users", tags=["Usuários"])


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
    controller: UserControllerDep,
) -> UserModel:
    new_user: UserModel = controller.create(payload)
    return new_user


@router.get(
    "/",
    name="Listar Usuários",
    description="Traz a lista completa de todos os usuários cadastrados no sistema",
    response_model=list[UserResponseSchema],
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def all(controller: UserControllerDep) -> list[UserModel]:
    users: list[UserModel] = controller.load_all()
    return users


@router.get(
    "/{id}",
    name="Buscar usuário por ID",
    description="Através do ID informado, faz a busca do usuário correspondente",
    response_model=UserResponseSchema,
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def find_by_id(id: str, controller: UserControllerDep) -> UserModel:
    user: UserModel = controller.find_by_id(id=id)
    return user


@router.delete(
    "/{id}",
    name="Deletar Usuário",
    description="Excluí o usuário com o ID corresponde informado",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(id: str, controller: UserControllerDep) -> None:
    controller.delete(id=id)
    return


@router.patch(
    "/{id}",
    name="Atualizar Usuário",
    description="Faz a atualização parcial ou completa das informações do usuário",
    response_model=UserResponseSchema,
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def update(
    id: str,
    payload: UserUpdateRequestSchema,
    controller: UserControllerDep,
) -> UserModel:
    updated_user: UserModel = controller.update(id=id, payload=payload)
    return updated_user
