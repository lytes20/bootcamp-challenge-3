import psycopg2
from pprint import pprint

#TODO: create new user, login user,
#TODO: Create new request, fetch all requests, fetch user requests, fetch a single request

class dbConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname = d3c948urar7lgr user=svqtcjjrkmjmxs password=bc43b8ad99fed7cc7fc5c7121e69b5175de6303d93e4c6fdd3a8b0ce1498713c host=ec2-23-21-171-249.compute-1.amazonaws.com port =5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("made connection")
        except:
            pprint("can connect to the database")

    def create_new_user(self, user_id, name, email, password, is_admin):
        create_new_user_command = ("INSERT INTO USERS VALUES ('{}', '{}', '{}', '{}', '{}')" .format(user_id, name, email, password, is_admin))
        self.cursor.execute(create_new_user_command)

    def get_user_by_email(self, email):  
        self.cursor.execute("SELECT * from USERS where email = '{}'" .format(email))
        user_email = self.cursor.fetchone()
        return user_email

    def create_new_request(self, request_id, title, request_desc, requester_name, request_status):
        create_new_request_command = ("INSERT INTO USER_REQUESTS VALUES ('{}', '{}', '{}', '{}', '{}')" .format(request_id, title, request_desc, requester_name, request_status))
        self.cursor.execute(create_new_request_command)

    def get_a_single_user_request(self, request_id):
        """ function to retrieve a single request from the database for a logged in user"""
        self.cursor.execute("SELECT * FROM user_requests WHERE request_id = '{}'" .format(request_id))
        req = self.cursor.fetchall()
        if not req:
            return {"msg": "request doesn't exist"}
        return req

    def get_a_user_requests(self, username):
        """ function to fetch all requests for a signed in user """
        self.cursor.execute("SELECT * FROM user_requests WHERE request_owner = '{}'" .format(username))
        req = self.cursor.fetchall()
        if not req:
            return {"msg": "No requests yet"}
        return req
        
    def update_user_request(self, title, request_desc, request_id):
        update_command = ("UPDATE user_requests SET request_title='{}', request_request_desc='{}' where request_id='{}'" .format(title, request_desc, int(request_id)))
        self.cursor.execute(update_command)

    def get_all_app_requests(self):
        self.cursor.execute("SELECT * from user_requests")
        all_rows = self.cursor.fetchall()
        return all_rows

    def update_request_status(self, request_id, request_status):
        update_command = ("UPDATE user_requests SET request_status='{}' where request_id='{}'" .format(request_status, int(request_id)))
        self.cursor.execute(update_command)

class createTables(dbConnection):
    """This class does database transactions for requests"""

    def __init__(self):
        self.instance = dbConnection.__init__(self)

    def create_users_table(self):
        try:
            self.cursor.execute(
                "CREATE TABLE users (id serial PRIMARY KEY, username varchar(100) UNIQUE, email varchar(100), password varchar(100), isadmin boolean);")
            self.connection.commit()
            pprint("Successfully created user table")
        except:
            pprint("We have an error in creating user table")
            pass

    def create_requests_table(self):
        try:
            self.cursor.execute(
                "CREATE TABLE user_requests (id serial PRIMARY KEY, request_id int, title varchar(100), request_desc text, requester_name varchar(100), request_status varchar(20));")
            self.connection.commit()
            pprint("Succesfully created  requests table")
        except:
            pprint("We have an error in creating requests table")
            pass

    def drop_tbs(self):
        try:
            self.cursor.execute("DROP TABLE USERS;")
            self.cursor.execute("DROP TABLE USER_REQUESTS;")
            self.connection.commit()
        except:
            pass

    
createTables().create_requests_table()
createTables().create_users_table()



   