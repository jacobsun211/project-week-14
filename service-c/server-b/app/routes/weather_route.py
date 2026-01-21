from fastapi import routing

from services.clean_service import WeatherService
from models.weather_model import WeatherInModel

router = routing.APIRouter(prefix="/clean", tags=["clean"])

@router.post("")
async def get_weather(weather_data: WeatherInModel):

    return await WeatherService().handle_clean_pipeline(weather_data)
