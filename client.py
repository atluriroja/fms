import asyncio


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
        writer.write(message.encode())
        data = await reader.read(100)
        print(f'Received: {data.decode()}')
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
          
async def quit():
    pass
asyncio.run(tcp_echo_client())
