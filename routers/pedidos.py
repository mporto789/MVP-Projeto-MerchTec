from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Pedido, Produto
from schemas import PedidoCreate, PedidoOut

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[PedidoOut])
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(Pedido).all()

@router.post("/", response_model=PedidoOut)
def criar_pedido(pedido: PedidoCreate, cliente: str, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == pedido.produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    if produto.estoque < pedido.quantidade:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")
    produto.estoque -= pedido.quantidade
    novo_pedido = Pedido(produto_id=pedido.produto_id, quantidade=pedido.quantidade, cliente=cliente)
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido
