from fastapi import APIRouter
from src.routers import users_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(users_router.router)


@v1_router.get("/health", tags=["Health"])
def health_check() -> dict:
    return {"status": "OK"}
