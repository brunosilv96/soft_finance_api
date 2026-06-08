from fastapi import APIRouter, status
from src.dependencies import CustomerControllerDep
from src.models.customer_model import CustomerModel
from src.schemas.customer_schema import (
    CustomerRequestSchema,
    CustomerResponseSchema,
    CustomerUpdateRequestSchema,
)

router = APIRouter(prefix="/users", tags=["Clientes"])


@router.post(
    "/",
    name="Criar um novo cliente",
    description="Faz o registro de um novo usuário no sistema",
    response_model=CustomerResponseSchema,
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True,
)
async def create(
    payload: CustomerRequestSchema,
    controller: CustomerControllerDep,
) -> CustomerModel:
    new_user: CustomerModel = controller.create(payload)
    return new_user


@router.get(
    "/",
    name="Listar Usuários",
    description="Traz a lista completa de todos os usuários cadastrados no sistema",
    response_model=list[CustomerResponseSchema],
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def all(controller: CustomerControllerDep) -> list[CustomerModel]:
    users: list[CustomerModel] = controller.load_all()
    return users


@router.get(
    "/{id}",
    name="Buscar usuário por ID",
    description="Através do ID informado, faz a busca do usuário correspondente",
    response_model=CustomerResponseSchema,
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def find_by_id(id: str, controller: CustomerControllerDep) -> CustomerModel:
    user: CustomerModel = controller.find_by_id(id=id)
    return user


@router.delete(
    "/{id}",
    name="Deletar Usuário",
    description="Excluí o usuário com o ID corresponde informado",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(id: str, controller: CustomerControllerDep) -> None:
    controller.delete(id=id)
    return


@router.patch(
    "/{id}",
    name="Atualizar Usuário",
    description="Faz a atualização parcial ou completa das informações do usuário",
    response_model=CustomerResponseSchema,
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def update(
    id: str,
    payload: CustomerUpdateRequestSchema,
    controller: CustomerControllerDep,
) -> CustomerModel:
    updated_user: CustomerModel = controller.update(id=id, payload=payload)
    return updated_user
