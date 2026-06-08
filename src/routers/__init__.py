from fastapi import APIRouter
from src.routers import customers_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(customers_router.router)


@v1_router.get("/health", tags=["Health"])
def health_check() -> dict:
    return {"status": "OK"}
