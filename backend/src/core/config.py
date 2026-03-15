from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "dev-secret"
    JWT_ALGORITHM: str = "HS256"
    DATABASE_URL: str = "sqlite:///./vortex.db"

    class Config:
        env_file = ".env"

settings = Settings()
