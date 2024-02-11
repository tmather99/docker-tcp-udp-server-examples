# Build stage
FROM debian:bullseye-slim AS builder

RUN apt-get update && apt-get install -y g++ make

WORKDIR /app

COPY . .

RUN g++ -pthread -o server server.cpp

# Run stage
FROM debian:bullseye-slim

COPY --from=builder /app/server /app/server

EXPOSE 12345/udp 54321/tcp

CMD ["/app/server"]