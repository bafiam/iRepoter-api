from flask_restful import Resource, request
from flask import make_response, jsonify
from .models_users import UserModel


class CreateUser(Resource, UserModel):
    def __init__(self):
        self.db = UserModel()

    def post(self):
        create_account = request.get_json()
        firstname = create_account['firstname'],
        lastname = create_account['lastname'],
        othername = create_account['othername'],
        email = create_account['email'],
        phoneNumber = create_account['phoneNumber'],
        username = create_account['username'],
        password = create_account['password']
        data = self.db.data_save_user(firstname, lastname, othername, email,
                                      phoneNumber, username, password
                                      )
        return make_response(jsonify({
            "message": "Registration successfully"
        }), 201)


class GetUserLogin(Resource, UserModel):
    def __init__(self):
        self.db = UserModel()

    def post(self):
        data = request.get_json()
        username = data['username'],
        password = data['password']

        user = self.db.get_user_data_login(username)

        if user['password'] == password:
            return make_response(jsonify({
                "message": "Login successfully"
            }), 201)
        else:
            return make_response(jsonify({
                "message": "Wrong password or username"
            }), 401)
