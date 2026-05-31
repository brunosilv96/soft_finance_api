from fastapi import APIRouter
from src.app.schemas.users.user import User

router = APIRouter(
    prefix="/users",
    tags=["Usuários"]
)

@router.post("/")
async def create(user: User) -> User:
    return user