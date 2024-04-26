import os
import sys

from app.ETL.extract import get_csv_data
from dotenv import load_dotenv


if len(sys.argv) != 2:
    print("Usage: python script.py <sql_file_name>")
    sys.exit(1)

SQL_FILE_NAME = sys.argv[1] + ".sql"

if not isinstance(SQL_FILE_NAME, str):
    sys.exit(1)

load_dotenv()
STORAGE_SQL_FILE_PATH = os.path.join(os.getenv('STORAGE_TRANSFORMED_DATA_PATH'), SQL_FILE_NAME)

all_storage_extracted_data = []
all_file_names = {}
flat_files_index = 0
for storage_file_name in os.listdir(os.getenv('STORAGE_FLAT_DATA_PATH')):
    all_file_names[flat_files_index] = storage_file_name
    flat_files_index += 1
    storage_flat_data_path = os.path.join(os.getenv('STORAGE_FLAT_DATA_PATH'), storage_file_name)
    if os.path.isfile(storage_flat_data_path):
        all_storage_extracted_data.append(get_csv_data(storage_flat_data_path))

sql_sentences = []
table_index = 0
for storage_extracted_data in all_storage_extracted_data:
    for index, row in storage_extracted_data.iterrows():
        columns = ', '.join(all_storage_extracted_data[table_index].columns.values)
        values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in row])
        table_name = all_file_names[table_index].replace('.csv', '')
        sentence = f"INSERT INTO {table_name} ( {columns} ) VALUES ({values});\n"
        sql_sentences.append(sentence)
    table_index += 1

with open(STORAGE_SQL_FILE_PATH, 'w') as file:
    sql_file_data = "".join(sql_sentences)
    file.write(sql_file_data)
