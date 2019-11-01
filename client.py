import asyncio
import os
from path import Path
import datetime
import time

root='E:\\Ass3\\fms\\client'


async def tcp_echo_client():
    commands_history=[] 
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    message = ''
    while True:
        message = input('>')
        commands_history.append(message)
        
        if(message.startswith('commands')):
            await commands(message, commands_history)
            #continue
        writer.write(message.encode())
        data = await reader.read(100)
        print(f'Received: {data.decode()}')

        if message == 'quit':
            break

    print('Close the connection')
    writer.close()


async def commands(value, commands_history):
    """Input availble commands with options for the user."""
     
    if value == 'commands':
        """input availble commands"""
        print("""
             change_folder <name>
             list
             read_file <name>
             write_file <name>
             input
             create_folder <name>
             register <username>  <password> <priviledges>
             login <username> <password>
             delete <username> <password>
             quit
             """)
    elif value=='commands issued':
         """Input issued by the user"""
         for i in commands_history:
             print(i)
                
    elif value == 'commands clear':
         """Clear commands"""
         commands_history==[]
         print("All the commands are cleared")
          
    else:
        """False input"""
        print("Invalid input")




async def listDir(path):
    
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



async def new():
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
    
          
asyncio.run(tcp_echo_client())
