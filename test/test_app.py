import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_carre(client):
    response = client.get('/calcul?figure=carre&cote=4')
    data = response.get_json()
    assert data["figure"] == "carre"
    assert data["surface"] == 16.0
    assert data["perimetre"] == 16.0

def test_rectangle(client):
    response = client.get('/calcul?figure=rectangle&longueur=3&largeur=5')
    data = response.get_json()
    assert data["figure"] == "rectangle"
    assert data["surface"] == 15.0
    assert data["perimetre"] == 16.0

def test_triangle(client):
    response = client.get('/calcul?figure=triangle&base=3&hauteur=4')
    data = response.get_json()
    assert data["figure"] == "triangle"
    assert round(data["surface"], 2) == 6.0
    assert round(data["perimetre"], 2) == 12.0

def test_cercle(client):
    response = client.get('/calcul?figure=cercle&rayon=1')
    data = response.get_json()
    assert data["figure"] == "cercle"
    assert round(data["surface"], 2) == round(3.14159, 2)
    assert round(data["perimetre"], 2) == round(6.28318, 2)

def test_figure_inconnue(client):
    response = client.get('/calcul?figure=trapeze')
    assert response.status_code == 400
    assert "error" in response.get_json()
