# Data Engineering Automation Project

This project automates the end-to-end process of ingesting, transforming, and exporting data using Python, PostgreSQL, and AWS S3.

## Project Structure

The project consists of the following components:

1. `ingest_data.ipynb`: Python notebook for ingesting data from an S3 bucket and loading it into a PostgreSQL database.
2. `export_data.ipynb`: Python notebook for exporting aggregated tables to CSV and dumping them into another S3 bucket.
3. SQL Scripts:
   - `create_agg_public_holiday.sql`: Creates the aggregated holiday table.
   - `create_best_performing_product.sql`: Creates the best-performing product table.
   - `create_agg_shipments.sql`: Creates the aggregated shipments table.
   - `insert_into_agg_holiday.sql`: Inserts data into the aggregated holiday table.
   - `insert_into_best_performing_product.sql`: Inserts data into the best-performing product table.
   - `insert_into_agg_shipments.sql`: Inserts data into the aggregated shipments table.

4. `automation_script.py`: Python script to automate the entire process.

## Usage

### 1. Install all dependencies
Run the command below to ensure there are not dependency confusions.

`pip install -r requirements.txt`

### 2. Running the Automation Script

The entire workflow in this project is triggered by executing the command below:

```bash
python pipeline.py
```

This script consolidates the steps below:

### 3. Ingesting Data
Converts `ingest_data.ipynb` to a Python script.
Runs the script to download the raw files from the specified s3 bucket and load it into PostgreSQL.

### 4. SQL Transformations
Executes SQL scripts in the following order:
- `create_agg_public_holiday.sql`
- `create_agg_shipments.sql`
- `create_best_performing_product.sql`
- `insert_into_agg_holiday.sql`
- `insert_into_agg_shipments.sql`
- `insert_into_best_performing_product.sql`

### 5. Exporting Data
Runs `export_data.ipynb` to export aggregated tables to CSV.
Uploads CSV files to specified S3 bucket destination.

### Prerequisites
Ensure you have the following prerequisites installed:

Python 3.x
Jupyter Notebook
PostgreSQL
AWS CLI (configured with necessary credentials)

### Configuration
Before running the automation script, modify the following configurations:

Database connection details in `ingest_data.ipynb` and `export_data.ipynb.`
S3 bucket details in the Python script and notebooks.
