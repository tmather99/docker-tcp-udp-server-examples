#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <arpa/inet.h>

#define TCP_PORT 54321
#define UDP_PORT 12345
#define BUFFER_SIZE 1024

void *tcp_server(void *arg) {
    int sockfd, new_sock;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_size;
    char buffer[BUFFER_SIZE];

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("TCP socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(TCP_PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("TCP bind failed");
        exit(EXIT_FAILURE);
    }

    if (listen(sockfd, 5) < 0) {
        perror("TCP listen failed");
        exit(EXIT_FAILURE);
    }

    printf("TCP server listening on port %d\n", TCP_PORT);

    while (1) {
        addr_size = sizeof(client_addr);
        new_sock = accept(sockfd, (struct sockaddr *)&client_addr, &addr_size);
        if (new_sock < 0) {
            perror("TCP accept failed");
            continue;
        }

        memset(buffer, 0, BUFFER_SIZE);
        read(new_sock, buffer, BUFFER_SIZE);
        printf("TCP server received: %s\n", buffer);
        write(new_sock, buffer, strlen(buffer)); // Echo back
        close(new_sock);
    }

    close(sockfd);
    return NULL;
}

void *udp_server(void *arg) {
    int sockfd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_size;
    char buffer[BUFFER_SIZE];

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        perror("UDP socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(UDP_PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("UDP bind failed");
        exit(EXIT_FAILURE);
    }

    printf("UDP server listening on port %d\n", UDP_PORT);

    while (1) {
        addr_size = sizeof(client_addr);
        memset(buffer, 0, BUFFER_SIZE);
        recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&client_addr, &addr_size);
        printf("UDP server received: %s\n", buffer);
        sendto(sockfd, buffer, strlen(buffer), 0, (struct sockaddr *)&client_addr, addr_size); // Echo back
    }

    close(sockfd);
    return NULL;
}

int main() {
    pthread_t tcp_thread, udp_thread;

    if (pthread_create(&tcp_thread, NULL, tcp_server, NULL) != 0) {
        perror("Failed to create TCP server thread");
        return EXIT_FAILURE;
    }

    if (pthread_create(&udp_thread, NULL, udp_server, NULL) != 0) {
        perror("Failed to create UDP server thread");
        return EXIT_FAILURE;
    }

    pthread_join(tcp_thread, NULL);
    pthread_join(udp_thread, NULL);

    return EXIT_SUCCESS;
}
