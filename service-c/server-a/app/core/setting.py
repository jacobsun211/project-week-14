from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST_B: str = '127.0.0.1'
    PORT_B: str = '8080'


settings = Settings()