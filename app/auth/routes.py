from flask.views import MethodView
from flask import Blueprint, jsonify, request
from app.models import User
from dbconnection import dbConnection

auth = Blueprint("auth", __name__)
db_connection = dbConnection()

class RegisterUser(MethodView):
    """ Route class to register a user """
    def post(self):
        """ Register a user """
                
        post_data = request.get_json()

        username = post_data.get('username')
        email = post_data.get('email')
        password = post_data.get('password')
        isAdmin = post_data.get('isAdmin')

        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not email:
            return jsonify({"msg": "Missing email parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400  
        
        new_user = User(username, email, password, isAdmin)
        db_connection.create_new_user(1, username, email, password, isAdmin)
        return jsonify({"new_user":new_user.__dict__}), 200

class LoginUser(MethodView):
    """ class to login a user """    
    def post(self):
        """ Login a user """
        
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