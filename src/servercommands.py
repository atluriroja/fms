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
        register(command):
            used to register the user.

        login(user_name, password):
            Function to authenticate the user.
    """
    def register(self, cmd):
        """register user.

        Check if the user exists in file system.

        If user does not exists, register the user in the file system.
        Create a user folder and add credentials.

        Parameters:
            cmd : string
                A register command as a string with user name, password and privileage details.
        """
        args = cmd.strip().split()
        if(len(args) != 4 or args[0] != 'register' or args[3] not in ['admin', 'user']):
            return "Invalid command, register <user_name> <password> <privileage>"

        user_name = args[1]
        password = args[2]
        privilege = args[3]
        my_dict = {'users':[]}
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

            user = {'user_name':user_name, 'password':password, 'privilege':privilege}
            my_dict['users'].append(user)

            with open(credentials_file, 'w') as file:
                json.dump(my_dict, file)
            os.mkdir(path)
            return "Registered successfully, please login.."
        except OSError:
            print("Creation of the user failed")
            return "User Registration Failed"

    def login(self, user_name, password):
        """login user.

        Check if the user exists in file system.

        If any user exists, validate the credentials.

        Parameters:
            user : string
                A string variable with a user name.
            password : string
                A string variable with a user password.
        """
        result = {"status":"Failure", "message":"", "user":{}}
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
        