from fastapi import FastAPI
app = FastAPI()

usuarios = [(1, 'caio', 'minhasenha1'), (2, 'joao', 'minhasenha2')]

@app.get("/teste/{id}")
def main(id: int):
    for i in usuarios:
        if i[0] == id:
            return i[0]
    return {'valor': id *10}