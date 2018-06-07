from flask import Flask
from app.routes import user_requests
from app.auth.routes import auth
from flask_jwt_extended import JWTManager
from app import routes


app = Flask(__name__)

app.register_blueprint(user_requests)
app.register_blueprint(auth)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'i-got-the-source'
jwt = JWTManager(app)
