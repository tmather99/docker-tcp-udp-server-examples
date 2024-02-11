# Use the official Gradle image to create a build artifact.
# This is a multi-stage build. In the first stage, we build the application.
FROM gradle:8.5-jdk17 AS build
COPY --chown=gradle:gradle . /home/gradle/src
WORKDIR /home/gradle/src
RUN gradle build --no-daemon

# Use OpenJDK for smaller image size.
FROM eclipse-temurin:17-jre-alpine

EXPOSE 12345/udp 54321/tcp

# Copy the jar to the production image from the builder stage.
COPY --from=build /home/gradle/src/build/libs/*.jar /app/spring-boot-application.jar

ENTRYPOINT ["java","-jar","/app/spring-boot-application.jar"]
