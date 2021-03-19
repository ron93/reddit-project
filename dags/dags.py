from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.models import DagBag
from airflow.models.serialized_dag import SerializedDagModel
#from utils import insert_question, write_questions_to_s3, render_template

#from stream import  save_in_db,del_from_db
#from src.reddit.redd import SubredditScraper

def start_task():
    pass

def save_topics():
    #save data to Kafka topics: Posts and Comments
    pass

def del_from_db():
    pass


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
    dag_bag = DagBag()

    # Check DB for missing serialized DAGs, and add them if missing
    for dag_id in dag_bag.dag_ids:  
        if not SerializedDagModel.get(dag_id):
            dag = dag_bag.get_dag(dag_id)
            SerializedDagModel.write_dag(dag)
            
    Task_I = PythonOperator(
        task_id="save_in_db",
        python_callable=save_in_db
    )

    Task_II = PythonOperator(
        task_id="del_from_db", python_callable=del_from_db
    )

Task_I >> Task_II