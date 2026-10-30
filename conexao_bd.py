import psycopg2


def conectar():
    return psycopg2.connect(
        host='localhost',
        database='Biblioteca',
        user='postgres',
        password='12345',
        port='5432'
    )

