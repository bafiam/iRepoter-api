red_flag_records = []
user_model = []


class RedFlagRecordsModel():

    def __init__(self):
        self.db = red_flag_records

    def data_save(self, type, location, status, comment):
        user_data = {
            "id": self.__user__id(),
            "type": type,
            "location": location,
            "status": status,
            "comment": comment

        }
        self.db.append(user_data)
        return self.db

    """get all records"""

    def get_red_flag_records(self):
        return self.db

    """generate records ids"""

    def __user__id(self):
        if len(self.db):
            return self.db[-1]["id"] + 1
        else:
            return 1

    """get a single record"""

    def get_single_red_flag_records(self):
        return self.db

    def find(self, id):
        result = None

        for instance in self.db:
            if instance['id'] == id:
                result = instance
                return result


"""users model"""

class UserModel():
    def __init__(self):
        self.db = user_model

    def data_save_user(self, firstname, lastname, othername, email, phoneNumber, username, password):
        is_valid = self.validate_the_user_username(username)
        if is_valid:
            return {"message": "The user does exist"}
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

    """generate user ids"""

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
