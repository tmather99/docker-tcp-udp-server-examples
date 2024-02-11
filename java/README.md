# Java based TCP/UDP examples

This folder contains multiple examples for Java using typical
runtime environments and tools for the build life cycle.

All are finally created and run based on their respective Dockerfile.

For the Lifecycle and Dependency management tools Maven and Gradlew
their wrapper tools are included, so that no local setup is required.

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
