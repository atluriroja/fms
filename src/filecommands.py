"""
This module contains the class Commands which is for file commands given by user.
"""
import os
import sys
import time


class Commands():
    """
    A simple structure for a filecommands given by user.

    Attributes:
    -----------------
        user_name : string
            The name of the user who logged in

        password : string
            The password of the user who logged in

        privilege : string
            The privilege of the user who logged in

        pathsrc : string
            Just a string value

        admin_wrd : string
            The path specified by an admin to navigate through

        const_ad : string
            The initial current working directory of an admin

        current_wrd : string
            The path specified by a user to navigate through

        const_wrd : string
            The initial current working directory of a user

        cwd : string
            The current working directory

        num : int
            Denotes the first character in a string

        size : int
            Denotes till 100th character in a string

        files1 : int,string
            Just a value

    Methods:
    -----------------
        create_folder(user_cmd):
            Checks if the folder exists, if not creates the folder.

        change_folder(user_cmd):
            Updates the specified path and changes directory to the specified path.

        read_file(user_cmd):
            Reads 100 characters from a file every time its called.
    """

    def __init__(self, user_name, password, privilege):
        """
        Initialize the Commands.

        Parameters:
        ------------------------------------------
        user_name : string
            The name of the user who logged in

        password : string
            The password of the user who logged in

        privilege : string
            user or admin

        pathsrc : string
            Just a string value  "\\src\\users\\"

        admin_wrd : string
            The path specified by an admin to navigate through
            current working directory and pathsrc

        const_ad : string
            The initial current working directory of an admin
            current working directory and pathsrc

        current_wrd : string
            The path specified by a user to navigate through
            current working directory,pathsrc and username

        const_wrd : string
            The initial current working directory of a user\
            current working directory,pathsrc and username

        cwd : string
            The current working directory

        num : int
            Denotes the first character in a string

        size : int
            Denotes till 100th character in a string

        files1 : int,string
            Just a value 
        """
        self.user_name = user_name
        self.password = password
        self.privilege = privilege
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
        """
        Creates folder

        Checks if the folder exists, if not creates the folder.

        Parameters:
            user_cmd : string
                A create_folder command as a string with folder name.
        """
        status = ""
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
                    status = "Folder created succesfully"
                else:
                    status = "Folder already exists"

        except IndexError:
            print('Give folder name')
            status = "Folder creation failed"

        except FileNotFoundError:
            print('Folder not found')
            status = "Folder creation failed"

        except FileExistsError:
            print('Folder already exists')
            status = "Folder already exists"

        except OSError:
            print('Error creating directory.' + folder)
            status = "Folder creation failed"

        finally:
            return status

    def change_folder(self, user_cmd):
        """
        Changes to the specific folder path

        Updates the specified path and changes directory to the specified path.
        if '..' is given as the folder name its changes directory to the previous path.

        Parameters:
            user_cmd : string
                A change_folder command as a string with folder name or '..' .
        """
        status = ""
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
                    assert cwd is not self.const_wrd, "User outside its access"
                    print("You have no access beyond this folder")
                    status = "You have no access beyond this folder"
                elif cwd == self.const_ad:
                    assert cwd is not self.const_ad, "Admin outside its access"
                    print("You have no access beyond this folder")
                    status = "You have no access beyond this folder"
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
            status = "Moved to given folder succesfully"

        except IndexError:
            print('Give folder name')
            status = "Give folder name"

        except FileNotFoundError:
            print('Folder not found')
            status = "Cannot move to the folder as the given folder does not exist"

        except:
            print("Something wrong with specified directory. Exception - ",
                  sys.exc_info())
            status = "Cannot move to the folder as Something wrong with specified directory"

        finally:
            return status

    def read_file(self, user_cmd):
        """
        Reads 100 characters from a file

        First time called reads the first 100 characters from the given file.
        The consequent times called reads the next 100 characters till the end of the file.
        If nothing is given as the file name, it closes the file.
        If file is called again after closing starts reading from the first 100 characters.

        Parameters:
            user_cmd : string
                A read_file command as a string with filename.txt or empty .
        """
        status = ""
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
                        status = "The file is closed"
                        self.num = 0
                        self.size = 100
                    else:
                        string = the_file.read()[self.num:self.size]
                        print(string)
                        status = string
                        self.num += 100
                        self.size += 100

                        if len(string) < 100:
                            #string = the_file.read()[self.num:self.size]
                            # print(string)
                            the_file.close()
                            print(
                                "The whole file is read , you can try reading again")
                            self.num = 0
                            self.size = 100

        except IOError:
            print('Error.' + files)
            status = "File cannot be read due to error."

        finally:
            return status

    def write_file(self, cmd):
        """As it is called ,opens user inputted filename ".txt" and allows
        user to write in data into the file. If the filename".txt" doesn't
        exist it is created. If user input is empty text it clears the whole file.

        Parameters:
            user_cmd : string
                A write_file command as a string with filename.txt or empty .
        """
        try:
            if self.privilege == "admin":
                follow = self.admin_wrd
            else:
                follow = self.current_wrd

            if os.path.exists(follow):
                os.chdir(follow)
                cmmd = cmd.strip().split()
                newfile = cmmd[1]
                if len(cmmd) == 2:
                    with open(newfile, 'w') as file1:
                        file1.write(" ")
                    file1.close()
                else:
                    content1 = cmmd[2:]
                    content = ' '.join(content1)
                    with open(newfile, 'a') as file1:
                        file1.write("\n" + content)
                    file1.close()

        except IOError:
            print('Error.' + file1)

    def list(self, cmd):
        """
        list
        Allows the user to find list of files and folders in current working directory.
        With information of their size with time and date of creation.
        """
        if self.privilege == "admin":
            follow = self.admin_wrd
        else:
            follow = self.current_wrd

        if os.path.exists(follow):
            os.chdir(follow)
            directory = os.listdir(follow)
            for entry in directory:
                date1 = time.ctime(os.path.getctime(entry))
                print(f'{entry}\t Created: {date1} \tSize: {os.path.getsize(entry)}')
                return f'{entry}\t Created: {date1} \tSize: {os.path.getsize(entry)}'

    def getUserName(self):
        return self.user_name
