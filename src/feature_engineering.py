import pandas as pd
import hashlib
import os # HATA 1: Bu kütüphane eklendi ama hiç kullanılmadı (F401)

def load_data(path):
    df = pd.read_csv(path)
    return df
# HATA 2: Fonksiyonlar arasında 2 boş satır olması gerekirken hiç boşluk yok (E302)
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
# HATA 3: Dosyanın en sonuna bilerek 3-4 tane boş satır ekle (W391)