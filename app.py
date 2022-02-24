from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/') 
def products():
    return'this ia product page'  

if __name__ == "__main__":
    app.run(debug=True, port=8000) 