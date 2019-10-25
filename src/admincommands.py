import os
import sys
import json
from src.filecommands import Commands
class AdminCommands(Commands):
    
    def __init__(self, user_name, password, privilage, curwd):
       Commands.__init__(self, user_name, password, privilage, curwd) 
  
    def delete(self, cmd):
        args = cmd.strip().split()
        if (len(args) != 3 or args[0] != 'delete'):
            return "Invalid Command"
        elif self.password != args[1]:
            return "Invalid password"
             
        credentials_file = os.path.join(os.getcwd(), 'src\\credentials.json')
        is_user_exists = False
        #my_dict = {'users':[]}
        with open(credentials_file, 'r') as file:
            my_dict = json.load(file)
            for i in my_dict['users']:
                if i['user_name'] == args[1]:
                    is_user_exists = True
                    del my_dict[i]
                    with open(credentials_file, 'w') as file: 
                        json.dump(my_dict, file)
                    try:
                        path = os.path.join(credentials_file, 'src\\users\\'+args[1])
                        os.rmdir(path)
                        print ("Successfully deleted the user %s" % path)
                        
                    except OSError:
                        print ("Deletion of the user %s failed")
                    
                    break
            if not is_user_exists: return "Invalid username"            
        