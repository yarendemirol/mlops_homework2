import os
import pandas as pd
import hashlib


def load_data(path):
    df = pd.read_csv(path)
    return df


def encode_gender(gender):
    if isinstance(gender, str):
        return 0 if gender == 'Male' else 1
    else:
        return gender.map({'Male': 0, 'Female': 1})


def hash_customer_id(customer_id, num_buckets=10):
    if isinstance(customer_id, int):
        return int(hashlib.md5(str(customer_id).encode()).hexdigest(), 16) % num_buckets
    else:
        return customer_id.apply(lambda x: int(hashlib.md5(str(x).encode()).hexdigest(), 16) % num_buckets)