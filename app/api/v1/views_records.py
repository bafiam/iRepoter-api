from flask import make_response, jsonify

from .models_records import RedFlagRecordsModel
from flask_restful import Resource, abort, request


class RedFlagRecords(Resource, RedFlagRecordsModel):
    def __init__(self):
        self.db = RedFlagRecordsModel()

    def get(self):
        resp = self.db.get_red_flag_records()
        if resp:
            return make_response(jsonify({
                "message":"Your accident records are:",
                "data":[resp]
            }), 200)
        else:
            return make_response(
                "Your accident records is empty", 404)

    def post(self):
        data_save = request.get_json()
        type = data_save['type'],
        location = data_save['location'],
        status = data_save['status'],
        comment = data_save['comment']
        resp = self.db.data_save(type, location, status, comment)
        return make_response(jsonify({
            "message":"Accident record created",
            "data": [resp]
        }), 201)


class RedFlagRecord(Resource, RedFlagRecordsModel):
    def __init__(self):
        self.db = RedFlagRecordsModel()

    def get(self, id):
        datas = self.db.get_single_red_flag_records()
        for data in datas:
            if data['id'] == id:
                return make_response(jsonify({"message":"your accident is",
                                              "data":data}), 200)
            else:
                return make_response("No record with that id", 404)

    def delete(self, id):
        del_datas = self.db.get_single_red_flag_records()
        to_delete = self.db.find(id)

        if not to_delete:
            return {'message': 'not found'}, 404
        else:
            data = del_datas.remove(to_delete)
        # for del_data in del_datas:
        #     if del_data['id'] == id:
        #         del_datas.remove(del_data)
        return make_response(jsonify({"message": "Red flag record deleted",
                                      "data": data}), 200)

    def patch(self, id):
        to_update = self.db.find(id)
        if not to_update:
            return {'message': 'not found'}, 404
        else:
            to_update.update(request.get_json())
        return make_response(jsonify({"message":"My red-flag records updated",
                                      "data":to_update
        }), 201)
