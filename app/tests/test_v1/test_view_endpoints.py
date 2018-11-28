import json
import unittest
from . import BaseTestCase


class APIEndpointsTestCase(BaseTestCase):
    """Test for API endpoints.
    create the base post for data creation  """

    def create_record(self):
        new_accident_record = {
            'id':'1',
            'type': 'red flag case',
            'location': 'Nyeri',
            'status': 'Not approved',
            'comment': 'police at the road blocks collecting bribes on the highway'
        }
        response = self.client.post('/api/v1/red_flag_records',
                                    data=json.dumps(new_accident_record),
                                    headers={"content-type": "application/json"})
        return response
    # it will test if the record was actually created
    def test_create_read_flag_record(self):
        record = self.create_record()
        self.assertIn('Accident record created', str(record.data))
        self.assertEqual(record.status_code, 201)
    # it will test if the record was actually created
    def test_fetch_all_accidents(self):
        """Test that endpoint fetches all accidents"""
        self.create_record()
        # now fetch the accident records
        response = self.client.get("/api/v1/red_flag_records")
        self.assertIn('Your accident records are', str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_fetch_single_accident(self):
        self.create_record()
        # now fetch a single accident records
        response = self.client.get("/api/v1/red_flag_record/1")
        self.assertIn('your accident is', str(response.data))
        self.assertEqual(response.status_code, 200)

    # def test_delete_single_accident(self):
    #     self.create_record()
    #     response = self.client.delete("/api/v1/red_flag_record/1")
    #     self.assertIn('Red flag record deleted', str(response.data))
    #     self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
