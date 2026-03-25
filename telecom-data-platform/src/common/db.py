from sqlalchemy import create_engine
from src.common.config import DB_URL

def get_engine():
    return create_engine(DB_URL)
