package io.eol.demo.tcpudpserver;

import java.io.IOException;

public class ServerApplication {

    public static void main(String[] args) {
        Thread udpServerThread = new Thread(ServerApplication::startUdpServer);
        Thread tcpServerThread = new Thread(ServerApplication::startTcpServer);

        udpServerThread.start();
        tcpServerThread.start();
    }

    private static void startUdpServer() {
        try {
            UdpServer.main(new String[]{});
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static void startTcpServer() {
        try {
            TcpServer.main(new String[]{});
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
