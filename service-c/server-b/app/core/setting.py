from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST_C: str = '192.168.30.62'
    PORT_C: str = '8081'


settings = Settings()