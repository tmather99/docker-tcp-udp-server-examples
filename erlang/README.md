# CPP based TCP/UDP example

## Build

```bash
docker build -t erlang-tcp-udp-server .
```

## Run Container

```bash
docker run --rm --name tcp-udp-erlang -p 54321:54321/tcp -p 12345:12345/udp erlang-tcp-udp-server
```

## Remove container

```bash
docker rm -f tcp-udp-erlang
```

## References

- https://www.erlang.org/
