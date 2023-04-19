import socket
import threading

PORT = 47047
HOST = '127.0.0.1'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

def handle_client(connection,address):
    with connection:
        print('Connected by: ',address)

        while True:
            d = connection.recv(1024).decode('utf-8')
            print(f'{address}, {d}')

            if d == 'DISCONNECT':
                break
            if not d:
                break


def start():
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(daemon=True,target=handle_client,args=(conn,addr))
        thread.start()


if __name__ == '__main__':

    start()




