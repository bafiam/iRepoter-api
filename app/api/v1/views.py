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
