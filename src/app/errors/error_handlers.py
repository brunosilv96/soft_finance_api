from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.app.errors.invalid_payload_error import InvalidPayloadError
from src.app.errors.not_found_error import NotFoundError


async def not_found_error_handler(request: Request, exc: NotFoundError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error_code": "NOT_FOUND",
            "message": exc.message,
        },
    )


async def invalid_payload_error_handler(
    request: Request, exc: InvalidPayloadError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error_code": "INVALID_PAYLOAD",
            "message": exc.message,
        },
    )
