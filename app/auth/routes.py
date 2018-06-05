from flask.views import MethodView
from flask import Blueprint, jsonify, request

auth = Blueprint("auth", __name__)

class RegisterUser(MethodView):
    """ Route class to register a user """
    def post(self):
        """ Register a user """
        if request.content_type == 'application/json':
            post_data = request.get_json()
            username = post_data.get('username')
            email = post_data.get('email')
            password = post_data.get('password')
            
            new_user = ""
           



registration_view = RegisterUser.as_view('register_user')

auth.add_url_rule("/api/v1/user/register",  view_func=registration_view, methods=['POST'])