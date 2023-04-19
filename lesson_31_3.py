import multiprocessing
import socket

HOST = '127.0.0.1'
PORT = 47047

def handle_client(connection,address):
    print('Connected by ',address)

    with connection as conn:

        conn.sendall(b'HIIIII!!!!!!!!!')




with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((HOST,PORT))
    server.listen()
    print(f'Server is alive on the {HOST}:{PORT}')

    while True:
        conn,addr = server.accept()
        process = multiprocessing.Process(target=handle_client,args=(conn,addr))
        process.start()