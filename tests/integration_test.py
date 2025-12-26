import pytest
from serve import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    sample_data = {
        "CustomerID": 123,
        "Gender": "Female",
        "Age": 28,
        "Annual Income": 55000,
        "Spending Score": 60
    }
    response = client.post("/predict", json=sample_data)
    data = response.get_json()
    assert response.status_code == 200
    assert "cluster" in data
    assert isinstance(data["cluster"], int)
