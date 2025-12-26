import requests
import time


def test_smoke():
    url = "http://127.0.0.1:5000/predict"
    sample = {
        "CustomerID": 999,
        "Gender": "Male",
        "Age": 30,
        "Annual Income": 60000,
        "Spending Score": 50
    }

    # Container’in açılması için kısa bekleme
    time.sleep(5)
    response = requests.post(url, json=sample)
    assert response.status_code == 200
    assert "cluster" in response.json()
