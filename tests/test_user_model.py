# from app import app
# from flask_testing import TestCase
# from app.models import User


# class UserModelTest(TestCase):

#     def create_app(self):
#         return app

#     def test_create_user(self):
#         """ Function to test that a user is created from the user model"""
#         user = User("Gideon Bamuleseyo", "gideon@mail.com", "secret")
#         self.assertEqual(user.name, "Gideon Bamuleseyo")
#         self.assertEqual(user.email, "gideon@mail.com")
#         self.assertEqual(user.password, "secret")
#         self.assertEqual(user.isAdmin, False)