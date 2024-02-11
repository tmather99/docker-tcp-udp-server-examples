package io.eol.demo.tcpudpserver;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class UdpServer {
    public static void main(String[] args) throws IOException {

        try {
            DatagramSocket socket = new DatagramSocket(12345);
            byte[] receiveBuffer = new byte[1024];
            System.out.println("UDP Server started on port 12345");

            while (true) {
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                socket.receive(receivePacket);
                String receivedData = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("Received: " + receivedData);

                // Echo data back to client
                DatagramPacket sendPacket = new DatagramPacket(
                        receivePacket.getData(),
                        receivePacket.getLength(),
                        receivePacket.getAddress(),
                        receivePacket.getPort());
                socket.send(sendPacket);
            }
        } catch (IOException e) {
            System.err.println("UDP Server IOException: " + e.getMessage());
        }
    }
}