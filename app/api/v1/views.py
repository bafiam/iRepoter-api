from .models import RedFlagRecordsModel
from flask_restful import Resource


class RedFlagRecords(Resource, RedFlagRecordsModel):
    def __init__(self):
        self.db = RedFlagRecordsModel()

    def get(self):
        resp = self.db.get_red_flag_records()

        return resp, 200
