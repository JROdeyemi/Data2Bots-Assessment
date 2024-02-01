from airflow import DAG
from airflow import operators 
from airflow.operators import python_operator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os 

# Set your Airflow DAG parameters
default_args = {
    'owner': 'your_owner',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define your DAG
dag = DAG(
    's3_postgres_dag',
    default_args=default_args,
    description='Description of your DAG',
    schedule_interval='@daily',  # Set your desired schedule interval
    catchup=False,
)

# Define the function to run your Python script
def run_pipeline():
    # Provide the path to your Python script
    script_path = "C:\\Users\\USER\\Documents\\Data2Bots Assessment\\pipeline.py"

    # Execute the Python script
    os.system(f"python {script_path}")

# Create a task to run your Python script
run_pipeline_task = PythonOperator(
    task_id='run_pipeline_task',
    python_callable=run_pipeline,
    dag=dag,
)

# Set task dependencies as needed
# For example, you may want to run the script daily after some other tasks
# other_task >> run_pipeline_task

if __name__ == "__main__":
    dag.cli()
