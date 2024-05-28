from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("microservice")
    return "This is the message / response from the microservice"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)