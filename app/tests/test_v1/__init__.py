import json
import unittest
import pytest

from app import create_app
from app.api.v1 import api

from app.api.v1.models import RedFlagRecordsModel as db

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
        pass

if __name__ == '__main__':
    unittest.main()
