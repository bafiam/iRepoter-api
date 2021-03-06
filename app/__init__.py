from flask import Flask
from flask_jwt_extended import JWTManager
from instance.config import app_config
from .api.v1 import version_1 as v1
from database import create_tables,create_admin
import datetime
from os import environ
time_out_token = datetime.timedelta(seconds=6000000)


def create_app():
    config_name = environ.get('FLASK_ENV')
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SECRET_KEY'] = 'some636363hhhhhgddd7e7@#$5ffff^^^^&hhshdhdhdfhfdhdg'
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = time_out_token
    JWTManager(app)
    create_tables()
    create_admin()
    app.register_blueprint(v1)
    return app
