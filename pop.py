from main import Produto, Pedido, SessionLocal

db = SessionLocal()
p1 = Produto(nome="Arroz", descricao="Arroz tipo 1", preco=20.5, estoque=100)
p2 = Produto(nome="Feijão", descricao="Feijão preto", preco=8.9, estoque=200)
db.add_all([p1, p2])
db.commit()

pedido1 = Pedido(produto_id=p1.id, quantidade=10, cliente="Supermercado ABC")
db.add(pedido1)
db.commit()
db.close()
