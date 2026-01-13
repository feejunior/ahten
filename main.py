from fastapi import FastAPI

app = FastAPI(title="Sistema de Logística para Psicólogas")

@app.get("/")
def home():
    return {"status": "ok", "mensagem": "API rodando"}
