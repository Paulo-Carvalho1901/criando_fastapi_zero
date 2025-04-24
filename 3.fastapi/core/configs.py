from typing import List
from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    # CONFIGURAÇÕES GERAIS USADAS NA APLICAÇÃO
    API_V1_STR: str = '/api/p1'
    DB_URL: str = 'postgresql+asyncpg://user:password@localhost:5432/facaldade'
    DBBaseModel = declarative_base()

    