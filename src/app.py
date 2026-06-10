from fastapi import FastAPI
from src.errors import error_handlers
from src.routers import v1_router

# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
#     create_db_and_tables()
#     yield


app = FastAPI(
    title="Bruniele Silva Estética API",
    description="Gerenciamento de Agenda e Produtos Facilitado",
    version="1.0.0",
    exception_handlers=error_handlers.handlers,
    # lifespan=lifespan,
)

app.include_router(v1_router)
