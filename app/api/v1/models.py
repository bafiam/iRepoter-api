red_flag_records = []


class RedFlagRecordsModel():
    def __init__(self):
        self.db = red_flag_records

    def data_save(self, id, createdOn, createdBy, type, location, status, image, video, comment):
        user_data = {
            "id": self.__user__id(),
            "type": type,
            "location": location,
            "status": status,
            "comment": comment

        }
        self.db.append(user_data)
        return self.db

    def get_red_flag_records(self):
        return self.db

    def update_red_flag_records(self):
        pass

    def __user__id(self):
        if len(self.db):
            return self.db[-1] + 1
        else:
            return 1
