from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST_B: str 
    PORT_B: str 


settings = Settings()