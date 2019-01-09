import bcrypt
import psycopg2
from .database_config import DatabaseTables
from instance.config import app_config
import os

env = os.environ['FLASK_ENV']
URL = app_config[env].DATABASE_URL
username = os.getenv('ADMIN_USERNAME')
password = (bcrypt.hashpw(os.getenv('ADMIN_PASSWORD').encode('utf-8'), bcrypt.gensalt())).decode('utf-8')
email = os.getenv('ADMIN_EMAIL')



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
    # admin

    # take a table from the tables def and depending on the one execute it and close the connection when do
    for sql in queries:
        cur.execute(sql)
        connection.commit()
    cur.close()


def create_admin():
    admin = {
        "username": username,
        "password": password,
        "isAdmin": True,
        "email": email,

    }
    query = """INSERT INTO users(username,password,is_admin, email ) VALUES('{0}','{1}','{2}','{3}');""".format(
        admin['username'], admin['password'], admin['isAdmin'], admin['email'])
    # connect the db
    connect = db_conn()
    # create a  cursor that will be used though out the program
    cur = connect.cursor()
    try:
        cur.execute(query)
        connect.commit()
        print("admin created")
    except:
        print("That admin already exists")


