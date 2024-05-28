from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def hello():
    print("Main API")

    # Try changing the enviroment variable below between MICROSERVICE_URL and LOCALHOST_URL
    # Save the code and then spin the containers up and down. Which one works and why? (explained in README)
    microservice_url = os.getenv('MICROSERVICE_URL')
    response = requests.get(microservice_url)
    return f'This is a message from the main service. Response from the url {microservice_url} is... {response}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
