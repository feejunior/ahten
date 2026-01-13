from pydantic import BaseModel, EmailStr

class PsicologaCreate(BaseModel):
    nome: str
    email: EmailStr
    crp: str
    ativa: bool = True
