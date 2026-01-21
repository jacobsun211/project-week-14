from fastapi import Request
from fastapi.responses import JSONResponse
from core.errors import EndpointNotFoundError
import httpx

def register_error_handlers(app):

    @app.exception_handler(EndpointNotFoundError)
    async def endpoint_not_found_exception_handler(request: Request, 
                                                   exc: EndpointNotFoundError):
        return JSONResponse(
            status_code=404,
            content={"message": exc.message},
        )

    @app.exception_handler(httpx.ConnectError)
    async def httpx_connect_error_handler(request: Request, exc: httpx.ConnectError):

        external_url = getattr(exc.request, "url", "external server")

        return JSONResponse(
            status_code=503,
            content={"message": f"Connection to {external_url} failed."},
        )

    @app.exception_handler(httpx.TimeoutException)
    async def httpx_timeout_error_handler(request: Request, exc: httpx.TimeoutException):

        external_url = getattr(exc.request, "url", "external server")

        return JSONResponse(
            status_code=504,
            content={"message": f"No response was received from an {external_url} "
                                "within a reasonable period of time."},
        )

    @app.exception_handler(httpx.HTTPStatusError)
    async def httpx_status_error_handler(request: Request, exc: httpx.HTTPStatusError):

        external_url = getattr(exc.request, "url", "External server")

        return JSONResponse(
            status_code=exc.response.status_code,
            content={
                "message": f"{external_url} error: {exc.response.status_code}",
                "body": exc.response.text
            },
        )

    @app.exception_handler(httpx.RequestError)
    async def httpx_request_error_handler(request: Request, exc: httpx.RequestError):

        external_url = getattr(exc.request, "url", "external server")

        return JSONResponse(
            status_code=500,
            content={"message": f"General error in request to {external_url}: {str(exc)}"},
        )
 