from datetime import datetime

from pprint import pprint

from airflow.api_connexion.schemas.xcom_schema import xcom_schema, XComSchema
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from pendulum import DateTime

with DAG(
    dag_id="03_context",
    start_date=datetime(year=2024, month=10, day=5),
    end_date=datetime(year=2024, month=12, day=30),
    schedule='@hourly',
):
    bash_context_operator = BashOperator(
        task_id='bash_context_operator',
        bash_command='echo "{{ task.task_id }} is running in the {{ dag.dag_id }} pipeline"',
    )

    def print_context(**context):
        execution_datetime: DateTime = context['execution_date']
        pprint(f"This script was executed at {execution_datetime.strftime('%Y-%m-%d')}")
        pprint(f"Three days after execution is {execution_datetime.add(days=3).strftime('%Y-%m-%d')}")
        pprint(f"This script run date is {context['ts']}")

    python_context_operator = PythonOperator(
        task_id='python_context_operator',
        python_callable=print_context,
    )

    bash_context_operator >> python_context_operator

