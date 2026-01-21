from pydantic import BaseModel
from datetime import datetime
from typing import List


class WeatherModel(BaseModel):

    timestamp: str | None = None
    location_name: str | None = None
    country: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    temperature: float | None = None
    wind_speed: float | None = None
    humidity: int | None = None
    

class WeatherInModel(BaseModel):
    data: List[WeatherModel]