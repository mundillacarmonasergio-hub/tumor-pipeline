from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

PROJECT = "/opt/airflow/project"
VENV = "/opt/airflow/pipeline_venv/bin"

with DAG(
    dag_id="tumor_pipeline",
    start_date=datetime(2026, 10, 1),
    schedule=None,
    catchup=False,
):
    ingest = BashOperator(
        task_id="ingest",
        bash_command=f"cd {PROJECT} && {VENV}/python ingest/ingest.py",
    )
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {PROJECT}/dbt_project && {VENV}/dbt run --profiles-dir .",
    )
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {PROJECT}/dbt_project && {VENV}/dbt test --profiles-dir .",
    )

    ingest >> dbt_run >> dbt_test