from datetime import datetime

from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="00_hello_world",
    start_date=datetime(year=2019, month=1, day=1),
    end_date=datetime(year=2019, month=1, day=5),
    schedule="@daily",
):
    hello = BashOperator(
        task_id="hello",
        bash_command="echo 'hello'",
    )
    
    world = PythonOperator(
        task_id="world",
        python_callable=lambda: print("world"),
    )

    how_are_you_doing_operator = PythonOperator(
        task_id="how_are_you_doing",
        python_callable=lambda: print("how are you doing?"),
    )

    empty_operator_1 = EmptyOperator(task_id="empty_operator_1")

    empty_operator_2 = EmptyOperator(task_id="empty_operator_2")


    hello >> world >> [empty_operator_1, empty_operator_2] >> how_are_you_doing_operator
