import pandas as pd
from sklearn.cluster import KMeans

_model = None

def train_model(df):
    global _model
    features = df[['Age', 'Annual Income', 'Spending Score', 'Gender', 'CustomerID_hashed']]
    model = KMeans(n_clusters=3, random_state=42)
    model.fit(features)
    _model = model
    return model

def predict_cluster(customer_id, gender, age, income, score):
    global _model
    if _model is None:
        return 0
    features = pd.DataFrame([{
        'CustomerID_hashed': customer_id,
        'Gender': gender,
        'Age': age,
        'Annual Income': income,
        'Spending Score': score
    }])
    return int(_model.predict(features)[0])
