from fastapi import FastAPI
from src.models import Base
from src.banco_de_dados import engine
from src.rotas import rotas_marca, rotas_tipo_produto, rotas_produto, rotas_cor
import time
from sqlalchemy.exc import OperationalError
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Qual Base - API",
    version="1.0",
    description="Esta é a primeira versão da api da Qual Base. 💄",
    openapi_url="/api/v1/openapi.json",
)

# ⚙️ Permitir tudo para dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    for _ in range(10):
        try:
            Base.metadata.create_all(bind=engine)
            break
        except OperationalError as e:
            time.sleep(2)
    else:
        raise

@app.get("/healthz")
def healthz():
    return {"mensagem": "Aplicação está em saudável."}

app.include_router(rotas_marca.router, prefix="/api/v1")  # Consistência
app.include_router(rotas_tipo_produto.router, prefix="/api/v1")
app.include_router(rotas_produto.router, prefix="/api/v1")
app.include_router(rotas_cor.router, prefix="/api/v1")