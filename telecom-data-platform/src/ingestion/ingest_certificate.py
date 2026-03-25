import pandas as pd
from src.common.config import RAW_CERT_PATH

def extract_certificate():
    return pd.read_csv(RAW_CERT_PATH)

if __name__ == "__main__":
    print(extract_certificate().head())
