import asyncio
import signal
from src.servercommands import ServerCommands
from src.filecommands import Commands
from src.admincommands import AdminCommands

session = []
signal.signal(signal.SIGINT, signal.SIG_DFL)

async def handle_echo(reader, writer):

    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected !!!!"

    cmd_list = ['register', 'login', 'create_folder', 'read_file',
                'write_file', 'change_folder', 'list', 'delete', 'exit']
    user = None
    send_msg = ''

    while True:
        data = await reader.read(100)
        message = data.decode().strip()

        print(f"Received command {message} from {addr}")

        if(message == '' or message.split()[0] not in cmd_list):
            send_msg = 'Invalid command'
        elif message == 'exit' or message == 'quit':
            break
        elif message.startswith('register'):
            send_msg = ServerCommands().register(message)
        elif message.startswith('login'):
            result = ServerCommands().login(message)
            if(result['status'] == 'Success'):
                session.append(message.split()[1])
                x = list(result['user'].values())
                if(x[2] == 'admin'):
                    user = AdminCommands(x[0],x[1],x[2])
                else:
                    user = Commands(x[0],x[1],x[2]) 
            send_msg=result['message'] 
        elif user != None and message.startswith('create_folder'):
            user.create_folder(message)
        elif user != None and message.startswith('read_file'):
            user.read_file(message)
        elif user != None and message.startswith('write_file'):
            user.write_file(message)
        elif user != None and message.startswith('change_folder'):
            user.change_folder(message)
        elif user != None and message.startswith('list'):
             send_msg = user.list(message)
        elif user != None and message.startswith('delete'):
            send_msg = user.delete(message)
        else:
            print("invalid command")
            
        print(f"Send: {send_msg}")
        writer.write(('\n'+send_msg).encode())
        await writer.drain()

    print("Close the connection")
    if user != None:
        session.remove(user.user_name)
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
