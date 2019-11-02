import os
import shutil
import sys
import json
from src.filecommands import Commands


class AdminCommands(Commands):

    def __init__(self, user_name, password, privilege):
        super().__init__(user_name, password, privilege)

    def delete(self, user):
        user_folder_path = os.path.join(os.getcwd(), 'src\\users\\'+user)
        if os.path.exists(user_folder_path):
            my_dict = None
            try:
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
            except Exception:
                return "Deletion of the user failed"
            else:
                return "Successfully deleted the user"
        else:
            return "Username doesn't not exists"
            
