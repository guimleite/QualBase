from pydantic import BaseModel
from typing import Optional, List


# ------------------ Marca ------------------

class MarcaBase(BaseModel):
    nome: str

class MarcaOut(MarcaBase):
    id: int

    class Config:
        orm_mode = True
        
class MarcaCreate(BaseModel):
    nome: str


# TipoProduto

class TipoProdutoBase(BaseModel):
    nome: str

class TipoProdutoCreate(TipoProdutoBase):
    pass

class TipoProdutoOut(TipoProdutoBase):
    id: int

    class Config:
        orm_mode = True

# ------------------ Produto ------------------

class ProdutoBase(BaseModel):
    nome: str

class ProdutoCreate(BaseModel):
    nome: str
    marca_id: int
    tipo_id: int

class ProdutoOut(BaseModel):
    id: int
    nome: str
    marca_id: int
    tipo_id: int

    class Config:
        orm_mode = True
# ------------------ Cor ------------------

class RGB(BaseModel):
    r: int
    g: int
    b: int

class CorBase(BaseModel):
    nome: str
    cor_r: int
    cor_g: int
    cor_b: int

class CorCreate(BaseModel):
    nome: str
    cor_r: int
    cor_g: int
    cor_b: int
    produto_id: int

class CorOut(BaseModel):
    id: int
    nome: str
    cor_r: int
    cor_g: int
    cor_b: int
    produto_id: int

    class Config:
        orm_mode = True
