import requests
import time
import pytest  # Bu eksikti, ekledik


def test_smoke():
    url = "http://127.0.0.1:5000/predict"
    sample = {
        "CustomerID": 999,
        "Gender": "Male",
        "Age": 30,
        "Annual_Income": 60000,
        "Spending_Score": 50
    }

    # 5 deneme x 10 saniye = 50 saniye boyunca deneyecek
    for i in range(5):
        try:
            response = requests.post(url, json=sample, timeout=5)
            if response.status_code == 200:
                assert "cluster" in response.json()
                return
        except requests.exceptions.ConnectionError:
            print(f"Deneme {i + 1}: Uygulama henüz hazır değil, bekleniyor...")
            time.sleep(10)  # Bekleme süresini artırdık

    pytest.fail("Uygulama zamanında ayağa kalkmadı.")