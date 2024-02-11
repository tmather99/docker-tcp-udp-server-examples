# Build stage
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Run stage
FROM node:alpine

WORKDIR /app

COPY --from=builder /app .

EXPOSE 12345/udp 54321/tcp

CMD ["node", "server.js"]
