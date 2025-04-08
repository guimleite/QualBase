from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.banco_de_dados import SessionLocal
from src.models import Marca
from src.esquemas import MarcaOut, MarcaCreate
from typing import List

router = APIRouter(tags=["Marcas"])

# Dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1. Listar marcas
@router.get("/marcas", response_model=List[MarcaOut])
def listar_marcas(db: Session = Depends(get_db)):
    return db.query(Marca).all()


# 2. Criar nova marca
@router.post("/marcas", response_model=MarcaOut, status_code=201)
def criar_marca(marca: MarcaCreate, db: Session = Depends(get_db)):
    marca_existente = db.query(Marca).filter(Marca.nome.ilike(marca.nome)).first()
    if marca_existente:
        raise HTTPException(status_code=400, detail="Marca já cadastrada.")
    
    nova_marca = Marca(nome=marca.nome)
    db.add(nova_marca)
    db.commit()
    db.refresh(nova_marca)
    return nova_marca
