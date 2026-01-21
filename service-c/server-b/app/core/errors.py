class EndpointNotFoundError(Exception):
    def __init__(self, endpoint: str):
        
        self.message = f"{endpoint} does not exist in the api repository"
        super().__init__(self.message)
