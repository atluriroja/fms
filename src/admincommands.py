"""
This module contains the class AdminCommands, the commands class for the admin user.
"""
import os
import shutil
import json
from src.filecommands import Commands
class AdminCommands(Commands):
    """
    A simple structure for admin level commands.

    Attributes:
    -----------------

    Methods:
    -----------------
        delete(user):
            Function to delete the user.
    """
    def __init__(self, user_name, password, privilege):
        """Initialize the Commands. The parameters are passed on to the init function of super
        class

        Parameters:
        ------------------------------------------
        user_name : string
            The name of the user who logged in

        password : string
            The password of the user who logged in

        privilege : string
            The privilege of the user who logged in
        """
        super().__init__(user_name, password, privilege)

    def delete(self, user):
        """Delete user.

        Check if the user exists in file system.

        If any user exists delete the user folder and remove the user credentials.

        Parameters:
            user : string
                A string variable containing a user name to delete.
        """
        user_folder_path = os.path.join(os.getcwd(), 'src\\users\\'+user)
        if os.path.exists(user_folder_path):
            my_dict = None

            try:
                assert user != "", "User value should not be an empty string"
                credentials_file = os.path.join(os.getcwd(), 'src\\credentials.json')
                with open(credentials_file, 'r') as file:
                    my_dict = json.load(file)

                for i in my_dict['users']:
                    if i['user_name'] == user:
                        my_dict['users'].remove(i)
                        with open(credentials_file, 'w') as file:
                            json.dump(my_dict, file)

                        if os.path.isdir(user_folder_path):
                            shutil.rmtree(user_folder_path)
                        break
            except FileNotFoundError:
                print("File not found error")
                return "Deletion of the user failed"
            except OSError:
                print("OS error")
                return "Deletion of the user failed"
            except AssertionError:
                print("Deletion of the user failed")
                return "Deletion of the user failed"
            except Exception:
                print("Exception")
                return "Deletion of the user failed"
            else:
                return "Successfully deleted the user"
        else:
            return "User doesn't not exists"
            