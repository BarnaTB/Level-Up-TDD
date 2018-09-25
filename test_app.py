import unittest
from app import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(
            'Barnabas Tumuhairwe', 'Barna', 'barna@gmail.com', 30, 'password'
            )

    def test_creation(self):
        """Test the class is created"""
        self.user

    def test_validate_email(self):
        """Test a valid email is allowed"""
        self.assertEqual(self.user.validate_email(), True)
