from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Notebook",
        "preco": 3500.00,
    },
    {
        "id": 2,
        "nome": "PC",
        "preco": 2000.00,
    },
    {
        "id": 3,
        "nome": "TV",
        "preco": 1200.00,
    }

]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/produtos")
def listar_produtos():
    return produtos