import pandas as pd
import os


def get_csv_data(csv_path):
    return pd.read_csv(csv_path)


def extract_csv_data(path):
    all_storage_extracted_data = []
    for storage_file_name in os.listdir(path):
        storage_flat_data_path = os.path.join(path, storage_file_name)
        if os.path.isfile(storage_flat_data_path):
            all_storage_extracted_data.append(get_csv_data(storage_flat_data_path))

    return all_storage_extracted_data


def get_all_file_names(path):
    file_names = {}
    for index, storage_file_name in enumerate(os.listdir(path)):
        file_names[index] = storage_file_name

    return file_names
