# Java based TCP/UDP example

The lifecycle tool used here is Maven.

## Local usage

With a regular local Java VM 17 or higher:

```bash
./mvnw clean install
./mvnw exec:java -Dexec.mainClass="io.eol.demo.tcpudpserver.ServerApplication"
```

## Build

```bash
docker build -t java-tcp-udp-server .
```

## Run Container

```bash
docker run --rm --name tcp-udp-java -p 54321:54321/tcp -p 12345:12345/udp java-tcp-udp-server
```

## Remove container

```bash
docker rm -f tcp-udp-java
```

## References

- https://dev.java/
