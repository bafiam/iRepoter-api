import datetime

# red_flag_records = []
# user_model = []
from database import db_conn, create_tables


class RedFlagRecordsModel():

    def __init__(self):
        self.db = db_conn()
        self.cursor = create_tables()
        self.createdOn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def data_save(self, createdBy, type, location, status, comment):
        user_data = {
            # "id": self.__user__id(),
            "createdOn": self.createdOn,
            "createdBy": createdBy,
            "type": type,
            "location": location,
            "status": status,
            "comment": comment

        }
        query = """INSERT INTO incidents(createdon, createdby, type, location, status, comment)
         VALUES ('{0}','{1}','{2}','{3}','{4}','{5}');""".format(
            user_data['createdOn'], user_data['createdBy'], user_data['type'],
            user_data['location'], user_data['status'], user_data['comment'])
        # self.db.append(user_account_data)
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        save.commit()
        # self.db.append(user_data)
        return user_data

    # get all records

    def get_incidence_records_by_id(self, id):
        """we will be getting a record incidence based on the id or the incidence type"""
        query = """SELECT * from incidents WHERE incident_id='{0}'""".format(id)
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        get_specific_incidence = cur.fetchone()
        if not get_specific_incidence:
            return None
        else:
            return get_specific_incidence

    def get_all_incidences(self):
        """This will get all incidents all in the database"""
        query = """SELECT * from incidents """
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        get_all_incidences = cur.fetchall()
        if not get_all_incidences:
            return None
        else:
            return get_all_incidences

    def get_incidence_records_by_created_by(self, username):
        """we will be getting a record based on the user.
        the user in session need to be the one who created it
        also get an incidence based on the id or the incidence type"""
        query = """SELECT * from incidents WHERE createdby='{0}'""".format(username)
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        get_incidence_by_created_by = cur.fetchone()
        if not get_incidence_by_created_by:
            return None
        else:
            return get_incidence_by_created_by

    def delete_incidence(self, id):
        """ This will delete an incidence based on its id"""
        query = """DELETE FROM incidents WHERE incident_id='{0}'""".format(id)
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        save.commit()

    def update_incidence(self, images, video, id):
        # update the incidences images and video
        query = """ UPDATE incidents SET images=%s,video=%s WHERE incident_id='{0}';""".format(id)
        data = (images, video,)
        save = self.db
        cur = save.cursor()
        cur.execute(query, data)
        save.commit()


# generate records ids

# def __user__id(self):
#     if len(self.db):
#         return self.db[-1]["id"] + 1
#     else:
#         return 1

# get a single record

# def get_single_red_flag_records(self):
#     return self.db

# def find(self, id):
#     result = None
#
#     for instance in self.db:
#         if instance['id'] == id:
#             result = instance
#             return result


class UserModel():
    """users model"""

    def __init__(self):
        self.db = db_conn()
        self.cursor = create_tables()
        self.registered = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.isAdmin = False
        # self.db = user_model

    def data_save_user(self, username, password, email):
        user_account_data = {
            # "id": self.__user__id(),
            "username": username,
            "password": password,
            "email": email,
            "registered": self.registered,
            "isAdmin": self.isAdmin,

        }
        query = """INSERT INTO users(username,password, email, registered,is_admin) VALUES ('{0}','{1}','{2}','{3}','{4}');""".format(
            user_account_data['username'], user_account_data['password'], user_account_data['email'],
            user_account_data['registered'], user_account_data['isAdmin'])
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

    def update_user_data(self, firstname, lastname, othernames, phoneNumber):
        # update the user profile data.
        query = """ UPDATE users SET firstname=%s,lastname=%s,othernames=%s,phone_number=%s;"""
        data = (firstname, lastname, othernames, phoneNumber,)
        # self.db.append(user_account_data)
        save = self.db
        cur = save.cursor()
        cur.execute(query, data)
        save.commit()
        # return update_profile_data
