from datetime import datetime
from pydantic import BaseModel

class Base_data(BaseModel):
    timestamp: datetime
    location_name: str
    country: str
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    humidity: int


class Extra_data(Base_data):
    temperature_category: str 
    wind_category: str 