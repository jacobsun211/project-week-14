from fastapi import FastAPI
import uvicorn

from core.setting import settings
from core.handle_errors import register_error_handlers
from routes.weather_route import router as weather_router


app = FastAPI()
register_error_handlers(app)

app.include_router(weather_router)


if __name__ == "__main__":

    uvicorn.run(
        "main:app", host='127.0.0.1', port=8080, reload=True)
