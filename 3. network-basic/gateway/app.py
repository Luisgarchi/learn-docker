from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def hello():
    print("API Gateway")
    microservice_url = os.getenv('MICROSERVICE_URL')
    response = requests.get(microservice_url)
    return 'Hello from gateway service. Microservice service says: ' + response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)