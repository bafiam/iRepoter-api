import psycopg2
import os
from .database_config import DatabaseTables


def db_conn():
    """Create Database Connection"""
    db_url="'ireporter', user='bafiam_admin', password='bafiam', host='localhost', port='5432'"

    connection = psycopg2.connect(db_url)
    return connection


def create_tables():
    """Creates the Tables"""

    connection = db_conn()
    cursor = connection.cursor()

    database = DatabaseTables()
    queries = database.table_query()

    for sql in queries:
        cursor.execute(sql)
        connection.commit()
    cursor.close()