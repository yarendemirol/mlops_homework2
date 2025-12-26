from flask import Flask, request, jsonify
from feature_engineering import encode_gender, hash_customer_id, load_data
from model import train_model, predict_cluster
import pandas as pd

app = Flask(__name__)

df = load_data("data/mall_customers.csv")
df['Gender'] = encode_gender(df['Gender'])
df['CustomerID_hashed'] = hash_customer_id(df['CustomerID'], num_buckets=10)
train_model(df)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    customer_id = hash_customer_id(data["CustomerID"], num_buckets=10)
    gender = encode_gender(data["Gender"])
    age = data["Age"]
    income = data["Annual Income"]
    score = data["Spending Score"]
    prediction = predict_cluster(customer_id, gender, age, income, score)
    return jsonify({"cluster": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
