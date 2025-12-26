import pytest
import pandas as pd
from feature_engineering import encode_gender, hash_customer_id

def test_encode_gender():
    df = pd.DataFrame({'Gender': ['Male', 'Female']})
    df['Gender'] = encode_gender(df['Gender'])
    assert df['Gender'].tolist() == [0, 1]

def test_hash_customer_id():
    df = pd.DataFrame({'CustomerID': [101, 102, 103]})
    df['CustomerID_hashed'] = hash_customer_id(df['CustomerID'], num_buckets=5)
    for val in df['CustomerID_hashed']:
        assert 0 <= val < 5
