from dbconnection import dbConnection
from validate_email import validate_email

db_connection = dbConnection()


class ValidateAuthData:
    """ class to validate data that will be entered by users"""
    def validate_register_data(self, username, email, password, isAdmin):
        """ function to validate data entered while trying to register """
        if not username:
            return {"msg": "Missing username parameter"}
        if not email:
            return {"msg": "Missing email parameter"}
        if not password:
            return {"msg": "Missing password parameter"}
        if username == "":
            return {"msg": "Missing username parameter"}
        if email == "":
            return {"msg": "Missing email parameter"}
        if password == "":
            return {"msg": "Missing password parameter"}
        is_valid = validate_email(email)
        if not is_valid:
            return {"msg": "Email invalid"}        
        returned_user = db_connection.get_user_by_email(email)
        if returned_user:
            return {"msg": "User already exists"}

    def validate_login_data(self, email, password):
        """ function to validate data while trying to log in """
        if not email:
            return {"msg": "Missing email parameter"}
        if not password:
            return {"msg": "Missing password parameter"}
        if email == "":
            return {"msg": "Missing email parameter"}
        if password == "":
            return {"msg": "Missing password parameter"}
        is_valid = validate_email(email)
        if not is_valid:
            return {"msg": "Email invalid"}