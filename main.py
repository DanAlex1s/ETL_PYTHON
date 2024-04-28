import os
import sys

from app.ETL.extract import extract_csv_data
from app.ETL.transform import transform_to_sql_list
from app.ETL.load import create_sql_file, load_data_to_database
from dotenv import load_dotenv


if len(sys.argv) != 2:
    print("Usage: python script.py <sql_file_name>")
    sys.exit(1)

SQL_FILE_NAME = sys.argv[1] + ".sql"

if not isinstance(SQL_FILE_NAME, str):
    sys.exit(1)

load_dotenv()

STORAGE_SQL_FILE_PATH = os.path.join(os.getenv('STORAGE_TRANSFORMED_DATA_PATH'), SQL_FILE_NAME)

all_storage_extracted_data = extract_csv_data(os.getenv('STORAGE_FLAT_DATA_PATH'))
sql_sentences_list = transform_to_sql_list(all_storage_extracted_data)
create_sql_file(STORAGE_SQL_FILE_PATH, sql_sentences_list)
load_data_to_database(STORAGE_SQL_FILE_PATH)