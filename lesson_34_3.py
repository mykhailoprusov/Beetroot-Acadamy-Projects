import asyncio
import socket

HOST = '127.0.0.1'
PORT = 40000


async def handle_client(connection,address):
    print('Connected by ',address)

    with connection as conn:
        info = b'HII'
        conn.sendto(info, address)



async def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        print('Before listening')

        s.listen()
        print('After listening')

        conn, addr = s.accept()


        task = asyncio.create_task(handle_client(conn,addr))
        await task


asyncio.run(main())