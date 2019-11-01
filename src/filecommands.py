import os
import sys


class Commands():

    # def __init__(self, user_name, password, privilege, curwd):
    #     self.user_name = user_name
    #     self.password = password
    #     self.privilege = privilege
    #     self.curwd = curwd
    #     self.rootd = os.getcwd()
    #     self.directory = ""
    #     self.filename = ""
    #     #access_rights = "user"

    def createfolder(self, user_cmd):
        cmmd = user_cmd.strip().split()
        folder = cmmd[1]
        try:
            if not os.path.exists(folder):
                os.makedirs(folder)
        except OSError:
            print('Error creating directory.' + folder)

    def changefolder(self, user_cmd):
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

    def readfile(self, user_cmd):
        cmmd = user_cmd.strip().split()
        files = cmmd[1]
        cwd = os.getcwd()
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


obj = Commands()
obj.readfile('read_file hi.txt ')
#Commands().readfile('./Socket connection/', 'my.txt')
