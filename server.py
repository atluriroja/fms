import asyncio
import signal
from src.servercommands import ServerCommands
signal.signal(signal.SIGINT, signal.SIG_DFL)

async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected !!!!"
    print(message)
    while True:
        data = await reader.read(100)
        message = data.decode().strip()
        print(f"Received {message} from {addr}")
        if message == 'quit':
            break
        elif message.startswith('register'):
            message = ServerCommands().register(message)
        elif message.startswith('login'):
            message = ServerCommands().login(message)
        elif message.startswith('create_folder'):
            pass
        elif message.startswith('read_file'):
            pass
        elif message.startswith('write_file'):
            pass
        elif message.startswith('change_folder'):
            pass
        elif message.startswith('list'):
            pass
        elif message.startswith('delete'):
            pass
        else:
            print("invalid command")
        print(f"Send: {message}")
        writer.write(data + '\n'.encode())
        #writer.write(message)
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