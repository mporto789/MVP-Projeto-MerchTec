from pydantic import BaseModel

class ProdutoOut(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    estoque: int

    model_config = {
        "from_attributes": True
    }

class PedidoCreate(BaseModel):
    produto_id: int
    quantidade: int

class PedidoOut(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    cliente: str

    model_config = {
        "from_attributes": True
    }

class UsuarioCreate(BaseModel):
    username: str
    password: str
    tipo: str  # "supermercado" ou "atacadista"

class UsuarioOut(BaseModel):
    id: int
    username: str
    tipo: str

    model_config = {
        "from_attributes": True
    }
