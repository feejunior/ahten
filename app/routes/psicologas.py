from fastapi import APIRouter
from app.schemas.psicologa import PsicologaCreate
from fastapi import HTTPException

router = APIRouter(
    prefix="/psicologas",
    tags=["Psicólogas"]
)

# Lista em memória (simula banco)
psicologas_db = []

@router.post("/")
def criar_psicologa(psicologa: PsicologaCreate):
    psicologas_db.append(psicologa)
    return psicologa

@router.get("/")
def listar_psicologas():
    return psicologas_db

@router.delete("/{email}")
def deletar_psicologa(email: str):
    for psicologa in psicologas_db:
        if psicologa.email == email:
            psicologas_db.remove(psicologa)
            return {"mensagem": "Psicóloga removida com sucesso!"}

    raise HTTPException(
        status_code=404,
        detail="Psicóloga não encontrada!"
    )
