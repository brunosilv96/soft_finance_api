from datetime import datetime
import uuid

from src.repositories.customer_repository import CustomerRepository
from src.models.customer_model import CustomerModel
from src.schemas.customer_schema import (
    CustomerRequestSchema,
    CustomerUpdateRequestSchema,
)
from src.errors.invalid_payload_error import InvalidPayloadError
from src.errors.not_found_error import NotFoundError


class CustomersController:
    def __init__(self, user_repository: CustomerRepository) -> None:
        self.users_repository = user_repository

    def create(self, payload: CustomerRequestSchema) -> CustomerModel:
        user_model = CustomerModel(
            id=str(uuid.uuid4()),
            name=payload.name,
            email=payload.email,
            created_at=datetime.now(),
        )

        new_user: CustomerModel = self.users_repository.save(user_model)

        return new_user

    def load_all(self) -> list[CustomerModel]:
        return self.users_repository.find_all()

    def find_by_id(self, id: str) -> CustomerModel:
        if id == "" or id.strip() == "":
            raise InvalidPayloadError(message="ID is required")

        user: CustomerModel | None = self.users_repository.find_by_id(id=id)

        if not user:
            raise NotFoundError(message="Customer not found")

        return user

    def delete(self, id: str) -> None:
        if id == "" or id.strip() == "":
            raise InvalidPayloadError(message="ID is required")

        user: CustomerModel | None = self.users_repository.find_by_id(id=id)

        if not user:
            raise NotFoundError(message="Customer not found")

        return self.users_repository.delete(user)

    def update(self, id: str, payload: CustomerUpdateRequestSchema) -> CustomerModel:
        if id == "" or id.strip() == "":
            raise InvalidPayloadError(message="ID is required")

        user: CustomerModel | None = self.users_repository.find_by_id(id=id)

        if not user:
            raise NotFoundError(message="Customer not found")

        # Exclude null fields
        updated_date = payload.model_dump(exclude_unset=True)

        if not updated_date:
            raise InvalidPayloadError(message="There is no data to update.")

        for key, value in updated_date.items():
            # Updated using memory reference
            setattr(user, key, value)

        user.updated_at = datetime.now()

        return user
