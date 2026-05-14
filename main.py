from fastapi import FastAPI
from app.routes.conta import router as conta_router

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}

app.include_router(conta_router)