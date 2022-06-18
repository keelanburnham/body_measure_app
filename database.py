import sqlite3

database_name = ''


def connect_to_db(database=None):
    if database is None:
        database_name = ':memory:'
        print('Database created in memory.')
    else:
        database_name = f'{database}.db'
    try:
        connection = sqlite3.connect(database_name, isolation_level=None)
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='body_measurements';")
        if not cursor.fetchone()[0] == 1:
            cursor.execute(
                'CREATE TABLE body_measurements (id INTEGER PRIMARY KEY AUTOINCREMENT, weight NUMERIC NOT NULL);')
    except Exception as error:
        print('Unable to connect to database.\n'
              f'Error --> {error}')
        exit()
    return connection
