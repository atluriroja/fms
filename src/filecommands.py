""" hi """
import os
import sys
import datetime
import time
from path import Path


class Commands():
    """ hi """

    def __init__(self, user_name, password, privilege):
        """ hi """

        self.user_name = user_name
        self.password = password
        self.privilege = privilege
        self.curwd = user_name
        self.rootd = user_name
        self.pathsrc = "\\src\\users\\"
        self.admin_wrd = os.getcwd()+self.pathsrc
        self.const_ad = os.getcwd()+self.pathsrc
        self.current_wrd = os.getcwd() + self.pathsrc + user_name
        self.const_wrd = os.getcwd() + self.pathsrc + user_name
        self.cwd = os.getcwd()
        self.num = 0
        self.size = 100
        self.files1 = 0

    def create_folder(self, user_cmd):
        """ hi """

        try:
            cmmd = user_cmd.strip().split()
            folder1 = cmmd[1:]
            folder = '_'.join(folder1)
            if self.privilege == "admin":
                follow = self.admin_wrd
            else:
                follow = self.current_wrd

            if os.path.exists(follow):
                os.chdir(follow)

                if not os.path.exists(folder):
                    os.makedirs(folder)

        except IndexError:
            print('Give folder name')

        except FileNotFoundError:
            print('Folder not found')

        except OSError:
            print('Error creating directory.' + folder)

    def change_folder(self, user_cmd):
        """ hi """

        try:
            cmmd = user_cmd.strip().split()
            folder1 = cmmd[1:]
            folder = '_'.join(folder1)

            if self.privilege == "admin":
                follow = self.admin_wrd
            else:
                follow = self.current_wrd
            cwd = follow
            cwd1 = cwd.rsplit('\\', 1)[0]

            if folder == '..':
                if cwd == self.const_wrd:
                    print("You have no access beyond this folder")
                elif cwd == self.const_ad:
                    print("You have no access beyond this folder")
                else:
                    follow = cwd1

                    if self.privilege == "admin":
                        self.admin_wrd = follow
                    else:
                        self.current_wrd = follow

                    os.chdir(follow)
            else:
                follow += "\\" + folder

                if self.privilege == "admin":
                    self.admin_wrd = follow
                else:
                    self.current_wrd = follow

                os.chdir(follow)
            print("Inserting inside-", follow)

        except IndexError:
            print('Give folder name')

        except FileNotFoundError:
            print('Folder not found')

        except:
            print("Something wrong with specified directory. Exception - ",
                  sys.exc_info())

    def read_file(self, user_cmd):
        """ hi """

        try:
            if self.privilege == "admin":
                follow = self.admin_wrd
            else:
                follow = self.current_wrd

            if os.path.exists(follow):
                os.chdir(follow)
                cmmd = user_cmd.strip().split()
                the_file1 = 0
                if len(cmmd) == 1:
                    the_file1 = None
                else:
                    files = cmmd[1]
                    self.files1 = files
                with open(self.files1, 'r') as the_file:
                    if the_file1 is None:
                        the_file.close()
                        print("The file is closed")
                        self.num = 0
                        self.size = 100
                        the_file1 = 0
                    else:
                        string = the_file.read()[self.num:self.size]
                        print(string)
                        self.num += 100
                        self.size += 100

                        if len(string) < 100:
                            string = the_file.read()[self.num:self.size]
                            print(string)
                            the_file.close()
                            print(
                                "The whole file is read , you can try reading again")
                            self.num = 0
                            self.size = 100

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
