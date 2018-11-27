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

    def delete(self, id):
        del_datas = self.db.get_single_red_flag_records()
        to_delete = self.db.find(id)

        if not to_delete:
            return {'message': 'not found'}, 404
        else:
            del_datas.remove(to_delete)
        # for del_data in del_datas:
        #     if del_data['id'] == id:
        #         del_datas.remove(del_data)
        return make_response(jsonify({"response":"Red flag record deleted"}), 200)

    def patch(self, id):
        to_update = self.db.find(id)
        if not to_update:
            return {'message': 'not found'}, 404
        else:
            to_update.update(request.get_json())
        return make_response(jsonify({
                    "My red-flag records updated:": to_update
                }), 201)
