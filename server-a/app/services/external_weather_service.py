from datetime import datetime

from external_api.registry_weather import get_resource as get_weather_resource
from external_api.registry_server_b import get_resource as get_server_b_resource
from core.errors import LocationNotFoundError


class ExternalWeatherService:

    async def fetch_coordinates(self, location_name: str) -> dict:
        params = {
            "name": location_name,
            "count": 1
            }
        
        client =  get_weather_resource("loc")
        res = await client.call(params=params)


        if "results" not in res.data or not res.data["results"]:
            raise LocationNotFoundError(location_name)

        return res.data["results"][0]

    async def fetch_hourly_weather(self, latitude: float, longitude: float) -> dict:

        params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,wind_speed_10m,relative_humidity_2m",
        "past_days": 1,
        "timezone": "UTC"
        }

        client = get_weather_resource("weather")
        res = await client.call(params=params)

        return res.data["hourly"]
    

    def data_organization(self, data_loc, data_weather) -> list[dict]:

        records = []

        data_loc = {
            "location_name": data_loc.get("name"),
            "country": data_loc.get("country"),
            "latitude": data_loc.get("latitude"),
            "longitude": data_loc.get("longitude")
        }
        
        times = data_weather["time"]
        temperatures = data_weather["temperature_2m"]
        wind_speeds = data_weather["wind_speed_10m"]
        humidities = data_weather["relative_humidity_2m"]


        for i in range(len(times)):
            record = {
                "timestamp": str(datetime.fromisoformat(times[i])),
                **data_loc,
                "temperature": temperatures[i],
                "wind_speed": wind_speeds[i],
                "humidity": humidities[i]

            }
            records.append(record)

        return records
    

    async def handle_weather_pipeline(self, location_name: str) -> list[dict]:
        data_loc = await self.fetch_coordinates(location_name)
        data_weather = await self.fetch_hourly_weather(
            latitude=data_loc["latitude"],
            longitude=data_loc["longitude"]
        )
        data = {"data": self.data_organization(data_loc, data_weather)}

        client = get_server_b_resource("clean")
        res = await client.call(json=data)

        return res.data
