from fastapi import FastAPI
from src.app.errors.error_handlers import (
    invalid_payload_error_handler,
    not_found_error_handler,
)
from src.app.errors.invalid_payload_error import InvalidPayloadError
from src.app.errors.not_found_error import NotFoundError
from src.app.routers import v1_router

app = FastAPI(
    title="Soft Finance",
    description="Gerenciador de finanças fácil e confiável",
    version="1.0.0",
    exception_handlers={
        NotFoundError: not_found_error_handler,
        InvalidPayloadError: invalid_payload_error_handler,
    },
)

app.include_router(v1_router)
