import socket
import argparse
import requests

#
#  udp client
#
def udp_client(host, port):
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

#
#  tcp client
#
def tcp_client(host, port):
    print(f"TCP client sending port {host}:{port}")
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    message = input(" -> ")  # take input

    with client_socket:
        while message and message.lower().strip() != 'bye':
            try:
                client_socket.send(message.encode())  # send message
                data = client_socket.recv(1024).decode()  # receive response
                print('Received from server: ' + data)  # show in terminal
                message = input(" -> ")  # again take input
            except Exception as e:
                print(f"Error with connection to {host}:{port} -- {e}")
                break

#
#  http get network exception
#
def http_get_error(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("GET request successful!")
            print("Response content:", response.content)
        else:
            print(f"GET request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


#
# python3 .\client.py --protocol tcp --host 10.48.209.50 --port 5000
# python3 .\client.py --protocol udp --host 10.48.209.50 --port 12345
# python3 .\client.py --protocol http --host 10.48.209.50 --port 8484 --error none, reset, timeout, disconnect, etc.
#
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP and UDP Client')
    parser.add_argument('--protocol', choices=['tcp', 'udp', 'http'], default='tcp', required=False)
    parser.add_argument('--host', type=str, default='10.48.209.50', required=False)
    parser.add_argument('--port', type=int, default=5000, required=False)
    parser.add_argument('--error', type=str, default='reset', required=False)

    args = parser.parse_args()
    protocol = args.protocol
    host = args.host
    port = args.port
    error = args.error

    match protocol:
        case 'tcp':
            tcp_client(host, port)
        case 'udp':
            udp_client(host, port)
        case 'http':
            http_get_error(f'http://{host}:{port}/{error}')