import pandas as pd

def transform_certificate(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    today = pd.Timestamp.today().normalize()
    df["issue_date"] = pd.to_datetime(df["issue_date"], errors="coerce").dt.date
    df["expiry_date"] = pd.to_datetime(df["expiry_date"], errors="coerce").dt.date
    expiry_ts = pd.to_datetime(df["expiry_date"], errors="coerce")
    df["days_to_expiry"] = (expiry_ts - today).dt.days

    def status(days):
        if pd.isna(days):
            return "unknown"
        if days < 0:
            return "expired"
        if days <= 30:
            return "expiring_soon"
        return "valid"

    df["document_status"] = df["days_to_expiry"].apply(status)
    return df
