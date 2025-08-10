# Build stage for installing dependencies and copying source files
FROM python:3.13.6-slim AS builder

WORKDIR /app

# Copy only the requirements.txt.txt initially to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Run stage using a smaller base image
FROM python:3.13.6-alpine

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 12345/udp 54321/tcp

CMD ["python", "./server.py"]
