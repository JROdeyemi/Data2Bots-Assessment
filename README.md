# Data Engineering Automation Project

This project automates the end-to-end process of ingesting, transforming, and exporting data using Python, PostgreSQL, and AWS S3.

## Project Structure

The project consists of the following components:

1. `ingest_data.ipynb`: Python notebook for ingesting data from an S3 bucket and loading it into a PostgreSQL database.
2. `export_data.ipynb`: Python notebook for exporting aggregated tables to CSV and dumping them into another S3 bucket.
3. SQL Scripts:
   - `create_agg_holiday.sql`: Creates the aggregated holiday table.
   - `create_best_performing_product.sql`: Creates the best-performing product table.
   - `create_agg_shipments.sql`: Creates the aggregated shipments table.
   - `insert_into_agg_holiday.sql`: Inserts data into the aggregated holiday table.
   - `insert_into_best_performing_product.sql`: Inserts data into the best-performing product table.
   - `insert_into_agg_shipments.sql`: Inserts data into the aggregated shipments table.

4. `automation_script.py`: Python script to automate the entire process.

## Usage

### 1. Running the Automation Script

To automate the entire data pipeline, execute the following steps:

```bash
python automation_script.py

