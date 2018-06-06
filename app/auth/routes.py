from flask.views import MethodView
from flask import Blueprint, jsonify, request
from app.models import User
from dbconnection import dbConnection
from app.auth.utitlity import ValidateAuthData
import uuid

auth = Blueprint("auth", __name__)
db_connection = dbConnection()
val_data = ValidateAuthData()

class RegisterUser(MethodView):
    """ Route class to register a user """
    def post(self):
        """ Register a user """
                
        post_data = request.get_json()

        username = post_data.get('username')
        email = post_data.get('email')
        password = post_data.get('password')
        isAdmin = post_data.get('isAdmin')
        user_id = uuid.uuid4().int & (1<<24)-1

        
        response = val_data.validate_register_data(username, email, password, isAdmin)
        if response:
            return jsonify(response), 400
        else:
            new_user = User(username, email, password, isAdmin)
            db_connection.create_new_user(user_id, username, email, password, isAdmin)
            return jsonify({"new_user":new_user.__dict__}), 200

class LoginUser(MethodView):
    """ class to login a user """    
    def post(self):
        """ Login a user """
        
        post_data = request.get_json()
        email = post_data.get('email')
        password = post_data.get('password')

        response = val_data.validate_login_data(email, password)

        if response:
            return jsonify(response), 400
        else:
            returned_email = db_connection.get_user_email(email)
            return jsonify({"msg":returned_email}), 200

registration_view = RegisterUser.as_view('register_user')
login_view = LoginUser.as_view('login')

auth.add_url_rule("/api/v1/user/register",  view_func=registration_view, methods=['POST'])
auth.add_url_rule('/api/v1/user/login', view_func=login_view, methods=['POST'])