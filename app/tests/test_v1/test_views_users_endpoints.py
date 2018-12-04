import json
import unittest
from . import BaseTestCase


class TestUserAccountAPI(BaseTestCase):
    def create_user_account_data(self):
        user = {
            "firstname": "stephen",
            "lastname": "gumba",
            "othername": "wachiuri",
            "email": "steve@gmail.com",
            "phoneNumber": "981234567",
            "username": "bafiam",
            "password": "1234567890"
        }
        response = self.client.post('/api/v1/register',
                                    data=json.dumps(user),
                                    headers={"content-type": "application/json"})
        return response

    def test_user_register(self):
        record = self.create_user_account_data()
        self.assertIn('Registration successfully', str(record.data))
        self.assertEqual(record.status_code, 201)

    def test_user_login(self):
        self.create_user_account_data()
        new_user = {
            "username": "bafiam",
            "password": "1234567890"
        }
        response = self.client.post("/api/v1/login", data=json.dumps(new_user),
                                    headers={"content-type": "application/json"})
        self.assertIn('Login successfully', str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_user_login_wrong_password(self):
        self.create_user_account_data()
        new_user_with_wrong_pass = {
            "username": "bafiam",
            "password": "123456789"
        }
        response = self.client.post("/api/v1/login", data=json.dumps(new_user_with_wrong_pass),
                                    headers={"content-type": "application/json"})
        self.assertIn('Wrong password or username', str(response.data))
        self.assertEqual(response.status_code, 401)

    def test_case_user_provides_empty_information_login(self):
        self.create_user_account_data()
        empty_user_data = {
            "username":'',
            "password":''
        }
        responce = self.client.post('/api/v1/login', data=json.dumps(empty_user_data),
                                    headers={"content-type": "application/json"})
        self.assertEqual('Please provide all credentials', str(responce.data))


if __name__ == '__main__':
    unittest.main()
