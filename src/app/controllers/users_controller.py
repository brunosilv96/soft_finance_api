from datetime import datetime
import uuid

from src.app.repositories.user_repository import UserRepository
from src.app.models.user_model import UserModel
from src.app.schemas.users.user import (UserRequestSchema, UserResponseSchema)

class UsersController:
    def __init__(self, user_repository: UserRepository) -> None:
        self.users_repository = user_repository
        
    def create(self, payload: UserRequestSchema) -> UserResponseSchema:
        user_model = UserModel(
            id = str(uuid.uuid7()),
            name = payload.name,
            email = payload.email,
            created_at = datetime.now()
        )

        user_model = self.users_repository.save(user_model)

        return user_model
    
    def loadAll(self) -> list[UserResponseSchema]:
        users: list[UserModel] = self.users_repository.findAll()

        return users