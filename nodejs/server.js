const dgram = require('dgram');
const net = require('net');

// UDP Server
const udpServer = dgram.createSocket('udp4');

udpServer.on('error', (err) => {
  console.log(`UDP Server error:\n${err.stack}`);
  udpServer.close();
});

udpServer.on('message', (msg, rinfo) => {
  console.log(`UDP Server got: ${msg} from ${rinfo.address}:${rinfo.port}`);
  // Echoing message back to UDP client
  udpServer.send(msg, rinfo.port, rinfo.address, (err) => {
    if (err) {
      udpServer.close();
    }
  });
});

udpServer.on('listening', () => {
  const address = udpServer.address();
  console.log(`UDP Server listening on ${address.address}:${address.port}`);
});

udpServer.bind(12345); // UDP server listens on port 12345

// TCP Server
const tcpServer = net.createServer((socket) => {
  console.log('TCP Client connected');

  socket.on('data', (data) => {
    console.log(`TCP Server received: ${data}`);
    // Echoing data back to TCP client
    socket.write(data);
  });

  socket.on('end', () => {
    console.log('TCP Client disconnected');
  });

  socket.on('error', (err) => {
    console.error(`TCP Server error: ${err}`);
  });
});

tcpServer.listen(54321, () => {
  console.log('TCP Server listening on port 54321');
});
