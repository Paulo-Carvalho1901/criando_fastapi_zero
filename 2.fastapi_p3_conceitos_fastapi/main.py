# IMPORTA FASTAPI
from fastapi import FastAPI, HTTPException, status

# Instanciando o Objeto
app = FastAPI()

# Didionários de cursos
cursos = {
    1: {
        "titulo": "Programação para leigod",
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
    curso = cursos[curso_id]
    curso.update({"id": curso_id} )

    return curso



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)