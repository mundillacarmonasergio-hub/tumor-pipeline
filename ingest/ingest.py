import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

CSV_PATH = Path("data/raw/tumores.csv")


def get_engine():
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5440")
    url = (
        f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:"
        f"{os.environ['POSTGRES_PASSWORD']}@{host}:{port}/"
        f"{os.environ['POSTGRES_DB']}"
    )
    return create_engine(url)


def main():
    df = pd.read_csv(CSV_PATH, dtype=str)
    engine = get_engine()

    # Una sola transacción: si algo falla, la tabla no queda vacía.
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw"))
        conn.execute(
            text(
                """
                DO $$
                BEGIN
                    IF to_regclass('raw.tumores') IS NOT NULL THEN
                        TRUNCATE TABLE raw.tumores;
                    END IF;
                END $$;
                """
            )
        )
        df.to_sql("tumores", conn, schema="raw", if_exists="append", index=False)

    print(f"{len(df)} filas cargadas en raw.tumores")


if __name__ == "__main__":
    main()