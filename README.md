#MVP Entrega Atacadista-Supermercado (FastAPI + HTTPS)
Projeto básico de backend para um MVP de sistema de entrega de mercadorias entre atacadistas e supermercados.

Funcionalidades principais
Cadastro e login de usuários (supermercados e atacadistas) com senha hashed (bcrypt)

Listagem de produtos

Criação e listagem de pedidos

Banco SQLite simples com SQLAlchemy ORM

API segura via HTTPS usando certificados SSL (self-signed ou Let's Encrypt)

Tecnologias usadas
Python 3.11+

FastAPI

SQLAlchemy

Pydantic (v2)

Uvicorn (com suporte SSL)

bcrypt para hash de senha

Como rodar
Instale dependências:

bash
Copiar
Editar
pip install fastapi uvicorn[standard] sqlalchemy pydantic bcrypt python-multipart
Gere certificados SSL (para desenvolvimento):

bash
Copiar
Editar
openssl req -x509 -newkey rsa:4096 -keyout certs/key.pem -out certs/cert.pem -days 365 -nodes
Inicie o servidor HTTPS:

bash
Copiar
Editar
uvicorn app.main:app --host 0.0.0.0 --port 443 --ssl-keyfile=certs/key.pem --ssl-certfile=certs/cert.pem
Estrutura do projeto
pgsql
Copiar
Editar
app/
├── main.py
├── models.py
├── database.py
├── schemas.py
├── routers/
│   ├── auth.py
│   ├── produtos.py
│   └── pedidos.py
certs/
├── cert.pem
└── key.pem
Se quiser, posso te ajudar a montar um README.md completo com instruções, exemplos de requisições e dicas de deploy! Quer?
