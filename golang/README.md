# Golang based TCP/UDP example

## Build

```bash
docker build -t golang-tcp-udp-server .
```

## Run Container

```bash
docker run --rm --name tcp-udp-golang -p 54321:54321/tcp -p 12345:12345/udp golang-tcp-udp-server
```

## Remove container

```bash
docker rm -f tcp-udp-golang
```

## References

- https://go.dev/
