from fastapi import FastAPI

# Intanciancio um objeto
app = FastAPI()

@app.get('/')
async def root():
    return {"msg": "criado minha primeira API com FasTAPI"}

