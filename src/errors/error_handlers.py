from typing import Any, Callable, Coroutine

from fastapi import Request, Response, status
from fastapi.datastructures import State
from fastapi.responses import JSONResponse

from src.errors.invalid_payload_error import InvalidPayloadError
from src.errors.not_found_error import NotFoundError


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


handlers: dict[
    int | type[Exception],
    Callable[[Request[State], Any], Coroutine[Any, Any, Response]],
] = {
    NotFoundError: not_found_error_handler,
    InvalidPayloadError: invalid_payload_error_handler,
}
