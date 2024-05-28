FROM python:3.10-slim

WORKDIR /gateway

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /gateway

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application
CMD ["python",  "app.py"]