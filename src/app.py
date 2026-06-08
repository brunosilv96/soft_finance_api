from fastapi import FastAPI
from src.errors import error_handlers
from src.routers import v1_router

app = FastAPI(
    title="Bruniele Silva Estética API",
    description="Gerenciamento de Agenda e Produtos Facilitado",
    version="1.0.0",
    exception_handlers=error_handlers.handlers,
)

app.include_router(v1_router)
