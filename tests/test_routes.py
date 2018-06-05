"""
This file contains tests for the app.py file that contains my api endpoints
"""
from flask_testing import TestCase
from app import app
import json

class TestRun(TestCase):

    def create_app(self):
        return app

    def test_create_request(self):
        """ test create user request endpoint """
        with self.client:
            response = self.client.post("/api/v1/users/requests", content_type='application/json',
                                        data=json.dumps(dict(
                                            request_title="Fix iphone", 
                                            request_description="iphone screen needs fixing",
                                            requester_name="Gideon B",
                                            request_status="pending",
                                            req_id=1)))
            self.assertEquals(response.status_code, 200)

    def test_fetch_requests(self):
        """ test fetch all user requests endpoint """
        with self.client:
            response = self.client.get("/api/v1/users/requests")        
            self.assertEquals(response.status_code, 200)

    def test_fetch_a_request(self):
        """ test for fetching a single request for a logged in user"""
        with self.client:
            response = self.client.get("/api/v1/users/requests/1")
            self.assertEquals(response.status_code, 200)

    def test_edit_request(self):
        """ test for edit a request for a logged in user"""
        with self.client:
            response = self.client.put(
                "/api/v1/users/requests/1",
                content_type='application/json',
                data=json.dumps(dict(
                    request_title="Fix Car",
                    request_description="Car wind shield needs fixing"))
                    )
        self.assertEquals(response.status_code, 200)

    def test_fetch_all_app_requests(self):
        """ test for fetch all requests on the app endpoint """
        with self.client:
            response = self.client.get("/api/v1/requests")
            self.assertEquals(response.status_code, 200)

    def test_approve_a_request(self):
        """ test for approve a request endpoint"""
        pass