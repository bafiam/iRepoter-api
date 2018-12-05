import re

import bcrypt
from flask_restful import Resource, request, reqparse
from flask import make_response, jsonify
from .models import UserModel


class CreateUser(Resource, UserModel):
    """user account creation"""
    def __init__(self):
        self.db = UserModel()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('email', help='Email required', required=True)
        self.reqparse.add_argument('username', type=str, help='Username required', required=True)
        self.reqparse.add_argument('password', type=str, help='Password required', required=True)

    def post(self):
        user_data = self.reqparse.parse_args()
        if not user_data['username'] or not user_data['password']:
            return make_response(jsonify({'error': 'Username and password required'}), 400)
        elif not str.isalpha(user_data['username']):
            return make_response(jsonify({'error': 'All characters in the Username string can only contain alphabets'}), 400)
        elif not re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", user_data['email']):
            return make_response(jsonify({'error': 'Provide a valid email address'}), 400)
        else:
            if len(user_data['password']) < 7:
                return make_response(jsonify({'error':
                             'Password must be atleast 8 characters long!'
                         }), 400)
            else:
                create_account = user_data
                email = create_account['email']
                username = create_account['username']
                password = (bcrypt.hashpw(create_account['password'].encode('utf-8'), bcrypt.gensalt())).decode('utf-8')
                is_valid = self.db.validate_the_user_username(username)
                if is_valid:
                    return make_response(jsonify({"message": "The user does exist"}), 409)
                else:
                    data = self.db.data_save_user(username, password, email)
                    return make_response(jsonify({
                        "message": "Registration successfully",
                        "User information":[
                         username,
                         email
                    ]


                    }), 201)


class GetUserLogin(Resource, UserModel):
    """user login and validation"""
    def __init__(self):
        self.db = UserModel()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, help='Username required', required=True)
        self.reqparse.add_argument('password', type=str, help='Password required', required=True)

    def post(self):
        user_login_data = self.reqparse.parse_args()
        if not user_login_data['username'] or not user_login_data['password']:
            return make_response(jsonify({'message': 'Please provide all credentials'}), 400)
        else:
            login_user = user_login_data
            username = login_user['username'],
            password = login_user['password']
            for user in self.db.get_all_users():
                if user['username'] == username:
                    if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):

                        return make_response(jsonify({"message": "Login successfully"}), 200)
                    else:
                        return make_response(jsonify({"message": "Wrong password or username"}), 400)

                else:
                    return make_response(jsonify({"message": "user does not exist"}), 404)
