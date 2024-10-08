from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.http.sensors.http import HttpSensor

with DAG(
    dag_id='capstone_project',
    start_date=datetime(2024, 10, 8),
    schedule='@daily',
):

    poll_upcoming_launches_sensor = HttpSensor(
        task_id='poll_spacedevs_api_sensor',
        http_conn_id='thespacedevs_dev',
        endpoint='/launch/upcoming/',
        mode='reschedule',
    )

    is_launched_scheduled_for_today_operator = EmptyOperator(
        task_id='is_launch_scheduled_for_today_operator',
    )

    fetch_recent_launches_and_persist_in_cloud_storage_bucket_operator = EmptyOperator(
        task_id='fetch_recent_launches_and_persist_in_cloud_storage_bucket_operator',
    )

    load_from_cloud_storage_bucket_to_bigquery_operator = EmptyOperator(
        task_id='load_from_cloud_storage_bucket_to_bigquery_operator',
    )

    load_from_cloud_storage_bucket_to_postgres_operator = EmptyOperator(
        task_id='load_from_cloud_storage_bucket_to_postgres_operator',
    )

    poll_upcoming_launches_sensor >> is_launched_scheduled_for_today_operator \
    >> fetch_recent_launches_and_persist_in_cloud_storage_bucket_operator \
    >> [load_from_cloud_storage_bucket_to_bigquery_operator, load_from_cloud_storage_bucket_to_postgres_operator]
