from fastapi import routing

from services.external_weather_service import ExternalWeatherService

router = routing.APIRouter(prefix="/ingest", tags=["weather"])

@router.get("/{location_name}")
async def get_weather(location_name: str):
    return await ExternalWeatherService().process(location_name)
