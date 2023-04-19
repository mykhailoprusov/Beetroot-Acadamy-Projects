import socket
import time

PORT = 47047
HOST = '127.0.0.1'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST,PORT))

letter2 = b'hello'
letter1 = b'3'
def receive_letter():
    data  = client_socket.recv(1024)
    print(data)

def send_letter(letter):

    client_socket.sendall(letter)



send_letter(letter1)
time.sleep(0.5)
send_letter(letter2)
receive_letter()

client_socket.close()