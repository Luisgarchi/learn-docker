from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("Microservice")
    return "Response from Secondary Service"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)