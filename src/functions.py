import os
import sys


class Commands():

    def __init__(self, directory, filename):
        self.directory = self.directory
        self.filename = self.filename
        #access_rights = "user"

    def createfolder(self):
        try:
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
        except OSError:
            print('Error creating directory.' + self.directory)

    def changefolder(self):
        cwd = os.getcwd()
        try:
            os.chdir(self.directory)
            print("Inserting inside-", os.getcwd())

        except:
            print("Something wrong with specified directory. Exception - ",
                  sys.exc_info())

        finally:
            print("Restoring the path")
            os.chdir(cwd)
            print("Current directory is-", os.getcwd())

    def readfile(self):
        cwd = os.getcwd()
        print(cwd)
        try:
            f = open(self.filename, "r")
            print(f.read())
            if self.directory == cwd:
                print(f.read())
                # print(contents[0:100])
        except IOError:
            print('Error.' + self.filename)


#Commands().readfile('./Socket connection/', 'my.txt')
