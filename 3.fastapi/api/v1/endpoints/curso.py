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

router = APIRouter()


# POST curso - criando recurso
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)

    db.add(novo_curso)
    await db.commit()
    await db.refresh(novo_curso)

    return novo_curso


# GET cursos - trazer todos recursos
@router.get('/', response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()

        return cursos


# GET curso - trazer um recurso especifico
@router.get('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        
        if curso:
            return curso
        else:
            raise HTTPException(detail='Curso não encontrado', 
                                status_code=status.HTTP_404_NOT_FOUND)
        

# PUT curso - fazer atualizaçao do recurso
@router.put('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up = result.scalar_one_or_none()
        
        # Fazendo a atulização'
        if curso_up:
            curso_up.titulo = curso.titulo
            curso_up.aulas = curso.aulas
            curso_up.horas = curso.horas

            await session.commit()

            return curso_up
        else:
            raise HTTPException(detail='Curso não encontrado', 
                                status_code=status.HTTP_404_NOT_FOUND)
        

# DELETE curso - fazer um delete
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del = result.scalar_one_or_none()
        
        # Fazendo o delete do curso'
        if curso_del:
            await session.delete(curso_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Curso não encontrado', 
                                status_code=status.HTTP_404_NOT_FOUND)