from getpass import getpass
import mysql.connector
from mysql.connector import connect, Error
from config import host, user, password, db_name
try:
    with connect(
        host=host,
        user=user,
        port=3306,
        password=password,
        database=db_name,
    ) as connection:

except Error as e:
    print(e)

