import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.serve import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    sample_data = {
        "CustomerID": 123,
        "Gender": "Female",
        "Age": 28,
        "Annual_Income": 55000,
        "Spending_Score": 60
    }
    response = client.post("/predict", json=sample_data)
    data = response.get_json()
    assert response.status_code == 200
    assert "cluster" in data