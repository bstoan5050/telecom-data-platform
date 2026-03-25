import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL", "postgresql+psycopg2://telecom_user:telecom_pass@localhost:5432/telecom_db")
RAW_KPI_PATH = os.getenv("RAW_KPI_PATH", "data/raw/kpi_sample.csv")
RAW_CERT_PATH = os.getenv("RAW_CERT_PATH", "data/raw/certificate_sample.csv")
