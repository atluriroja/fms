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
    cmd_list = ['register','login','create_folder','read_file','write_file','change_folder','list','delete','exit']
    print(message)
    user=[]
    send_msg = ''
    while True:
        data = await reader.read(100)
        message = data.decode().strip()
        print(f"Received command {message} from {addr}")
        if(message == '' or message.split()[0] not in cmd_list):
            send_msg = 'Invalid command'
        if message == 'exit' or message == 'quit':
            break
        elif message.startswith('register'):
            send_msg = ServerCommands().register(message)
        elif message.startswith('login'):
            send_msg = ServerCommands().login(message)
            if(send_msg == 'Success'):
                session.append(message.split()[1])
                user=(message.split()[1], message.split()[2], 'Admin', message.split()[1])
        elif user != [] and  message.startswith('create_folder'):
            pass
        elif user != [] and message.startswith('read_file'):
            pass
        elif user != [] and message.startswith('write_file'):
            pass
        elif user != [] and message.startswith('change_folder'):
            pass
        elif user != [] and message.startswith('list'):
            pass
        elif user != None and message.startswith('delete'):
            send_msg = AdminCommands(user[0], user[1], user[2], user[3]).delete(message)
        else:
            print("invalid command")
        print(f"Send: {send_msg}")
        writer.write(('\n'+send_msg).encode())
        await writer.drain()
    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
