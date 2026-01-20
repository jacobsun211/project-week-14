from external_api.client import ExternalApiClient
from core.errors import EndpointNotFoundError
from core.setting import settings

base_url = settings.HOST_B
port = settings.PORT_B

reservoir = {

    "bla": {"base_url": base_url, "port": port, "endpoint": "/bla", 
            "method": "GET", "headers": None},

    "bli": {"base_url": base_url, "port": port, "endpoint": "/bli", "method": "POST", 
            "headers": {"Content-Type": "application/json"}}
}


def get_resource(resource_name: str) -> ExternalApiClient:

    resource = reservoir.get(resource_name)

    if not resource:
        raise EndpointNotFoundError(resource_name)

    return ExternalApiClient(**resource)

# def list_registry_server_n_resources() -> list[str]:
#     return list(reservoir.keys())

# def register_resource(
#     resource_name: str,
#     endpoint: str,
#     method: str,
#     headers: dict = None,
#     params: dict = None,
#     json: dict = None
# ) -> None:
    
#     reservoir[resource_name] = {
#         "endpoint": endpoint,
#         "method": method,
#         "headers": headers,
#         "params": params,
#         "json": json
#     }