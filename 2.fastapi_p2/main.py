from fastapi import FastAPI

# IMPORTANDO AS ROTAS PARA MAIN
from routes import curso_router
from routes import user_router

# INSTÂNCIANDO A CLASSE FASTAPI
app = FastAPI()

# INCLUINDO AS ROTAS 
app.include_router(curso_router.router, tags=['cursos'])
app.include_router(user_router.router, tags=['users'])


# ENTRADAS
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)
