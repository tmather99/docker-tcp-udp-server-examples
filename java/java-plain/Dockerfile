# Stage 1: Build the application
FROM maven:3.8.4-openjdk-17 AS build
COPY src /home/app/src
COPY pom.xml /home/app
RUN mvn -f /home/app/pom.xml clean package -DskipTests

# Stage 2: Run the application

# Stage 2: Run the application with Eclipse Temurin JRE
FROM eclipse-temurin:17-jre-alpine

# Copy the jar to the production image from the builder stage.
COPY --from=build /home/app/target/*.jar /usr/local/lib/app.jar

EXPOSE 12345/udp 54321/tcp

ENTRYPOINT ["java", "-jar", "/usr/local/lib/app.jar"]
