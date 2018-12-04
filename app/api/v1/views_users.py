import bcrypt
from flask_restful import Resource, request, reqparse
from flask import make_response, jsonify
from .models import UserModel


class CreateUser(Resource, UserModel):
    """user account creation"""
    def __init__(self):
        self.db = UserModel()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, help='Username required', required=True)
        self.reqparse.add_argument('password', type=str, help='Password required', required=True)

    def post(self):
        user_data = self.reqparse.parse_args()
        if not user_data['username'] or not user_data['password']:
            return {'error': 'Username and password required'}, 400
        else:
            if len(user_data['password']) < 7:
                return ({'error':
                             'Password must be atleast 8 characters long!'
                         }, 400)
            else:
                create_account = user_data
                username = create_account['username'],
                password = (bcrypt.hashpw(create_account['password'].encode('utf-8'), bcrypt.gensalt())).decode('utf-8')
                is_valid = self.db.validate_the_user_username(username)
                if is_valid:
                    return {"message": "The user does exist"}, 404
                else:
                    data = self.db.data_save_user(username, password)
                    return make_response(jsonify({
                        "message": "Registration successfully"

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
            return {'message': 'Please provide all credentials'}, 400
        else:
            login_user = user_login_data
            username = login_user['username'],
            password = login_user['password']
            for user in self.db.get_all_users():
                if user['username'] == username:
                    if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):

                        return make_response(jsonify({"message": "Login successfully"}), 200)
                    else:
                        return {"message": "Wrong password or username"}, 400

                else:
                    return {"message": "user does not exist"}, 404
