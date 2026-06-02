from datetime import datetime
import uuid

from fastapi import HTTPException, status
from src.app.repositories.user_repository import UserRepository
from src.app.models.user_model import UserModel
from src.app.schemas.users.user import (
    UserRequestSchema,
    UserResponseSchema,
    UserUpdateRequestSchema,
)


class UsersController:
    def __init__(self, user_repository: UserRepository) -> None:
        self.users_repository = user_repository

    def create(self, payload: UserRequestSchema) -> UserResponseSchema:
        try:
            user_model = UserModel(
                id=str(uuid.uuid7()),
                name=payload.name,
                email=payload.email,
                created_at=datetime.now(),
            )

            user_model = self.users_repository.save(user_model)

            return user_model
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error to create new user in user controller {error}",
            )

    def load_all(self) -> list[UserResponseSchema]:
        try:
            users: list[UserModel] = self.users_repository.find_all()

            return users
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error to load user list in user controller {error}",
            )

    def find_by_id(self, id: str) -> UserResponseSchema:
        try:
            if id == "" or not id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail="id is required"
                )

            print("find_by_id: ", id)

            user: UserModel | None = self.users_repository.find_by_id(id=id)

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
                )

            return user
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"failed to load user by id {error}",
            )

    def delete(self, id: str) -> None:
        try:
            if id == "" or not id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail="id is required"
                )

            user: UserModel | None = self.users_repository.find_by_id(id=id)

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
                )

            return self.users_repository.delete(user)

        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"failed to delete user by id {error}",
            )

    def update(self, id: str, payload: UserUpdateRequestSchema) -> UserResponseSchema:
        try:
            if id == "" or not id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail="id is required"
                )

            user: UserModel | None = self.users_repository.find_by_id(id=id)

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
                )

            # Exclude null fields
            updated_date = payload.model_dump(exclude_unset=True)

            if not updated_date:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="there is no data to update.",
                )

            for index, value in updated_date.items():
                # Updated using memory reference
                setattr(user, index, value)

            user.updated_at = datetime.now()

            return user

        except Exception as error:
            print("ERRO FATAL", error)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"failed to update user by id {error}",
            )
