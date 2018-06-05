from flask import Flask
from app.routes import user_requests
from app.auth.routes import auth

app = Flask(__name__)

app.register_blueprint(user_requests)
app.register_blueprint(auth)

from app import routes
