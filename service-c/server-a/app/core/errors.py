class EndpointNotFoundError(Exception):
    def __init__(self, endpoint: str):
        
        self.message = f"{endpoint} does not exist in the api repository"
        super().__init__(self.message)


class LocationNotFoundError(Exception):
    def __init__(self, location_name: str):
        
        self.message = f"Location not found: {location_name}"
        super().__init__(self.message)
