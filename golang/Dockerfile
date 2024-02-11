FROM golang:1.21 as builder

# Create and change to the app directory.
WORKDIR /app

# Copy local code to the container image.
COPY . .

# Build the binary.
# -o myapp specifies the output name of the binary.
RUN CGO_ENABLED=0 GOOS=linux go build -v -o tcp-udp-server

# Use a Docker multi-stage build to create a lean production image.
# Start from the alpine:latest image for a lightweight base.
FROM alpine:latest

# Copy the binary from the builder stage to the production image.
COPY --from=builder /app/tcp-udp-server .

# This container exposes port 12345 to the outside world (UDP) and port 54321 (TCP)
EXPOSE 12345/udp 54321/tcp

# Run the binary.
CMD ["./tcp-udp-server"]
