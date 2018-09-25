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

    def validate_password(self):
        """
        Method to check that a password contains uppercase, lowercase and
        number characters. Also checks that a password is longer than four
        characters.

        :returns:

        True - if the password contains all required characters and is 4 or
        more characters long.

        False - if the password doesn't contain the required characters and
        is not 4 or more characters long.
        """
        low = re.search(r"[a-z]", self.password)
        up = re.search(r"[A-Z]", self.password)
        num = re.search(r"[0-9]", self.password)
        if not all((low, up, num)) or len(self.password) < 4:
            return False
        else:
            return True
