import os
import sys


class Commands:
    def createfolder(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error creating directory.' + directory)

    def changefolder(self, directory):
        cwd = os.getcwd()
        try:
            os.chdir(directory)
            print("Inserting inside-", os.getcwd())

        except:
            print("Something wrong with specified directory. Exception - ",
                  sys.exc_info())

        finally:
            print("Restoring the path")
            os.chdir(cwd)
            print("Current directory is-", os.getcwd())

    def readfile(self, directory, filename):
        cwd = os.getcwd()
        print(cwd)
        try:
            f = open(filename, "r")
            print(f.read())
            if directory == cwd:
                print(f.read())
                # print(contents[0:100])
        except IOError:
            print('Error.' + filename)


#Commands().readfile('./Socket connection/', 'my.txt')
