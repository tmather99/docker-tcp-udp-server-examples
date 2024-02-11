# Docker images with TCP/UDP server examples

The purpose of this repository is to demonstrate simple
tcp/udp servers based on different programming languages.

It also shows a typical containerization for them
including multistage builds


## Testing the containers

Once a container has been started, use `socat` and 
send the command `DISCOVER` from stdin to the sockets:

### TCP

```bash
socat - tcp4-connect:localhost:54321
```

### UDP

```bash
socat - udp4-connect:localhost:12345
```

## Docker Image size

At the time of writing the image sizes for the respective demo docker images
were as follows after adding multistage builds for all:

| Image                      |    Size |
|----------------------------|--------:|
| c-tcp-udp-server           |  80.6MB |
| cpp-tcp-udp-server         |  80.6MB |
| erlang-tcp-udp-server      | 259.0MB |
| golang-tcp-udp-server      |  10.4MB |
| java-spring-tcp-udp-server | 184.0MB |
| java-tcp-udp-server        | 167.0MB |
| nodejs-tcp-udp-server      | 141.0MB |
| python-tcp-udp-server      |  48.2MB |
| rust-tcp-udp-server        |  73.0MB |


## References

- https://www.redhat.com/sysadmin/getting-started-socat
