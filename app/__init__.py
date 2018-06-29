from flask import Flask
from app.routes import user_requests
from app.auth.routes import auth
from flask_jwt_extended import JWTManager
from app import routes
from config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_object(app_config[config_name])
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')

    # registering plugable views
    app.register_blueprint(user_requests)
    app.register_blueprint(auth)

    # Setup the Flask-JWT-Extended extension
    app.config['JWT_SECRET_KEY'] = 'i-got-the-source'
    jwt = JWTManager(app)

    return app
