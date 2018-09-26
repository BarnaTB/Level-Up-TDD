import re


class User:
    def __init__(self, *args):
        self.name = args[0]
        self.username = args[1]
        self.email = args[2]
        self.age = args[3]
        self.password = args[4]
        self.is_active = False
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

    def validate_user_names(self):
        """
        Method validates that the username and name of the user are not
        less than 4 characters long and are not not equal to each other.

        :returns:

        True - if the username is not equal to the name or if they are not
        less than 4 characters long.

        False - if the username is equal to the name or if they are
        less than 4 characters long.
        """
        if self.username == self.name and len(self.username) < 4 and\
                len(self.name) < 4:
            return False
        else:
            return True

    def validate_age(self):
        """
        Method checks that the user's age is an integer greater or equal to 0.

        :returns:

        True - if the age of the user is an integer greater or equal to 0.

        False - if the age of the user is not an integer that is greater than
        0.
        """
        if not isinstance(self.age, int) or self.age < 0:
            return False
        else:
            return True

    def register_user(self):
        """
        Method registers a user using their username, name, age, password and
        email.

        :returns:

        A success message upon the succesfull registration of the user.
        """
        user = dict(
            name=self.name,
            username=self.username,
            email=self.email,
            password=self.password,
            age=self.age,
            active=self.is_active
        )
        if not self.validate_age():
            return 'You age cannot be a negative number or a string!'
        if not self.validate_email():
            return 'Invalid email! Email should in the form - johndoe@mail.com'
        if not self.validate_password:
            return 'Password should contain an uppercase, lowercase and a\
                number character and be at least 4 characters long!'
        if not self.validate_user_names:
            return 'Your username cannot be the same as your name and less\
                than 4 characters long!'
        else:
            self.users.append(user)
            return 'User {0} has been registered\
 successfully!'.format(self.username)

    def login_user(self, username, password):
        """
        Method logs in a user to their account.

        :returns:

        True for the value of is_active
        """
        for user in self.users:
            if username not in user['name']:
                return 'Sorry this user does not exist!'
            if user['username'] == username and user['password'] == password:
                self.is_active = True
                return 'You are logged in now'
            else:
                return 'Sorry wrong email or password!'

    def fetch_all_info(self, username):
        """
        Method checks all a user's information on the platform and returns it.

        :returns:

        A list of all a user's information.
        """
        for user in self.users:
            if username not in user.keys():
                return 'Sorry, this user does not exist!'
            if user['username'] == username and user['is_active'] is False:
                return 'Please log in first!'
            return '''Name: {0},
                    Username: {1},
                    Email: {2},
                    Age: {3}
                    '''.format(
                user['name'], user['username'],
                user['email'], user['age'])
