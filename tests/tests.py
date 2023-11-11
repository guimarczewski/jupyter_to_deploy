from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_main_response():
    response = client.get("/")
    assert response.json() == {"Hello": "World"}

def testa_produto():
    response = client.get("/produtos/1")
    assert response.json() == {
    "id": 1,
    "nome": "Notebook",
    "preco": 3500
}