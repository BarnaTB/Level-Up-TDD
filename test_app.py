import unittest
from app import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(
            'Barnabas Tumuhairwe', 'Barna', 'barna@gmail.com', '3', 'password'
        )
        self.legit_user = User(
            'Barnabas Tumuhairwe', 'Barna', 'barna@gmail.com', 21, 'P@ss123'
        )
        self.registered_user = self.legit_user.register_user()

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

    def test_register_user(self):
        """Test a user can register successfully"""
        self.assertEqual(
            self.legit_user.register_user(),
            'User Barna has been registered successfully!'
        )

    def test_login_user(self):
        """Test user can login successfully"""
        self.assertEqual(
            self.legit_user.register_user(),
            'User Barna has been registered successfully!'
        )
        self.assertEqual(
            self.legit_user.login_user('Barna', 'P@ss123'),
            'You are logged in now'
        )

    def test_fetch_all_info(self):
        """
        Test that a user can fetch all their information on the application
        """
        self.assertEqual(
            self.legit_user.register_user(),
            'User Barna has been registered successfully!'
        )
        self.assertEqual(
            self.legit_user.login_user('Barna', 'P@ss123'),
            'You are logged in now'
        )

        self.assertEqual(self.legit_user.fetch_all_info('Barna'), '''Name: Barnabas Tumuhairwe,\
 Username: Barna,\
 Email: barna@gmail.com,\
 Age: 21''')
