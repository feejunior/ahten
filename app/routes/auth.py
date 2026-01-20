from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserLogin, Token
from app.core.security import verificar_senha, criar_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=Token)
def login(dados: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == dados.email).first()

    if not user or not verificar_senha(dados.senha, user.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_access_token({"sub": str(user.id)})
    return {"access_token": token}
