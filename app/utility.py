
class ValidateRequestData:
    """ class to validate request deatails entered by users """

    def validate_request_creation(self, req_title, req_desc, requester_name, req_status):
        """ Function to validdate data entered while creating a request """
        if not req_title or req_title == "":
            return {"msg": "Misssing request title"}
        if not req_desc or req_desc == "":
            return {"msg": "Misssing request description"}
        if not requester_name or requester_name == "":
            return {"msg": "Misssing request owner"}
        if not req_status or req_status == "":
            return {"msg": "Misssing request status"}

    def validate_request_id(self, request_id):
        """ function to validate the request id entered """
        try:
            int(request_id)
        except:
            return {"msg": "invalid request id"}

    def validate_edit_request_data(self, req_title, req_desc):
        """ function to validate the new data being entered by a user """
        if not req_title or req_title == "":
            return {"msg": "Misssing request title"}
        if not req_desc or req_desc == "":
            return {"msg": "Misssing request description"}
