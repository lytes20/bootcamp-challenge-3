""" 
Models script
"""
class User:
    """
    User model to be reused through out for creating instances of a user
    """
    def __init__(self, name, email, password, isAdmin=False):
        """ Creating a constructor for a user model """
        self.name = name
        self.email= email
        self.password = password
        self.isAdmin = isAdmin


class MaintenanceRequest:
    def __init__(self, title, desc, requester_name, request_status, request_id):
        """Initialise the MaintenanceRequest"""
        self.title = title
        self.description = desc
        self.requester_name = requester_name
        self.request_status = request_status
        self.request_id = request_id