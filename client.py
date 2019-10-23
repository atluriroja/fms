import asyncio


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    message = ''
    while True:
        message = input('>')
        writer.write(message.encode())
        data = await reader.read(100)
        print(f'Received: {data.decode()}')
    print('Close the connection')
    writer.close()


async def quit():
    pass


async def commands():
    pass
asyncio.run(tcp_echo_client())
