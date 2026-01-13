from fastapi import APIRouter
from app.schemas.psicologa import PsicologaCreate

router = APIRouter(
    prefix="/psicologas",
    tags=["Psicólogas"]
)

@router.post("/")
def criar_psicologa(psicologa: PsicologaCreate):
    return psicologa
    