from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator


from logic.reddit import redd
from logic.telegram import telbot

default_args = {
    "owner": "ron",
    "depends_on_past": False,
    "start_date": datetime(2019, 10, 9),
    "email": ["my_email@mail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=1),
    "schedule_interval": "@daily",
}

with DAG("stack_overflow_questions", default_args=default_args) as dag:

    Task_I = PythonOperator(
        task_id="get_subs",
        python_callable=
      
    )

    Task_II = PythonOperator(
        task_id="get_sub_data", python_callable=get_data
    )

    Task_III = PythonOperator(
        task_id="analyse", python_callable=analyse
    )

    Task_IV = PythonOperator(
        task_id="post",
        python_callable=telegram_callback,
        provide_context=True,
    )

 

Task_I >> Task_II >> Task_III >> Task_IV

