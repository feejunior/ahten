from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class Psicologa(Base):
    __tablename__ = "psicologas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    crp = Column(String, unique=True, nullable=False)
    ativa = Column(Boolean, default=True)
