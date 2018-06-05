from flask.views import MethodView
from flask import Blueprint, jsonify


class UserRequests(MethodView):
    def post(self):
        """ create a new request """
        return jsonify({'msg': 'created request'}), 200

    def get(self, requestid=None):
        """ get all requests for a logged in user, a single req """
        if requestid:
            return jsonify({"msg": "fetched the request"}), 200
        else:
            return jsonify({"msg": "fetched all requests"}), 200
    

    


user_requests = Blueprint("user_requests", __name__)

user_requests_view = UserRequests.as_view('user_requests')

user_requests.add_url_rule("/api/v1/users/requests",  view_func=user_requests_view, methods=['POST', 'GET'])
user_requests.add_url_rule("/api/v1/users/requests/<requestid>",  view_func=user_requests_view, methods=['GET'])