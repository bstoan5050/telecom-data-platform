from src.ingestion.ingest_certificate import extract_certificate
from src.transform.transform_certificate import transform_certificate
from src.load.load_postgres import load_dataframe

def run() -> None:
    df = extract_certificate()
    df = transform_certificate(df)
    load_dataframe(df, "fact_certificate")

if __name__ == "__main__":
    run()
