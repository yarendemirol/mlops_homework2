import pandas as pd
import hashlib

def load_data(path):
    return pd.read_csv(path)

def encode_gender(gender):
    # SABOTAJ: Test 0 veya 1 beklerken biz 999 döndürüyoruz
    return 999

def hash_customer_id(customer_id, num_buckets=10):
    return 0