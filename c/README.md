# C based TCP/UDP example

## Build

```bash
docker build -t c-tcp-udp-server .
```

## Run Container

```bash
docker run --rm --name tcp-udp-c -p 54321:54321/tcp -p 12345:12345/udp c-tcp-udp-server
```

## Remove container

```bash
docker rm -f tcp-udp-c
```

## References

- https://en.wikipedia.org/wiki/The_C_Programming_Language
