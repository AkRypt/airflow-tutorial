from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'akrypt',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='first_dag_v5',
    default_args=default_args,
    description='this is our first dag',
    start_date=datetime(2024, 1, 10, 4),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, first task'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo I am second task haha'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo I am third running same as task 2'
    )

    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    task1 >> [task2, task3]