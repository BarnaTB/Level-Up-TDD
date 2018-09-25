import unittest
from app import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(
            'Barnabas Tumuhairwe', 'Barna', 'barna@gmail.com', '3', 'password'
            )

    def test_creation(self):
        """Test the class is created"""
        self.user

    def test_validate_email(self):
        """Test a valid email is valid"""
        self.assertEqual(self.user.validate_email(), True)

    def test_validate_password(self):
        """Test a password is valid"""
        self.assertEqual(self.user.validate_password(), False)

    def test_validate_user_names(self):
        """
        Test that user names are not equal to each other and are not
        less than 4 characters long.
        """
        self.assertEqual(self.user.validate_user_names(), True)

    def test_validate_age(self):
        """Test that a user's age is an integer greater or equal to 0."""
        self.assertEqual(self.user.validate_age(), False)
