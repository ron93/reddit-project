from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

#from utils import insert_question, write_questions_to_s3, render_template

from src.reddit.stream import  save_in_db
from src.reddit.redd import SubredditScraper

default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2019, 10, 9),
    "email": ["my_email@mail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=1),
    "schedule_interval": "@daily",
}

def hello():
    return 'Hello airflow!!'
def bye():
    return "Bye"

with DAG("reddit_data", default_args=default_args) as dag:


    Task_II = PythonOperator(
        task_id="listener", python_callable= SubredditScraper
    )


    Task_I= PythonOperator(
        task_id="hello", python_callable=hello
        )

Task_II >> Task_I