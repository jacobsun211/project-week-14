from fastapi import Request
from fastapi.responses import JSONResponse
from core.errors import MySQLError
from fastapi import FastAPI


def register_error_handlers(app: FastAPI):

    @app.exception_handler(MySQLError)
    def mysql_error_handler(request: Request, exe: MySQLError):
        return JSONResponse(status_code=500, content={'massage': exe.msg})

