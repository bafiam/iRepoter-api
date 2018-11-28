import json
import unittest
import pytest

from app import create_app
from app.api.v1 import api

from app.api.v1.views import RedFlagRecord, RedFlagRecords, RedFlagRecordsModel
from run import app


class BaseTestCase(unittest.TestCase):
    def create_app(self):
        app.testing = True
        self.app = create_app()
        return self.app

    def setUp(self):
        """ set the wide set variable"""
        self.app = self.create_app()
        self.client = self.app.test_client()
        self.accident_data = {'type': 'red flag case', 'location': 'nairobi', 'status': 'approved',
                              'comment': 'police collecting bribes on the highway'}

        # set api endpoints
        api.add_resource(RedFlagRecords, '/api/v1/red_flag_records')
        api.add_resource(RedFlagRecord, '/api/v1/red_flag_record/<int:id>')

        # create accident for first user
        self.client.post('/api/v1/red_flag_records',
                         data=self.accident_data)


if __name__ == '__main__':
    unittest.main()
