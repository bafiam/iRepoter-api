from .views_records import IncidentRecords, SingleIncidentRecord, UpdateSingleIncidentRecord
from .views_users import CreateUser, UserLogin, UpdateUser
from flask_restful import Resource, Api
from flask import Blueprint

version_1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_1)
api.add_resource(IncidentRecords, '/incidents')
api.add_resource(SingleIncidentRecord, '/incidents/<int:id>')
api.add_resource(CreateUser, '/auth/register')
api.add_resource(UserLogin, '/auth/login')
api.add_resource(UpdateUser, '/profile/<username>')
api.add_resource(UpdateSingleIncidentRecord, '/incidences/update/<int:id>')

