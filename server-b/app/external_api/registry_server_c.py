from external_api.client import ExternalApiClient
from core.errors import EndpointNotFoundError
from core.setting import settings

base_url = 'http://' + settings.HOST_C
port = settings.PORT_C

reservoir = {

    "create": {"base_url": base_url, "port": port, "endpoint": "records", 
            "method": "POST", "headers": None},


}


def get_resource(resource_name: str) -> ExternalApiClient:

    resource = reservoir.get(resource_name)

    if not resource:
        raise EndpointNotFoundError(resource_name)

    return ExternalApiClient(**resource)
