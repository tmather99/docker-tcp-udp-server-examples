import socket
import sys

def client_program():
    # use server name or ip if specified else assume current host
    host = socket.gethostname() if len(sys.argv) == 1 else sys.argv[1]    
    port = 5000  # socket server port number

    print(f"TCP client sending port {host}:{port}")

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message and message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()