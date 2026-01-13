from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.psicologas import router as psicologas_router

app = FastAPI(title="Ahten Psico")

app.include_router(health_router)
app.include_router(psicologas_router)
