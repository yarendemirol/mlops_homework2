import requests
import time

def test_smoke():
    url = "http://127.0.0.1:5000/predict"
    sample = {
        "CustomerID": 999,
        "Gender": "Male",
        "Age": 30,
        "Annual_Income": 60000,
        "Spending_Score": 50
    }
    # Konteynerın hazır olması için kısa bir bekleme
    response = requests.post(url, json=sample)
    assert response.status_code == 200
    assert "cluster" in response.json()