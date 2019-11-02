"""
This module containing the script for the running TCP/IP server.
"""
import asyncio
import signal
from src.servercommands import ServerCommands
from src.filecommands import Commands
from src.admincommands import AdminCommands

session = []
signal.signal(signal.SIGINT, signal.SIG_DFL)

async def handle_echo(reader, writer):
    """Handles a new connection whenever a new connection is established

        Checks whether the client enters valid command
        Checks whether the user is already logged in

    Parameters:
        reader : StreamReader
            reader is StreamReader object, used to read data from client in byte streams
        writer : StreamWriter
            writer is StreamWriter object, used to write the data to the client in byte streams
    """
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected !!!!"
    print(message)
    cmd_list = ['register', 'login', 'create_folder', 'read_file',
                'write_file', 'change_folder', 'list', 'delete', 'quit']
    user = None

    while True:
        send_msg = ''
        data = await reader.read(100)
        message = data.decode().strip()

        print(f"Received command {message} from {addr}")

        if message == '':
            send_msg = 'Enter Command'
        else:
            args = message.strip().split()

            if args[0] not in cmd_list:
                send_msg = "Invalid command"
            elif args[0] == 'quit':
                if user is not None:
                    if session.count(user.user_name) > 0:
                        session.remove(user.user_name)
                break
            elif args[0] == 'register':
                send_msg = ServerCommands().register(message)
            elif  args[0] == 'login' and len(args) == 3 and user is None:

                if args[1] not in session:
                    result = ServerCommands().login(args[1], args[2])

                    if result['status'] == 'Success':
                        session.append(message.split()[1])
                        auth_user = list(result['user'].values())

                        if auth_user[2] == 'admin':
                            user = AdminCommands(auth_user[0], auth_user[1], auth_user[2])
                        else:
                            user = Commands(auth_user[0], auth_user[1], auth_user[2])

                    send_msg = result['message']
                else:
                    send_msg = "User already logged in"
            elif user is not None and message.startswith('create_folder'):
                user.create_folder(message)
            elif user is not None and message.startswith('read_file'):
                user.read_file(message)
            elif user is not None and message.startswith('write_file'):
                user.write_file(message)
            elif user is not None and message.startswith('change_folder'):
                user.change_folder(message)
            elif user is not None and message.startswith('list'):
                send_msg = user.list(message)
            elif user is not None and message.startswith('delete'):
                args = message.strip().split()
                if user.password != args[2]:
                    send_msg = "Invalid admin password"
                elif user.user_name == args[1] or user.privilege != 'admin':
                    send_msg = "You don't have privilege's to delete user"
                else:
                    send_msg = user.delete(args[1])
            else:
                print("Not Allowed")
                send_msg = args[0] + " not allowed"
        print(f"Send message to {addr}: {send_msg}")
        writer.write(('\n'+send_msg).encode())
        await writer.drain()

    print(f"Close the connection{addr}")
    writer.close()


async def main():
    """The main entry point to start the server"""
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
