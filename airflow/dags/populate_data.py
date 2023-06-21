from datetime import timedelta
from datetime import datetime as dt

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.mysql.operators.mysql import MySqlOperator


default_args = {
    'depends_on_past': False,
    'retries': 1,
    'start_date': days_ago(1),
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'populate_data',
    default_args=default_args,
    description='An Airflow DAG to populate data',
    schedule_interval="@once",
)

insert_existing_csv_data = MySqlOperator(
    task_id='insert_existing_csv_data',
    mysql_conn_id="mysql_conn_id",
    sql='./insert_existing_csv_data.sql',
    dag=dag
)

insert_existing_csv_data
