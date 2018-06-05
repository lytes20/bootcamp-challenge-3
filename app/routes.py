from flask.views import MethodView
from flask import Blueprint, jsonify

user_requests = Blueprint("user_requests", __name__)

class UserRequests(MethodView):
    """ class for creating, reading and editing user requests """
    def post(self):
        """ create a new request """
        return jsonify({'msg': 'created request'}), 200

    def get(self, requestid=None):
        """ get all requests for a logged in user, a single req """
        if requestid:
            return jsonify({"msg": "fetched the request"}), 200
        else:
            return jsonify({"msg": "fetched all requests"}), 200
    def put(self, requestid):
        """ fuction to edit a user request"""
        return jsonify({"msg": "edited request"}), 200

class AdminActions(MethodView):
    """ class contains actions that can be performed by admin users """
    # TODO: approve(put), disapprove (put), resolve (put), view all reqquests (get)
    def get(self):
        """ fuction to fetch all requests on the application """
        return jsonify({"msg": "fetched all requests"}), 200            

    




user_requests_view = UserRequests.as_view('user_requests')
admin_actions_view = AdminActions.as_view('admin_actions')

#url rules for user_requests
user_requests.add_url_rule("/api/v1/users/requests",  view_func=user_requests_view, methods=['POST', 'GET'])
user_requests.add_url_rule("/api/v1/users/requests/<requestid>",  view_func=user_requests_view, methods=['GET'])
user_requests.add_url_rule("/api/v1/users/requests/<requestid>",  view_func=user_requests_view, methods=['PUT'])

#url rules for admin actions
user_requests.add_url_rule("/api/v1/requests",  view_func=admin_actions_view, methods=['GET'])