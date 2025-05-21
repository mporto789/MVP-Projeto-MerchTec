#MVP Entrega Atacadista-Supermercado

Projeto backend básico para um MVP de sistema de entrega entre atacadistas e supermercados, desenvolvido com FastAPI, SQLite e HTTPS.

Funcionalidades
Cadastro e login de usuários (supermercado ou atacadista)

Listagem de produtos

Criação e visualização de pedidos

API segura com HTTPS usando certificados SSL

Tecnologias
Python 3.11+

FastAPI

SQLAlchemy (ORM)

SQLite (banco de dados)

Uvicorn com suporte a HTTPS

Como rodar
Instale as dependências:

pip install fastapi uvicorn[standard] sqlalchemy pydantic bcrypt python-multipart

Gere certificados SSL para testes locais:

openssl req -x509 -newkey rsa:4096 -keyout certs/key.pem -out certs/cert.pem -days 365 -nodes

Inicie o servidor HTTPS:

uvicorn app.main:app --host 0.0.0.0 --port 443 --ssl-keyfile=certs/key.pem --ssl-certfile=certs/cert.pem

Estrutura do projeto