import pandas as pd
import os


def get_csv_data(csv_path):
    return pd.read_csv(csv_path)


def extract_data():
    for storage_file_name in os.listdir(os.getenv('STORAGE_FLAT_DATA_PATH')):
        all_file_names = get_all_file_names(os.getenv('STORAGE_FLAT_DATA_PATH'))
        flat_files_index += 1
        storage_flat_data_path = os.path.join(os.getenv('STORAGE_FLAT_DATA_PATH'), storage_file_name)
        if os.path.isfile(storage_flat_data_path):
            all_storage_extracted_data.append(get_csv_data(storage_flat_data_path))


def get_all_file_names(path):
    file_names = {}
    for index, storage_file_name in enumerate(os.listdir(path)):
        file_names[index] = storage_file_name

    return file_names
