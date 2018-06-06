from flask import jsonify
class ValidateAuthData:

    def validate_register_data(self, username, email, password, isAdmin):
        if not username:
            return {"msg": "Missing username parameter"}
        if not email:
            return {"msg": "Missing email parameter"}
        if not password:
            return {"msg": "Missing password parameter"}
        if username == "":
            return {"msg": "Missing username parameter"}
        if email == "" :
            return {"msg": "Missing email parameter"}
        if password == "":
            return {"msg": "Missing password parameter"}

    def validate_login_data(self, email, password):        
        if not email:
            return {"msg": "Missing email parameter"}
        if not password:
            return {"msg": "Missing password parameter"}
        if email == "" :
            return {"msg": "Missing email parameter"}
        if password == "":
            return {"msg": "Missing password parameter"}


