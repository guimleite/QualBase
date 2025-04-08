from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)

    produtos = relationship("Produto", back_populates="marca")

class TipoProduto(Base):
    __tablename__ = "tipos_produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)

    produtos = relationship("Produto", back_populates="tipo")

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    marca_id = Column(Integer, ForeignKey("marcas.id"), nullable=False)
    tipo_id = Column(Integer, ForeignKey("tipos_produto.id"), nullable=False)
    nome = Column(String, nullable=False)

    marca = relationship("Marca", back_populates="produtos")
    tipo = relationship("TipoProduto", back_populates="produtos")
    cores = relationship("Cor", back_populates="produto")

class Cor(Base):
    __tablename__ = "cores"

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    nome = Column(String, nullable=False)  # Ex: "230 Rosado"
    cor_r = Column(Integer, nullable=False)
    cor_g = Column(Integer, nullable=False)
    cor_b = Column(Integer, nullable=False)

    produto = relationship("Produto", back_populates="cores")
