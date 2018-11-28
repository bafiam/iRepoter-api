red_flag_records = []


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

    def get_single_red_flag_records(self):
        return self.db

    def find(self, id):
        result = None

        for instance in self.db:
            if instance['id'] == id:
                result = instance
                return result
