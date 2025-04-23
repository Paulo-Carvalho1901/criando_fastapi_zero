from fastapi import FastAPI

app = FastAPI()  # estanciando o obejeto


@app.get('/mensagem')  # endpoit ('/msg') ou qualquer coisa que queira
async def mensagem():
    return {"msg": "Hello, World..."}


# Fazendo a chamada direta no código
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)
