from fastapi.testclient import TestClient
from code.main import app
clientes = TestClient(app)

def test_index():
    response = clientes.get("/") # requests
    data = {"message":"Hello World"}
    assert response.status_code == 200
    assert response.json() == data

def test_clientes():
    response = clientes.get("/clientes/") #requests
    data = [{"id_cliente":1,"nombre":"Fernando","email":"fer@email.com"},
            {"id_cliente":2,"nombre":"Erick","email":"erick@email.com"},
            {"id_cliente":3,"nombre":"Nataly","email":"nat@email.com"}]
    assert response.status_code == 200
    assert response.json() == data 

def test_clientes_1():
    response = clientes.get("/clientes/1") #request
    data = [{"id_cliente":1,"nombre":"Fernando","email":"fer@email.com"}]
    assert response.status_code == 200
    assert response.json() == data       