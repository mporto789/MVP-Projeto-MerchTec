from fastapi import APIRouter, Depends
from typing import List
from models import Produto
from schemas import ProdutoOut
from database import SessionLocal

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.get("/", response_model=List[ProdutoOut])
def listar_produtos():
    db = SessionLocal()
    produtos = db.query(Produto).all()
    db.close()
    return produtos
