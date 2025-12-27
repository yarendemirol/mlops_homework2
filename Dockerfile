FROM python:3.11-slim

WORKDIR /app

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Klasörleri kopyala
COPY src/ src/
COPY data/ data/

# Çevresel değişken (Import hatalarını önlemek için)
ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["python", "src/serve.py"]