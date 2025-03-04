import mysql.connector
from mysql.connector import Error

try:
    dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
    )

    cursorObject = dataBase.cursor()
    cursorObject.execute('CREATE DATABASE dcrm')
    print("Baza danych została pomyślnie utworzona")

except Error as e:
    print(f"Błąd: {e}")

