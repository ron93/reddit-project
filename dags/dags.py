from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.models import DagBag
# from airflow.models.serialized_dag import SerializedDagModel
#from utils import insert_question, write_questions_to_s3, render_template

#from stream import  save_in_db,del_from_db
#from src.reddit.redd import SubredditScraper
# from src.scripts.mod import start_task,save_topics,del_from_db


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

    # # Check DB for missing serialized DAGs, and add them if missing
    # for dag_id in dag_bag.dag_ids:  
    #     if not SerializedDagModel.get(dag_id):
    #         dag = dag_bag.get_dag(dag_id)
    #         SerializedDagModel.write_dag(dag)
            
    Task_I = PythonOperator(
        task_id="save_in_db",
        python_callable= save_topics
    )

    Task_II = PythonOperator(
        task_id="del_from_db", python_callable=del_from_db
    )

Task_I >> Task_II


def start_task():
    return 'Task'

def save_topics():
    #save data to Kafka topics: Posts and Comments
    return 'Topics'

def del_from_db():
    return 'Save'

