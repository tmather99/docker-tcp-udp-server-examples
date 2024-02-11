package io.eol.demo.tcpudpserver;

import jakarta.annotation.PostConstruct;
import org.springframework.stereotype.Component;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

@Component
public class UdpServerComponent {

    private final int udpPort = 12345; // Example port

    @PostConstruct
    public void startServer() {
        Thread thread = new Thread(() -> {
            try (DatagramSocket socket = new DatagramSocket(udpPort)) {
                byte[] buffer = new byte[1024];
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                System.out.println("UDP Server started on port " + udpPort);

                while (true) {
                    socket.receive(packet);
                    String received = new String(packet.getData(), 0, packet.getLength());
                    System.out.println("Received: " + received);
                    // Echo the received message back
                    socket.send(new DatagramPacket(packet.getData(), packet.getLength(), packet.getAddress(), packet.getPort()));
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
        thread.start();
    }
}
