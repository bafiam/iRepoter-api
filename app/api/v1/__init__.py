from .views import RedFlagRecords
from flask_restful import Resource, Api
from flask import Blueprint

version_1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_1)
api.add_resource(RedFlagRecords, '/red_flag_records' )
