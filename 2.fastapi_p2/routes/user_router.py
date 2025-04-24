from fastapi import APIRouter

# a variável 'router' esta sendo uma instância da classe APIRouter()
router = APIRouter()

@router.get('/api/v1/users')
async def get_users():
    return {"info": "Todos os usuarios"}