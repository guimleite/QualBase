from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.banco_de_dados import SessionLocal
from src.models import TipoProduto
from src.esquemas import TipoProdutoOut, TipoProdutoCreate
from typing import List

router = APIRouter(
    prefix="/tipos-produto",
    tags=["Tipos de Produto"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TipoProdutoOut])
def listar_tipos(db: Session = Depends(get_db)):
    return db.query(TipoProduto).all()

@router.post("/", response_model=TipoProdutoOut, status_code=201)
def criar_tipo(tipo: TipoProdutoCreate, db: Session = Depends(get_db)):
    existente = db.query(TipoProduto).filter(TipoProduto.nome.ilike(tipo.nome)).first()
    if existente:
        raise HTTPException(status_code=400, detail="Tipo de produto já existe.")
    
    novo_tipo = TipoProduto(nome=tipo.nome)
    db.add(novo_tipo)
    db.commit()
    db.refresh(novo_tipo)
    return novo_tipo
