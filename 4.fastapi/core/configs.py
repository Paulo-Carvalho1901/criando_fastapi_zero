from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:D%40vi0406@127.0.0.1:5432/faculdade"


    class Config:
        case_sensitive = True

settings = Settings = Settings()