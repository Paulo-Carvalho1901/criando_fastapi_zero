from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    # CONFIGURAÇÕES GERAIS USADAS NA APLICAÇÃO
    API_V1_STR: str = '/api/p1'
    DB_URL: str = 'postgresql+asyncpg://user:password@localhost:5432/facaldade'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()