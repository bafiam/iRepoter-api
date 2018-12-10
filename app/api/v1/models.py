red_flag_records = []
# user_model = []
from database import db_conn, create_tables


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

    # generate records ids

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
        self.db = db_conn()
        self.cursor = create_tables()
        # self.db = user_model

    def data_save_user(self, username, password, email):
        user_account_data = {
            # "id": self.__user__id(),
            "username": username,
            "password": password,
            "email": email,

        }
        query = """INSERT INTO users(username,password, email) VALUES ('{0}','{1}','{2}');""".format(
            user_account_data['username'], user_account_data['password'], user_account_data['email'])
        # self.db.append(user_account_data)
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        save.commit()
        return user_account_data

    def get_user_by_username(self, username):
        # This will get the user by their username
        query = """SELECT * from users WHERE username='{0}'""".format(username)
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        get_specific_user = cur.fetchone()
        if get_specific_user == 0:
            return None

        else:
            return get_specific_user


