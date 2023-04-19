import multiprocessing
import socket

HOST = '127.0.0.1'
PORT = 40000


def handle_client(user_data,address):
    print('Connected by ',address)
    print(user_data)
    send_back = f'Returned: {user_data}'
    s.sendto(send_back, address)



with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:


    print(f'Server is alive on the {HOST}:{PORT}')
    while True:
        message,addr = s.recvfrom(1024)
        process = multiprocessing.Process(target=handle_client,args=(message,addr))
        process.start()