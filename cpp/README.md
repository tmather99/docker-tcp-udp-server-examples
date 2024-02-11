# CPP based TCP/UDP example

## Build

```bash
docker build -t cpp-tcp-udp-server .
```

## Run Container

```bash
docker run --rm --name tcp-udp-cpp -p 54321:54321/tcp -p 12345:12345/udp cpp-tcp-udp-server
```

## Remove container

```bash
docker rm -f tcp-udp-cpp
```

## References

- https://en.wikipedia.org/wiki/C%2B%2B
