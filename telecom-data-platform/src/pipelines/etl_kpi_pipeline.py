from src.ingestion.ingest_kpi import extract_kpi
from src.transform.transform_kpi import transform_kpi
from src.load.load_postgres import load_dataframe

def run() -> None:
    df = extract_kpi()
    df = transform_kpi(df)
    load_dataframe(df, "fact_network_kpi_hourly")

if __name__ == "__main__":
    run()
