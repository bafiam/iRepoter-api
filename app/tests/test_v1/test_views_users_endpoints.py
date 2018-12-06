import json
import unittest
from . import BaseTestCase


class TestUserAccountAPI(BaseTestCase):
    def create_user_account_data(self):
        user = {
            "email":"stevebafiam@gmail.com",
            "username": "bafiam",
            "password": "1234567890"
        }
        response = self.client.post('/api/v1/register',
                                    data=json.dumps(user),
                                    headers={"content-type": "application/json"})
        return response

    def test_user_register(self):
        # test the post success
        record = self.create_user_account_data()
        self.assertEqual(201, record.status_code)

    def test_user_login(self):
        # test user login
        self.create_user_account_data()
        new_user = {
            "username":"bafiam",
            "password":"1234567890"
        }
        response = self.client.post("/api/v1/login", data=json.dumps(new_user),
                                    headers={"content-type": "application/json"})
        self.assertEqual(200, response.status_code )
        # # test token generation
        # self.assertIn("Authorization", response.data.decode("ascii"))
        # self.assertEqual(response.data["Authorization"], self.token)

    def test_user_login_wrong_password(self):
        self.create_user_account_data()
        new_user_with_wrong_pass = {
            "username":"bafiam",
            "password":"1456790",
        }
        response = self.client.post("/api/v1/login", data=json.dumps(new_user_with_wrong_pass),
                                    headers={"content-type": "application/json"})
        self.assertEqual(400, response.status_code)

    def test_case_user_provides_empty_information_login(self):
        self.create_user_account_data()
        empty_user_data = {
            "username":'',
            "password":''
        }
        response = self.client.post('/api/v1/login', data=json.dumps(empty_user_data),
                                    headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 400)

    def test_user_provide_dublicate_username(self):
        same_user = {
            "email":"stevebafiam@gmail.com",
            "username": "bafiam",
            "password": "1234567890"
        }
        self.create_user_account_data()
        response = self.client.post('/api/v1/register', data=json.dumps(same_user),
                                                        headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 409)

    def test_user_provide_short_pass(self):
        short_pass = {
            "email":"stevebafiam@gmail.com",
            "username": "stephen",
            "password": "12345"
        }
        response = self.client.post('/api/v1/register', data=json.dumps(short_pass),
                                    headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 400)






if __name__ == '__main__':
    unittest.main()
