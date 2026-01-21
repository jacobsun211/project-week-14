from utils.client import async_request, Response


class ExternalApiClient:
    def __init__(self, base_url, port, endpoint, method,*,headers=None):

        self.base_url = base_url
        self.port = port
        self.endpoint = endpoint
        self.method = method
        self.headers = headers


    def build_uri(self, resource_id=None) -> str:
        url = f"{self.base_url}:{self.port}"

        if self.endpoint:
            url += f"/{self.endpoint}"
        if resource_id:
            url += f"/{resource_id}"
        
        return url  

    async def call(self, resource_id=None, params=None, json=None) -> Response:

        uri = self.build_uri(resource_id=resource_id)
        
        response = await async_request(self.method, 
                                       uri, 
                                       headers=self.headers, 
                                       params=params, 
                                       json=json)
        return response
