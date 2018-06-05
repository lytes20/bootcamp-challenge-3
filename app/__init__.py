from flask import Flask
from app.routes import index

app = Flask(__name__)
app.register_blueprint(index)

from app import routes
