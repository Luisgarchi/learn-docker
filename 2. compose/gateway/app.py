from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    print("API Gateway")
    response = requests.get('http://microservice:6000/')
    return 'Hello from Flask! Secondary service says: ' + response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)