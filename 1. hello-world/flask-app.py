from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = os.getenv('NAME', 'World')
    return f'<h1>Hello {name}</h1>'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)