# Multi-Container Flask Application with Docker Compose

This project demonstrates how to run multiple Docker containers that communicate with each other using Docker Compose. One service (the main service) makes a request to another service (the microservice) and returns both responses. This example illustrates how to use the Docker network service name to access the *microservice* from the *main* service.

## Project Layout

### Files Overview

- **compose.yaml**: Defines the Docker Compose configuration for the multi-container application. It specifies the services, their build contexts, ports, dependencies, and environment variables.
- **main/**: Contains the main service code and its Dockerfile.
  - **Dockerfile**: Instructions for building the Docker image for the main service.
  - **app.py**: The main service Flask application code.
  - **requirements.txt**: Lists the Python dependencies for the main service.
- **microservice/**: Contains the microservice code and its Dockerfile.
  - **Dockerfile**: Instructions for building the Docker image for the microservice.
  - **microservice.py**: The microservice Flask application code.
  - **requirements.txt**: Lists the Python dependencies for the microservice.

# Compose 

```yaml
version: '3.8'
services:
  main:
    build: 
      context: ./main
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    depends_on:
      - microservice
    environment:
      - MICROSERVICE_URL=http://microservice:5050/
      - LOCALHOST_URL=http://localhost:5050/
      
  microservice:
    build:
      context: ./microservice
      dockerfile: Dockerfile
    ports:
      - "5050:5050"

```
- version: Specifies the version of the Docker Compose file format.
- services: Defines the services that make up the application.
    - main: The main service.
        - build: Specifies the build context and Dockerfile for the main service.
        - ports: Maps port 5000 of the host to port 5000 of the container.
        - depends_on: Specifies that the main service depends on the microservice.
        - environment: Sets environment variables for the main service, including URLs for accessing the microservice.
    - microservice: The microservice.
        - build: Specifies the build context and Dockerfile for the microservice.
        - ports: Maps port 5050 of the host to port 5050 of the container.

# Main 

Defines a Flask application for the main service. It makes a request to the microservice and returns the combined response.
- It reads the MICROSERVICE_URL environment variable, makes a GET request to the microservice, and returns the response.

# Microservice 

Defines a simple Flask application for the microservice. It returns a static message at the root endpoint.


# Compose

Docker Compose allows you to define and run multi-container Docker applications. Here's how to build and run the containers.

```
docker compose up --build -d
```

**The main service can be accessed at http://localhost:5000 and the microservice at http://localhost:5050.**


# localhost inside main?

The reason calling `localhost:6000` from your main service does not work, even though your microservice is running on port 6000 on your machine, is due to the way Docker handles networking for containers.

## Docker Networking Basics

- Isolation: Docker containers run in isolated environments. Each container has its own network namespace, which means they have their own private IP addresses.
- Localhost Reference: When you reference `localhost` inside a Docker container, it refers to the container's own loopback network interface, not your host machine's network interface. Therefore, `localhost:6000` in the main service container would try to connect to port 6000 inside the main service container itself, not on the host machine or any other container.
- Docker Network: Docker provides a virtual network that containers can join. Containers on the same Docker network can communicate with each other using their service names as hostnames. Docker Compose sets up a default network for all services defined in a `compose.yaml` file, allowing them to discover each other by their service names.

## Accessing Services by Name

In your Docker Compose setup, you defined two services: `main` and `microservice`. Docker Compose automatically creates a network and includes both services in it. This setup allows the `main` service to communicate with the `microservice` service using the hostname `microservice`.

## Why localhost:6000 Doesn't Work

- Network Isolation: As mentioned, localhost inside the main container refers to the main container itself, not the host machine.
- Host Network: Even though your microservice is accessible on your host machine at localhost:6000, this is not visible or accessible to other containers because of Docker's network isolation.
- Cross-Network Communication: To allow communication between containers, you need to use Docker's networking features, which let you reference other containers by their service names.