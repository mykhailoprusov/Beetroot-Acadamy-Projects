import socket

HOST = '127.0.0.1'
PORT = 40000


client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


msg = b'Hi'
client_socket.sendto(msg,(HOST,PORT))

received = client_socket.recvfrom(1024)
print(received)

client_socket.close()