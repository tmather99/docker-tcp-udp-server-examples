FROM rust:1.56 as builder
WORKDIR /usr/src/tcp-udp-server
COPY . .
RUN cargo install --path .

FROM debian:buster-slim
COPY --from=builder /usr/local/cargo/bin/tcp-udp-server /usr/local/bin/tcp-udp-server
EXPOSE 12345/udp 54321/tcp
CMD ["tcp-udp-server"]