from pydantic.v1 import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar


class Settings(BaseSettings):
    # CONFIGURAÇÕES GERAIS USADAS NA APLICAÇÃO
    API_V1_STR: str = '/api/v1' # Versão da API
    DB_URL: str = 'postgresql+asyncpg://postgres:D@vi0406d@127.0.0.1:5432/faculdade'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings() 