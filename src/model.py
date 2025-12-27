import pandas as pd
from sklearn.cluster import KMeans

_model = None


def train_model(df):
    global _model
    features = df[['Age', 'Annual_Income', 'Spending_Score', 'Gender', 'CustomerID_hashed']]
    model = KMeans(n_clusters=3, random_state=42)
    model.fit(features)
    _model = model
    return model


def predict_cluster(customer_id, age, income, score, gender):
    if _model is None:
        return 0
    features = pd.DataFrame([{
        'Age': age,
        'Annual_Income': income,
        'Spending_Score': score,
        'Gender': gender,
        'CustomerID_hashed': customer_id
    }])

    return int(_model.predict(features)[0])

# (Buraya bir kez Enter'a basıp boş satır bırakmayı unutma)