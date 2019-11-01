import os
import sys
from path import Path
import datetime
import time


class Commands():

    def __init__(self, user_name, password, privilege):
        self.user_name = user_name
        self.password = password
        self.privilege = privilege
        self.curwd = user_name
        self.rootd = user_name
        self.pathsrc = "\\src\\users\\"
        self.current_wrd = os.getcwd() + self.pathsrc + user_name
        self.const_wrd = os.getcwd() + self.pathsrc + user_name

    def create_folder(self, user_cmd):
        cmmd = user_cmd.strip().split()
        folder = cmmd[1]
        print(self.current_wrd)
        try:
            if os.path.exists(self.current_wrd):
                if self.privilege == "Users" or "users":
                    os.chdir(self.current_wrd)

                if not os.path.exists(folder):
                    os.makedirs(folder)
        except OSError:
            print('Error creating directory.' + folder)

    def change_folder(self, user_cmd):
        cmmd = user_cmd.strip().split()
        folder = cmmd[1]
        print(folder)
        cwd = os.getcwd()
        try:
            if folder == '..':
                os.chdir(cwd)
            else:
                os.chdir(folder)
            print("Inserting inside-", os.getcwd())

        except:
            print("Something wrong with specified directory. Exception - ",
                  sys.exc_info())

        # finally:
        #     print("Restoring the path")
        #     os.chdir(cwd)
        #     print("Current directory is-", os.getcwd())

    def read_file(self, user_cmd):
        cmmd = user_cmd.strip().split()
        files = cmmd[1]
       # cwd = os.getcwd()
        try:
            f = open(files, 'r')
            string = f.read()[0:100]
            print(string)
            f.close()
            # if self.directory == cwd:
            #     print(f.read())
            #     print(contents[0:100])
        except IOError:
            print('Error.' + files)


root = 'E:\\Ass3\\fms\\client'


def list(self, path):
    """check current working directory"""
    cwd = os.getcwd()
    """move to current working directory"""
    cwd = Path(path)
    """current working directory"""

    directory = os.listdir(path)
    """initiaalizing files and directories 
    in current working directory"""
    for d in directory:
        folder_path = os.path.join(d)
        print(d)

    """initializing file size in 
     the current working directory"""
    for file in cwd.files():
        """path for current working directory"""
        folder_path = os.path.join(file)
        """date & time of creating files 
        current working directory"""
        last_Mod = os.stat(file).st_ctime
        """size of the files in the current directory"""
        size = os.stat(file).st_size
        print(folder_path)
        print("Size:", size)
        print(datetime.datetime.strptime(
            time.ctime(last_Mod), "%a %b %d %H:%M:%S %Y"))
        return ""


def write_file():
    # asks user for filename
    newfile = input("Insert 'newfile.txt' >>> ")
    # clear_files=[]

    # opens user inputted filename ".txt" and (w+) makes new and writes
    with open(newfile, 'w') as f:
        # asks for user input to enter into the file
        user_input = input("user input >>> ")
        # writes user input to the file and adds new line
        if user_input == []:
            f.write("")
            # return(clear_files)

        elif user_input != []:
            f.write(user_input)

        f.write("\n")
    return ""
