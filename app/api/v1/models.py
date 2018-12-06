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
        return user_data

    # get all records

    def get_red_flag_records(self):
        return self.db

    #generate records ids

    def __user__id(self):
        if len(self.db):
            return self.db[-1]["id"] + 1
        else:
            return 1

    # get a single record

    # def get_single_red_flag_records(self):
    #     return self.db

    def find(self, id):
        result = None

        for instance in self.db:
            if instance['id'] == id:
                result = instance
                return result




class UserModel():
    """users model"""
    def __init__(self):
        self.db = user_model

    def data_save_user(self, username, password, email):
        user_account_data = {
            "id": self.__user__id(),
            "username": username,
            "password": password,
            "email": email,



            }
        self.db.append(user_account_data)
        return user_account_data

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

    def get_all_users(self):
        return self.db

