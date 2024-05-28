# Demo Project

This demo project demonstrates a setup using Docker Compose with two services: gateway and microservice. The gateway service is accessible from the host machine, while the microservice is isolated and only accessible within the Docker network.
Services
- gateway: A Flask-based API that listens on port 5000. It makes internal requests to the microservice.
- microservice: A Flask-based secondary service that listens on port 6000 but is not exposed to the host machine.

```
version: '3.8'

services:
  gateway:
    build: 
      context: ./gateway
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    depends_on:
      - microservice
    networks:
      - internal_net

  microservice:
    build:
      context: ./microservice
      dockerfile: Dockerfile
    networks:
      - internal_net

networks:
  internal_net:
    driver: bridge
```

# Network Usage

- Both services are connected to the same custom Docker network (internal_net), defined at the bottom of the docker-compose.yml file.
- This network configuration ensures that microservice is not exposed to the host but can still be accessed by gateway internally via the environment variable MICROSERVICE_URL.
- The bridge network driver is used to facilitate communication between the services while isolating them from external access.

# Run the application

```
docker compose up --build -d
```