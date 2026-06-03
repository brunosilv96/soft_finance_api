from datetime import datetime
import uuid

from src.app.repositories.user_repository import UserRepository
from src.app.models.user_model import UserModel
from src.app.schemas.user_schema import (
    UserRequestSchema,
    UserResponseSchema,
    UserUpdateRequestSchema,
)
from src.app.errors.invalid_payload_error import InvalidPayloadError
from src.app.errors.not_found_error import NotFoundError


class UsersController:
    def __init__(self, user_repository: UserRepository) -> None:
        self.users_repository = user_repository

    def create(self, payload: UserRequestSchema) -> UserResponseSchema:
        user_model = UserModel(
            id=str(uuid.uuid4()),
            name=payload.name,
            email=payload.email,
            created_at=datetime.now(),
        )

        return self.users_repository.save(user_model)

    def load_all(self) -> list[UserResponseSchema]:
        return self.users_repository.find_all()

    def find_by_id(self, id: str) -> UserResponseSchema:
        if id == "" or id.strip() == "":
            raise InvalidPayloadError(message="ID is required")

        user: UserModel | None = self.users_repository.find_by_id(id=id)

        if not user:
            raise NotFoundError(message="User not found")

        return user

    def delete(self, id: str) -> None:
        if id == "" or id.strip() == "":
            raise InvalidPayloadError(message="ID is required")

        user: UserModel | None = self.users_repository.find_by_id(id=id)

        if not user:
            raise NotFoundError(message="User not found")

        return self.users_repository.delete(user)

    def update(self, id: str, payload: UserUpdateRequestSchema) -> UserResponseSchema:
        if id == "" or id.strip() == "":
            raise InvalidPayloadError(message="ID is required")

        user: UserModel | None = self.users_repository.find_by_id(id=id)

        if not user:
            raise NotFoundError(message="User not found")

        # Exclude null fields
        updated_date = payload.model_dump(exclude_unset=True)

        if not updated_date:
            raise InvalidPayloadError(message="There is no data to update.")

        for key, value in updated_date.items():
            # Updated using memory reference
            setattr(user, key, value)

        user.updated_at = datetime.now()

        return user
