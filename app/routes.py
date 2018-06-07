from flask.views import MethodView
from flask import Blueprint, jsonify, request
from app.models import MaintenanceRequest
from dbconnection import dbConnection
from app.utility import ValidateRequestData
import uuid

user_requests = Blueprint("user_requests", __name__)
db_connection = dbConnection()
val_req_data = ValidateRequestData ()

class UserRequests(MethodView):
    """ class for creating, reading and editing user requests """
    def post(self):
        #get entered data
        data = request.get_json()

        #picking the request attributes
        req_title = data.get("request_title")
        req_desc = data.get("request_description")
        requester_name = "Gideon"
        req_status = "pending"
        req_id = uuid.uuid4().int & (1<<24)-1

        #validation        
        response = val_req_data.validate_request_creation(req_title, req_desc, requester_name, req_status)
        if response:
            return jsonify(response), 400
        else:
            #storing entered request
            new_request = MaintenanceRequest(req_title, req_desc, requester_name, req_status, req_id)        
            db_connection.create_new_request(req_id, req_title, req_desc, requester_name, req_status)
            return jsonify({'request': new_request.__dict__}), 200

    def get(self, requestid=None):
        """ get all requests for a logged in user, a single req """        

        #check if request id was passed or not
        if requestid and requestid != None:
            #validation
            response = val_req_data.validate_request_id(requestid)
            if response:
                return jsonify(response), 400
            else:
                returned_req = db_connection.get_a_single_user_request(requestid)
                return jsonify({"request": returned_req}), 200
        else:
            returned_reqs = db_connection.get_a_user_requests("Gideon")
            return jsonify({"msg": returned_reqs}), 200
    
    def put(self, requestid):
        """ fuction to edit a user request"""

        if requestid and requestid != None:
            #validating requestid
            res = val_req_data.validate_request_id(requestid)
            if res:
                return jsonify(res), 400
            else:
                #get entered data
                data = request.get_json()

                #picking the request attributes
                req_title = data.get("request_title")
                req_desc = data.get("request_description")
                
                #validating new entered data        
                response = val_req_data.validate_edit_request_data(req_title, req_desc)

                if response:
                    return jsonify(response), 400
                else:
                    #updating request
                    db_connection.update_user_request(req_title, req_desc, requestid)
                    updated_req = db_connection.get_a_single_user_request(requestid)
                    return jsonify({'request': updated_req}), 200


class AdminActions(MethodView):
    """ class contains actions that can be performed by admin users """
    # TODO: approve(put), disapprove (put), resolve (put), view all reqquests (get)

    def get(self):
        """ fuction to fetch all requests on the application """
        returned_reqs = db_connection.get_all_app_requests()
        return jsonify({"msg": returned_reqs}), 200
        

class ApproveRequest(MethodView):
    """ class to approve  a request """
    def put(self, requestid):
        if requestid and requestid != None:
            #validating requestid
            res = val_req_data.validate_request_id(requestid)
            if res:
                return jsonify(res), 400
            else:                
                #updating request        
                db_connection.update_request_status(requestid, "approve")
                updated_req = db_connection.get_a_single_user_request(requestid)
                return jsonify({'request': updated_req}), 200

class DisapproveRequest(MethodView):
    """ class to disapprove a request """
    def put(self, requestid):
        if requestid and requestid != None:
            #validating requestid
            res = val_req_data.validate_request_id(requestid)
            if res:
                return jsonify(res), 400
            else:                
                #updating request        
                db_connection.update_request_status(requestid, "disapprove")
                updated_req = db_connection.get_a_single_user_request(requestid)
                return jsonify({'request': updated_req}), 200

class ResolveRequest(MethodView):
    """ class to resolve a request """
    def put(self, requestid):
        if requestid and requestid != None:
            #validating requestid
            res = val_req_data.validate_request_id(requestid)
            if res:
                return jsonify(res), 400
            else:                
                #updating request        
                db_connection.update_request_status(requestid, "resolve")
                updated_req = db_connection.get_a_single_user_request(requestid)
                return jsonify({'request': updated_req}), 200 


    




user_requests_view = UserRequests.as_view('user_requests')
admin_actions_view = AdminActions.as_view('admin_actions')
approve_request_view = ApproveRequest.as_view('approve_request')
disapprove_request_view = DisapproveRequest.as_view('dispprove_request')
resolve_request_view = ResolveRequest.as_view('resolve_requeest')

#url rules for user_requests
user_requests.add_url_rule("/api/v1/users/requests",  view_func=user_requests_view, methods=['POST', 'GET'])
user_requests.add_url_rule("/api/v1/users/requests/<requestid>",  view_func=user_requests_view, methods=['GET'])
user_requests.add_url_rule("/api/v1/users/requests/<requestid>",  view_func=user_requests_view, methods=['PUT'])

#url rules for admin actions
user_requests.add_url_rule("/api/v1/requests",  view_func=admin_actions_view, methods=['GET'])
user_requests.add_url_rule("/api/v1/requests/<requestid>/approve",  view_func=approve_request_view, methods=['PUT'])
user_requests.add_url_rule("/api/v1/requests/<requestid>/disapprove",  view_func=disapprove_request_view, methods=['PUT'])
user_requests.add_url_rule("/api/v1/requests/<requestid>/resolve",  view_func=resolve_request_view, methods=['PUT'])