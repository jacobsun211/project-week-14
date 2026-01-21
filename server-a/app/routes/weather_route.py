from fastapi import routing

from services.external_weather_service import ExternalWeatherService

router = routing.APIRouter(prefix="/ingest", tags=["weather"])

@router.post("/")
async def get_weather(location_name: str):
    return await ExternalWeatherService().handle_weather_pipeline(location_name)
