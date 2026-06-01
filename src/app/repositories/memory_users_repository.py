from src.app.models.user_model import UserModel

class MemoryUsersRepository:
    def __init__(self):
        self.users: list[UserModel] = []

    def save(self, user: UserModel) -> UserModel:
        self.users.append(user)

        return user
    
    def findAll(self) -> list[UserModel]:
        return self.users