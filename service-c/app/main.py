from fastapi import FastAPI
from core.db import SQL_Manager
from core.handle_errors import register_error_handlers
from routes.storage_route import router as storage_router
from contextlib import asynccontextmanager
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQL_Manager.connect()
    SQL_Manager.init()
    yield 
    SQL_Manager.close()



app = FastAPI(lifespan=lifespan)
register_error_handlers(app)
app.include_router(storage_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8081, reload=True)