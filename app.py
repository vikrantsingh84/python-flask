from distutils.log import debug
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return'hello, world'

@app.route('/') 
def products():
    return'this ia product page'  

if __name__ == "__main__":
    app.run(debug=True, port=8000)