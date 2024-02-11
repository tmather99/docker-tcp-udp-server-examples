import socket
import threading

def udp_server():
    udp_ip = '0.0.0.0'
    udp_port = 12345

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))

    print(f"UDP server up and listening on port {udp_port}")

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print(f"Received message: {data} from {addr}")
        sock.sendto(data, addr)  # Echo back the data

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
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)  # Echo back the data

if __name__ == "__main__":
    udp_thread = threading.Thread(target=udp_server)
    tcp_thread = threading.Thread(target=tcp_server)

    udp_thread.start()
    tcp_thread.start()

    udp_thread.join()
    tcp_thread.join()
