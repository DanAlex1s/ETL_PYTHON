import os

from .extract import get_all_file_names


def transform_to_sql_list(data):
    sql_sentences = []
    sql_sentences.extend(create_tables_sql(data))
    sql_sentences.extend(create_inserts_sql(data))

    return sql_sentences


def create_tables_sql(data):
    sql_sentences = []
    for table_index, storage_extracted_data in enumerate(data):
        columns = ', '.join([f"{column} VARCHAR(255)" for column in data[table_index].columns.values])
        table_name = get_all_file_names(os.getenv('STORAGE_FLAT_DATA_PATH'))[table_index].replace('.csv', '')
        sentence = (f"DROP TABLE IF EXISTS {table_name};\n"
                    f"CREATE TABLE {table_name} ( {columns} );\n")
        sql_sentences.append(sentence)

    return sql_sentences


def create_inserts_sql(data):
    sql_sentences = []
    for table_index, storage_extracted_data in enumerate(data):
        for index, row in storage_extracted_data.iterrows():
            columns = ', '.join(data[table_index].columns.values)
            values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in row])
            table_name = get_all_file_names(os.getenv('STORAGE_FLAT_DATA_PATH'))[table_index].replace('.csv', '')
            sentence = f"INSERT INTO {table_name} ( {columns} ) VALUES ({values});\n"
            sql_sentences.append(sentence)

    return sql_sentences
