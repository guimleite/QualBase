from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.banco_de_dados import SessionLocal
from src.models import Produto, Marca, TipoProduto
from src.esquemas import ProdutoOut, ProdutoCreate
from typing import List

router = APIRouter(
    prefix="/produto",
    tags=["Produto"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Listar todos os produtos
@router.get("/", response_model=List[ProdutoOut])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()

# 2. Criar um produto
@router.post("/", response_model=ProdutoOut, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    marca = db.query(Marca).filter(Marca.id == produto.marca_id).first()
    tipo = db.query(TipoProduto).filter(TipoProduto.id == produto.tipo_id).first()

    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de produto não encontrado")

    novo_produto = Produto(
        marca_id=produto.marca_id,
        tipo_id=produto.tipo_id,
        nome=produto.nome
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

# 3. Produtos por marca
@router.get("/marca/{marca_id}", response_model=List[ProdutoOut])
def listar_por_marca(marca_id: int, db: Session = Depends(get_db)):
    return db.query(Produto).filter(Produto.marca_id == marca_id).all()

# 4. Produtos por tipo
@router.get("/tipo/{tipo_id}", response_model=List[ProdutoOut])
def listar_por_tipo(tipo_id: int, db: Session = Depends(get_db)):
    return db.query(Produto).filter(Produto.tipo_id == tipo_id).all()
