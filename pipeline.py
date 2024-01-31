#!/usr/bin/env python3.8

import subprocess
import os


# Function to run the Python notebooks
def run_python_notebook(notebook_path):
    subprocess.run(['jupyter', 'nbconvert', '--to', 'script', notebook_path])
    subprocess.run(['python', notebook_path.replace('.ipynb', '.py')])

# Function to run SQL scripts
def run_sql_scripts(sql_folder, script_order, db_host, db_port, db_name, db_user, db_password):
    for script_name in script_order:
        script_path = os.path.join(sql_folder, script_name)
        subprocess.run([
            'psql',
            '-h', db_host,
            '-p', str(db_port),
            '-d', db_name,
            '-U', db_user,
            '-W',  # Prompt for password
            '-f', script_path
        ], input=db_password.encode('utf-8'))


if __name__ == "__main__":
    # Define paths and configurations
    python_notebook_path_1 = "C:\\Users\\USER\\Documents\\Data2Bots Assessment\\ingest_data_test.ipynb"
    sql_scripts_folder = "C:\\Users\\USER\\Documents\\Data2Bots Assessment\\sql_transformations"
    #python_notebook_path_2 = '/path/to/notebook2.ipynb'

    # Define the order in which SQL scripts should be executed
    script_order = ['create_agg_public_holiday.sql', 'create_agg_shipments.sql', 'create_best_peeforming_product.sql',
                    'insert_into_agg_public_holiday.sql', 'insert_into_agg_shipments.sql', 'insert_into_best_performing_product.sql']

    # Database connection details
    PG_USERNAME = os.getenv("PG_USERNAME")
    PG_PASS = os.getenv("PG_PASS")
    PG_HOST = os.getenv("PG_HOST")
    PG_DB = os.getenv("PG_DB")


    # Run the pipeline
    run_python_notebook(python_notebook_path_1)
    run_sql_scripts(sql_scripts_folder, script_order, db_host=PG_HOST, db_port=5433, db_name=PG_DB, db_user=PG_USERNAME, db_password=PG_PASS)
    #run_python_notebook(python_notebook_path_2)