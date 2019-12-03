import asyncio

commands_history = []

"""
   A TCP client function, establish the connection with the server to handle the user 
   commands and closes the connection on quit.   
"""
async def tcp_echo_client():
    
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8000)
    print(reader)
    assert reader is not None, "Server doesn't return a Asyncio StreamReader object "
    assert writer is not None, "Server doesnt rerurn a Asyncio Streamwriter object"
    message = ''
    while True:
        message = input('>>')
        commands_history.append(message)

        if(message.startswith('commands')):
            await commands(message, commands_history)
            continue
        writer.write(message.encode())
        data = await reader.read(100)
        print(f'Received: {data.decode()}')

        if message == 'quit':
            break

    print('Close the connection')
    writer.close()

"""
    Checks if the user inputs valid command arguments/value.

    If invalid argument, error message is displayed.
    if no arguments, displays all the available commands
    if the argument is 'issued', displays all the list of commands excuted.
    if the arguments is 'clear', clears all the previous history of commands
        
    Parameters:
        value : string
            A value is a 'commands' command as a string with or without arguments.
        commands_history : list
            A commands_history is a list contains all the commands that user has sent.
"""
async def commands(value, commands_history):

    if value == 'commands':
        """Print all the available commands"""
        print("""
             Available Commands:
             change_folder <name>
             list
             read_file <name>
             write_file <name>
             input
             create_folder <name>
             register <username> <password> <priviledges>
             login <username> <password>
             delete <username> <password>
             quit
             """)
    elif value == 'commands issued':
        """commands issued by the user"""
        for i in commands_history:
            print(i)

    elif value == 'commands clear':
        """Clear commands"""
        commands_history.clear()
        print("All the commands are cleared")

    else:
        """False input"""
        print("Invalid input")

asyncio.run(tcp_echo_client())
