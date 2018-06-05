from flask.views import MethodView
from flask import Blueprint, jsonify, request
from app.models import User

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
            isAdmin = post_data.get('isAdmin')
            
            new_user = User(username, email, password, isAdmin)
            return jsonify({"new_user":new_user.__dict__}), 200

class LoginUser(MethodView):
    """ class to login a user """    
    def post(self):
        """ Login a user """
        if request.content_type == 'application/json':
            post_data = request.get_json()
            email = post_data.get('email')
            password = post_data.get('password')
            
            if email != 'email@email.com' or password != 'secret':
                return jsonify({"msg": "Invalid username or password"}), 401
            return jsonify({"msg":"Successful login"}), 200

           



registration_view = RegisterUser.as_view('register_user')
login_view = LoginUser.as_view('login')

auth.add_url_rule("/api/v1/user/register",  view_func=registration_view, methods=['POST'])
auth.add_url_rule('/api/v1/user/login', view_func=login_view, methods=['POST'])