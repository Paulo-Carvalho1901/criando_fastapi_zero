from fastapi import FastAPI
from cursos_router import router

app = FastAPI(
    title="API de cursos",
    version="0.0.1",
    description="Uma API para estudo do FastAPI",
    )

app.include_router(router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)
