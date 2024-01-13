from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'akrypt',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_cron_expression_v1',
    default_args=default_args,
    start_date=datetime(2024, 1, 4),
    schedule_interval='0 3 * * Tue ', #crontab guru
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo this is simple'
    )

    task1