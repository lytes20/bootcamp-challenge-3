from flask import Flask
from app.routes import user_requests

app = Flask(__name__)

app.register_blueprint(user_requests)

from app import routes
