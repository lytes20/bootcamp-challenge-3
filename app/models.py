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