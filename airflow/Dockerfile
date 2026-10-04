FROM apache/airflow:3.3.1

RUN python -m venv /opt/airflow/pipeline_venv \
    && /opt/airflow/pipeline_venv/bin/pip install --no-cache-dir \
       pandas sqlalchemy psycopg2-binary python-dotenv dbt-core dbt-postgres