from pydantic import BaseModel, EmailStr
from typing import Optional


class PsicologaCreate(BaseModel):
    nome: str
    email: EmailStr
    crp: str
    ativa: bool = True


class PsicologaResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    crp: str
    ativa: bool

    class Config:
        from_attributes = True

class PsicologaUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    crp: Optional[str] = None
    ativa: Optional[bool] = None
    