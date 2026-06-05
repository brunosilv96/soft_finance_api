from datetime import datetime
import uuid

from src.repositories.user_repository import UserRepository
from src.models.user_model import UserModel
from src.schemas.user_schema import (
    UserRequestSchema,
    UserUpdateRequestSchema,
)
from src.errors.invalid_payload_error import InvalidPayloadError
from src.errors.not_found_error import NotFoundError


class UsersController:
    def __init__(self, user_repository: UserRepository) -> None:
        self.users_repository = user_repository

    def create(self, payload: UserRequestSchema) -> UserModel:
        user_model = UserModel(
            id=str(uuid.uuid4()),
            name=payload.name,
            email=payload.email,
            created_at=datetime.now(),
        )

        new_user: UserModel = self.users_repository.save(user_model)

        return new_user

    def load_all(self) -> list[UserModel]:
        return self.users_repository.find_all()

    def find_by_id(self, id: str) -> UserModel:
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

    def update(self, id: str, payload: UserUpdateRequestSchema) -> UserModel:
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
