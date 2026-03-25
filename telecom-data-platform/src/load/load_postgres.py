import pandas as pd
from src.common.db import get_engine

def load_dataframe(df: pd.DataFrame, table_name: str, if_exists: str = "append") -> None:
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists=if_exists, index=False)
    print(f"Loaded {len(df)} rows into {table_name}")
