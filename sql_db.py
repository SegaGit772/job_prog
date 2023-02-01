import sqlite3
"""Создание базы данных и таблицы"""
try:

    sqlite_connection = sqlite3.connect('dens_db.db')
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS densities (
                                width1 INTEGER,
                                width2 INTEGER,
                                thickness REAL,
                                density REAL,
                                kef INTEGER);'''
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    cursor.close()


except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
