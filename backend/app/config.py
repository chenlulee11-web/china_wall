from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./data/china_wall.db"
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]
    wikipedia_user_agent: str = "ChinaWall/1.0 (educational project)"
    seed_data_path: str = "./data/seed.json"

    class Config:
        env_file = ".env"


settings = Settings()
