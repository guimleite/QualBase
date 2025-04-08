from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.banco_de_dados import SessionLocal
from src.models import Cor, Produto
from src.esquemas import CorCreate, CorOut

router = APIRouter(
    prefix="/cor",
    tags=["Cor"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CorOut, status_code=201)
def criar_cor(cor: CorCreate, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == cor.produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    nova_cor = Cor(
        nome=cor.nome,
        cor_r=cor.cor_r,
        cor_g=cor.cor_g,
        cor_b=cor.cor_b,
        produto_id=cor.produto_id
    )
    db.add(nova_cor)
    db.commit()
    db.refresh(nova_cor)
    return nova_cor

@router.get("/produto/{produto_id}", response_model=List[CorOut])
def listar_cores_por_produto(produto_id: int, db: Session = Depends(get_db)):
    cores = db.query(Cor).filter(Cor.produto_id == produto_id).all()
    return cores
