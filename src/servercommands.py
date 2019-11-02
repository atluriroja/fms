from random import randrange
import json
import os


class ServerCommands:
    def register(self, user_cmd):
        if(self.validate_input(user_cmd)):
            args = user_cmd.split() 
            user_name = args[1]
            password = args[2]
            privilege = args[3]
            my_dict = {'users':[]}
            user = {'user_name':user_name,'password':password,'privilege':privilege}
            #THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            credentials_file = os.path.join(os.getcwd(), 'src\\credentials.json')
            try:
                with open(credentials_file, 'r') as file:
                    my_dict = json.load(file)
        
                for i in my_dict['users']:
                    if i['user_name'] == user_name:
                        print("User Registration Failed, user already exists")
                        return 'User already exists'
                path = os.path.join(os.getcwd(), 'src\\users\\'+user_name)
                if(os.path.exists(path)):
                    print("User Registration Failed, directory already exists")
                    return "User Registration Failed"

                my_dict['users'].append(user) 

                with open(credentials_file, 'w') as file: 
                    json.dump(my_dict, file)

                os.mkdir(path)

                return "Registered Successfully, Please login with the login command"
            except:
                print ("Creation of the user failed")
                return "User Registration Failed"                           
        else:
            return "Invalid command, register <user_name> <password> <privileage>"

    def validate_input(self, user_cmd):
        args = user_cmd.strip().split()
        if(len(args) != 4 or args[0] != 'register' or args[3] not in ['admin', 'user']):
            return False
        return True

    def login(self, user_cmd):
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
        except:
                print ("Login failed for the user:")
                result['message'] = 'User login Failed'
        return result
        
