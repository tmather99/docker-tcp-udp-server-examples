package io.eol.demo.tcpudpserver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class TcpServer {
    public static void main(String[] args) throws Exception {
        try {
            ServerSocket serverSocket = new ServerSocket(54321);
            System.out.println("TCP Server started on port 54321");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

                String inputLine;
                while ((inputLine = in.readLine()) != null) {
                    System.out.println("Received: " + inputLine);
                    out.println(inputLine); // Echo the input line back to the client
                }
            }
        } catch (IOException e) {
            System.err.println("TCP Server IOException: " + e.getMessage());
        }
    }
}
