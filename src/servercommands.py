"""
This module contains the class ServerCommands, for user authentication and registration.
"""
import json
import os

class ServerCommands:
    """
    A simple structure for authentication and registration of user.

     Attributes:
    -----------------

    Methods:
    -----------------
        register(user):
            Function to register a user.

        login(user):
            Function to authenticate the user.
    """
    def register(self, user_cmd):
        """login user.

        Check if the user exists in file system.

        If user does not exists, register the user in the file system.
        Create a user folder and add credentials.

        Parameters:
            user : string
                A string variable containing a user name to delete.
        """
        if self.validate_input(user_cmd):
            args = user_cmd.split()
            user_name = args[1]
            password = args[2]
            privilege = args[3]
            my_dict = {'users':[]}
            user = {'user_name':user_name, 'password':password, 'privilege':privilege}
            credentials_file = os.path.join(os.getcwd(), 'src\\credentials.json')
            try:
                with open(credentials_file, 'r') as file:
                    my_dict = json.load(file)

                for i in my_dict['users']:
                    if i['user_name'] == user_name:
                        print("User Registration Failed, user already exists")
                        return 'User already exists'
                path = os.path.join(os.getcwd(), 'src\\users\\'+user_name)

                if os.path.exists(path):
                    print("User registration failed, directory already exists")
                    return "User registration failed"

                my_dict['users'].append(user)
                with open(credentials_file, 'w') as file:
                    json.dump(my_dict, file)
                os.mkdir(path)
                return "Registered successfully, please login with the login command"
            except OSError:
                print("Creation of the user failed")
                return "User Registration Failed"
        else:
            return "Invalid command, register <user_name> <password> <privileage>"

    def validate_input(self, user_cmd):
        args = user_cmd.strip().split()
        if(len(args) != 4 or args[0] != 'register' or args[3] not in ['admin', 'user']):
            return False
        return True

    def login(self, user_cmd):
        """login user.

        Check if the user exists in file system.

        If any user exists, validate the credentials.

        Parameters:
            user : string
                A string variable containing a user name to delete.
        """
        result = {"status":"Failure", "message":"", "user":{}}
        args = user_cmd.strip().split()
        if(len(args) != 3 or args[0] != 'login'):
            return "Invalid Command"
        user_name = args[1]
        password = args[2]
        credentials_file = os.path.join(os.getcwd(), 'src\\credentials.json')
        my_dict = {'users':[]}

        try:
            with open(credentials_file, 'r') as file:
                my_dict = json.load(file)
            for i in my_dict['users']:
                if i['user_name'] == user_name and i['password'] == password:
                    result['status'] = 'Success'
                    result['user'] = i
                    result['message'] = "Successfully logged in"
                    break
            else:
                result['message'] = 'Invalid credentials'
        except OSError:
            print("Login failed for the user:")
            result['message'] = 'User login failed'
        return result
        