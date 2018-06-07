import psycopg2
from pprint import pprint

#TODO: create new user, login user,
#TODO: Create new request, fetch all requests, fetch user requests, fetch a single request

class dbConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname = demo user=postgres password=Bamela@20 host=localhost port =5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("made connection")
        except:
            pprint("can connect to the database")

    def create_new_user(self, user_id, name, email, password, is_admin):
        create_new_user_command = ("INSERT INTO USER_TABLE VALUES ('{}', '{}', '{}', '{}', '{}')" .format(user_id, name, email, password, is_admin))
        self.cursor.execute(create_new_user_command)

    def get_user_email(self, email):  
        self.cursor.execute("SELECT * from user_table where email = '{}'" .format(email))
        user_email = self.cursor.fetchone()
        return user_email

    def create_new_request(self, request_id, title, desc, requester_name, request_status):
        create_new_request_command = ("INSERT INTO USER_REQUESTS VALUES ('{}', '{}', '{}', '{}', '{}')" .format(request_id, title, desc, requester_name, request_status))
        self.cursor.execute(create_new_request_command)

    def get_a_single_user_request(self, request_id):
        """ function to retrieve a single request from the database for a logged in user"""
        self.cursor.execute("SELECT * FROM user_requests WHERE request_id = '{}'" .format(request_id))
        req = self.cursor.fetchall()
        return req

    def get_a_user_requests(self, username):
        self.cursor.execute("SELECT * FROM user_requests WHERE request_owner = '{}'" .format(username))
        req = self.cursor.fetchall()
        return req

    def get_all_app_requests(self):
        self.cursor.execute("SELECT * from user_requests")
        all_rows = self.cursor.fetchall()
        return all_rows

    def update_request_status(self, request_id):
        self.cursor.execute()
    




   