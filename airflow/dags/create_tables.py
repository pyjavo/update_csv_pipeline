from datetime import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.utils.dates import days_ago


default_args = {
    'depends_on_past': False,
    'retries': 1,
    'start_date': days_ago(1),
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'create_tables',
    default_args=default_args,
    description='An Airflow DAG to create tables',
    schedule_interval='@once',
)

create_table_raw_data = MySqlOperator(
    task_id='create_table_raw_data',
    mysql_conn_id='mysql_conn_id',
    sql='raw_data_schema.sql',
    dag=dag,
)

create_table_transformed_data = MySqlOperator(
    task_id='create_table_transformed_data',
    mysql_conn_id='mysql_conn_id',
    sql='transformed_data_schema.sql',
    dag=dag,
)


create_table_raw_data >> create_table_transformed_data
