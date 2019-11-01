import os
from path import Path
import datetime
import time

"""path for client folder"""
root='E:\\Ass3\\fms\\client'
def listDir(path):
    
    """check current working directory"""
    cwd=os.getcwd()
    """move to current working directory"""
    cwd=Path(path)
    """current working directory"""

    directory = os.listdir(path)
    """initiaalizing files and directories 
    in current working directory"""
    for d in directory:
        folder_path=os.path.join(d)
        print(d)

    """initializing file size in 
     the current working directory"""
    for file in cwd.files():
        """path for current working directory"""
        folder_path=os.path.join(file)
        """date & time of creating files 
        current working directory"""
        last_Mod=os.stat(file).st_ctime
        """size of the files in the current directory"""
        size=os.stat(file).st_size
        print(folder_path)
        print("Size:",size)
        print(datetime.datetime.strptime(time.ctime(last_Mod),"%a %b %d %H:%M:%S %Y"))



def new():
    # asks user for filename
    newfile = input("Insert 'newfile.txt' >>> ")
    #clear_files=[]
 
    # opens user inputted filename ".txt" and (w+) makes new and writes
    with open(newfile, 'w') as f:
        # asks for user input to enter into the file
        user_input = input("user input >>> ")
        # writes user input to the file and adds new line
        if user_input==[]:
            f.write("")
            #return(clear_files)
    
        elif user_input!=[]:
           f.write(user_input)
        
        f.write("\n")
    return new
    
            
           
listDir(root)

