import uvicorn
from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)