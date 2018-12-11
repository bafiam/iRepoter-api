import psycopg2
from .database_config import DatabaseTables
from instance.config import app_config
import os
env= os.environ['FLASK_ENV']
URL = app_config[env].url
def db_conn():
    """Create Database Connection"""
    connection = psycopg2.connect(URL)
    print("Opened database successfully")
    return connection


def create_tables():
    """Creates the Tables"""

    # connect the db
    connection = db_conn()
    # create a  cursor that will be used though out the program
    cur = connection.cursor()
    # create the database tables after the db has been created
    database = DatabaseTables()
    queries = database.table_query()
    # take a table from the tables def and depending on the one execute it and close the connection when do
    for sql in queries:
        cur.execute(sql)
        connection.commit()
    cur.close()
