import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

CSV_PATH = Path("data/raw/tumores.csv")


def get_engine():
    url = (
        f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:"
        f"{os.environ['POSTGRES_PASSWORD']}@localhost:5440/"
        f"{os.environ['POSTGRES_DB']}"
    )
    return create_engine(url)


def main():
    df = pd.read_csv(CSV_PATH, dtype=str)
    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw"))

    df.to_sql("tumores", engine, schema="raw", if_exists="replace", index=False)
    print(f"{len(df)} filas cargadas en raw.tumores")


if __name__ == "__main__":
    main()