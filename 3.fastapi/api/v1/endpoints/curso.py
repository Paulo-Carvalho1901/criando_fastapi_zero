# importando lib typing
from typing import List

# importando funcionalidades do fastpai
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

# importando funcionalidades do sqlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# importando os importes dos aquivos 
from models.curso_models import CursoModel
from schemas.curso_schema import CursoSchema
from core.deps import get_session

