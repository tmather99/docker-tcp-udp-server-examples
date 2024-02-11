const dgram = require('dgram');
const net = require('net');

// Simulated UDP sources
const udpSources = [
  { id: 1, port: 5001 },
  { id: 2, port: 5002 },
];

// Function to simulate discovering UDP sources
function discoverUDPSources(callback) {
  // Simulate asynchronous discovery
  setTimeout(() => {
    callback(udpSources.map(source => `ID: ${source.id}, Port: ${source.port}`));
  }, 1000);
}

// TCP server to interact with clients
const tcpServer = net.createServer(socket => {
  console.log('Client connected');

  socket.on('data', data => {
    console.log(`Received: ${data}`);
    if (data.toString().trim() === 'DISCOVER') {
      discoverUDPSources((sources) => {
        socket.write(sources.join('\n') + '\n');
      });
    }
  });

  socket.on('end', () => {
    console.log('Client disconnected');
  });
});

tcpServer.on('error', (err) => {
  console.error('Server error:', err);
});

tcpServer.listen(54321, () => {
  console.log('TCP Server listening on port 54321');
});
