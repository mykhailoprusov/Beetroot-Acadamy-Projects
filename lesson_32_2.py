import socket
import threading

PORT = 47047
HOST = '127.0.0.1'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


def handle_client(connection, address):
    with connection as conn:
        print('Connected by: ', address)

        key = conn.recv(1024).decode()
        print(f'{address},key: {key}')

        msg = conn.recv(1024).decode()
        print(msg)
        encrypted_text = encrypt(msg,int(key))

        conn.sendall(encrypted_text.encode())

def encrypt(plain_text,shift_amount):
    cipher_text =""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:
            new_position2 = new_position-26
            new_letter2 = alphabet[new_position2]
            cipher_text += new_letter2
        else:
            new_letter1 = alphabet[new_position]
            cipher_text += new_letter1
    print(f"The encoded text is {cipher_text}.")
    return cipher_text




def start():
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(daemon=True,target=handle_client,args=(conn,addr))
        thread.start()


if __name__ == '__main__':

    start()