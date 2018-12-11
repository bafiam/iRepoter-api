
import unittest

from app.api.v1.models import UserModel
from database.database_config import DatabaseTables
from database import db_conn
from app import create_app


from run import app


class BaseTestCase(unittest.TestCase):
    def create_app_base(self):
        app.testing = True
        self.app = create_app()
        return self.app

    def setUp(self):
        """ set the wide set variable"""
        self.app = self.create_app_base()
        self.client = self.app.test_client()

    def tearDown(self):
        q=DatabaseTables().drop_table_query()
        conn= db_conn()
        cur=conn.cursor()
        for sql in q:
            cur.execute(sql)
            conn.commit()



if __name__ == '__main__':
    unittest.main()
