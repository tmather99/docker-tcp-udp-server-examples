package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net"
	"strings"
)

func main() {
	go startUDPServer()
	startTCPServer() // TCP server will block further execution
}

func startUDPServer() {
	udpAddr, err := net.ResolveUDPAddr("udp", ":12345")
	if err != nil {
		panic(err)
	}

	udpConn, err := net.ListenUDP("udp", udpAddr)
	if err != nil {
		panic(err)
	}
	defer udpConn.Close()

	fmt.Println("UDP server listening on port 12345")
	buffer := make([]byte, 1024)

	for {
		n, addr, err := udpConn.ReadFromUDP(buffer)
		text := string(buffer[:n])
		fmt.Printf("Received '%s' from %s\n", text, addr)

		if strings.TrimSpace(text) == "STOP" {
			fmt.Println("UDP client disconnected")
			break
		} else if strings.TrimSpace(text) == "DISCOVER" {
			response := fmt.Appendln(getData())
			go sendResponse(udpConn, addr, response)
		}

		if err != nil {
			fmt.Println(err)
			continue
		}
	}
}

func sendResponse(conn *net.UDPConn, addr *net.UDPAddr, response []byte) {
	_, err := conn.WriteToUDP(response, addr)
	if err != nil {
		fmt.Printf("Couldn't send response %v", err)
	}
}

func startTCPServer() {
	listener, err := net.Listen("tcp", ":54321")
	if err != nil {
		panic(err)
	}
	defer listener.Close()

	fmt.Println("TCP server listening on port 54321")

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println(err)
			continue
		}

		go handleTCPConnection(conn)
	}
}

func handleTCPConnection(conn net.Conn) {
	defer conn.Close()
	fmt.Printf("TCP client connected from %s\n", conn.RemoteAddr().String())

	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		text := scanner.Text()
		fmt.Printf("Received: %s\n", text)
		if strings.TrimSpace(text) == "STOP" {
			fmt.Println("TCP client disconnected")
			break
		} else if strings.TrimSpace(text) == "DISCOVER" {
			conn.Write(fmt.Appendln(getData()))
		}

	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}

func getData() []byte {
	data := map[string]interface{}{
		"intValue":    1234,
		"boolValue":   true,
		"stringValue": "hello!",
		"objectValue": map[string]interface{}{
			"arrayValue": []int{1, 2, 3, 4},
		},
	}

	jsonData, err := json.Marshal(data)
	if err != nil {
		fmt.Printf("could not marshal json: %s\n", err)
		return nil
	}

	return jsonData
}
