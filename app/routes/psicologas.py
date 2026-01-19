from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.psicologa import Psicologa
from app.schemas.psicologa import (
    PsicologaCreate,
    PsicologaResponse,
    PsicologaUpdate
)

router = APIRouter(
    prefix="/psicologas",
    tags=["Psicólogas"]
)

@router.post("/", response_model=PsicologaResponse, status_code=201)
def criar_psicologa(
    psicologa: PsicologaCreate,
    db: Session = Depends(get_db)
):
    existe = (
        db.query(Psicologa)
        .filter(Psicologa.email == psicologa.email)
        .first()
    )

    if existe:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado"
        )

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


@router.delete("/{psicologa_id}", status_code=204)
def deletar_psicologa(
    psicologa_id: int,
    db: Session = Depends(get_db)
):
    psicologa = (
        db.query(Psicologa)
        .filter(Psicologa.id == psicologa_id)
        .first()
    )

    if not psicologa:
        raise HTTPException(
            status_code=404,
            detail="Psicóloga não encontrada"
        )

    db.delete(psicologa)
    db.commit()


@router.patch("/{psicologa_id}", response_model=PsicologaResponse)
def atualizar_psicologa(
    psicologa_id: int,
    dados: PsicologaUpdate,
    db: Session = Depends(get_db)
):
    psicologa = (
        db.query(Psicologa)
        .filter(Psicologa.id == psicologa_id)
        .first()
    )

    if not psicologa:
        raise HTTPException(
            status_code=404,
            detail="Psicóloga não encontrada"
        )

    dados_update = dados.model_dump(exclude_unset=True)

    if "email" in dados_update:
        email_existe = (
            db.query(Psicologa)
            .filter(
                Psicologa.email == dados_update["email"],
                Psicologa.id != psicologa_id
            )
            .first()
        )

        if email_existe:
            raise HTTPException(
                status_code=400,
                detail="Email já cadastrado para outra psicóloga"
            )

    for campo, valor in dados_update.items():
        setattr(psicologa, campo, valor)

    db.commit()
    db.refresh(psicologa)

    return psicologa
