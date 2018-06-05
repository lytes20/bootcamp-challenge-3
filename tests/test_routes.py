"""
This file contains tests for the app.py file that contains my api endpoints
"""
from flask_testing import TestCase
from app import app
import json

class TestRun(TestCase):

    def create_app(self):
        return app

    def test_create_request(self): #req_title, req_desc, requester_name, req_id
        with self.client:
            response = self.client.post("/api/v1/users/requests", content_type='application/json',
                                        data=json.dumps(dict(
                                            request_title="Fix iphone", 
                                            request_description="iphone screen needs fixing",
                                            requester_name="Gideon B",
                                            request_status="pending",
                                            req_id=1)))
            self.assertEquals(response.status_code, 200)