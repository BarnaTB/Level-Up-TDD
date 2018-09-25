import re


class User:
    def __init__(self, name, username, email, age, password):
        self.name = name
        self.username = username
        self.email = email
        self.age = age
        self.password = password
        self.users = []

    def validate_email(self):
        """
        Method to validate user email(e.g johndoe@gmail.com)

        :returns:

        True - if the email matches the required attributes of a valid email.

        False - if the email doesn't match the required attributes of a valid 
        email.
        """
        if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return False
        else:
            return True
