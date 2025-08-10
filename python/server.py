import socket
import threading
from datetime import datetime

#
#  UDP server
#
def udp_server():
    udp_ip = '0.0.0.0'
    udp_port = 12345

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))

    print(f"UDP server up and listening on port {udp_port}")

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        now = datetime.now()
        resp_data = f"{now} {data}".encode()
        print(f"Received message: {data} from {addr}")
        sock.sendto(resp_data, addr)  # Echo back the data


#
#  TCP server handling multiple clients sequentially 
#
def tcp_server():
    tcp_ip = '0.0.0.0'
    tcp_port = 54321

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((tcp_ip, tcp_port))
    sock.listen()

    print(f"TCP server up and listening on port {tcp_port}")

    while True:
        conn, addr = sock.accept()
        print(f"Connection from {addr}")

        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                now = datetime.now()
                resp_data = f"{now} {data}"
                print(resp_data)
                conn.sendall(resp_data)  # Echo back the data
            except Exception as e:
                print(f"Error with connection from {addr}: {e}")
                break
        conn.close()  # close the connection


#
#  TCP server handling multiple clients concurrently
#
def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"TCP server listening on port {port}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.activeCount() - 1}")

#
#  Client thread handler
#
def handle_client(conn, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            now = datetime.now()
            resp_msg = f"{now} {msg}"
            print(f"Message from {addr}: {msg}")
            conn.sendall(resp_msg.encode())
        except Exception as e:
            print(f"Error with connection from {addr}: {e}")
            break
    conn.close()

#
#  Main thread
#
if __name__ == "__main__":
    udp_thread = threading.Thread(target=udp_server)
    tcp_thread = threading.Thread(target=tcp_server)
    srv_thread = threading.Thread(target=server_program)

    udp_thread.start()
    tcp_thread.start()
    srv_thread.start()

    udp_thread.join()
    tcp_thread.join()
    srv_thread.join()
