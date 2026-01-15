from pydantic import BaseModel, EmailStr

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
