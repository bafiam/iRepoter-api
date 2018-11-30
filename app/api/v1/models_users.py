user_model = []


class UserModel():
    def __init__(self):
        self.db = user_model

    def data_save_user(self, firstname, lastname, othername, email, phoneNumber, username, password):
        is_valid = self.validate_the_user_username(username)
        if is_valid:
            return {"message":"The user does exist"}
        else:
            user_account_data = {
                "id": self.__user__id(),
                "firstname": firstname,
                "lastname": lastname,
                "othername": othername,
                "email": email,
                "phoneNumber": phoneNumber,
                "username": username,
                "password": password,

        }
        self.db.append(user_account_data)
        return self.db

    # generate user ids

    def __user__id(self):
        if len(self.db):
            return self.db[-1]["id"] + 1
        else:
            return 1

    def validate_the_user_username(self, username):
        for user_name in self.db:
            if user_name['username'] == username:
                return True
            else:
                return False

    def get_user_data_login(self, username):
        for user in self.db:
            if user['username'] == username:
                return user


