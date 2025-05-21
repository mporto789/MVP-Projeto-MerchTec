from fastapi import FastAPI
from routers import auth, produtos, pedidos

app = FastAPI()

app.include_router(auth.router)
app.include_router(produtos.router)
app.include_router(pedidos.router)
