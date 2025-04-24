from fastapi import APIRouter

# a variável 'router' esta sendo uma instância da classe APIRouter()
router = APIRouter()

# ROTA DOS CURSOS - ENDPOINT
@router.get('/api/v1/cursos') 
async def get_cursos():
    return {"info": "Todos os cursos"}
