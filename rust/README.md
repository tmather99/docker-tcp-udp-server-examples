# Rust based TCP/UDP example

## Build

```bash
docker build -t rust-tcp-udp-server .
```

## Run Container

```bash
docker run --rm --name tcp-udp-rust -p 54321:54321/tcp -p 12345:12345/udp rust-tcp-udp-server
```

## Remove container

```bash
docker rm -f tcp-udp-rust
```

## References

- https://www.rust-lang.org/
