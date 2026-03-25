import pandas as pd
from src.common.config import RAW_KPI_PATH

def extract_kpi():
    return pd.read_csv(RAW_KPI_PATH)

if __name__ == "__main__":
    print(extract_kpi().head())
