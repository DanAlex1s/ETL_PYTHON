import os

from .extract import get_all_file_names


def transform_to_sql_list(data):
    sql_sentences = []
    for table_index, storage_extracted_data in enumerate(data):
        for index, row in storage_extracted_data.iterrows():
            columns = ', '.join(data[table_index].columns.values)
            values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in row])
            table_name = get_all_file_names(os.getenv('STORAGE_FLAT_DATA_PATH'))[table_index].replace('.csv', '')
            sentence = f"INSERT INTO {table_name} ( {columns} ) VALUES ({values});\n"
            sql_sentences.append(sentence)

    return sql_sentences

