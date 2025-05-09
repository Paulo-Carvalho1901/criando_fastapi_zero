# IMPORTA FASTAPI
from fastapi import FastAPI, HTTPException, status

# IMPORTA MODEL
from models import Curso

# Instanciando o Objeto
app = FastAPI()

# Dicionários de cursos
cursos = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 122,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmo e logica de programação",
        "aulas": 87,
        "horas": 67
    }
}

"""
GET CURSOS 
Busca todos os cursos existentes no seu python
"""
@app.get('/cursos') # definindo o seu endpoint '/cursos'
async def get_cursos(): 
    return cursos


"""
GET CURSO
Busca apenas curso pelo curso_id

/cursos/: É a parte fixa do caminho.
{curso_id}: É um path parameter (parâmetro de caminho). Indica que, no lugar de curso_id, 
o valor específico fornecido na requisição será usado.
"""
@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int): # fazendo type hint informando o tipo de dado que iremos passar
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

"""
POST CURSO - Adicionando um curso a lista de cursos

"""

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

"""
PUT CURSO - Atualizar um curso na lista
"""

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com id {curso_id}')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)