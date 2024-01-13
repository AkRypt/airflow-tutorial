from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'akrypt',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id='dag_with_taskflow_v2',
    default_args=default_args,
    start_date=datetime(2024, 1, 11),
    schedule_interval='@daily')
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            "firstname": "Jerry",
            "lastname": "Bery"
        }
    
    @task()
    def get_age():
        return 20
    
    @task()
    def greet(firstname, lastname, age):
        print(f"Hello World! My name is {firstname} {lastname} "
              f"and I am {age} years old!")

    name = get_name()
    age = get_age()
    greet(
        firstname=name['firstname'], 
        lastname=name['lastname'],
        age=age)

greet_dag = hello_world_etl()