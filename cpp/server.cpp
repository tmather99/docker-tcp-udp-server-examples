#include <iostream>
#include <cstring>
#include <thread>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

const int TCP_PORT = 54321;
const int UDP_PORT = 12345;
const int BUFFER_SIZE = 1024;

void tcpServer() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt));

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(TCP_PORT);

    bind(server_fd, (struct sockaddr *)&address, sizeof(address));
    listen(server_fd, 3);

    std::cout << "TCP Server listening on port " << TCP_PORT << std::endl;

    while (true) {
        new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen);
        read(new_socket, buffer, BUFFER_SIZE);
        std::cout << "TCP Server received: " << buffer << std::endl;
        send(new_socket, buffer, strlen(buffer), 0);
        close(new_socket);
    }
}

void udpServer() {
    int sockfd;
    char buffer[BUFFER_SIZE];
    struct sockaddr_in servaddr, cliaddr;

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    memset(&servaddr, 0, sizeof(servaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(UDP_PORT);

    bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr));

    std::cout << "UDP Server listening on port " << UDP_PORT << std::endl;

    while (true) {
        int len, n;
        len = sizeof(cliaddr); // Initialize len to size of an address
        n = recvfrom(sockfd, (char *)buffer, BUFFER_SIZE, MSG_WAITALL, (struct sockaddr *) &cliaddr, (socklen_t*)&len);
        buffer[n] = '\0';
        std::cout << "UDP Server received: " << buffer << std::endl;
        // Using 0 instead of MSG_CONFIRM
        sendto(sockfd, (const char *)buffer, strlen(buffer), 0, (const struct sockaddr *) &cliaddr, len);
    }
}

int main() {
    std::thread tcpThread(tcpServer);
    std::thread udpThread(udpServer);

    tcpThread.join();
    udpThread.join();

    return 0;
}
