import os
import shutil
import sys
import json
from src.filecommands import Commands


class AdminCommands(Commands):

    def __init__(self, user_name, password, privilage):
        Commands.__init__(self, user_name, password, privilage)

    def delete(self, cmd):
        args = cmd.strip().split()
        if (len(args) != 3 or args[0] != 'delete'):
            return "Invalid Command"
        elif self.password != args[2]:
            return "Invalid password"

        credentials_file = os.path.join(os.getcwd(), 'src\\credentials.json')
        is_user_exists = False
        my_dict = {'users': []}
        with open(credentials_file, 'r') as file:
            my_dict = json.load(file)
            for i in my_dict['users']:
                if i['user_name'] == args[1]:
                    is_user_exists = True
                    my_dict['users'].remove(i)
                    with open(credentials_file, 'w') as file:
                        json.dump(my_dict, file)
                    try:
                        path = os.path.join(
                            os.getcwd(), 'src\\users\\'+args[1])
                        if os.path.isdir(path):
                            shutil.rmtree(dir_name)
                        return "Successfully deleted the user"
                    except:
                        return "Deletion of the user failed"

            if not is_user_exists:
                return "Invalid username"
