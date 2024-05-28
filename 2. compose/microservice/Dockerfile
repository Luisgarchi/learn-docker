# Using a different version of Python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /microservice

# Copy the requirements file and install dependencies
COPY requirements.txt /microservice
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /microservice

# Make port 5000 available to the world outside this container
EXPOSE 6000

# Expose port 6000
EXPOSE 6000

# Command to run the app
CMD ["python", "microservice.py"]