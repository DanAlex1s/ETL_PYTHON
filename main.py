import os

from app.ETL.extract import get_csv_data

STORAGE_DATA_DIR = 'storage'
STORAGE_FLAT_DATA_DIR = 'flat_data'
STORAGE_TRANSFORMER_DATA_DIR = 'transformer_data'
STORAGE_FLAT_DATA_PATH = os.path.join(STORAGE_DATA_DIR, STORAGE_FLAT_DATA_DIR)
STORAGE_TRANSFORMER_DATA_PATH = os.path.join(STORAGE_DATA_DIR, STORAGE_TRANSFORMER_DATA_DIR)

all_storage_extracted_data = []
for storage_file in os.listdir(STORAGE_FLAT_DATA_PATH):
    storage_flat_data_path = os.path.join(STORAGE_FLAT_DATA_PATH, storage_file)
    if os.path.isfile(storage_flat_data_path):
        all_storage_extracted_data.append(get_csv_data(storage_flat_data_path))

sql_sentences = []
for storage_extracted_data in all_storage_extracted_data:
    for index, row in storage_extracted_data.iterrows():
        values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in row])
        sentence = f"INSERT INTO tabla_datos (ID, Nombre, Edad) VALUES ({values});"
        sql_sentences.append(sentence)

if sql_sentences:

print(sql_sentences)
exit()
#print(all_storage_extracted_data[1]['Nombre'])
