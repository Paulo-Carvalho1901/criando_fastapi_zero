from fastapi import FastAPI

# Intanciancio um objeto
app = FastAPI()

@app.get('/mensagem') # endpoints da nossa api
async def mensagem():
    return {"msg": "criado minha primeira API com FasTAPI"}


# CRIANDO UMA ENTRADA PARA EXECUÇÃO
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)
