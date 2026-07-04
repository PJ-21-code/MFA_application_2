from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 20

    class Config:
        env_file = '.env'
        extra= 'ignore'

settings= Settings()        