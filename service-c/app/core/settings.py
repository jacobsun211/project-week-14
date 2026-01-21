from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    HOST_MYSQL: str = '127.0.0.1'
    PORT_MYSQL: str = '3306'
    USER_MYSQL: str = 'root'
    PASSWORD_MYSQL: str = 'pass'
    DATABASE_MYSQL: str = 'WEATHER_DB' 


setting = Settings() 

 