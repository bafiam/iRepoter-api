import datetime

# red_flag_records = []
# user_model = []
from database import db_conn, create_tables


class RedFlagRecordsModel():

    def __init__(self):
        self.db = db_conn()
        self.cursor = create_tables()
        self.createdOn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = ''

    def data_save(self, createdBy, type, location, comment):
        user_data = {
            # "id": self.__user__id(),
            "createdOn": self.createdOn,
            "createdBy": createdBy,
            "type": type,
            "location": location,
            "status": self.status,
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
        """we will be getting a record _incidence based on the id or the _incidence type"""
        query = """SELECT incident_id, createdon, createdby,type, location,status,comment 
         from incidents WHERE incident_id='{0}'""".format(
            id)
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        get_specific_incidence = cur.fetchone()
        if not get_specific_incidence:
            return None
        else:
            incidence_list = dict(
                id=get_specific_incidence[0],
                createdOn=get_specific_incidence[1],
                createdBy=get_specific_incidence[2],
                type=get_specific_incidence[3],
                location=get_specific_incidence[4],
                status=get_specific_incidence[5],
                comment=get_specific_incidence[6]
            )
            return incidence_list

    def get_all_incidences(self):
        """This will get all incidents all in the database"""
        query = """SELECT incident_id, createdon, createdby,type, location,status,comment  from incidents """
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        get_all_incidences = cur.fetchall()
        if not get_all_incidences:
            return None
        else:
            all_incidences = []
            for incidence in get_all_incidences:
                datar = dict(
                    id=incidence[0],
                    createdOn=incidence[1],
                    createdBy=incidence[2],
                    type=incidence[3],
                    location=incidence[4],
                    status=incidence[5],
                    comment=incidence[6])
                all_incidences.append(datar)
            return all_incidences

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

    def update_incidence_records(self, status, location, comment, id):
        # update an incidence status, location and comment
        query = """UPDATE incidents SET status=%s, location=%s, comment=%s WHERE incident_id='{0}';""".format(id)
        data = (status, location, comment)
        save = self.db
        cur = save.cursor()
        cur.execute(query, data)
        save.commit()

    def get_record_who_created_it(self, id):
        """After a check that the incidence does exist.current_identity
         will run this to return who created the record
         IT will be based on this the current_identity
         at this point,  i will compare with current_identity, the person in session"""
        query = """SELECT createdby FROM incidents WHERE incident_id='{0}';""".format(id)
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        created_by = cur.fetchone()[0]
        if not created_by:
            return None
        return created_by





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
        query = """SELECT * FROM users WHERE username='{0}'""".format(username)
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        get_specific_user = cur.fetchone()
        if get_specific_user == 0:
            return None
        else:
            return get_specific_user

    def get_user_email(self, email):
        # this will get the user email
        query = """SELECT email FROM users WHERE email='{0}'""".format(email)
        save = self.db
        cur = save.cursor()
        cur.execute(query)
        get_user_email = cur.fetchone()
        if get_user_email == 0:
            return None
        return get_user_email

    def update_user_data(self, firstname, lastname, othernames, phoneNumber, username):
        # update the user profile data.
        query = """ UPDATE users SET firstname=%s,lastname=%s,othernames=%s,phone_number=%s WHERE username='{0}';""".format(
            username)
        data = (firstname, lastname, othernames, phoneNumber,)
        # self.db.append(user_account_data)
        save = self.db
        cur = save.cursor()
        cur.execute(query, data)
        save.commit()
        # return update_profile_data
