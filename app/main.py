from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.psicologas import router as psicologas_router
from app.db.database import engine, Base
from app.models import psicologa


app = FastAPI(title="Ahten Psico")

app.include_router(health_router)
app.include_router(psicologas_router)
Base.metadata.create_all(bind=engine)

