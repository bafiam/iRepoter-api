from flask import make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from .models import RedFlagRecordsModel
from flask_restful import Resource, abort, request, reqparse


class RedFlagRecords(Resource, RedFlagRecordsModel):
    """Represent a resource class where user can  post and fetch all all accident """

    def __init__(self):
        self.db = RedFlagRecordsModel()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('type', type=str, help="This field cannot be empty "
                                                          " Bad choice: {error_msg},"
                                                          " Valid choices are intervention and red-flag ",
                                   required=True,
                                   choices=("red-flag", "intervention"))
        self.reqparse.add_argument('location', type=str, help='Provide a location', required=True)
        self.reqparse.add_argument('status', type=str, help="Provide a valid accident status"
                                                            " Bad choice: {error_msg},"
                                                            "Valid choices are under investigation,"
                                                            "rejected,resolved, not approved,approved", required=True,
                                   choices=("under investigation", "rejected", "resolved", "not approved", "approved"))
        self.reqparse.add_argument('comment', type=str, help='Provide a comment for the accident', required=True)

    @jwt_required
    def get(self):
        resp = self.db.get_all_incidences()
        if resp:
            return make_response(jsonify({
                "message": "Your accident records are:",
                "data": resp
            }), 200)
        else:
            return make_response(jsonify({"message": "Your accident records is empty"}), 404)

    @jwt_required
    def post(self):
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        record_data = self.reqparse.parse_args()
        data_save = record_data
        createdBy = current_user
        type = data_save['type']
        location = data_save['location']
        status = data_save['status']
        comment = data_save['comment']
        resp = self.db.data_save(createdBy,type, location, status, comment)
        return make_response(jsonify({
            "message": "Accident record created",
            "data": resp
        }), 201)


class RedFlagRecord(Resource, RedFlagRecordsModel):
    """Represent a resource class where user can  fetch, update and delete accident record based on record id"""

    def __init__(self):
        self.db = RedFlagRecordsModel()

    @jwt_required
    def get(self, id):
        datas = self.db.get_incidence_records_by_id(id)
        if datas:
            return make_response(jsonify({"message": "your accident is",
                                          "data": datas
                                          }), 200)
        else:
            return make_response(jsonify({"message": "No record with that id"}), 404)

    @jwt_required
    def delete(self, id):
        del_datas = self.db.get_incidence_records_by_id(id)
        if not del_datas:
            return make_response(jsonify({'message': 'accident not found'}), 404)
        else:
            self.db.delete_incidence(id)
            return make_response(jsonify({"message": "Red flag record deleted"
                                          }), 200)

    @jwt_required
    def patch(self, id):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('images', type=str,help="Provide a valid image"
                                   , required=True,)
        self.reqparse.add_argument('video', type=str, help='Provide a video for the accident', required=False)
        to_update = self.db.get_incidence_records_by_id(id)
        if not to_update:
            return make_response(jsonify({'message': 'incident record for update not found'}), 404)
        else:
            data_4_update = self.reqparse.parse_args()
            update = data_4_update
            images=update['images']
            video=update['video']
            self.db.update_incidence(images, video,id)
            return make_response(jsonify({"message": "The incident records has been updated",
                                          "data": data_4_update

                                          }), 201)
