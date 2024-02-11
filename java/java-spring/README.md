# Java based TCP/UDP example

The lifecycle tool used here is Gradle.

## Local usage

With a regular local Java VM 17 or higher:

```bash
./gradlew clean build bootRun
```

## Build

```bash
docker build -t java-spring-tcp-udp-server .
```

## Run Container

```bash
docker run --rm --name tcp-udp-spring -p 54321:54321/tcp -p 12345:12345/udp java-spring-tcp-udp-server
```

## Remove container

```bash
docker rm -f tcp-udp-spring
```

## References

- https://dev.java/
