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
        fetch_a_single_user = ("SELECT * from user_table where email = '{}'" .format(email))        
        self.cursor.execute(fetch_a_single_user)
        user_email = self.cursor.fetchone()
        return user_email

    def create_new_request(self, request_id, title, desc, requester_name, request_status):
        create_new_request_command = ("INSERT INTO USER_REQUESTS VALUES ('{}', '{}', '{}', '{}', '{}')" .format(request_id, title, desc, requester_name, request_status))
        self.cursor.execute(create_new_request_command)





   