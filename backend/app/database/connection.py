from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlmodel import create_engine

BACKEND_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        extra="ignore"
    )

settings = Settings()

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)
