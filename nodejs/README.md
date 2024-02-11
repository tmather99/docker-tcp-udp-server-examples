# Node.js based TCP/UDP example

## Build

```bash
docker build -t nodejs-tcp-udp-server .
```

## Run Container

```bash
docker run --rm --name tcp-udp-nodejs -p 54321:54321/tcp -p 12345:12345/udp nodejs-tcp-udp-server
```

## Remove container

```bash
docker rm -f tcp-udp-nodejs
```

## References

- https://nodejs.org/
