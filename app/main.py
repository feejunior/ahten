from fastapi import FastAPI

app = FastAPI(title="Ahten Psico")

@app.get("/")
def home():
    return {"status": "ok", "mensagem": "API rodando"}
