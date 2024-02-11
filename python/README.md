# Python based TCP/UDP example

## Build

```bash
docker build -t python-tcp-udp-server .
```

## Run Container

```bash
docker run --rm --name tcp-udp-python -p 54321:54321/tcp -p 12345:12345/udp python-tcp-udp-server
```

## Remove container

```bash
docker rm -f tcp-udp-python
```

## References

- https://www.python.org/