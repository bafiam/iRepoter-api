import json
import unittest


from . import BaseTestCase


class APIEndpointsTestCaseSuccess(BaseTestCase):
    """Test for API endpoints.
    create the base post for data creation  """

    def set_config(self):
        user = {
            "email":"stevebafiam@gmail.com",
            "username": "bafiam",
            "password": "12@34A6e89"
        }
        self.client.post('/api/v1/auth/register',
                         data=json.dumps(user),
                         headers={"content-type": "application/json"})
        user_login= {
            "username": "bafiam",
            "password": "12@34A6e89"
        }
        response = self.client.post('/api/v1/auth/login',
                                    data=json.dumps(user_login),
                                    headers={"content-type": "application/json"})

        self.auth_token = response.get_json()['access_token']

    def create_record(self):
        self.set_config()
        new_accident_record = {
            "type": "intervention",
            "location": "Nyeri",
            "comment": "police at the road blocks collecting bribes on the highway"
        }
        response = self.client.post('/api/v1/incidents',
                                    data=json.dumps(new_accident_record),
                                    headers={"content-type": "application/json",
                                             'authorization': 'Bearer ' + self.auth_token})
        return response

    """ it will test if the record was actually created. """

    def test_create_read_flag_record(self):
        self.set_config()
        record = self.create_record()
        self.assertEqual(record.status_code, 201)

    """ it will test if the record was actually created. """

    def test_fetch_all_accidents(self):
        self.set_config()
        """Test that endpoint fetches all accidents"""
        self.create_record()
        """now fetch the accident records."""
        response = self.client.get("/api/v1/incidents", headers={'authorization': 'Bearer ' + self.auth_token})
        self.assertEqual(response.status_code, 200)

    def test_fetch_single_accident(self):
        self.set_config()
        self.create_record()
        """now fetch a single accident records"""
        response = self.client.get("/api/v1/incidents/1", headers={'authorization': 'Bearer ' + self.auth_token})
        self.assertEqual(response.status_code, 200)

    def test_patch_accident_record(self):
        self.set_config()
        self.create_record()
        patch_accident_record = {
            "location": "nakuru",
            "comment": "police beating citizens"

        }
        response = self.client.patch("/api/v1/incidences/update/1",
                                     data=json.dumps(patch_accident_record),
                                     headers={"content-type": "application/json",
                                              'authorization': 'Bearer ' + self.auth_token})
        self.assertEqual(response.status_code, 201)


class TestSensitiveEndPointsSuccess(BaseTestCase):
    def set_config(self):
        user = {
            "email": "steyvebafiam@gmail.com",
            "username": "bafiam",
            "password": "12@34A6e89"
        }
        self.client.post('/api/v1/auth/register',
                         data=json.dumps(user),
                         headers={"content-type": "application/json"})
        user_login= {
            "username": "bafiam",
            "password": "12@34A6e89"
        }
        response = self.client.post('/api/v1/auth/login',
                                    data=json.dumps(user_login),
                                    headers={"content-type": "application/json"})

        self.auth_token = response.get_json()['access_token']

    def create_sensitive_record(self):
        self.set_config()
        accident_record_for_delete_only = {
            'type': 'intervention',
            "location": "nakuru",
            "comment": "police beating citizens"
        }
        response = self.client.post('/api/v1/incidents',
                                    data=json.dumps(accident_record_for_delete_only),
                                    headers={"content-type": "application/json",
                                             'authorization': 'Bearer ' + self.auth_token})
        return response

    def test_sensitive_record_creation(self):
        self.set_config()
        record = self.create_sensitive_record()
        self.assertEqual(record.status_code, 201)

    def test_delete_single_accident(self):
        self.set_config()
        self.create_sensitive_record()
        response = self.client.delete('/api/v1/incidents/1', headers={"content-type": "application/json",
                                                                       'authorization': 'Bearer ' + self.auth_token})

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
