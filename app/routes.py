# from app import app
from flask.views import MethodView
from flask import Blueprint, jsonify
# from flask_restful import Resource

class HelloWorld(MethodView):
    def get(self):
        return jsonify({'hello': 'world'})

index = Blueprint("index", __name__)
user_view = HelloWorld.as_view('hello_world')
index.add_url_rule("/",  view_func=user_view, methods=['GET', 'POST'])
