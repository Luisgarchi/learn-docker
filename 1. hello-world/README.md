# Hello World Flask App with Docker

This project demonstrates a simple Flask application containerized using Docker. Below, you'll find explanations of the various files in the directory, the purpose of the Dockerfile, and instructions on how to build and run the Docker container.

## Project Layout

.
├── .dockerignore
├── .gitignore
├── Dockerfile
├── flask-app.py
└── requirements.txt


### Files Overview

- **.dockerignore**: Lists files and directories that should be ignored by Docker when building the image. This helps to reduce the build context sent to the Docker daemon.
  
- **.gitignore**: Specifies files and directories that should be ignored by Git. Typically used to avoid committing temporary files, build artifacts, and virtual environments.
  
- **Dockerfile**: Contains instructions for building the Docker image. It defines the base image, sets up the working directory, installs dependencies, copies the application code, and specifies how to run the application.
  
- **flask-app.py**: The Flask application code. It defines a simple web server with one endpoint (`/`) that returns a "Hello World" message.
  
- **requirements.txt**: Lists the Python dependencies required by the Flask application. These dependencies will be installed inside the Docker container.

## Dockerfile Explanation
- **FROM python:3.10-alpine**: This line specifies the base image for our Docker image. You can search the internet to find the appropriate image for the distribution you are using.

- **WORKDIR /app**: Sets the working directory inside the container to /app. All subsequent commands will be run from this directory.

- **COPY requirements.txt ./**: Copies the requirements.txt file to the working directory in the container. This step is done separately to take advantage of Docker's layer caching. By copying requirements.txt first, Docker can cache this step if requirements.txt hasn't changed, even if other files have.

- **RUN pip install --no-cache-dir -r requirements.txt**: Installs the Python packages listed in requirements.txt inside the container without using the pip cache, which helps to keep the image size small.

- **COPY . /app**: Copies the rest of the application code to the container. This step is done after installing the dependencies to ensure that code changes do not invalidate the cached layer for dependency installation.

- **ENV NAME=World**: Sets an environment variable NAME with a default value of "World". This can be used by the application to customize behavior.

- **ENV PORT=8080**: Sets an environment variable PORT with a default value of 8080. This specifies the port the application will listen on.

- **EXPOSE 8080**: Informs Docker that the container will listen on port 8080 at runtime.

- **CMD ["python", "flask-app.py"]**: Specifies the command to run the Flask application when the container starts.

# Building and Running the Docker Container
## Building the Docker Image

A Docker image is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software, including the code, runtime, libraries, and dependencies.

To build the Docker image, run the following command in the directory containing the Dockerfile:

```
docker build -t hello-world-flask .
```

This command creates a Docker image named hello-world-flask.


## Running the Docker Container

A Docker container is a runtime instance of a Docker image. It includes the application and its dependencies, but it runs in an isolated environment.

To run the Docker container, use the following command:
```
docker run -p 8080:8080 hello-world-flask
```

This command runs the container and **maps port 8080 of the container** *to* **port 8080 on your local machine**. You can then access the application at http://localhost:8080.


## Accessing the Application

Once the container is running, open your web browser and navigate to http://localhost:8080. You should see a message that says "Hello World" or "Hello [NAME]" if you have set the NAME environment variable to a different value.

## Cleaning Up

To stop the running container, press Ctrl+C in the terminal where the container is running. To remove the container, you can use the following command:

```
docker rm $(docker ps -a -q -f status=exited)
```

To remove the image, use:

```
docker rmi hello-world-flask
```

Alternatively you can use the Docker destop application to stop, start and remmove contain and or images.