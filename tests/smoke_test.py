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

    # Uygulamanın hazır olması için 5 kez, 5 saniye arayla deneme yapar
    for i in range(5):
        try:
            response = requests.post(url, json=sample, timeout=5)
            if response.status_code == 200:
                assert "cluster" in response.json()
                return  # Başarılıysa testi bitir
        except requests.exceptions.ConnectionError:
            print(f"Bağlantı denemesi {i + 1} başarısız, bekleniyor...")
            time.sleep(5)

    # Eğer 5 deneme de başarısız olursa testi fail et
    pytest.fail("Uygulama zamanında ayağa kalkmadı.")