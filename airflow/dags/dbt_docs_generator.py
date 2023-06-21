from datetime import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


default_args = {
    'depends_on_past': False,
    'retries': 1,
    'start_date': days_ago(1),
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'dbt_docs_generator_dag',
    default_args=default_args,
    description='An Airflow DAG to invoke simple dbt commands',
    schedule_interval='@once',
)


generate_docs = BashOperator(
    task_id='generate_docs',
    bash_command='cd ../../dbt && dbt docs generate',
    dag=dag
)

generate_docs
