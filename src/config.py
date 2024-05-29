from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CMC_API_KEY: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    SECRET_KEY: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
