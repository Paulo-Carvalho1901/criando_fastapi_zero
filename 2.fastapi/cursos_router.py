from fastapi import APIRouter, HTTPException, status
from models import Curso
from models import cursos
from typing import List, Optional, Any, Dict
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from time import sleep
from fastapi import Depends


def fake_db():
    try:
        print('Abrindo conexao com banco de dados')
        sleep(1)
    finally:
        print('Fechando conexao com banco de dados')
        sleep(1)


router = APIRouter()


@router.get('/cursos', 
        description='Retorna todos os cursos, ou uma lista vazia', 
        summary='Retorna todos os cursos',
        response_model=List[Curso],
        response_description='Cursos encontrados com sucesso.'
        )
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@router.get('/cursos/{curso_id}', 
            description='Retorna cada curso pelo ID do curso', 
            summary='Retorna cada curso pelo ID')
async def get_curso(curso_id: int = Path(title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@router.post('/cursos', status_code=status.HTTP_201_CREATED, 
             description='Adiciona curso na lista de cursos', 
             summary='Adiciona cursos',
             response_model=Curso)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
     
    return curso


@router.put('/cursos/{curso_id}', 
            description='Atualiza cursos existente da lista de cursos', 
            summary='Atualiza cursos')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Não existe um curso com ID {curso_id}")


@router.delete('/cursos/{curso_id}', description='Exclui cursos da lista pelo ID', summary='Exclui cursos existente pelo ID')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não exciste um curso com ID {curso_id}')


@router.get('/calculadora')
async def calcula(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default=None), c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma = soma + c

    print(f'X-GEEK: {x_geek}')

    return {'resultado': soma}
