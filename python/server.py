import http.server
import socket
import threading
from datetime import datetime

#
#  TCP server handling multiple clients concurrently
#
def tcp_server():
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
        print(f"Active connections: {threading.active_count() - 1}")

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
# Various HTTP status codes and network exceptions.
#
class ExceptionSimulatingHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.strip("/")
        
        # Simulate network exceptions based on the URL path
        match path:
            case "socketerror":
                raise socket.error("Simulated generic socket error")
            case "brokenpipe":
                raise BrokenPipeError("Simulated broken pipe error")
            case "connreset":
                raise ConnectionResetError("Simulated connection reset by peer")
            case "internalerror":
                self.send_error(500, "Simulated internal server error")
                raise RuntimeError("Simulated internal server error")
            case "disconnect":
                self.send_error(500, "Simulated disconnection exception")
                raise ConnectionError("Simulated disconnection exception")
            case "reset":
                self.send_error(502, "Simulated network reset exception")
                raise ConnectionResetError("Simulated network reset exception")
            case "badgateway":
                self.send_error(502, "Simulated bad gateway exception")
                raise OSError("Simulated bad gateway exception")
            case "unavailable":
                self.send_error(503, "Simulated service unavailable exception")
                raise ConnectionAbortedError("Simulated service unavailable exception")
            case "timeout":
                self.send_error(504, "Simulated timeout exception")
                raise TimeoutError("Simulated timeout exception")
            case "badrequest":
                self.send_error(400, "Simulated bad request exception")
                raise ValueError("Simulated bad request exception")
            case "unauthorized":
                self.send_error(401, "Simulated unauthorized access exception")
                raise PermissionError("Simulated unauthorized access exception")
            case "forbidden":
                self.send_error(403, "Simulated forbidden access exception")
                raise PermissionError("Simulated forbidden access exception")
            case "notfound":
                self.send_error(404, "Simulated not found exception")
                raise FileNotFoundError("Simulated not found exception")
            case _:
                # Handle normally if no exception simulation is required
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                now = datetime.now()
                resp_msg = f"{now} error={path}\r\n"
                print(f"{self.headers}")
                self.wfile.write(resp_msg.encode())

def http_server(server_class=http.server.HTTPServer, handler_class=ExceptionSimulatingHandler):
    server_address = ('', 8484)
    httpd = server_class(server_address, handler_class)
    print("Starting HTTP server on port 8484")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("HTTP server closed")       

#
#  Main thread
#
if __name__ == "__main__":
    tcp_thread = threading.Thread(target=tcp_server)
    http_thread = threading.Thread(target=http_server)

    tcp_thread.start()
    http_thread.start()

    tcp_thread.join()
    http_thread.join()
