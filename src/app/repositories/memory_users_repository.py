from src.app.models.user_model import UserModel


class MemoryUsersRepository:
    def __init__(self):
        self.users: list[UserModel] = []

    def save(self, user: UserModel) -> UserModel:
        self.users.append(user)

        return user

    def find_all(self) -> list[UserModel]:
        return self.users

    def find_by_id(self, id: str) -> UserModel | None:
        find_user: UserModel | None = next(
            (user for user in self.users if user.id == id), None
        )

        return find_user

    def delete(self, user: UserModel) -> None:
        self.users.remove(user)
        return
