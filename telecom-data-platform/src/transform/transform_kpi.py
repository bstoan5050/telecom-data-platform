import pandas as pd

def transform_kpi(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp", "station_code", "cell_code"]).drop_duplicates()

    for col in ["total_call_attempt", "connected_call", "miss_call", "silence_call", "drop_call"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df["miss_call_rate"] = df["miss_call"] / df["total_call_attempt"].replace(0, 1)
    df["silence_call_rate"] = df["silence_call"] / df["connected_call"].replace(0, 1)
    df["mc_staon_num_r"] = (df["miss_call"] + df["silence_call"]) / df["total_call_attempt"].replace(0, 1)
    return df
