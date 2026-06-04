from fastapi import FastAPI
from src.app.errors import error_handlers
from src.app.routers import v1_router

app = FastAPI(
    title="Soft Finance",
    description="Gerenciador de finanças fácil e confiável",
    version="1.0.0",
    exception_handlers=error_handlers.handlers,
)

app.include_router(v1_router)
