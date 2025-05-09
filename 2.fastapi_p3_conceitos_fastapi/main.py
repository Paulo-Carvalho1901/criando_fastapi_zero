# IMPORTA FASTAPI
from fastapi import FastAPI

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
@app.get('/cursos')
async def get_cursos():
    return cursos


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)