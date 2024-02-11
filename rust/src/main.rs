use std::net::{UdpSocket, TcpListener, TcpStream};
use std::{io, thread};
use std::io::{Read, Write};

fn handle_udp_client(socket: &UdpSocket) -> io::Result<()> {
    let mut buf = [0u8; 1024];
    let (amt, src) = socket.recv_from(&mut buf)?;

    // Echo back the received data
    socket.send_to(&buf[..amt], &src)?;

    Ok(())
}

fn handle_tcp_client(mut stream: TcpStream) {
    let mut buf = [0; 1024];
    while match stream.read(&mut buf) {
        Ok(size) => {
            if size == 0 {
                // connection was closed
                return;
            }
            stream.write_all(&buf[..size]).unwrap();
            true
        },
        Err(_) => {
            println!("An error occurred, terminating connection with {}", stream.peer_addr().unwrap());
            stream.shutdown(std::net::Shutdown::Both).unwrap();
            false
        }
    } {}
}

fn main() -> io::Result<()> {
    let udp_socket = UdpSocket::bind("0.0.0.0:12345")?;
    udp_socket.set_nonblocking(true)?;

    let tcp_listener = TcpListener::bind("0.0.0.0:54321")?;
    tcp_listener.set_nonblocking(true)?;

    println!("UDP server listening on port 12345");
    println!("TCP server listening on port 54321");

    loop {
        // Handle UDP clients
        match handle_udp_client(&udp_socket) {
            Ok(_) => (),
            Err(ref e) if e.kind() == io::ErrorKind::WouldBlock => {
                // No UDP packets to read, this is expected due to non-blocking
            },
            Err(e) => eprintln!("UDP error: {}", e),
        }

        // Handle TCP clients
        match tcp_listener.accept() {
            Ok((stream, _addr)) => {
                thread::spawn(move || handle_tcp_client(stream));
            },
            Err(ref e) if e.kind() == io::ErrorKind::WouldBlock => {
                // No TCP connections to accept, this is expected due to non-blocking
            },
            Err(e) => eprintln!("TCP error: {}", e),
        }

        // Sleep to prevent the loop from running too fast and consuming 100% CPU
        thread::sleep(std::time::Duration::from_millis(100));
    }
}
