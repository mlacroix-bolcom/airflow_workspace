from datetime import datetime

from airflow.models import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id="01_launch",
        start_date=datetime(year=2024, month=10, day=5),
        end_date=datetime(year=2019, month=1, day=5),
        schedule="@daily",
):
    procure_rocket_material_operator = EmptyOperator(
        task_id="procure_rocket_material",
    )

    procure_fuel_operator = EmptyOperator(
        task_id="procure_fuel",
    )

    build_stage_1_operator = EmptyOperator(
        task_id="build_stage_1",
    )

    build_stage_2_operator = EmptyOperator(
        task_id="build_stage_2",
    )

    build_stage_3_operator = EmptyOperator(
        task_id="build_stage_3",
    )

    launch_operator = EmptyOperator(
        task_id="launch",
    )

    procure_rocket_material_operator >> [
        build_stage_1_operator,
        build_stage_2_operator,
        procure_fuel_operator >> build_stage_3_operator,
    ] >> launch_operator
