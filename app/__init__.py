from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from instance.config import app_config
from .api.v1 import version_1 as v1

import datetime
time_out_token = datetime.timedelta(6000)
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config['SECRET_KEY'] = 'some636363gddd7e7@#$5ffff^^^^&hhshdhdhdfhfdhdg'
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = time_out_token
    JWTManager(app)
    app.register_blueprint(v1)
    return app
