# from flask_testing import TestCase
# from run import app
# from app.models import MaintenanceRequest

# class RequestModelTest(TestCase):

#     def create_app(self):
#         return app

#     def test_create_request(self):
#         req = MaintenanceRequest("Fix iPhone", "My iPhone's screen is broken, i might need a new one", "Gideon B", "pending", 124)
#         self.assertEqual(req.title, "Fix iPhone")
#         self.assertEqual(req.description, "My iPhone's screen is broken, i might need a new one")
#         self.assertEqual(req.requester_name, "Gideon B")
#         self.assertEqual(req.request_status, "pending")
#         self.assertEqual(req.request_id, 124)