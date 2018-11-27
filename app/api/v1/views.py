from flask import make_response, jsonify

from .models import RedFlagRecordsModel
from flask_restful import Resource, abort, request


class RedFlagRecords(Resource, RedFlagRecordsModel):
    def __init__(self):
        self.db = RedFlagRecordsModel()

    def get(self):
        resp = self.db.get_red_flag_records()
        return make_response(jsonify({
            "All red-flag records:": resp}), 200)

    def post(self):
        data_save = request.get_json()
        type = data_save['type'],
        location = data_save['location'],
        status = data_save['status'],
        comment = data_save['comment']
        resp = self.db.data_save(type, location, status, comment)
        return make_response(jsonify({
            "My new red-flag records:": resp
        }), 201)
class RedFlagRecord(Resource, RedFlagRecordsModel):
    def __init__(self):
        self.db = RedFlagRecordsModel()

    def get(self, id):
        datas = self.db.get_single_red_flag_records()
        for data in datas:
            if data['id'] == id:
                return make_response(jsonify({"user_data":data}),200)



