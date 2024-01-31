
import subprocess
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv("/workspaces/Data2Bots-Assessment/.env")

# Function to run the Python notebooks
def run_python_notebook(notebook_path):
    subprocess.run(['jupyter', 'nbconvert', '--to', 'script', notebook_path])
    subprocess.run(['python', notebook_path.replace('.ipynb', '.py')])


# Function to run SQL scripts
def run_sql_scripts(connection, sql_folder, script_order):
    for script_name in script_order:
        script_path = os.path.join(sql_folder, script_name)
        with connection.cursor() as cursor:
            with open(script_path, 'r') as script_file:
                cursor.execute(script_file.read())
                print(f'Successfully executed {script_name}')
        connection.commit()

# Function to create a PostgreSQL connection
def create_postgres_connection(host, port, database, user, password):
    return psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )


if __name__ == "__main__":
    # Define paths and configurations
    ingest_data = "/workspaces/Data2Bots-Assessment/Ingest_data.ipynb"
    sql_scripts_folder = "/workspaces/Data2Bots-Assessment/sql_transformations"
    export_data = "/workspaces/Data2Bots-Assessment/export_data.ipynb"

    # Define the order in which SQL scripts should be executed
    script_order = ['create_agg_public_holiday.sql', 'create_agg_shipments.sql', 'create_best_performing_product.sql',
                    'insert_into_agg_public_holiday.sql', 'insert_into_agg_shipments.sql', 'insert_into_best_performing_product.sql']

     


    # Database connection details
    PG_USERNAME = os.getenv("PG_USERNAME")
    PG_PASS = os.getenv("PG_PASS")
    PG_HOST = os.getenv("PG_HOST")
    PG_DB = os.getenv("PG_DB")

    # Create PostgreSQL connection
    connection = create_postgres_connection(host=PG_HOST, port=5432, database=PG_DB, user=PG_USERNAME, password=PG_PASS)

    # Run the pipeline
    run_python_notebook(notebook_path=ingest_data)
    run_sql_scripts(connection, sql_scripts_folder, script_order)
    run_python_notebook(notebook_path=export_data)