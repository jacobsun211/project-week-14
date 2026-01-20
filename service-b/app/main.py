
from pydantic import BaseModel
from datetime import datetime
import pandas as pd


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
    temperature_category: str = 'None'
    wind_category: str = 'None'


df = pd.DataFrame(df)

df['temperature_category'] = pd.cut(df['temperature'],
                                    bins=[0, 18, 25,100],
                                    labels=['cold', 'moderate', 'hot'])



df['wind_category'] = pd.cut(df['wind_speed'],
                                bins=[0, 10, 100],
                                labels=['calm', 'windy'])
