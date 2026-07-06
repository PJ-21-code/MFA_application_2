from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):

    JWT_SECRET_KEY: Optional[str]
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 20
    JWKS_URL: Optional[str]= "http://localhost:8080/realms/MFA_application/protocol/openid-connect/certs"

    class Config:
        env_file = '.env'
        extra= 'ignore'

settings= Settings()        