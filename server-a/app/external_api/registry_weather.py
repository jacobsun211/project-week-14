from external_api.client import ExternalApiClient
from core.errors import EndpointNotFoundError
from core.setting import settings

base_url_loc = 'https://geocoding-api.open-meteo.com'
base_url_weather = 'https://api.open-meteo.com'
port = 443

reservoir = {

    "loc": {"base_url": base_url_loc, "port": port, "endpoint": "/v1/search", 
                "method": "GET", "headers": None},

    "weather": {"base_url": base_url_weather, "port": port, "endpoint": "/v1/forecast",
                 "method": "GET", "headers": None},        
}


def get_resource(resource_name: str) -> ExternalApiClient:

    resource = reservoir.get(resource_name)

    if not resource:
        raise EndpointNotFoundError(resource_name)

    return ExternalApiClient(**resource)
