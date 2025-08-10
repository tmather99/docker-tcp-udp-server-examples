import socket
import sys

def udp_client():
    # use server name or ip if specified else assume current host
    host = socket.gethostname() if len(sys.argv) == 1 else sys.argv[1]    
    # socket server port number
    port = 12345 if len(sys.argv) == 2 else int(sys.argv[2] )  

    # Define the server address and port
    server_address = (host, port)
    
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = input(" -> ")  # take input

    with client_socket:
        while message and message.lower().strip() != 'bye':
            try:
                client_socket.sendto(message.encode(), server_address)  # send message
                data = client_socket.recv(1024).decode()  # receive response
                print('Received from server: ' + data)  # show in terminal
                message = input(" -> ")  # again take input
            except Exception as e:
                print(f"Error with connection to {host}:{port} -- {e}")
                break

if __name__ == '__main__':
    udp_client()