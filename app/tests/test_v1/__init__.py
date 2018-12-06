
import unittest

from app.api.v1.models import user_model
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
        user_model.clear()

if __name__ == '__main__':
    unittest.main()
