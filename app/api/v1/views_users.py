import re
from flask_jwt_extended import create_access_token, jwt_required
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
            return make_response(jsonify({'error': 'All characters in the Username string can only contain alphabets'}),
                                 400)
        elif not re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", user_data['email']):
            return make_response(jsonify({'error': 'Provide a valid email address'}), 400)

        if len(user_data['password']) < 7:
            return make_response(jsonify({'error': 'Password must be at least 8 characters long!'}), 400)
        elif re.search('[0-9]', (user_data['password'])) is None:
            return make_response(jsonify({'error': 'Password must have at least one number in it!'}), 400)
        elif re.search('[A-Z]', (user_data['password'])) is None:
            return make_response(jsonify({'error': 'Password must have at least one capital letter in it!'}), 400)
        elif re.search('[a-z]', (user_data['password'])) is None:
            return make_response(jsonify({'error': 'Password must have at least one alphabet letter in it!'}), 400)
        elif re.search('[!,#,$,%,&,*,+,-,<,=,>,?,@,^,_,{,|,},~,]', (user_data['password'])) is None:
            return make_response(jsonify({'error': 'Password must have at least a special character in it!'}), 400)
        else:
            create_account = user_data
            email = create_account['email']
            username = create_account['username']
            password = (bcrypt.hashpw(create_account['password'].encode('utf-8'), bcrypt.gensalt())).decode('utf-8')
            is_valid = self.db.get_user_by_username(username)
            if is_valid:
                return make_response(jsonify({"message": "A user with same username exist"}), 409)
            else:
                find_email = self.db.get_user_email(email)
                if find_email:
                    return make_response(jsonify({"message": "A user with same email exist"}), 409)
                self.db.data_save_user(username, password, email)
                access_token = create_access_token(identity=username)
                return make_response(jsonify({
                    "message": "Registration successfully",
                    "User information": [
                        username,
                        email,
                    ]
                }), 201)


class UserLogin(Resource, UserModel):
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

        login_user = user_login_data
        username = login_user['username']
        password = login_user['password']
        check_registration = self.db.get_user_by_username(username)
        if check_registration:
            if bcrypt.checkpw(password.encode('utf-8'), check_registration[9].encode('utf-8')):
                access_token = create_access_token(identity=username, expires_delta=None)
                return make_response(jsonify({"message": "Login successfully",
                                              "access_token": access_token,
                                              "id":check_registration[0],
                                              "Name":check_registration[4]

                                              }), 200)
            else:
                return make_response(jsonify({"message": "Wrong password or username"}), 400)
        else:
            return make_response(jsonify({"message": "Please register as a user into the system to login"}), 500)


class UpdateUser(Resource, UserModel):

    def __init__(self):
        self.db = UserModel()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('firstname', type=str, help='First name required', required=True)
        self.reqparse.add_argument('lastname', type=str, help='Last name required', required=True)
        self.reqparse.add_argument('othername', type=str, help='Other name required', required=True)
        self.reqparse.add_argument('phoneNumber', type=str, help='”Phone number required', required=True)

    @jwt_required
    def patch(self, username):
        """
        it will be by user id . as in allow update on the logged in user row only.
        will reuse  find user by username
        :return:
        """
        # find by username
        user_profile = self.db.get_user_by_username(username)
        if user_profile:
            user_data = self.reqparse.parse_args()
            update = user_data
            firstname = update['firstname']
            lastname = update['lastname']
            othername = update['othername']
            phoneNumber = update['phoneNumber']
            self.db.update_user_data(firstname, lastname, othername, phoneNumber, username)

            return make_response(jsonify({"Message": "Update successful",
                                          "data": update}), 201)
        else:
            return make_response(jsonify({"Message": "Something went wrong.Try again"}), 500)
