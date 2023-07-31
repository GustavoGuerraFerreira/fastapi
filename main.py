from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    senha: str

lista = [
    Usuario(id=1, nome='Gustavo', senha="1"),
    Usuario(id=2, nome='Matheus', senha="2"),
    Usuario(id=3, nome='Roberto', senha="3")
]
@app.post("/usuario")
def main(usuario : Usuario):
    lista.append(usuario)
    return "usuario cadastrado"

@app.get("/usuariolistar")
def main():
    return lista