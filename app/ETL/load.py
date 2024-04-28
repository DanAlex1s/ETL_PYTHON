from app.database.connection import conn


def create_sql_file(path, sql_sentences_list):
    with open(path, 'w') as file:
        sql_file_data = "".join(sql_sentences_list)
        file.write(sql_file_data)


def load_data_to_database(sql_file_path):
    cursor = conn.cursor()
    try:
        with open(sql_file_path, "r") as file:
            sql_queries = file.read().split(";")
            for query in sql_queries:
                if query.strip():
                    cursor.execute(query)
        conn.commit()
        print("Data loaded successfully")
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
        print("Connection closed")
