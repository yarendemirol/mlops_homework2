import sys
import os
import pandas as pd

# src klasörünü bulabilmesi için yolu ekliyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.feature_engineering import encode_gender, hash_customer_id

def test_encode_gender():
    df = pd.DataFrame({'Gender': ['Male', 'Female']})
    df['Gender'] = encode_gender(df['Gender'])
    assert df['Gender'].tolist() == [0, 1]

def test_hash_customer_id():
    # Hashing logic: bucket index kontrolü [cite: 13]
    df = pd.DataFrame({'CustomerID': [101, 102, 103]})
    df['CustomerID_hashed'] = hash_customer_id(df['CustomerID'], num_buckets=5)
    for val in df['CustomerID_hashed']:
        assert 0 <= val < 5