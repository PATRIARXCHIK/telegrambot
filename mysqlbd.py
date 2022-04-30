import mysql.connector
from mysql.connector import Error
from config import db_config

def create_connection_mysql_db(db_host, user_name, user_password, db_name = None):
    connection_db = None
    try:
        connection_db = mysql.connector.connect(
            host = db_host,
            user = user_name,
            password = user_password,
            db_name = db_name,
        )
        print("Подключение к MySQL успешно выполнено")
    except Error as db_connection_error:
        print("Возникла Ошибка: ", db_connection_error)
    return connection_db

conn = create_connection_mysql_db(db_config["mysql"]["host"],
                                  db_config["mysql"]["user"],
                                  db_config["mysql"]["pass"])
cursor = conn.cursor()
create_db_sql_query = 'Create DATABASE {}'.format('Test')
cursor.execute(create_db_sql_query)
cursor.close()
conn.close()

conn = create_connection_mysql_db(db_config["mysql"]["host"],
                                  db_config["mysql"]["user"],
                                  db_config["mysql"]["pass"],
                                  "Test")
try:
    #Создание таблицы
