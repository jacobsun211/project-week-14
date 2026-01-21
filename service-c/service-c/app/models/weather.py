from datetime import datetime
from pydantic import BaseModel

class WeatherModel(BaseModel):
    timestamp: datetime | None = None
    location_name: str | None = None
    country: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    temperature: float | None = None
    wind_speed: float | None = None
    humidity: int | None = None
    temperature_category: str | None = None
    wind_category: str | None = None


