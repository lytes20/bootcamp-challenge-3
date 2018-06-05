from flask_testing import TestCase
from app import app
import json


class AuthTest(TestCase):
    """ class to test user authentication """
    def create_app(self):
        return app

    def test_register_user(self):
        """ Test for successful user register """
        with self.client:
            response = self.client.post(
                "api/v1/user/register",
                content_type='application/json',
                data=json.dumps(dict(username="Gideon B", email="email@email.com", password="secret"))
                )            
            self.assertEqual(response.status_code, 200)


    def test_user_login_successfully(self):
        """ Test for login end point """
        with self.client:
            res = self.client.post(
                "api/v1/user/register",
                content_type='application/json',
                data=json.dumps(dict(username="Gideon B", email="email@email.com", password="secret"))
                )
            self.assertEqual(res.status_code, 200)
            
            response = self.client.post(
                "api/v1/user/login",
                content_type='application/json',
                data=json.dumps(dict(email="email@email.com", password="secret"))
                )            
            
            self.assertEquals(response.status_code, 200)