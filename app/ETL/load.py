

def create_sql_file(path, sql_sentences_list):
    with open(path, 'w') as file:
        sql_file_data = "".join(sql_sentences_list)
        file.write(sql_file_data)