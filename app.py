from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/<name>')

@app.route('/')
def index(name=''):
    return "<h1>Hello World</h1>"

if __name__== '__main__':
    app.run(port=5050, debug=True)