from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy import DummyOperator

#from utils import insert_question, write_questions_to_s3, render_template

from stream import  save_in_db,del_from_db
#from src.reddit.redd import SubredditScraper

default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2019, 10, 9),
    "email": ["my_email@mail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "catchup":False,
    "retry_delay": timedelta(minutes=1),
    "schedule_interval": "@daily",
}



with DAG("reddit_data", default_args=default_args) as dag:

    Task_I = PythonOperator(
        task_id="save_in_db",
        python_callable=save_in_db
    )

    Task_II = PythonOperator(
        task_id="del_from_db", python_callable=del_from_db
    )

Task_I >> Task_II