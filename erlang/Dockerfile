# Build stage
FROM erlang:23 AS builder

WORKDIR /app

COPY . .

RUN erlc server.erl

# Run stage
FROM erlang:23-slim

COPY --from=builder /app/server.beam /app/

WORKDIR /app

EXPOSE 12345/udp 54321/tcp

CMD ["erl", "-noshell", "-s", "server", "start"]
