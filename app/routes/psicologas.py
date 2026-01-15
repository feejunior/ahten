from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.psicologa import PsicologaCreate
from app.models.psicologa import Psicologa
from app.db.database import get_db

from app.schemas.psicologa import PsicologaCreate, PsicologaResponse

router = APIRouter(
    prefix="/psicologas",
    tags=["Psicólogas"]
)

@router.post("/", response_model=PsicologaResponse, status_code=201)
def criar_psicologa(psicologa: PsicologaCreate, db: Session = Depends(get_db)):
    # verifica se email já existe
    existe = db.query(Psicologa).filter(Psicologa.email == psicologa.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    nova_psicologa = Psicologa(
        nome=psicologa.nome,
        email=psicologa.email,
        crp=psicologa.crp,
        ativa=psicologa.ativa
    )

    db.add(nova_psicologa)
    db.commit()
    db.refresh(nova_psicologa)

    return nova_psicologa


@router.get("/", response_model=list[PsicologaResponse])
def listar_psicologas(db: Session = Depends(get_db)):
    return db.query(Psicologa).all()


@router.delete("/{email}")
def deletar_psicologa(email: str, db: Session = Depends(get_db)):
    psicologa = db.query(Psicologa).filter(Psicologa.email == email).first()

    if not psicologa:
        raise HTTPException(status_code=404, detail="Psicóloga não encontrada")

    db.delete(psicologa)
    db.commit()

    return {"mensagem": "Psicóloga removida com sucesso!"}
